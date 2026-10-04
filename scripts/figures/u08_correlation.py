"""Unit VIII concept figure: three scatter plots with a strong positive link,
no link and a strong negative link. All data is made up and seeded."""
import matplotlib.pyplot as plt
import numpy as np

from figstyle import current, figure


@figure("u08-correlation")
def correlation_patterns():
    c = current()
    rng = np.random.default_rng(42)
    n = 60

    hours = rng.uniform(0.5, 9, n)
    marks_up = 20 + 7 * hours + rng.normal(0, 8, n)

    shoe = rng.uniform(5, 11, n)
    marks_none = rng.normal(50, 15, n)
    # remove any accidental straight-line pattern so that r is almost exactly 0
    marks_none = marks_none - np.polyval(np.polyfit(shoe, marks_none, 1), shoe) + 50

    absent = rng.uniform(0, 12, n)
    marks_down = 85 - 5 * absent + rng.normal(0, 8, n)

    panels = [
        ("Strong positive", "Hours studied", hours, marks_up),
        ("No relation", "Shoe size", shoe, marks_none),
        ("Strong negative", "Days absent", absent, marks_down),
    ]

    fig, axes = plt.subplots(1, 3, figsize=(10.5, 4.6), sharey=True)
    for ax, (name, xlabel, x, y) in zip(axes, panels):
        r = round(float(np.corrcoef(x, y)[0, 1]), 2) + 0.0   # + 0.0 turns -0.0 into 0.0
        label = f"{r:+.2f}" if r else "0.00"
        ax.scatter(x, y, s=55, color=c["series"][0])
        ax.set_title(f"{name}\nr = {label}", fontsize=16)
        ax.set_xlabel(xlabel)
        ax.locator_params(axis="x", nbins=5)
        ax.grid(axis="x", visible=False)
    axes[0].set_ylabel("Marks")
