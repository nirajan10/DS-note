# Fundamentals of Data Science (DSC 481)

Lecture notes and lab sheets for **DSC 481 Fundamentals of Data Science**, BCSIT, Pokhara University.
Built with [MkDocs](https://www.mkdocs.org/) and the [Material](https://squidfunnel.github.io/mkdocs-material/) theme.
Every code example has been run, and the output shown under it is the real output.

## Quick start

```bash
make install     # create .venv and install everything
make serve       # live preview at http://127.0.0.1:8000
make build       # strict build into ./site
```

| Command | What it does |
|---------|--------------|
| `make figures` | Rebuild every PNG in `docs/assets/img/` (light and dark) and the interactive Plotly files in `docs/assets/plotly/` |
| `make data` | Rebuild the small practice datasets in `docs/assets/data/` |
| `make examples` | Re-run every Python example and rewrite its Output block |
| `make check` | Examples match real output, strict build passes, and the built HTML is inspected |

The first `make build` or `make serve` downloads the web fonts once and stores them in `.cache/`, so later builds
and the finished site work without internet. For a fully offline build, run it with `PRIVACY_PLUGIN=false`.

## Releasing topics gradually

Only the pages listed in `nav:` in `mkdocs.yml` are published. Everything else is **not built at all** (no page,
no URL, no search result), and links to it become plain text. Each topic has three lines in the nav: its note
(`unit-NN-*.md`), its lab sheet (`labs/lab-NN.md`, Units I to X) and its exam questions (`exam/unit-NN.md`).

1. Open `mkdocs.yml` and remove the `# ` in front of the topic's lines. Each line is independent, so
   uncommenting one topic never reveals another.
2. Rebuild and publish: `make build` (output in `site/`), or watch it live with `make serve`.
3. To hide a topic again, put the `# ` back.

`make build-all` builds the whole course (every topic released, via `mkdocs-all.yml`) into `site-all/`. That is
for checking only; do not give it to students. One limit: images and data files of a hidden topic are still
copied into `site/assets/`, so someone who guesses a file name could open it. The pages and their text are not
there.

## Layout

```
docs/                 notes (unit-NN-*.md), labs/lab-NN.md, exam/unit-NN.md, plus index, setup, references
hooks/release.py      publishes only the pages listed in the nav (see above)
mkdocs-all.yml        the same site with every topic released (for checks)
docs/assets/data/     practice datasets (small CSV, JSON, XLSX files and one zip)
docs/assets/img/      generated figures (do not edit by hand; run make figures)
docs/stylesheets/     the site design (colour tokens for light and dark, fonts, layout)
scripts/              build and check helpers (run_examples, make_figures, make_data, verify_site, page_stats, ...)
AUTHORING.md          how to write or change a page (rules, markup, directives)
```

To change a page, read `AUTHORING.md` first.

## Checks that were run

`make check` re-runs every code example and compares it with the output shown, builds with `--strict`, and inspects
the built HTML. Other scripts open the built site in a real browser (headless Chromium): `scripts/mobile_check.py`
(no sideways scroll at phone width) and `scripts/offline_check.py` (fonts and diagrams work with the network blocked).
