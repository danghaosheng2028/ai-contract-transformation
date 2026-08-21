# Interview Prep: Likely Questions on "From Hours to Output"

Not part of the paper — a private prep sheet for the Yau Awards defense/interview.
All answers use the paper's actual notation ($A$, $C$, $\alpha$, $\gamma$, $F$, $\tilde H$),
not any alternative notation you may see in outside feedback.

**Revision note:** This version supersedes the earlier draft. Three answers (Q4, Q5, Q7)
were substantively wrong under the corrected Section 7.3 (the earlier "blocks transformation
entirely" claim did not survive re-derivation of the firm's optimal γ under a binding wage
floor — see Section 7.3's revised text). Q3 is also rewritten: the model does *not*
"directly" handle hybrid base-pay-plus-commission contracts the way the old answer claimed;
Appendix C's Proposition 1 shows the opposite, and that tension is now stated honestly. Two
new questions (Q8, Q9) cover findings from later verification passes, and Q10 covers the most
recent — and most structural — unresolved critique.

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
worker-level data. (Verified directly against the original Chen and Guo paper: the 2.773
threshold, the 2,846-firm 2010–2020 panel, and the labor-substitution-vs-productivity
mechanism description in Section 3.5 all match the source exactly.)

**Q3. Does the model handle a "base pay + commission" hybrid contract?**

Be careful here — the honest answer is more nuanced than "yes, directly," and claiming
otherwise is a real risk if pressed.

Within the two named modes (T and P) as originally specified, the piece-rate contract
$w=\alpha+\gamma y$ *is* the general linear contract, and $\gamma=0$ formally recovers a
fixed-wage structure — but not Mode T's actual equilibrium, since $\gamma=0$ implies
worker effort $a^*=0$, not the enforced $a_0>0$ that defines Mode T. Appendix C
formalizes the correct unification: it introduces a second instrument, an
attendance-enforced effort floor $a_{\min}$, and *proves* (Proposition 1) that under the
paper's cost assumptions, the firm's optimum is always a corner — pure T ($\gamma=0$,
$a_{\min}=a_0$) or pure P ($a_{\min}=0$, $\gamma=\gamma^*$) — never a blend.

This is a real tension worth naming directly: real Chinese platform contracts (e.g., a
guaranteed base plus per-order commission) often *are* hybrids, and the model's corner
solution doesn't produce that. Appendix C says why: it's an artifact of assuming
attendance-based enforcement is available at *zero marginal cost* regardless of how it's
combined with $\gamma$. Relaxing that — e.g., a convex cost of running both enforcement
technologies at once, or letting $a_{\min}$ serve as risk-reducing income insurance rather
than pure enforcement — would likely make interior (hybrid) contracts optimal. The paper
flags this explicitly as a scope limitation rather than claiming to explain observed hybrid
pay.

**Q4. What does the minimum-wage result actually show — "blocked" or "delayed"?**

**Delayed, substantially — not blocked.** An earlier draft claimed a wage floor could
block transformation entirely within $A\in[0,3]$; that claim did not survive a corrected
re-derivation and has been removed from the paper.

The error in the earlier version: it computed the constrained base wage
$\alpha_{MW}=\max\{W_{\min},\alpha^*(\gamma)\}$ but kept the incentive slope $\gamma$ fixed
at its *unconstrained* optimum $\gamma^*=\tilde H^2/(\tilde H^2+rk\sigma^2)$. That's not
the firm's actual best response to a binding floor. Once $\alpha=W_{\min}$ is fixed, profit
becomes $\gamma\tilde H^2/k - \gamma^2\tilde H^2/k - W_{\min} - F$, a downward parabola in
$\gamma$ with an exact, parameter-free vertex at $\gamma_c^*=1/2$ — nothing like the
unconstrained $\gamma^*$, which can approach 1 as $A$ grows. Re-optimizing correctly gives
a *finite* threshold $A^*_{MW}$ for every wage floor tested, from $A^*_{MW}\approx1.33$
at $W_{\min}=0$ up to $\approx2.11$ at $W_{\min}=1.5$ — both still inside the paper's
empirically relevant range $[0,3]$, so transformation is delayed by roughly 2–3×, not
prevented (current Section 7.3, `simulation/minimum_wage.py`).

**Section 7.3.1's robustness check**, run afterward, confirms the *qualitative* mechanism
survives even under the strictest limited-liability reading ($\alpha\ge0$, no wage floor
needed at all): the constrained-branch profit at $\gamma_c^*=1/2$ is $\tilde H^2/(4k)-F$,
still quadratic in $A$ (coefficient $(\theta C)^2/(4k)$, one quarter the unconstrained
asymptotic rate) — so the paper's central convexity mechanism doesn't depend on allowing
unrealistic negative wages; it just produces a higher, still-finite threshold.

**Do not repeat the old claim** that "$\Pi_P^{MW}(A)$ stays essentially flat" or that it
"was confirmed on two separate machines" — both statements are gone from the current
paper because they were artifacts of the uncorrected $\gamma$.

**Q5. Isn't the negative-$\alpha^*$ result itself unrealistic?**

Yes, and the paper says so (Section 8.2, point 6) — but this is now a *resolved*
limitation, not just a flagged one. Section 7.3.1 directly tests what happens if
$\alpha\ge0$ is imposed as a hard floor, independent of any minimum-wage statute, and
shows the paper's headline mechanism (piece-rate profit's convexity eventually dominating
time-rate's linearity) survives intact — just with $A^*$ shifted up to $\approx1.33$
instead of $\approx0.65$. So the unrealistic feature (allowing $\alpha<0$) affects the
*exact numerical threshold*, not the *qualitative existence* of a threshold.

**Q6. What's the efficiency–equity tradeoff you mention in the conclusion?**

Delaying transformation (rather than "blocking" it — see Q4) has a cost (forgone
productivity gains from convex incentive pay at a given $A$) and a benefit (protecting
risk-averse workers from the income volatility that $\gamma^*>0$ contracts impose as
$\sigma^2$ rises, Section 6.2(i)). Section 8.1(4) states the model does not take a
position on how a regulator should weigh these — only that a wage floor cannot be tuned to
capture one effect without the other, since both flow from the same constraint on
$\alpha$. Section 8.2's newer point on the multitasking blind spot (see Q9) adds a
second, unmodeled channel that would only strengthen the equity case further.

**Q7. What would change if you imposed $\alpha\ge0$ as a standing model assumption?**

This is now directly answered in Section 7.3.1 rather than left as an untested
implication. Requiring $\alpha\ge0$ — with *no* legal minimum-wage statute at all — still
allows transformation, at $A^*\approx1.33$ (roughly double the unconstrained baseline).
It does **not** block transformation. (An earlier draft claimed it did; that claim
depended on the same $\gamma$-not-reoptimized error as Q4 and has been corrected.)

**Q8. Doesn't the model implicitly assume workers' outside option $\bar U$ never changes as
AI reshapes the whole labor market — isn't that a strong partial-equilibrium assumption?**

It's a partial-equilibrium simplification, but a provably harmless one for this specific
result. Because $\bar U$ (however it's specified — constant, or any function of $A$) enters
both $\Pi_T(A)$ and $\Pi_P^*(A)$ identically as a $-\bar U(A)$ term, it cancels exactly out
of $G(A)=\Pi_P^*(A)-\Pi_T(A)$. We checked this directly: substituting four different
specifications of $\bar U(A)$ — constant, linear in $A$, quadratic in $A$, and logarithmic
in $A$ — into the model, $A^*$ comes out to *exactly* the same value (0.649633) in every
case. So the threshold $A^*$ is provably invariant to whether or how the outside option
responds to economy-wide AI adoption; this isn't an assumption doing hidden work.

**Q9. The paper calls $C$ "human–AI complementarity," but doesn't $\tilde H = h+\theta AC$
actually describe perfect substitutability between human capital and AI, not
complementarity?**

This is a fair semantic critique and worth answering directly rather than deflecting. In
the standard production-theory sense, "complementarity" implies a *low* elasticity of
substitution (e.g., Leontief-style $\min(h,\theta AC)$, where AI is useless without a
baseline of human input). The paper's additive-linear form $h+\theta AC$ instead implies
*infinite* elasticity of substitution between $h$ and AI-augmented capacity — mathematically,
AI could in principle fully substitute for human capital as $A\to\infty$, which is the
opposite of complementarity in the classical sense. $C$ is better read as a *task-specific
marginal-effectiveness* parameter for AI augmentation, not complementarity in the CES
sense. This naming looseness doesn't invalidate any derivation — every proof goes through
correctly given the stated functional form — but it is a legitimate critique of how the
parameter is *labeled*, and Section 2.1's discussion of the functional-form choice should
be read with this caveat in mind. Reworking the model to use a genuinely low-substitution
form (e.g., CES with $\rho<1$) would break Mode T's linearity in $A$, which is the entire
mechanism behind Theorem 1's existence proof — not a change to make under time pressure.

**Q10. Is there a channel through which AI affects platform work that the model doesn't
capture at all — not just imperfectly, but structurally?**

Yes, and this is, candidly, the most significant open gap in the paper. The production
function $y=a\tilde H+\varepsilon$ routes *all* of AI's contribution to output through
multiplication by worker effort $a$ — if $a=0$, output is zero no matter how large $A$ is.
This models AI purely as an effort-amplifier. But a large share of what platform AI
actually does (route optimization, automated dispatch/matching) plausibly contributes to
output largely independent of the worker's momentary effort — the kind of contribution a
richer model might capture with an additional effort-independent term $g(A)$ in the
production function. If $g(A)$ were large relative to $a\tilde H$, the firm's problem would
shift from "redesign the incentive contract" toward "automate the task entirely," a
qualitatively different regime the paper's $A^*$ threshold does not speak to at all. This
is now listed as new point 9 in Section 8.2's Limitations, and is the honest answer if
pressed on "what would a stronger version of this model need to do."
