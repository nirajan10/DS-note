"""Open every built page at phone width and report horizontal page overflow.

    python scripts/mobile_check.py SITE_DIR [--width 390]

Code blocks and tables may scroll inside their own box; the PAGE itself must not scroll sideways.
"""
import argparse
import functools
import http.server
import threading
from pathlib import Path

from playwright.sync_api import sync_playwright

JS = """() => {
  const vw = document.documentElement.clientWidth;
  const bad = [];
  for (const el of document.querySelectorAll('.md-content__inner *')) {
    const r = el.getBoundingClientRect();
    if (r.width === 0) continue;
    if (r.right > vw + 1) {
      // ignore elements that live inside a scrolling box (pre, table wrapper, mermaid, iframe)
      let p = el.parentElement, boxed = false;
      while (p && p !== document.body) {
        const s = getComputedStyle(p);
        if (['auto', 'scroll'].includes(s.overflowX)) { boxed = true; break; }
        p = p.parentElement;
      }
      if (!boxed) bad.push(el.tagName.toLowerCase() + '.' + (el.className || '').toString().slice(0, 40) + ' right=' + Math.round(r.right));
    }
  }
  return {scrollWidth: document.documentElement.scrollWidth, clientWidth: vw, bad: bad.slice(0, 4)};
}"""


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args, **kwargs):
        pass


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("site")
    ap.add_argument("--width", type=int, default=390)
    args = ap.parse_args()
    site = Path(args.site)
    handler = functools.partial(QuietHandler, directory=site)
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{srv.server_address[1]}/"
    pages = sorted(p.parent.relative_to(site).as_posix() + "/" for p in site.glob("*/index.html")
                   if p.parent.name not in ("assets", "search", "stylesheets"))
    pages.insert(0, "")
    worst = 0
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        ctx = browser.new_context(viewport={"width": args.width, "height": 800})
        for pg in pages:
            page = ctx.new_page()
            page.goto(base + pg, wait_until="load")
            page.wait_for_timeout(1200)
            r = page.evaluate(JS)
            over = r["scrollWidth"] - r["clientWidth"]
            flag = "OVERFLOW" if over > 1 or r["bad"] else "ok"
            worst = max(worst, over)
            print(f"{flag:9} {pg or '/':32} page {r['scrollWidth']}px in {r['clientWidth']}px", *r["bad"], sep="  " if r["bad"] else "")
            page.close()
        browser.close()
    raise SystemExit(1 if worst > 1 else 0)


if __name__ == "__main__":
    main()
