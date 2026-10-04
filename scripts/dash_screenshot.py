"""Take the real screenshot of the Dash app in docs/unit-10-visualization.md.

    python scripts/dash_screenshot.py

The app code is read from the page itself (the first block marked `serve:`), saved as app.py
in a temporary folder with the data files, and started on a free port. A headless Chromium
(Playwright, see scripts/screenshot.py) opens it, picks "Sat" in the dropdown and saves
docs/assets/img/u10-dash-app.png. The server is stopped at the end.
"""
import os
import signal
import socket
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

from playwright.sync_api import sync_playwright

sys.path.insert(0, str(Path(__file__).resolve().parent))
import mdblocks as mb  # noqa: E402

PAGE = mb.DOCS / "unit-10-visualization.md"
OUT = mb.IMG / "u10-dash-app.png"


def app_code():
    """The first block of the page that is marked <!-- serve: ... -->."""
    _, blocks = mb.load(PAGE)
    for b in blocks:
        if b.kind == "run" and "serve" in b.directives and not b.indent:
            return b.code
    raise SystemExit("no serve block found in " + PAGE.name)


def free_port():
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def wait_until_up(url, seconds=30):
    for _ in range(int(seconds * 2)):
        try:
            urllib.request.urlopen(url + "_dash-layout", timeout=2)
            return
        except Exception:
            time.sleep(0.5)
    raise SystemExit("the Dash app did not start")


def main():
    folder = mb.workdir_with_data()
    (folder / "app.py").write_text(app_code() + "\n", encoding="utf-8")
    port = free_port()
    url = f"http://127.0.0.1:{port}/"
    # `import app` skips the `if __name__ == "__main__"` part, so we start the server here
    # on a free port (and without debug mode, so no developer badge is shown in the picture)
    server = subprocess.Popen(
        [sys.executable, "-c", f"import app; app.app.run(port={port}, debug=False)"],
        cwd=folder, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True,
    )
    try:
        wait_until_up(url)
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport={"width": 1000, "height": 600})
            page.goto(url, wait_until="networkidle")
            page.wait_for_selector(".js-plotly-plot")
            page.click("#day-dropdown")
            page.get_by_role("option", name="Sat").click()
            page.wait_for_selector("text=Tips on Sat")   # the callback has run
            page.wait_for_timeout(800)
            OUT.parent.mkdir(parents=True, exist_ok=True)
            page.screenshot(path=str(OUT))
            browser.close()
        print("saved", OUT.relative_to(mb.ROOT))
    finally:
        os.killpg(server.pid, signal.SIGTERM)
        server.wait(timeout=20)


if __name__ == "__main__":
    main()
