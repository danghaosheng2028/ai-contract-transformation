"""
simulation/minimum_wage.py  (revised)

Regenerates Figure 2 with the corrected constrained-optimization logic:
under a binding minimum-wage floor, the firm re-optimizes gamma rather
than retaining the unconstrained gamma*. The binding branch has a closed
form optimum at gamma_c* = 0.5, independent of H, sigma2, r, or W_min.

This replaces the earlier (incorrect) version of this script, which held
gamma fixed at the unconstrained optimum while only raising alpha to
W_min -- an inconsistent comparison, since a firm facing a binding wage
floor has no reason to retain the incentive slope optimal only in the
absence of that floor. See Section 7.3 (revised) of the paper.

Outputs:
  - simulation/fig2_minimum_wage.png   (the revised Figure 2)
  - simulation/mw_threshold_table.csv  (the six-row robustness table, Section 7.3)
"""

import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------------- #
# Baseline calibration (Section 3.4)
# ---------------------------------------------------------------- #
h, theta, C, k, a0, Ubar, r, sigma2, F = 2.0, 1.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.5


def Htilde(A, theta=theta, C=C, h=h):
    return h + theta * A * C


def Pi_T(A, h=h, theta=theta, C=C, k=k, a0=a0, U=Ubar):
    return a0 * (h + theta * A * C) - U - 0.5 * k * a0 ** 2


def Pi_P_unconstrained(A, h=h, theta=theta, C=C, k=k, r=r, sigma2=sigma2, U=Ubar, F=F):
    """Section 5.2 closed-form optimal piece-rate profit (no wage floor)."""
    H = Htilde(A, theta, C, h)
    return H ** 4 / (2 * k * (H ** 2 + r * k * sigma2)) - U - F


def Pi_P_constrained(A, W_min, h=h, theta=theta, C=C, k=k, r=r, sigma2=sigma2,
                      U=Ubar, F=F, n_grid=4000):
    """
    Correctly re-optimized piece-rate profit under a binding wage floor
    alpha >= W_min. For each gamma in [0,1], alpha(gamma) = max(W_min,
    alpha_star(gamma)); profit is then maximized numerically over gamma.
    Returns (max_profit, optimal_gamma).
    """
    H = Htilde(A, theta, C, h)
    gammas = np.linspace(0.0, 1.0, n_grid)
    a_star = gammas * H / k
    alpha_star = U + 0.5 * r * gammas ** 2 * sigma2 - (gammas ** 2 * H ** 2) / (2 * k)
    alpha = np.maximum(W_min, alpha_star)
    profit = (1 - gammas) * a_star * H - alpha - F
    idx = np.argmax(profit)
    return profit[idx], gammas[idx]


def find_Astar(profit_fn_T, profit_fn_P, A_max=50.0, coarse_n=4000):
    """Bisection root-find for the first crossing of Pi_P - Pi_T = 0."""
    As = np.linspace(0, A_max, coarse_n)
    diffs = np.array([profit_fn_P(A) - profit_fn_T(A) for A in As])
    sign_change = np.where((diffs[:-1] < 0) & (diffs[1:] >= 0))[0]
    if len(sign_change) == 0:
        return None
    i = sign_change[0]
    lo, hi = As[i], As[i + 1]
    for _ in range(60):
        mid = (lo + hi) / 2
        if profit_fn_P(mid) - profit_fn_T(mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


# ---------------------------------------------------------------- #
# 1. Robustness table (Section 7.3): A*_MW across six W_min values
# ---------------------------------------------------------------- #
W_min_grid = [0.0, 0.02, 0.1, 0.5, 1.0, 1.5]
results = []
for W_min in W_min_grid:
    def piP(A, W_min=W_min):
        return Pi_P_constrained(A, W_min)[0]

    A_mw = find_Astar(Pi_T, piP, A_max=50, coarse_n=3000)
    _, gamma_at_star = Pi_P_constrained(A_mw, W_min) if A_mw is not None else (None, None)
    results.append((W_min, A_mw, gamma_at_star))
    print(f"W_min={W_min:>4}: A*_MW = {A_mw:.4f}   (optimal gamma at threshold = {gamma_at_star:.4f})")

with open("/home/claude/mw_threshold_table.csv", "w") as f:
    f.write("W_min,A_star_MW,gamma_at_threshold\n")
    for W_min, A_mw, g in results:
        f.write(f"{W_min},{A_mw:.6f},{g:.6f}\n")

# ---------------------------------------------------------------- #
# 2. Figure 2: Pi_T, unconstrained Pi_P*, and corrected Pi_P^MW
#    (baseline W_min = 0.5, matching the paper's Figure 2 caption)
# ---------------------------------------------------------------- #
W_min_fig = 0.5
A_range = np.linspace(0, 3, 400)

piT_vals = np.array([Pi_T(A) for A in A_range])
piP_star_vals = np.array([Pi_P_unconstrained(A) for A in A_range])
piP_mw_vals = np.array([Pi_P_constrained(A, W_min_fig)[0] for A in A_range])
gamma_mw_vals = np.array([Pi_P_constrained(A, W_min_fig)[1] for A in A_range])

A_star_unconstrained = find_Astar(Pi_T, Pi_P_unconstrained, A_max=10, coarse_n=3000)
A_star_mw_fig = find_Astar(Pi_T, lambda A: Pi_P_constrained(A, W_min_fig)[0], A_max=10, coarse_n=3000)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 9), sharex=True,
                                gridspec_kw={"height_ratios": [3, 1]})

