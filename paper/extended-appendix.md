# From Hours to Output — Extended Online Appendix

This document collects the extended proofs, structural corollaries, and robustness
material referenced but not reproduced in full in the main paper (`from-hours-to-output.md`).
It is intended to be read alongside the main text; section numbers (A.5–A.7, C, D)
match the numbering used there. Nothing here changes any result in the main paper —
this is supporting derivation, not new content.

Repository: https://github.com/danghaosheng2028/ai-contract-transformation
Interactive simulation: https://danghaosheng2028.github.io/ai-contract-transformation/

---

## A.5 Corollary: Exact Closed-Form Dependence of $A^*$ on $\theta C$

Both $\Pi_T(A)$ and $\tilde H(A)$ depend on $\theta$ and $C$ only through the product $\psi\equiv\theta C$:

$$
\Pi_T(A) = a_0h + a_0\psi A - \bar U - \tfrac12 ka_0^2, \qquad \tilde H = h+\psi A.
$$

Substituting $x\equiv\psi A$, the equilibrium condition $G(A^*)=0$ becomes an equation purely in $x$ (all other parameters fixed), so its solution $x^*$ is a constant independent of how $\psi$ is decomposed into $\theta$ and $C$. Since $x^*=\psi A^*=\theta C\cdot A^*$, we obtain the exact closed form

$$
A^* = \frac{x^*}{\theta C},
$$

where $x^*\approx0.9744$ under baseline calibration. Two corollaries:

1. $\partial\ln A^*/\partial\ln\theta = \partial\ln A^*/\partial\ln C = -1$ exactly — confirmed numerically at $\pm1\%$, $\pm5\%$, $\pm10\%$, and $\pm20\%$ perturbations, all returning elasticity $-1.0000$ to four decimal places.
2. Since $\theta$ and $C$ enter identically, doubling either has an identical effect on $A^*$: AI-augmentation-skills training and technology upgrades that raise $\theta$ are, at the margin, perfect substitutes for accelerating contract transformation (cf. Section 8.1(2)).

## A.6 Corollary: Equal Elasticities for $r$ and $\sigma^2$

By an analogous argument, $r$ and $\sigma^2$ enter the model only through the product $b\equiv rk\sigma^2$. Since $\partial\ln b/\partial\ln r = \partial\ln b/\partial\ln\sigma^2 = 1$ identically, and $A^*$ depends on $r,\sigma^2$ only via $b$, it follows that

$$
\frac{\partial\ln A^*}{\partial\ln r} = \frac{\partial\ln A^*}{\partial\ln\sigma^2}
$$

exactly, for any parameter values. Confirmed numerically: both elasticities equal $0.213$ under baseline calibration. Worker risk aversion and output-noise variance are interchangeable drivers of the transformation threshold — a doubling of either has exactly the same proportional effect on $A^*$.

## A.7 Corollary: Invariance of $A^*$ to the Specification of Reservation Utility $\bar U$

The main text treats $\bar U$ as a constant, independent of $A$. We show this is a harmless normalization, not a substantive restriction: for *any* specification $\bar U(A)$ — constant, increasing, decreasing, or nonlinear in $A$ — the threshold $A^*$ is unchanged.

**Proof.** Both $\Pi_T(A)$ and $\Pi_P^*(A)$ contain $\bar U(A)$ as an additive term with coefficient $-1$:

$$
\Pi_T(A) = a_0\tilde H(A) - \bar U(A) - \tfrac12 ka_0^2, \qquad \Pi_P^*(A) = \frac{\tilde H(A)^4}{2k(\tilde H(A)^2+b)} - \bar U(A) - F.
$$

Hence $G(A) = \Pi_P^*(A) - \Pi_T(A)$ contains the term $-\bar U(A) - (-\bar U(A)) = 0$: **$\bar U(A)$ cancels exactly**, regardless of its functional form, because the same worker faces the same outside option under either contract mode. $G(A)$, and hence $A^*$, is therefore completely independent of how $\bar U$ varies with $A$. $\blacksquare$

We confirmed this numerically for four specifications — $\bar U(A) = 1.0$ (constant), $1.0+0.3A$ (linear), $1.0+0.2A+0.1A^2$ (quadratic), and $1.0+0.5\ln(1+A)$ (concave) — all four returning $A^*=0.649633$ to six decimal places. This directly addresses a natural general-equilibrium concern: even if AI adoption raises workers' economy-wide outside options as it becomes more prevalent, this does not affect the contract-mode threshold *for a given firm and worker*, since both contract modes draw on the same competitive labor market.
-e 
---

# Appendix C. A Unified Contract Family and Its Limits

This appendix formalizes the correspondence between Mode T and Mode P gestured at in Section 4.5, and — in the interest of intellectual honesty — states plainly where this formalization's central prediction departs from observed compensation practice.

## C.1 Extended Contract Space

