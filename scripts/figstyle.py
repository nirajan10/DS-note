"""Look of every plot in the notes: one place, two themes (light and dark).

Colours follow a validated categorical order (blue, orange, aqua, yellow, ...).
Use at most THREE series in a scatter plot; add a legend or direct labels,
because aqua is below 3:1 contrast on the light page.

The plot code shown in the notes stays plain (no colours set by hand). This module
supplies the colours, fonts and sizes when make_figures.py renders the PNGs.
"""
from __future__ import annotations

import matplotlib as mpl
from matplotlib.colors import LinearSegmentedColormap

# Page backgrounds must match docs/stylesheets/extra.css (--ds-paper in each scheme).
THEMES = {
    "light": dict(
        paper="#f7f8fa", ink="#14202e", ink2="#46536a", muted="#6b778c",
        grid="#dfe4ec", baseline="#b8c0cd",
        series=["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#4a3aa7", "#e34948"],
        seq=["#eaf2fc", "#9ec5f4", "#3987e5", "#1c5cab", "#0d366b"],
        div=["#2a78d6", "#f0efec", "#e34948"],
        accent="#eda100",
    ),
    "dark": dict(
        paper="#0f1520", ink="#e8ecf3", ink2="#b4bccb", muted="#8b95a7",
        grid="#223049", baseline="#34415a",
        series=["#3987e5", "#d95926", "#199e70", "#c98500", "#d55181", "#008300", "#9085e9", "#e66767"],
        seq=["#16283f", "#184f95", "#2a78d6", "#6da7ec", "#cde2fb"],
        div=["#3987e5", "#383835", "#e66767"],
        accent="#ffc233",
    ),
}

_REGISTRY: dict[str, callable] = {}


def figure(name):
    """Decorator: register a function that draws a concept figure (no savefig needed)."""
    def wrap(fn):
        _REGISTRY[name] = fn
        return fn
    return wrap


def registry():
    return dict(_REGISTRY)


_current = "light"


def colors(theme):
    return THEMES[theme]


def current():
    """Colours of the theme being rendered right now (use inside @figure functions)."""
    return THEMES[_current]


def apply(theme):
    """Set matplotlib defaults for the theme and return its colour dictionary."""
    global _current
    _current = theme
    c = THEMES[theme]
    mpl.rcdefaults()
    mpl.rcParams.update({
        "figure.figsize": (8, 4.5),
        "figure.dpi": 100,
        "savefig.dpi": 150,
        "figure.facecolor": c["paper"],
        "savefig.facecolor": c["paper"],
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.25,
        "figure.constrained_layout.use": True,
        "axes.facecolor": c["paper"],
        "axes.edgecolor": c["baseline"],
        "axes.linewidth": 1.2,
        "axes.labelcolor": c["ink2"],
        "axes.titlecolor": c["ink"],
        "axes.titlesize": 18,
        "axes.titleweight": "bold",
        "axes.titlelocation": "left",
        "axes.titlepad": 12,
        "axes.labelsize": 15,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.axisbelow": True,
        "axes.grid": True,
        "axes.grid.axis": "y",
        "axes.prop_cycle": mpl.cycler(color=c["series"]),
        "grid.color": c["grid"],
        "grid.linewidth": 1.0,
        "xtick.color": c["muted"],
        "ytick.color": c["muted"],
        "xtick.labelcolor": c["ink2"],
        "ytick.labelcolor": c["ink2"],
        "xtick.labelsize": 13,
        "ytick.labelsize": 13,
        "xtick.major.size": 4,
        "ytick.major.size": 0,
        "text.color": c["ink"],
        "font.family": "DejaVu Sans",
        "font.size": 14,
        "lines.linewidth": 2.4,
        "lines.markersize": 9,
        "patch.linewidth": 1.5,          # thin gap between touching bars
        "patch.edgecolor": c["paper"],
        "patch.force_edgecolor": True,
        "scatter.edgecolors": c["paper"],
        "legend.fontsize": 13,
        "legend.frameon": False,
        "legend.labelcolor": c["ink2"],
        "boxplot.boxprops.color": c["ink2"],
        "boxplot.boxprops.linewidth": 2.0,
        "boxplot.whiskerprops.color": c["ink2"],
        "boxplot.whiskerprops.linewidth": 2.0,
        "boxplot.capprops.color": c["ink2"],
        "boxplot.capprops.linewidth": 2.0,
        "boxplot.medianprops.color": c["series"][1],
        "boxplot.medianprops.linewidth": 2.6,
        "boxplot.flierprops.markeredgecolor": c["ink2"],
        "boxplot.flierprops.markersize": 8,
    })
    # Same colormap *names* the notes use (e.g. cmap="Blues"), but tuned for each theme.
    seq = LinearSegmentedColormap.from_list("Blues", c["seq"])
    div = LinearSegmentedColormap.from_list("coolwarm", c["div"])
    # matplotlib refuses to re-register built-in names, so swap them in its table directly
    table = mpl.colormaps._cmaps
    for cmap in (seq, div):
        table[cmap.name] = cmap
        table[cmap.name + "_r"] = cmap.reversed(name=cmap.name + "_r")
    return c
