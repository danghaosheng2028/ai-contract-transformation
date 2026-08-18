# Interview Prep: Likely Questions on "From Hours to Output"

Not part of the paper — a private prep sheet for the Yau Awards defense/interview.
All answers use the paper's actual notation ($A$, $C$, $\alpha$, $\gamma$, $F$, $\tilde H$),
not any alternative notation you may see in outside feedback.

---

**Q1. Why assume output noise $\varepsilon \sim N(0,\sigma^2)$? What if AI-driven risk is heavy-tailed?**

Normality paired with CARA utility gives a closed-form certainty equivalent, which is what
makes $\gamma^*$, $A^*$, and every comparative static in the paper solvable in closed form.
Heavy-tailed noise is flagged as a limitation (Section 8.2, point 1) — the qualitative
threshold logic (a fixed monitoring cost vs. convex incentive gains) likely survives, but
the exact closed-form expressions would not.

**Q2. Are the Table 2 sector calibrations estimated or assumed?**

Assumed / illustrative, stated explicitly in the paper (Section 7.5 note and Section 8.2,
point 5). The direction of each parameter choice follows from task characteristics
(monitorability → $\sigma^2$; AI-tool leverage → $C$) discussed in Sections 2.3 and 3.5, and
the qualitative ordering is consistent with Chen and Guo's (2023) independent panel-data
finding on digitalization and wage growth — but the specific numbers are not fit to
worker-level data.

**Q3. Does the model handle a "base pay + commission" hybrid contract?**

Yes, directly. The piece-rate contract $w = \alpha + \gamma y$ *is* the general linear
contract: $\gamma=0$ recovers pure time-rate, $\gamma \in (0,1]$ is exactly a base-pay +
commission structure. This is now stated explicitly in Section 4.5. There is no separate
"hybrid contract" case to add — it's already the object being optimized over.

**Q4. Why does the minimum-wage result come out as "blocked" rather than "delayed"?**

Because the unconstrained optimal base wage $\alpha^*$ falls *without bound* as $A$ rises
(Section 4.3) — the optimal incentive-heavy contract implies the firm effectively charges
the worker an increasingly large upfront fee, financed by high-powered pay. This divergence
is exactly what makes $\Pi_P^*(A)$ grow quadratically and eventually overtake $\Pi_T(A)$.
Any wage floor — even $\alpha \ge 0$ with no minimum-wage law at all — removes this specific
channel, so $\Pi_P^{MW}(A)$ stays essentially flat and never catches up within the
empirically relevant range (Section 7.3, verified by the $W_{\min}$ sweep in
`simulation/minimum_wage.py`, confirmed independently on two machines).

**Q5. Isn't the negative-$\alpha^*$ result itself unrealistic?**

Yes — and the paper says so directly (Section 7.3's third interpretation bullet, and
Section 8.2, point 6). It's a known feature of the frictionless linear-contract benchmark:
nothing in the unconstrained model prevents $\alpha<0$. That's exactly why Section 7.3
frames the wage-floor result as revealing how much of the model's headline result depends
on that assumption — the paper doesn't hide this, it uses it as the mechanism.

**Q6. What's the efficiency–equity tradeoff you mention in the conclusion?**

Blocking transformation has a cost (forgone productivity gains from convex incentive pay)
and a benefit (protecting risk-averse workers from the income volatility that $\gamma^*>0$
contracts impose as $\sigma^2$ rises). Section 8.1(4) states explicitly that the model does
not take a position on how a regulator should weigh these — only that a wage floor cannot
be tuned to capture one effect without the other, since both come from the same constraint
on $\alpha$.

**Q7. What would change if you imposed $\alpha \ge 0$ as a standing model assumption, rather
than treating it as a minimum-wage extension in Section 7?**

Nothing new needs deriving — this is exactly the $W_{\min}=0$ case already in the sweep
(Section 7.3's "institutional baseline" bullet). The result is that the baseline
non-negativity requirement alone is already enough to block transformation under Section
3.4's calibration; a legal minimum wage above zero only adds to a friction that already
exists.
