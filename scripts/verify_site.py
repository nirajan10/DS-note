"""Inspect the BUILT site (not just the markdown) and report problems.

    NO_MKDOCS_2_WARNING=true mkdocs build --strict -d /tmp/sitecheck
    python scripts/verify_site.py /tmp/sitecheck

Checks
  1. Leaked raw markdown inside each page's <article> (unrendered admonitions, cards, tabs,
     fences, tables, icon shortcodes) and Mermaid source that is not inside a mermaid block.
  2. Every href / src: relative targets exist, and every #fragment exists as an id= on the target.
  3. Every image / iframe / script / stylesheet that the pages reference exists in the build.
  4. extra.css: braces balanced, @import before any rule, every --ds-* token used is defined,
     and every token is defined in BOTH the light (:root) and dark (slate) schemes.
  5. Syllabus facts: unit hours (pages and home cards), 48 total, marks, sub-point counts,
     learning objectives, lab sheet count, one exam section per unit.
  6. Heading case: prose headings are in Title Case (advisory list, counted as problems).
"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urldefrag, urljoin, urlparse

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

# ---- the syllabus, typed once -----------------------------------------------------------
UNITS = {
    1: ("unit-01-intro", "Introduction to Data Science and Python", 3, 2,
        "Understand Data Science concepts; set up Python environment and write basic scripts."),
    2: ("unit-02-basics", "Python Programming Basics and Operators", 3, 2,
        "Understand Python syntax and use operators effectively; write basic Python programs."),
    3: ("unit-03-control", "Control Structures", 4, 1,
        "Implement decision-making and iterative programming in Python."),
    4: ("unit-04-functions", "Functions and Modules", 4, 1,
        "Write reusable Python functions and use modules."),
    5: ("unit-05-structures", "Data Structures in Python", 5, 1,
        "Use Python data structures for data storage and manipulation."),
    6: ("unit-06-files", "File Handling and Exception", 4, 1,
        "Perform file operations and handle errors in Python."),
    7: ("unit-07-cleaning", "Data Collection and Cleaning with Python", 4, 1,
        "Import and preprocess datasets; clean and transform data for analysis."),
    8: ("unit-08-eda", "Exploratory Data Analysis", 5, 3,
        "Perform statistical analysis; visualize data using charts and plots."),
    9: ("unit-09-ml", "Introduction to Machine Learning with Python", 6, 3,
        "Understand ML concepts; build regression, classification, and clustering models."),
    10: ("unit-10-visualization", "Data Visualization and Reporting", 4, 2,
         "Build advanced visualizations and dashboards; present data insights effectively."),
    11: ("unit-11-lab", "Practical Lab Work", 6, 0,
         "Apply Python skills to real-world datasets; build small data-driven projects."),
}
ROMAN = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X", 11: "XI"}
TOTAL_HOURS, FULL_MARKS, PASS_MARKS, CREDITS, LABS = 48, 100, 45, "3.0", 10

problems = []


def bad(kind, where, msg):
    problems.append((kind, where, msg))
    print(f"  {kind:<9} {where}: {msg}")


# ---- HTML parsing -----------------------------------------------------------------------
class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.in_article = False
        self.code_depth = 0
        self.mermaid_depth = 0
        self.text = []          # article text outside code/pre
        self.mermaid = []       # contents of <pre class="mermaid">
        self.links = []         # (tag, attr, value)
        self.ids = set()
        self.lang_mermaid = 0   # <code class="language-mermaid"> (fence not recognised)
        self.headings = []      # (level, text) inside article
        self._h = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        for k in ("id", "name"):
            if a.get(k):
                self.ids.add(a[k])
        for k in ("href", "src", "data-src"):
            if a.get(k) is not None and tag in ("a", "img", "script", "link", "iframe", "source", "video"):
                self.links.append((tag, k, a[k]))
        if tag == "article":
            self.in_article = True
        if not self.in_article:
            return
        classes = (a.get("class") or "").split()
        if tag in ("pre", "code", "script", "style"):
            self.code_depth += 1
        if tag == "pre" and "mermaid" in classes:
            self.mermaid_depth += 1
            self.mermaid.append("")
        if tag == "code" and "language-mermaid" in classes:
            self.lang_mermaid += 1
        if re.fullmatch(r"h[1-6]", tag):
            self._h = [int(tag[1]), ""]

    def handle_endtag(self, tag):
        if tag == "article":
            self.in_article = False
        if not self.in_article:
            return
        if tag in ("pre", "code", "script", "style"):
            if tag == "pre" and self.mermaid_depth:
                self.mermaid_depth -= 1
            self.code_depth = max(0, self.code_depth - 1)
        if self._h and tag == f"h{self._h[0]}":
            self.headings.append((self._h[0], self._h[1].strip()))
            self._h = None

    def handle_data(self, data):
        if not self.in_article:
            return
        if self.mermaid_depth:
            self.mermaid[-1] += data
        elif self.code_depth == 0:
            self.text.append(data)
        if self._h is not None and self.code_depth == 0:
            self._h[1] += data
        elif self._h is not None:
            self._h[1] += data


def parse(path):
    p = Page()
    p.feed(path.read_text(encoding="utf-8"))
    return p


LEAKS = [
    ("- **[", "an unrendered grid-cards list"),
    (":material-", "an icon shortcode (pymdownx.emoji is not enabled)"),
    ("!!! ", "an unrendered admonition"),
    ("??? ", "an unrendered collapsible block"),
    (":::", "an unrendered fence/container"),
    ("[!NOTE]", "a GitHub-style alert"),
    ("[!TIP]", "a GitHub-style alert"),
    ("[!WARNING]", "a GitHub-style alert"),
    ('=== "', "an unrendered tab"),
    ("```", "an unrendered code fence"),
    ("|---", "an unrendered table"),
    ("{ .text", "an attribute list that did not apply"),
    ("{: ", "an attribute list that did not apply"),
    ("<!--", "visible comment text"),
    ("![", "an unrendered image"),
    ("](", "an unrendered link"),
]
MERMAID_WORDS = re.compile(r"^\s*(flowchart|graph|sequenceDiagram|classDiagram|stateDiagram|erDiagram|gantt|pie)\b", re.M)


def check_pages(site):
    pages = sorted(p for p in site.rglob("*.html") if p.name != "404.html")
    parsed = {}
    for path in pages:
        rel = path.relative_to(site).as_posix()
        pg = parse(path)
        parsed[rel] = pg
        article = "".join(pg.text)
        for token, what in LEAKS:
            if token in article:
                i = article.index(token)
                bad("LEAK", rel, f"{what}: ...{article[max(0, i - 30):i + 50].strip()!r}")
        if pg.lang_mermaid:
            bad("LEAK", rel, "a ```mermaid fence rendered as a plain code block (superfences custom fence missing)")
        for m in pg.mermaid:
            if not MERMAID_WORDS.search(m):
                bad("MERMAID", rel, f"mermaid block does not start with a diagram keyword: {m[:60]!r}")
        if MERMAID_WORDS.search(article):
            bad("LEAK", rel, "mermaid diagram source found outside a mermaid block")
        if "PLACEHOLDER" in article:
            bad("TODO", rel, "page still contains PLACEHOLDER text")
    return pages, parsed


def target_file(site, page_rel, href):
    """Resolve an href the way a browser would from the page's served URL."""
    base = "/" + page_rel
    if base.endswith("index.html"):
        base = base[: -len("index.html")]
    joined = urljoin(base, href)
    path = unquote(urlparse(joined).path)
    f = site / path.lstrip("/")
    if path.endswith("/") or f.is_dir():
        f = f / "index.html"
    return f