Let the firm choose a triple $(\alpha,\gamma,a_{\min})$, where $a_{\min}\ge0$ is an enforced effort floor implemented through direct, attendance-style supervision — a technology distinct from, and not requiring, digital output monitoring. Given $(\gamma,a_{\min})$, the worker's realized effort is

$$
a(\gamma,a_{\min}) = \max\{a_{\min},\, \gamma\tilde H/k\}.
$$

The firm incurs the digital monitoring cost $F$ if and only if $\gamma>0$; enforcing a positive floor $a_{\min}$ via attendance supervision is available at zero marginal cost, consistent with the original Mode T specification of Section 4.2 (no separate cost parameter is introduced, so Sections 6–7 require no recalibration).

## C.2 Proposition 1 (T/P as a Discrete Regime Choice)

*Given the extended contract space above, the firm's optimal $(\alpha,\gamma,a_{\min})$ is always a corner: either (i) $\gamma=0$, $a_{\min}=a_0$ (Mode T exactly), or (ii) $a_{\min}=0$, $\gamma=\gamma^*=\tilde H^2/(\tilde H^2+rk\sigma^2)$ (Mode P exactly). No interior combination is ever optimal.*

**Proof.** Fix $\gamma>0$. If $a_{\min}\le\gamma\tilde H/k$, the floor is redundant (profit is independent of $a_{\min}$ in this range), so $a_{\min}=0$ is weakly optimal. If $a_{\min}>\gamma\tilde H/k$, realized effort equals $a_{\min}$ regardless of $\gamma$, so any $\gamma>0$ purchases no additional effort while still imposing the worker's risk cost $\tfrac12 r\gamma^2\sigma^2$ and the fixed cost $F$; $\gamma=0$ strictly dominates. Hence the optimum is always a corner. $\blacksquare$

## C.3 What This Buys, and an Honest Limitation

This gives a rigorous version of the "corner solution jumping to an interior solution" intuition for Theorem 1: $A^*$ is the point at which the firm's optimum switches from the pure-T corner to the pure-P corner of this two-instrument space. We verified numerically that this switch involves a genuine discontinuity — at $A=A^*\approx0.65$, $\Pi_T(A^*)\approx1.474$ while $\lim_{\gamma\to0^+}\Pi_P(\gamma;A^*)\approx-2.500$ — confirming the jump is real and driven entirely by the fixed cost $F$, consistent with the existence argument in Section 6.1.

**Limitation.** Proposition 1's strict-corner prediction is a direct consequence of assuming attendance-based effort enforcement is available at *zero marginal cost* regardless of how it is combined with $\gamma$. Under this assumption, layering a positive $a_{\min}$ alongside a positive $\gamma$ is either redundant or strictly dominant, which mechanically rules out any interior blend. This is not a deep economic result about why hybrid pay is suboptimal — it is an artifact of the specific (frictionless) cost structure assumed for tractability.

This matters because hybrid compensation — a guaranteed base wage combined with per-order or per-unit commission — is the empirically dominant structure in much of China's platform delivery and ride-hailing sector, not the pure-corner outcome Proposition 1 predicts. We see two natural channels, left to future work, through which the model could be extended to accommodate this:

1. **A positive, convex cost of layering enforcement on top of incentive pay** (e.g., attendance supervision becomes more expensive to run alongside digital output tracking, due to duplicated administrative overhead) would create an interior trade-off and could rationalize a strictly positive but sub-$a_0$ effort floor combined with $\gamma\in(0,1)$.
2. **$a_{\min}$ as partial insurance rather than pure enforcement**: if a positive $a_{\min}$ lowers the worker's effective risk exposure under CARA utility (by guaranteeing a floor income independent of output realization, distinct from simply mandating effort), it would enter the worker's certainty equivalent directly rather than only through the $\max\{\cdot\}$ operator, potentially making a blended contract optimal for sufficiently risk-averse workers even without extra monitoring cost.

We do not pursue either extension formally here, but flag this as the most direct way Proposition 1 could be reconciled with observed hybrid pay structures.

---

# Appendix D. Robustness to an Effort-Independent Automation Channel

A natural critique of the production function $y=a\tilde H+\varepsilon$ (Section 4.1) is that it routes all of AI's contribution to output through worker effort $a$ — if $a=0$, output is zero regardless of $A$. This section tests that concern directly by extending the production function to

$$
y = a\tilde H(A) + g(A) + \varepsilon,
$$

where $g(A)$ is an effort-independent automation contribution — e.g., algorithmic route optimization or automated order matching, realized whether or not the worker exerts effort — and asking whether this channel changes the paper's central threshold result.

## D.1 Re-derivation

