"""How long is each unit page compared with its teaching hours?

    python scripts/page_stats.py

Counts markdown lines without generated Output blocks, runnable examples and figures.
Unit pages should grow with teaching hours: Units I and II the shortest, Unit IX the longest.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import mdblocks as mb  # noqa: E402

HOURS = {1: 3, 2: 3, 3: 4, 4: 4, 5: 5, 6: 4, 7: 4, 8: 5, 9: 6, 10: 4, 11: 6}
STEMS = {1: "unit-01-intro", 2: "unit-02-basics", 3: "unit-03-control", 4: "unit-04-functions",
         5: "unit-05-structures", 6: "unit-06-files", 7: "unit-07-cleaning", 8: "unit-08-eda",
         9: "unit-09-ml", 10: "unit-10-visualization", 11: "unit-11-lab"}

print(f"{'unit':<6}{'hours':>6}{'lines':>8}{'lines/h':>9}{'examples':>10}{'figures':>9}{'diagrams':>10}")
total = 0
for n, stem in STEMS.items():
    path = mb.DOCS / f"{stem}.md"
    text = path.read_text(encoding="utf-8")
    lines = len(re.sub(r"```\{ \.text \.output.*?```", "", text, flags=re.S).split("\n"))
    _, blocks = mb.load(path)
    runs = sum(1 for b in blocks if b.kind == "run")
    figs = len(re.findall(r"^\s*!\[.*\]\(.*#only-light\)", text, flags=re.M))
    mer = text.count("```mermaid")
    total += lines
    print(f"{n:<6}{HOURS[n]:>6}{lines:>8}{lines / HOURS[n]:>9.0f}{runs:>10}{figs:>9}{mer:>10}")
print(f"total lines (units): {total}")
