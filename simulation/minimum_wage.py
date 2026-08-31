"""
simulation/minimum_wage.py

Section 7.3: under a binding minimum-wage floor alpha >= W_min, the firm
re-optimizes gamma over [0,1] against the *clamped* alpha, rather than
retaining the unconstrained gamma*. The binding branch has a closed-form
optimum at gamma_c* = 0.5, independent of H, sigma2, r, or W_min.

Outputs (written next to this script, not to a fixed absolute path):
  - mw_threshold_table.csv   (six-row robustness table, Section 7.3)
  - fig4_minimum_wage.png    (Figure 4: Pi_T, Pi_P*, Pi_P^MW, and optimal gamma)

This module is import-safe: importing it (e.g. from make_figures2.py) only
defines functions and does not run the table/figure pipeline. Run this file
directly (`python minimum_wage.py`) to regenerate the outputs.
"""

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))

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
    Firm's profit-maximizing choice of gamma under a binding wage floor
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


def Pi_P_MW(A, h, theta, C, k, r, sigma2, Ubar_, F_, W_min):
    """
    Convenience wrapper matching the (A, h, theta, C, k, r, sigma2, Ubar, F, W_min)
    argument order used elsewhere in the repo (e.g. make_figures2.py), returning
    just the profit value. Thin pass-through to Pi_P_constrained.
    """
    return Pi_P_constrained(A, W_min, h=h, theta=theta, C=C, k=k, r=r,
                             sigma2=sigma2, U=Ubar_, F=F_)[0]


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


def _main():
    # ------------------------------------------------------------ #
    # 1. Robustness table (Section 7.3): A*_MW across six W_min values
    # ------------------------------------------------------------ #
    W_min_grid = [0.0, 0.02, 0.1, 0.5, 1.0, 1.5]
    results = []
    for W_min in W_min_grid:
        def piP(A, W_min=W_min):
            return Pi_P_constrained(A, W_min)[0]

        A_mw = find_Astar(Pi_T, piP, A_max=50, coarse_n=3000)
        _, gamma_at_star = Pi_P_constrained(A_mw, W_min) if A_mw is not None else (None, None)
        results.append((W_min, A_mw, gamma_at_star))
        print(f"W_min={W_min:>4}: A*_MW = {A_mw:.4f}   (optimal gamma at threshold = {gamma_at_star:.4f})")

    csv_path = os.path.join(HERE, "mw_threshold_table.csv")
    with open(csv_path, "w") as f:
        f.write("W_min,A_star_MW,gamma_at_threshold\n")
        for W_min, A_mw, g in results:
            f.write(f"{W_min},{A_mw:.6f},{g:.6f}\n")
    print(f"\nWrote {csv_path}")

    # ------------------------------------------------------------ #
    # 2. Figure 4: Pi_T, unconstrained Pi_P*, and re-optimized Pi_P^MW
    #    (baseline W_min = 0.5, matching the paper's Figure 4 caption)
    # ------------------------------------------------------------ #
    W_min_fig = 0.5
    A_range = np.linspace(0, 3, 400)

    piT_vals = np.array([Pi_T(A) for A in A_range])
    piP_star_vals = np.array([Pi_P_unconstrained(A) for A in A_range])
    piP_mw_vals = np.array([Pi_P_constrained(A, W_min_fig)[0] for A in A_range])
    gamma_mw_vals = np.array([Pi_P_constrained(A, W_min_fig)[1] for A in A_range])

    # Unconstrained root search widened to 100 (see index.html fix note): a
    # finite A* always exists for positive parameters (Theorem 1), so the
    # search window should not be mistaken for a claim about non-existence.
    A_star_unconstrained = find_Astar(Pi_T, Pi_P_unconstrained, A_max=100, coarse_n=6000)
    A_star_mw_fig = find_Astar(Pi_T, lambda A: Pi_P_constrained(A, W_min_fig)[0], A_max=50, coarse_n=3000)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 9), sharex=True,
                                    gridspec_kw={"height_ratios": [3, 1]})

    ax1.plot(A_range, piT_vals, label=r"$\Pi_T(A)$ (time-rate)", color="#2b6cb0", linewidth=2.2)
    ax1.plot(A_range, piP_star_vals, label=r"$\Pi_P^*(A)$ (piece-rate, unconstrained)",
              color="#c53030", linewidth=2.2, linestyle="--")
    ax1.plot(A_range, piP_mw_vals,
              label=fr"$\Pi_P^{{MW}}(A)$ (piece-rate, $W_{{\min}}={W_min_fig}$)",
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
    ax1.set_title("Figure 4: Minimum-wage floor delays, but does not block,\n"
                   fr"contract transformation ($W_{{\min}}={W_min_fig}$)")
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
    fig_path = os.path.join(HERE, "fig4_minimum_wage.png")
    plt.savefig(fig_path, dpi=200)
    plt.close()

    print(f"\nSaved figure to {fig_path}")
    print(f"Unconstrained A* = {A_star_unconstrained:.4f}")
    print(f"A*_MW (W_min={W_min_fig}) = {A_star_mw_fig:.4f}")


if __name__ == "__main__":
    _main()