**Worker's problem.** With wage $w=\alpha+\gamma y = \alpha + \gamma(a\tilde H + g(A)) + \gamma\varepsilon$, the worker chooses $a$ to maximize $\alpha + \gamma a\tilde H + \gamma g(A) - \tfrac12 r\gamma^2\sigma^2 - \tfrac12 ka^2$. Since $\gamma g(A)$ does not depend on $a$, it drops out of the first-order condition entirely: $a^*=\gamma\tilde H/k$, **unchanged** from Section 4.3.

**Participation constraint.** $CE = \alpha + \gamma a^*\tilde H + \gamma g(A) - \tfrac12 r\gamma^2\sigma^2 - \tfrac12 k(a^*)^2 = \bar U$ gives

$$
\alpha = \bar U + \tfrac12 r\gamma^2\sigma^2 - \frac{\gamma^2\tilde H^2}{2k} - \gamma g(A).
$$

**Firm profit.** $\Pi_P(\gamma) = (1-\gamma)(a^*\tilde H + g(A)) - \alpha - F$. Substituting and simplifying, the $-\gamma g(A)$ term from $\alpha$ cancels against the $-\gamma g(A)$ term from $(1-\gamma)g(A)$, leaving

$$
\Pi_P(\gamma) = \frac{\gamma\tilde H^2}{k} - \frac{\gamma^2\tilde H^2}{2k} - \tfrac12 r\gamma^2\sigma^2 - \bar U - F + g(A),
$$

i.e., **exactly the original $\Pi_P(\gamma)$ of Section 4.3, plus $g(A)$ as an independent additive term**. Since $g(A)$ does not depend on $\gamma$, it does not affect the first-order condition for $\gamma$, so $\gamma^*=\tilde H^2/(\tilde H^2+rk\sigma^2)$ is also **unchanged**, and

$$
\Pi_P^{g,*}(A) = \Pi_P^*(A) + g(A).
$$

**Mode T.** The automation contribution is realized under time-rate pay as well (the algorithm runs regardless of contract mode), so $\Pi_T^g(A) = \Pi_T(A) + g(A)$.

## D.2 Proposition 2 (Invariance of $A^*$ to Mode-Common Automation)

*For any function $g(A)$ that enters $\Pi_T(A)$ and $\Pi_P^*(A)$ identically, the transformation threshold $A^*$ is exactly unchanged from Theorem 1's original value.*

**Proof.** $G^g(A) = \Pi_P^{g,*}(A) - \Pi_T^g(A) = [\Pi_P^*(A)+g(A)] - [\Pi_T(A)+g(A)] = G(A)$, identical to the original profit difference for any functional form of $g$. Since $A^*$ is defined by $G(A^*)=0$, it is unaffected. $\blacksquare$

This was verified numerically for $g(A) \in \{0.5A,\ 2A,\ 5A,\ 0.1A^2,\ 0.5A^2,\ A^2,\ 2\ln(1+A)\}$ — linear, convex, and concave specifications spanning a wide range of magnitudes — all eight returning $A^*=0.649633$ to six decimal places, matching the $g(A)=0$ baseline exactly.

## D.3 Corollary: Full Automation Never Dominates Under This Specification

A related question is whether sufficiently large $g(A)$ could make eliminating the worker entirely (retaining only $g(A)$) more profitable than either contract mode. Under Mode T, profit including the worker is $\Pi_T^g(A) = a_0\tilde H(A) + g(A) - \bar U - \tfrac12 ka_0^2$, while pure automation without a worker yields $\Pi_Z(A) = g(A)$. Their difference, $\Pi_T^g(A) - \Pi_Z(A) = a_0\tilde H(A) - \bar U - \tfrac12 ka_0^2$, does **not** depend on $g(A)$ at all, and is strictly positive under baseline calibration for every $A$ tested (confirmed numerically for automation coefficients up to $\mu=20$, far outside any plausible calibration, in the linear case $g(A)=\mu A$). Under this specification, keeping the worker is a free option that only adds value; full automation is never optimal.

## D.4 What This Resolves, and What Remains Open

Propositions 2 and the corollary above show the paper's central mechanism is robust to *mode-common* automation — the most natural first-pass extension, and arguably the empirically plausible baseline case, since a platform's routing or dispatch algorithm typically runs identically regardless of how the affected worker happens to be paid. They do **not** address the harder case where automation returns are themselves *endogenous to the contract mode* — for instance, if output-based pay gives firms a stronger incentive to invest in complementary automation than time-based pay does, so that $g_P(A) > g_T(A)$ systematically. In that case the $g(A)$ terms would not cancel in $G(A)$, and $A^*$ could shift. Formalizing this mode-dependent extension — and characterizing the boundary in $(A,\mu)$-space at which full automation would dominate human-inclusive production once $g$ becomes worker-*competing* rather than worker-*independent* — is the precise open question this analysis leaves for future work. This replaces the earlier, vaguer concern "AI might do more than amplify effort" with a specific, falsifiable modeling gap: *does the automation contribution differ systematically by contract mode, and does it substitute for rather than sit alongside the worker's output?*
