"""Unit IX concept picture: how train_test_split divides 60 student rows."""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch, Rectangle
from sklearn.model_selection import train_test_split

from figstyle import current, figure


@figure("u09-train-test-split")
def train_test_split_strip():
    c = current()
    rows = np.arange(60)
    # the very same call the notes use, so the picture shows the real split
    _, test_rows = train_test_split(rows, test_size=0.2, random_state=42)
    test_rows = set(test_rows.tolist())

    fig, ax = plt.subplots(figsize=(8, 4.2))
    top, bottom = 2.3, 0.0
    for i in rows:
        ax.add_patch(Rectangle((i, top), 0.82, 1, color=c["muted"], lw=0))
        colour = c["series"][1] if i in test_rows else c["series"][0]
        ax.add_patch(Rectangle((i, bottom), 0.82, 1, color=colour, lw=0))

    ax.text(0, top + 1.3, "study_marks.csv: 60 student rows", fontsize=14, color=c["ink"], va="bottom")
    ax.annotate(
        "", xy=(4, bottom + 1.25), xytext=(4, top - 0.25),
        arrowprops=dict(arrowstyle="-|>", color=c["ink2"], lw=2),
    )
    ax.text(6, 1.75, "train_test_split(test_size=0.2, random_state=42)",
            fontsize=13, color=c["ink2"], va="center")
    ax.text(0, bottom - 0.35, "The same 60 rows after the split (test rows are picked at random)",
            fontsize=13, color=c["ink2"], va="top")

    ax.set_xlim(-0.5, 60.5)
    ax.set_ylim(-2.2, 4.2)
    ax.set_axis_off()
    ax.set_title("Hold back 20% of the rows for testing")
    ax.legend(
        handles=[
            Patch(color=c["series"][0], label="Training data: 48 rows (80%), used by fit"),
            Patch(color=c["series"][1], label="Test data: 12 rows (20%), used only to check"),
        ],
        loc="lower center", bbox_to_anchor=(0.5, -0.04), ncol=1, handlelength=1.2,
    )