ax1.plot(A_range, piT_vals, label=r"$\Pi_T(A)$ (time-rate)", color="#2b6cb0", linewidth=2.2)
ax1.plot(A_range, piP_star_vals, label=r"$\Pi_P^*(A)$ (piece-rate, unconstrained)",
          color="#c53030", linewidth=2.2, linestyle="--")
ax1.plot(A_range, piP_mw_vals, label=fr"$\Pi_P^{{MW}}(A)$ (piece-rate, $W_{{\min}}={W_min_fig}$, $\gamma$ re-optimized)",
          color="#2f855a", linewidth=2.4)

ax1.axvline(A_star_unconstrained, color="#c53030", linestyle=":", alpha=0.6)
ax1.axvline(A_star_mw_fig, color="#2f855a", linestyle=":", alpha=0.6)
ax1.annotate(fr"$A^*\approx{A_star_unconstrained:.2f}$", xy=(A_star_unconstrained, ax1.get_ylim()[0]),
             xytext=(A_star_unconstrained + 0.05, min(piT_vals) - 0.3),
             color="#c53030", fontsize=9)
ax1.annotate(fr"$A^*_{{MW}}\approx{A_star_mw_fig:.2f}$", xy=(A_star_mw_fig, ax1.get_ylim()[0]),
             xytext=(A_star_mw_fig + 0.05, min(piT_vals) - 0.7),
             color="#2f855a", fontsize=9)

ax1.set_ylabel("Firm profit")
ax1.set_title(r"Figure 2 (revised): $\Pi_P^{MW}(A)$ under correctly re-optimized $\gamma$" + "\n"
               fr"Minimum-wage floor delays but does not block transformation ($W_{{\min}}={W_min_fig}$)")
ax1.legend(loc="upper left", fontsize=9)
ax1.grid(alpha=0.25)

ax2.plot(A_range, gamma_mw_vals, color="#2f855a", linewidth=2.0, label=r"optimal $\gamma$ under binding floor")
ax2.axhline(0.5, color="gray", linestyle=":", linewidth=1, label=r"$\gamma_c^*=0.5$ (closed form, binding branch)")
ax2.set_xlabel("AI intensity $A$")
ax2.set_ylabel(r"optimal $\gamma$")
ax2.set_ylim(-0.05, 1.05)
ax2.legend(loc="lower right", fontsize=8)
ax2.grid(alpha=0.25)

plt.tight_layout()
plt.savefig("/home/claude/fig2_minimum_wage.png", dpi=200)
print("\nSaved figure to fig2_minimum_wage.png")
print(f"Unconstrained A* = {A_star_unconstrained:.4f}")
print(f"A*_MW (W_min={W_min_fig}) = {A_star_mw_fig:.4f}")