def check_links(site, parsed):
    n = 0
    for rel, pg in parsed.items():
        for tag, attr, value in pg.links:
            if not value or re.match(r"^(https?:|mailto:|data:|tel:|javascript:|//)", value):
                continue
            n += 1
            href, frag = urldefrag(value)
            if not href:      # same-page fragment
                f, tgt_rel = site / rel, rel
            else:
                f = target_file(site, rel, href)
                tgt_rel = f.relative_to(site).as_posix() if f.is_relative_to(site) else None
            if tgt_rel is None or not f.exists():
                bad("BROKEN", rel, f"<{tag} {attr}={value!r}> does not resolve to a file")
                continue
            if frag and f.suffix == ".html" and frag not in ("top",):
                tp = parsed.get(tgt_rel) or parse(f)
                if unquote(frag) not in tp.ids:
                    bad("ANCHOR", rel, f"<{tag} {attr}={value!r}>: no id={frag!r} on {tgt_rel}")
    print(f"  checked {n} relative references")


# ---- CSS ----------------------------------------------------------------------------------
def top_level_blocks(css):
    """Split CSS into (selector, body) pairs at top level (media queries are kept whole)."""
    out, depth, start, sel_start = [], 0, None, 0
    for i, ch in enumerate(css):
        if ch == "{":
            if depth == 0:
                start, sel = i + 1, css[sel_start:i].strip()
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                out.append((sel, css[start:i]))
                sel_start = i + 1
        elif ch == ";" and depth == 0:
            sel_start = i + 1
    return out


