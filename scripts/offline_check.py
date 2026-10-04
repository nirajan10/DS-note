"""Open built pages in headless Chromium with ALL non-local network requests blocked, and check that
fonts load from the site itself and Mermaid diagrams are drawn.

    python scripts/offline_check.py SITE_DIR PAGE [PAGE ...]

PAGE is a path such as unit-03-control/ . Exit code 1 if anything external was requested or a check fails.
"""
import functools
import http.server
import sys
import threading

from playwright.sync_api import sync_playwright

FONTS = ["Atkinson Hyperlegible Next", "Bricolage Grotesque", "JetBrains Mono"]


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args, **kwargs):
        pass


def main():
    site, pages = sys.argv[1], sys.argv[2:]
    handler = functools.partial(QuietHandler, directory=site)
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{srv.server_address[1]}/"
    failed = False
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for page_path in pages:
            page = browser.new_page()
            blocked = []

            def gate(route):
                if route.request.url.startswith(base) or route.request.url.startswith("data:"):
                    route.continue_()
                else:
                    blocked.append(route.request.url)
                    route.abort()

            page.route("**/*", gate)
            page.goto(base + page_path, wait_until="load")
            page.wait_for_timeout(2500)
            fonts = page.evaluate(
                """async (names) => { await document.fonts.ready;
                   const out = {};
                   for (const n of names) out[n] = [...document.fonts].some(f => f.family.replace(/"/g,'') === n && f.status === 'loaded');
                   return out; }""", FONTS)
            diagrams = page.evaluate("document.querySelectorAll('div.mermaid').length")
            raw = page.evaluate("document.querySelectorAll('pre.mermaid').length")
            print(f"{page_path}: fonts loaded {fonts}; mermaid drawn={diagrams}, undrawn={raw}; blocked external requests={len(blocked)}")
            for url in blocked[:5]:
                print("   blocked:", url)
            if blocked or not all(fonts.values()) or raw:
                failed = True
            page.close()
        browser.close()
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
