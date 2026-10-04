import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from figstyle import figure, current


@figure("u05-set-venn")
def set_venn():
    c = current()
    fig, ax = plt.subplots(figsize=(8, 4.8))
    ax.set_axis_off()
    ax.set_aspect("equal")
    ax.set_xlim(-3.2, 4.2)
    ax.set_ylim(-2.3, 2.5)

    # two overlapping circles
    ax.add_patch(Circle((0, 0), 1.7, facecolor=c["series"][0], alpha=0.35,
                        edgecolor=c["series"][0], linewidth=2.5))
    ax.add_patch(Circle((2.0, 0), 1.7, facecolor=c["series"][1], alpha=0.35,
                        edgecolor=c["series"][1], linewidth=2.5))

    # names inside the three regions
    ax.text(-0.7, 0, "Asha\nBikash", ha="center", va="center", fontsize=15, color=c["ink"])
    ax.text(1.0, 0, "Sita\nRam", ha="center", va="center", fontsize=15, color=c["ink"])
    ax.text(2.7, 0, "Gita", ha="center", va="center", fontsize=15, color=c["ink"])

    # set names above the circles
    ax.text(-0.2, 2.0, "python_class", ha="center", fontsize=15, fontweight="bold",
            color=c["series"][0])
    ax.text(2.2, 2.0, "stats_class", ha="center", fontsize=15, fontweight="bold",
            color=c["series"][1])

    # what each region is called
    kw = dict(ha="center", va="center", fontsize=12, color=c["ink2"])
    ax.text(-0.95, -2.1, "difference\npython_class\n- stats_class", **kw)
    ax.text(1.0, -2.1, "intersection\npython_class\n& stats_class", **kw)
    ax.text(2.95, -2.1, "difference\nstats_class\n- python_class", **kw)
    ax.text(1.0, -3.15, "union (python_class | stats_class) = everyone in either circle", **kw)
    ax.set_ylim(-3.5, 2.5)
    ax.set_title("Two Sets and What They Share")
