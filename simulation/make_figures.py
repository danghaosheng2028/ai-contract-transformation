import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from simulate import Pi_T, Pi_P_star, baseline, sectors, solve_A_star

HERE = os.path.dirname(os.path.abspath(__file__))

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
NAVY, GOLD, GREY, RED = "#1F3864", "#C9A227", "#8C8C8C", "#B44646"

# ---------- Figure 3: baseline profit curves ----------
A = np.linspace(0, 3, 400)
p = baseline
piT = [Pi_T(a, p["a0"], p["h"], p["theta"], p["C"], p["k"], p["Ubar"]) for a in A]
piP = [Pi_P_star(a, p["h"], p["theta"], p["C"], p["k"], p["r"], p["sigma2"], p["Ubar"], p["F"]) for a in A]
A_star = solve_A_star(tuple(p.values()))

fig, ax = plt.subplots(figsize=(6.2, 3.6), dpi=200)
ax.plot(A, piT, color=GREY, linewidth=2.2, label=r"Time-rate profit $\Pi_T(A)$")
ax.plot(A, piP, color=NAVY, linewidth=2.2, label=r"Piece-rate profit $\Pi_P^*(A)$")
ax.axvline(A_star, color=RED, linestyle="--", linewidth=1.3)
ax.scatter([A_star], [Pi_T(A_star, p["a0"], p["h"], p["theta"], p["C"], p["k"], p["Ubar"])],
           color=RED, zorder=5, s=35)
ax.annotate(f"$A^*\\approx{A_star:.2f}$", xy=(A_star, -0.3), xytext=(A_star+0.15, -1.2),
            fontsize=10, color=RED)
ax.fill_between(A, -3, 4, where=(np.array(A) < A_star), color=GREY, alpha=0.07)
ax.fill_between(A, -3, 4, where=(np.array(A) >= A_star), color=NAVY, alpha=0.07)
ax.set_xlabel("AI intensity $A$")
ax.set_ylabel("Firm profit")
ax.set_ylim(-2, 3.5)
ax.set_title("Figure 3. Contract transformation threshold\n(baseline calibration)", fontsize=10.5)
ax.legend(loc="upper left", frameon=False, fontsize=9)
ax.spines[["top", "right"]].set_visible(False)
plt.tight_layout()
plt.savefig(os.path.join(HERE, "fig3_threshold.png"), transparent=True)
plt.close()

# ---------- Figure 5: sector heterogeneity ----------
names_cn = ["Delivery\nriders", "Livestream\nhosts", "Designers /\nknowledge work", "Manufacturing\nline workers"]
astars = []
for name, ov in sectors.items():
    pp = dict(baseline); pp.update(ov)
    a = solve_A_star(tuple(pp.values()), A_max=10.0)
    astars.append(a if a is not None else 10.0)

fig, ax = plt.subplots(figsize=(6.2, 3.6), dpi=200)
colors = [NAVY if a < 3 else RED for a in astars]
bars = ax.bar(names_cn, astars, color=colors, width=0.55)
for b, a in zip(bars, astars):
    label = f"{a:.2f}" if a < 3 else ">10\n(never)"
    ax.text(b.get_x()+b.get_width()/2, min(a, 2.6)+0.08, label, ha="center", fontsize=9, fontweight="bold")
ax.axhline(0.65, color=GOLD, linestyle=":", linewidth=1.3)
ax.text(3.35, 0.72, "baseline $A^*\\approx0.65$", color=GOLD, fontsize=8.5, ha="right")
ax.set_ylabel("Transformation threshold $A^*$")
ax.set_ylim(0, 3)
ax.set_title("Figure 5. Sector-heterogeneous transformation thresholds\n(lower = firms switch to piece-rate at lower AI intensity)", fontsize=10.5)
ax.spines[["top", "right"]].set_visible(False)
plt.tight_layout()
plt.savefig(os.path.join(HERE, "fig5_heterogeneity.png"), transparent=True)
plt.close()

print("figures saved:", os.path.join(HERE, "fig3_threshold.png"), "and", os.path.join(HERE, "fig5_heterogeneity.png"))
