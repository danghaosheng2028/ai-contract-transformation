import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from simulate import Pi_T, Pi_P_star, baseline
from minimum_wage import Pi_P_MW

HERE = os.path.dirname(os.path.abspath(__file__))

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
NAVY, GOLD, GREY, RED = "#1F3864", "#C9A227", "#8C8C8C", "#B44646"

# ---------- Figure 2: minimum-wage regulatory effect ----------
A = np.linspace(0, 3, 400)
p = baseline
piT   = [Pi_T(a, p["a0"], p["h"], p["theta"], p["C"], p["k"], p["Ubar"]) for a in A]
piP   = [Pi_P_star(a, p["h"], p["theta"], p["C"], p["k"], p["r"], p["sigma2"], p["Ubar"], p["F"]) for a in A]
W_MIN = 0.5
piPmw = [Pi_P_MW(a, p["h"], p["theta"], p["C"], p["k"], p["r"], p["sigma2"], p["Ubar"], p["F"], W_MIN) for a in A]

fig, ax = plt.subplots(figsize=(6.4, 3.8), dpi=200)
ax.plot(A, piT, color=GREY, linewidth=2.2, label=r"Time-rate profit $\Pi_T(A)$")
ax.plot(A, piP, color=NAVY, linewidth=2.0, linestyle="--", label=r"Piece-rate profit, unconstrained $\Pi_P^*(A)$")
ax.plot(A, piPmw, color=RED, linewidth=2.2, label=fr"Piece-rate profit under wage floor $\Pi_P^{{MW}}(A)$, $W_{{\min}}={W_MIN}$")
ax.set_xlabel("AI intensity $A$")
ax.set_ylabel("Firm profit")
ax.set_title("Figure 2. Minimum-wage floor removes the piece-rate\nadvantage over the empirically relevant AI-intensity range", fontsize=10.5)
ax.legend(loc="upper left", frameon=False, fontsize=8.3)
ax.spines[["top", "right"]].set_visible(False)
plt.tight_layout()
plt.savefig(os.path.join(HERE, "fig2_minimum_wage.png"), transparent=True)
plt.close()

# ---------- Figure 4: model timing schematic ----------
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
    ax.text(x + box_w/2, 1.28, num, color=GOLD, fontsize=13, fontweight="bold", ha="center")
    ax.text(x + box_w/2, 0.85, text, color="white", fontsize=8.3, ha="center", va="center")
    if i < len(steps) - 1:
        ax.annotate("", xy=(x + box_w + gap, 1.0), xytext=(x + box_w, 1.0),
                    arrowprops=dict(arrowstyle="-|>", color="#444444", lw=1.6))
    x += box_w + gap

plt.tight_layout()
plt.savefig(os.path.join(HERE, "fig4_timing.png"), transparent=True)
plt.close()

print("figures 2 and 4 saved")