def check_css():
    path = DOCS / "stylesheets" / "extra.css"
    raw = path.read_text(encoding="utf-8")
    css = re.sub(r"/\*.*?\*/", "", raw, flags=re.S)
    if css.count("{") != css.count("}"):
        bad("CSS", path.name, f"unbalanced braces: {css.count('{')} open, {css.count('}')} close")
    if css.count("(") != css.count(")"):
        bad("CSS", path.name, "unbalanced parentheses")
    # @import must come before every rule
    stripped = css.lstrip()
    first_rule = re.search(r"[^;{}@\s][^;{}]*\{", css)
    for m in re.finditer(r"@import\b", css):
        if first_rule and m.start() > first_rule.start():
            bad("CSS", path.name, "@import appears after a rule (browsers ignore it)")
    light = dark = None
    for sel, body in top_level_blocks(css):
        if sel == ":root" and light is None:
            light = body
        if sel == '[data-md-color-scheme="slate"]' and dark is None:
            dark = body
    if light is None or dark is None:
        bad("CSS", path.name, "need a :root block and a [data-md-color-scheme=\"slate\"] block")
        return
    defs = lambda body: set(re.findall(r"(--ds-[\w-]+)\s*:", body))
    d_light, d_dark = defs(light), defs(dark)
    for t in sorted(d_light - d_dark):
        bad("CSS", path.name, f"{t} is defined for light but not redefined for dark")
    for t in sorted(d_dark - d_light):
        bad("CSS", path.name, f"{t} is defined for dark but not in :root")
    used = set(re.findall(r"var\((--ds-[\w-]+)", css))
    local = set(re.findall(r"(--ds-[\w-]+)\s*:", css)) - d_light - d_dark   # component-local variables
    for t in sorted(used - d_light - local):
        bad("CSS", path.name, f"var({t}) is used but never defined")
    print(f"  {len(d_light)} colour/type tokens defined in both schemes; "
          f"{len(local)} component-local ({', '.join(sorted(local)) or 'none'})")


# ---- syllabus facts and structure -------------------------------------------------------
def read(name):
    return (DOCS / name).read_text(encoding="utf-8")


