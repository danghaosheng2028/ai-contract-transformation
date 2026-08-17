import sys
import numpy as np
from scipy.optimize import brentq
from simulate import Htilde, Pi_T, baseline, solve_A_star

try:
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:
    pass

def gamma_star(A, h, theta, C, k, r, sigma2):
    H = Htilde(A, h, theta, C)
    return H**2 / (H**2 + r * k * sigma2)

def alpha_star(A, h, theta, C, k, r, sigma2, Ubar):
    H = Htilde(A, h, theta, C)
    g = gamma_star(A, h, theta, C, k, r, sigma2)
    return Ubar + 0.5 * r * g**2 * sigma2 - 0.5 / k * g**2 * H**2

def Pi_P_MW(A, h, theta, C, k, r, sigma2, Ubar, F, Wmin):
    H = Htilde(A, h, theta, C)
    g = gamma_star(A, h, theta, C, k, r, sigma2)
    a_star = g * H / k
    alpha = alpha_star(A, h, theta, C, k, r, sigma2, Ubar)
    alpha_mw = max(Wmin, alpha)
    return (1 - g) * a_star * H - alpha_mw - F

def G_mw(A, params, Wmin):
    a0, h, theta, C, k, Ubar, r, sigma2, F = params
    return Pi_P_MW(A, h, theta, C, k, r, sigma2, Ubar, F, Wmin) - Pi_T(A, a0, h, theta, C, k, Ubar)

def solve_A_star_mw(params, Wmin, A_max=10.0):
    lo, hi = 0.0, A_max
    if G_mw(hi, params, Wmin) < 0:
        return None  # no finite crossing within [0, A_max] -> piece-rate never overtakes time-rate there
    return brentq(G_mw, lo, hi, args=(params, Wmin))

if __name__ == "__main__":
    p = baseline
    params = tuple(p.values())
    A_star = solve_A_star(params)
    print(f"Baseline A* (no minimum wage) = {A_star:.4f}")

    # Sweep several wage floors -- see paper Section 7.3 for why even a small
    # positive W_min prevents a finite crossing under baseline calibration.
    for W_min in [0.0, 0.02, 0.1, 0.5, 1.0, 1.5]:
        A_star_mw = solve_A_star_mw(params, W_min, A_max=50.0)
        if A_star_mw is None:
            print(f"W_min={W_min:<5} -> A*_MW does not exist for A in [0,50]: "
                  f"piece-rate profit never overtakes time-rate profit under this wage floor")
        else:
            print(f"W_min={W_min:<5} -> A*_MW = {A_star_mw:.4f}  "
                  f"(regulatory delay Delta A = {A_star_mw - A_star:.4f})")
