"""
make_figures2.py — Figure 1 (model timing schematic) only.

Figure 4 (minimum-wage floor) used to be generated here as well as in
minimum_wage.py, using two different implementations that had drifted out
of sync (this file imported a Pi_P_MW function that didn't actually exist
in minimum_wage.py). Figure 4 generation now lives solely in
minimum_wage.py — run `python minimum_wage.py` to regenerate it and
mw_threshold_table.csv. This file keeps only Figure 1, which nothing else
in the repo produces.
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
NAVY, GOLD, GREY, RED = "#1F3864", "#C9A227", "#8C8C8C", "#B44646"

# ---------- Figure 1: model timing schematic ----------
fig, ax = plt.subplots(figsize=(7.2, 2.0), dpi=200)
ax.set_xlim(0, 10)
ax.set_ylim(0, 2)
ax.axis("off")

steps = [
    ("1", "Firm chooses\ncontract mode\n(time-rate or\npiece-rate)"),
    ("2", "Under piece-rate,\nfirm sets\n" + r"$(\alpha,\gamma)$"),
    ("3", "Worker chooses\neffort " + r"$a$"),
    ("4", "Output realized;\nwage paid"),
]
box_w, gap = 2.0, 0.55
x = 0.3
for i, (num, text) in enumerate(steps):
    color = NAVY if i % 2 == 0 else "#2E5590"
    rect = plt.Rectangle((x, 0.5), box_w, 1.0, facecolor=color, edgecolor="none", alpha=0.9)
    ax.add_patch(rect)
    ax.text(x + box_w / 2, 1.28, num, color=GOLD, fontsize=13, fontweight="bold", ha="center")
    ax.text(x + box_w / 2, 0.85, text, color="white", fontsize=8.3, ha="center", va="center")
    if i < len(steps) - 1:
        ax.annotate("", xy=(x + box_w + gap, 1.0), xytext=(x + box_w, 1.0),
                    arrowprops=dict(arrowstyle="-|>", color="#444444", lw=1.6))
    x += box_w + gap

plt.tight_layout()
fig_path = os.path.join(HERE, "fig1_timing.png")
plt.savefig(fig_path, transparent=True)
plt.close()

print("figure 1 saved:", fig_path)