def check_facts():
    index = read("index.md")
    for label, value in (("Full marks", FULL_MARKS), ("Pass marks", PASS_MARKS),
                         ("Credit hours", CREDITS), ("Total hours", TOTAL_HOURS)):
        if not re.search(rf'ds-label">{label}</span><span class="ds-value">{re.escape(str(value))}<', index):
            bad("FACT", "index.md", f"{label} should be {value}")
    hours = 0
    for n, (stem, title, h, subs, objective) in UNITS.items():
        hours += h
        page = read(f"{stem}.md")
        first = page.split("\n", 1)[0]
        if first != f"# Unit {ROMAN[n]}: {title}":
            bad("FACT", f"{stem}.md", f"H1 should be '# Unit {ROMAN[n]}: {title}', found {first!r}")
        m = re.search(r"\*\*Teaching time:\*\* (\d+) hours?", page)
        if not m or int(m.group(1)) != h:
            bad("FACT", f"{stem}.md", f"Teaching time should be {h} hours")
        card = re.search(rf"\[Unit {ROMAN[n]}: [^\]]+\]\({stem}\.md\)\*\*\s*\n\s*\n\s*---\s*\n\s*\n\s*(\d+) hours", index)
        if not card or int(card.group(1)) != h:
            bad("FACT", "index.md", f"card for Unit {ROMAN[n]} should say {h} hours")
        if objective not in page:
            bad("FACT", f"{stem}.md", "learning objective is not the syllabus sentence")
        found = re.findall(rf"^## {n}\.(\d+) ", page, flags=re.M)
        if len(found) != subs:
            bad("FACT", f"{stem}.md", f"expected {subs} syllabus sub-point heading(s) '## {n}.x', found {len(found)}")
        elif found != [str(i) for i in range(1, subs + 1)]:
            bad("FACT", f"{stem}.md", f"sub-point numbers should run 1..{subs}, found {found}")
        for needed in ("## Quick Recap", "## Try It Yourself", "## Exam Questions for This Unit"):
            if needed not in page:
                bad("FACT", f"{stem}.md", f"missing section '{needed}'")
        anchor = f"exam-questions.md#unit-{ROMAN[n].lower()}-"
        if anchor not in page:
            bad("FACT", f"{stem}.md", f"no link into the exam page ({anchor}...)")
    if hours != TOTAL_HOURS:
        bad("FACT", "units", f"unit hours add up to {hours}, expected {TOTAL_HOURS}")
    labs = re.findall(r"^## Lab (\d+): ", read("practicals.md"), flags=re.M)
    if labs != [str(i) for i in range(1, LABS + 1)]:
        bad("FACT", "practicals.md", f"expected Lab 1..{LABS}, found {labs}")
    exam = read("exam-questions.md")
    for n, (stem, title, *_rest) in UNITS.items():
        if f"## Unit {ROMAN[n]}: {title}\n" not in exam:
            bad("FACT", "exam-questions.md", f"missing section '## Unit {ROMAN[n]}: {title}'")
    print(f"  units: {len(UNITS)}, hours: {hours}, labs: {len(labs)}")


# ---- heading case ----------------------------------------------------------------------
# Title Case rule used across the notes (Chicago style, the same as the syllabus unit names):
# articles, coordinating conjunctions and prepositions stay lowercase unless they start or end the
# heading or follow a colon. Everything else (is, not, up, ...) is capitalized. Words inside
# `code spans` are never touched.
SMALL = {"a", "an", "the", "and", "but", "or", "nor", "for", "at", "by", "in", "of", "on", "to", "as",
         "vs", "via", "with", "from", "into", "over", "per", "than", "onto", "upon"}


def title_words(text):
    """Return (word, must_be_lowercase) for each prose word; code spans count as capitalized words."""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"`[^`]*`", " CODE ", text)
    tokens = re.findall(r"[A-Za-z][A-Za-z'\u2019-]*|:", text)
    out, start = [], True
    words = [t for t in tokens if t != ":"]
    last_word = words[-1] if words else None
    n_seen = 0
    for t in tokens:
        if t == ":":
            start = True
            continue
        n_seen += 1
        is_last = n_seen == len(words)
        lower_ok = t.lower() in SMALL and not start and not is_last
        out.append((t, lower_ok))
        start = False
    return out


def heading_problems(text):
    bad_words = []
    for w, lower_ok in title_words(text):
        if "-" in w or w.isupper() or any(c.isupper() for c in w[1:]):
            continue                     # try-except, CSV, DataFrame
        if lower_ok and w != w.lower():
            bad_words.append(w)
        elif not lower_ok and w[0].islower():
            bad_words.append(w)
    return bad_words


def check_headings():
    for path in sorted(DOCS.glob("*.md")):
        fence = False
        for ln, line in enumerate(path.read_text(encoding="utf-8").split("\n"), 1):
            if line.lstrip().startswith("```"):
                fence = not fence
            m = None if fence else re.match(r"^(#{1,4}) (.+?)\s*$", line)
            if m:
                text = re.sub(r"\s*\{[^}]*\}$", "", m.group(2))
                words = heading_problems(text)
                if words:
                    bad("HEADING", f"{path.name}:{ln}", f"not Title Case ({', '.join(words)}): {text}")


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    site = Path(sys.argv[1])
    if not (site / "index.html").exists():
        sys.exit(f"{site} is not a built site (no index.html)")
    print("1. Leaked markdown and diagrams")
    pages, parsed = check_pages(site)
    print(f"  {len(pages)} pages scanned")
    print("2. Links, anchors and assets")
    check_links(site, parsed)
    print("3. CSS")
    check_css()
    print("4. Syllabus facts and page structure")
    check_facts()
    print("5. Heading case")
    check_headings()
    print(f"\n{len(problems)} problem(s)")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
