"""Rebuild every figure in docs/assets/img/ (a light and a dark PNG for each).

Two sources of figures:

1. Plot code inside the notes. Any Python block marked with
       <!-- figure: u08-hist-marks -->
   is run here and its plt.show() is replaced by "save as u08-hist-marks.png".
   So the code a student reads is exactly the code that drew the picture.
2. Concept pictures (train/test split, under/over-fitting, ...) written as functions
   in scripts/figures/*.py with the @figure("name") decorator from figstyle.py.
3. Interactive Plotly plots. A Python block marked <!-- plotly: u10-scatter --> that ends
   with fig.show() is saved as docs/assets/plotly/u10-scatter.html (+ -dark.html). The
   page embeds it in an <iframe>. plotly.min.js is stored once beside the HTML files, so
   the plots also work offline.

Run:
    python scripts/make_figures.py                      everything
    python scripts/make_figures.py docs/unit-08-eda.md  only figures from that page
    python scripts/make_figures.py --only u08-hist-marks u09-train-test
    python scripts/make_figures.py --list               show what would be built
"""
import argparse
import contextlib
import importlib.util
import os
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
import figstyle  # noqa: E402
import mdblocks as mb  # noqa: E402

THEME_SUFFIX = {"light": "", "dark": "-dark"}
PLOTLY_DIR = mb.DOCS / "assets" / "plotly"


def out_path(name, theme):
    return mb.IMG / f"{name}{THEME_SUFFIX[theme]}.png"


def save_current(name, theme):
    fig = plt.gcf()
    fig.savefig(out_path(name, theme), metadata={"Software": None})
    plt.close("all")


def doc_figures(pages):
    """Yield (kind, name, block) for every figure- or plotly-marked block in the notes."""
    seen = {}
    for path in mb.markdown_files(pages):
        _, blocks = mb.load(path)
        for b in blocks:
            for kind in ("figure", "plotly"):
                name = b.directives.get(kind)
                if not name:
                    continue
                if b.kind != "run":
                    raise SystemExit(f"{path.name}:{b.line}: {kind} block must be a runnable python block")
                if name in seen:
                    raise SystemExit(f"{path.name}:{b.line}: figure name '{name}' already used at {seen[name]}")
                shown = "plt.show()" if kind == "figure" else "fig.show()"
                if b.code.count(shown) != 1:
                    raise SystemExit(f"{path.name}:{b.line}: {kind} '{name}' must call {shown} exactly once")
                seen[name] = f"{path.name}:{b.line}"
                yield kind, name, b


def concept_figures():
    figdir = Path(__file__).resolve().parent / "figures"
    for f in sorted(figdir.glob("*.py")):
        if f.name.startswith("_"):
            continue
        spec = importlib.util.spec_from_file_location(f"figures_{f.stem}", f)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    return figstyle.registry()


@contextlib.contextmanager
def in_folder(path):
    old = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(old)


def render_doc_figure(name, block, theme):
    figstyle.apply(theme)
    plt.show = lambda *a, **k: save_current(name, theme)
    tmp = mb.workdir_with_data(block.files)
    try:
        with in_folder(tmp):
            code = compile(block.full_code, f"{block.path.name}:{block.line}", "exec")
            exec(code, {"__name__": "__main__"})
    finally:
        import shutil
        shutil.rmtree(tmp, ignore_errors=True)
        plt.close("all")


def render_plotly(name, block, theme):
    import plotly.basedatatypes as bdt

    c = figstyle.apply(theme)
    PLOTLY_DIR.mkdir(parents=True, exist_ok=True)

    def save_html(self, *args, **kwargs):
        self.update_layout(
            template="plotly_dark" if theme == "dark" else "plotly_white",
            paper_bgcolor=c["paper"], plot_bgcolor=c["paper"],
            font=dict(color=c["ink"], size=15), colorway=c["series"],
            margin=dict(l=60, r=30, t=60, b=50),
        )
        self.update_xaxes(gridcolor=c["grid"], zerolinecolor=c["grid"])
        self.update_yaxes(gridcolor=c["grid"], zerolinecolor=c["grid"])
        target = PLOTLY_DIR / f"{name}{THEME_SUFFIX[theme]}.html"
        self.write_html(target, include_plotlyjs="directory", full_html=True,
                        config={"displaylogo": False})
        # the page itself must match the notes: no white margin around a dark chart
        html = target.read_text(encoding="utf-8")
        style = f"<style>html,body{{margin:0;background:{c['paper']};overflow:hidden}}</style>"
        target.write_text(html.replace("</head>", style + "</head>", 1), encoding="utf-8")

    import plotly.express as px

    # Plotly Express reads these when it builds a figure, so the site colours apply to every trace
    px.defaults.template = "plotly_dark" if theme == "dark" else "plotly_white"
    px.defaults.color_discrete_sequence = c["series"]
    saved = bdt.BaseFigure.show
    bdt.BaseFigure.show = save_html
    tmp = mb.workdir_with_data(block.files)
    try:
        with in_folder(tmp):
            exec(compile(block.full_code, f"{block.path.name}:{block.line}", "exec"), {"__name__": "__main__"})
    finally:
        bdt.BaseFigure.show = saved
        px.defaults.template = None
        px.defaults.color_discrete_sequence = None
        import shutil
        shutil.rmtree(tmp, ignore_errors=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pages", nargs="*", help="only figures from these markdown pages")
    ap.add_argument("--only", nargs="+", metavar="NAME", help="only these figure names")
    ap.add_argument("--list", action="store_true", help="list figures and exit")
    args = ap.parse_args()

    mb.IMG.mkdir(parents=True, exist_ok=True)
    docs = list(doc_figures(args.pages or None))
    concepts = concept_figures() if not args.pages else {}
    wanted = set(args.only) if args.only else None

    jobs = [(kind, n, b) for kind, n, b in docs] + [("concept", n, fn) for n, fn in concepts.items()]
    jobs = [j for j in jobs if wanted is None or j[1] in wanted]
    if args.list:
        for kind, name, _ in jobs:
            print(f"{kind:8} {name}")
        return
    for kind, name, payload in jobs:
        for theme in ("light", "dark"):
            try:
                if kind == "figure":
                    render_doc_figure(name, payload, theme)
                elif kind == "plotly":
                    render_plotly(name, payload, theme)
                else:
                    figstyle.apply(theme)
                    payload()
                    save_current(name, theme)
            except Exception as e:  # keep going, report at the end
                print(f"FAILED {name} ({theme}): {type(e).__name__}: {e}")
                sys.exit(1)
        print(f"built {kind:8} {name}")
    print(f"\n{len(jobs)} figure(s) x 2 themes -> docs/assets/img and docs/assets/plotly")


if __name__ == "__main__":
    main()
