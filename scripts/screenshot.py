"""Take screenshots of built pages (needs: pip install playwright && playwright install chromium).

    python scripts/screenshot.py SITE_DIR OUT_DIR PAGE [PAGE ...] [--dark] [--width 1440] [--full]

PAGE is a path like unit-03-control/ or index.html. A tiny local web server is started for SITE_DIR.
"""
import argparse
import functools
import http.server
import threading
from pathlib import Path

from playwright.sync_api import sync_playwright


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args, **kwargs):
        pass


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("site")
    ap.add_argument("out")
    ap.add_argument("pages", nargs="+")
    ap.add_argument("--dark", action="store_true")
    ap.add_argument("--width", type=int, default=1440)
    ap.add_argument("--height", type=int, default=900)
    ap.add_argument("--full", action="store_true", help="capture the whole page, not just the first screen")
    args = ap.parse_args()

    handler = functools.partial(QuietHandler, directory=args.site)
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{srv.server_address[1]}/"
    Path(args.out).mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        ctx = browser.new_context(
            viewport={"width": args.width, "height": args.height},
            color_scheme="dark" if args.dark else "light",
        )
        for page_path in args.pages:
            page = ctx.new_page()
            msgs = []
            page.on("console", lambda m: msgs.append(f"{m.type}: {m.text}") if m.type in ("error", "warning") else None)
            page.on("pageerror", lambda e: msgs.append(f"pageerror: {e}"))
            page.goto(base + page_path, wait_until="networkidle")
            page.wait_for_timeout(1200)
            name = page_path.strip("/").replace("/", "_").replace(".html", "") or "index"
            suffix = "-dark" if args.dark else "-light"
            target = Path(args.out) / f"{name}{suffix}-{args.width}.png"
            page.screenshot(path=str(target), full_page=args.full)
            print(target, *msgs, sep="\n  ")
            page.close()
        browser.close()


if __name__ == "__main__":
    main()
