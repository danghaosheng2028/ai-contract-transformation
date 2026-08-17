"""
From Hours to Output -- simulation code
Computes the AI-intensity contract-transformation threshold A*
under baseline and sector-heterogeneous calibrations.
"""
import sys
import os
import json
import numpy as np
from scipy.optimize import brentq

# Make console output UTF-8 safe (fixes garbled Chinese text on Windows terminals)
try:
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:
    pass  # Python < 3.7 fallback, not expected here

# Always resolve paths relative to this script's own folder,
# so the code works no matter what directory it's run from.
HERE = os.path.dirname(os.path.abspath(__file__))

def Htilde(A, h, theta, C):
    return h + theta * A * C

def Pi_T(A, a0, h, theta, C, k, Ubar):
    return a0 * Htilde(A, h, theta, C) - Ubar - 0.5 * k * a0**2

def Pi_P_star(A, h, theta, C, k, r, sigma2, Ubar, F):
    H = Htilde(A, h, theta, C)
    return (H**4) / (2 * k * (H**2 + r * k * sigma2)) - Ubar - F

def G(A, params):
    a0, h, theta, C, k, Ubar, r, sigma2, F = params
    return Pi_P_star(A, h, theta, C, k, r, sigma2, Ubar, F) - Pi_T(A, a0, h, theta, C, k, Ubar)

def solve_A_star(params, A_max=10.0):
    # G(0) < 0 by construction (fixed cost F); find sign change up to A_max
    lo, hi = 0.0, A_max
    if G(hi, params) < 0:
        return None  # no crossing within range -> firm never transforms (time-rate dominant)
    return brentq(G, lo, hi, args=(params,))

# ---- Baseline calibration (paper Section 3.4) ----
baseline = dict(a0=1.0, h=2.0, theta=1.5, C=1.0, k=1.0, Ubar=1.0, r=1.0, sigma2=1.0, F=1.5)
base_params = tuple(baseline.values())
A_star_base = solve_A_star(base_params)

# ---- Sector heterogeneity ----
sectors = {
    "外卖/网约配送骑手 (Delivery riders)":      dict(C=1.2, sigma2=0.5, r=0.8),
    "直播主播 (Livestream hosts)":              dict(C=1.5, sigma2=1.8, r=1.0),
    "设计/知识工作者 (Designers, knowledge work)": dict(C=1.3, sigma2=1.3, r=1.5),
    "传统制造业产线工人 (Manufacturing line workers)": dict(C=0.4, sigma2=0.7, r=1.0),
}

def _compute_sector_results():
    results = {}
    for name, ov in sectors.items():
        p = dict(baseline)
        p.update(ov)
        params = tuple(p.values())
        results[name] = solve_A_star(params, A_max=10.0)
    return results

if __name__ == "__main__":
    print(f"Baseline A* = {A_star_base:.4f}")
    print("\nSector heterogeneity (baseline h, theta, k, a0, Ubar, F unchanged):")
    results = _compute_sector_results()
    for name, ov in sectors.items():
        A_star = results[name]
        if A_star is None:
            print(f"  {name}: C={ov['C']}, sigma2={ov['sigma2']}, r={ov['r']}  ->  A* > 10 (effectively never transforms)")
        else:
            print(f"  {name}: C={ov['C']}, sigma2={ov['sigma2']}, r={ov['r']}  ->  A* = {A_star:.3f}")

    out_path = os.path.join(HERE, "results.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump({"baseline_A_star": A_star_base,
                   "sectors": {k: (v if v is None else round(v, 4)) for k, v in results.items()}},
                  f, ensure_ascii=False, indent=2)
    print(f"\nWrote {out_path}")
