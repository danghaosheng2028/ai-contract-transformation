# From Hours to Output — Simulation Code

Reproduces the baseline contract-transformation threshold (A*) and the
sector-heterogeneity results reported in Sections 6–7 of the paper
*"From Hours to Output: A Principal–Agent Theory of AI-Driven Contract
Transformation and the Limits of Minimum-Wage Protection in China's
Platform Economy."*

## Files
- `simulate.py` — closed-form profit functions Π_T(A), Π_P*(A); root-finds
  the transformation threshold A* for the baseline calibration and for
  four illustrative worker types (delivery riders, livestream hosts,
  designers/knowledge workers, manufacturing line workers).
- `make_figures.py` — generates Figure 1 (baseline threshold crossing) and
  Figure 3 (sector-heterogeneous thresholds) used in the paper.
- `results.json` — numerical output (A* values) for citation/reproducibility.

## Usage
```bash
pip install numpy scipy matplotlib
python simulate.py        # prints A* for baseline + all sectors
python make_figures.py    # writes fig1_threshold.png, fig3_heterogeneity.png
```

## Baseline calibration
| Parameter | Value | Source |
|---|---|---|
| h (baseline human capital) | 2.0 | Section 3.4 |
| θ (AI amplification) | 1.5 | Section 3.4 |
| C (complementarity) | 1.0 | Section 3.4 |
| k (effort cost) | 1.0 | Section 3.4 |
| a₀ (min. enforceable effort) | 1.0 | Section 3.4 |
| Ū (reservation utility) | 1.0 | Section 3.4 |
| r (risk aversion) | 1.0 | Chetty (2006) midpoint |
| σ² (output noise) | 1.0 | Section 3.4 |
| F (monitoring cost) | 1.5 | Section 3.4 |

Baseline result: **A\* ≈ 0.65**.

## Sector heterogeneity (Section 7.5 in the revised paper)
Only (C, σ², r) are varied by sector; all other parameters use the
baseline values above.

| Sector | C | σ² | r | A* |
|---|---|---|---|---|
| Delivery riders | 1.2 | 0.5 | 0.8 | 0.466 |
| Livestream hosts | 1.5 | 1.8 | 1.0 | 0.500 |
| Designers / knowledge workers | 1.3 | 1.3 | 1.5 | 0.591 |
| Manufacturing line workers | 0.4 | 0.7 | 1.0 | 1.516 |

Sector parameter choices are illustrative, calibrated qualitatively from
task characteristics (monitorability, AI-tool complementarity, typical
risk exposure) discussed in the text — they are not estimated from
worker-level data and should be labelled as such in the paper.

## License
MIT. For academic use in connection with the 2026 Yau Awards
(Economics & Finance Modelling) submission.
