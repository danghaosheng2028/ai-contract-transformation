# From Hours to Output: A Principal–Agent Theory of AI-Driven Contract Transformation and the Limits of Minimum-Wage Protection in China's Platform Economy

Lucas Dang
RCF Experimental School, Beijing
July 2026

*Code and simulation scripts reproducing all figures and calibration results in this paper are publicly available at: https://github.com/danghaosheng2028/ai-contract-transformation. An interactive version of the core simulation — allowing readers to vary output noise $\sigma^2$, risk aversion $r$, human–AI complementarity $C$, and the minimum-wage floor $W_{\min}$ in real time — is available at https://danghaosheng2028.github.io/ai-contract-transformation/ (source: `docs/index.html` in the same repository).*

---

## Abstract

Rapid advances in artificial intelligence (AI) have transformed how firms allocate tasks, monitor performance, and design compensation systems. While AI increases productivity, it also amplifies output volatility and reshapes the allocation of risk between firms and workers. This paper develops a principal–agent model of AI‑augmented production in which effective human capital is:

$$
\tilde{H} = h + \theta AC
$$

where $A$ denotes AI utilization intensity and $C$ captures human–AI complementarity. Firms choose between a time‑rate contract with enforceable minimum effort and a piece‑rate contract that requires digital monitoring and exposes workers to output risk.

We derive closed‑form expressions for optimal effort, optimal piece‑rate incentives, and firm profit under each contract. A central theoretical result is the existence of a unique contract transformation threshold $A^*$ such that firms optimally switch from time‑rate to piece‑rate compensation once AI intensity exceeds this level. The threshold arises because time‑rate profit grows linearly in $A$, whereas piece‑rate profit grows convexly due to incentive amplification and AI‑enhanced productivity.

Using the implicit function theorem, we characterize the comparative statics of $A^*$; we further show that this threshold is inversely and exactly proportional to the product of the AI amplification coefficient $\theta$ and human–AI complementarity $C$. The threshold increases in output noise and worker risk aversion—reflecting the cost of risk exposure under piece‑rate pay, with output noise and risk aversion entering the threshold with identical elasticity—and decreases in human–AI complementarity, which strengthens incentive effectiveness. Numerical simulations confirm these results and show that China's minimum‑wage regulation substantially delays contract transformation: even a modest, strictly enforced wage floor roughly doubles to triples the AI intensity required before piece-rate compensation becomes optimal, by curbing (though not eliminating) the negative-base-wage channel that drives piece-rate profit's fastest growth — though transformation is delayed rather than categorically prevented within the empirically relevant AI-intensity range. We further show that the transformation threshold is highly sector‑heterogeneous: occupations with high monitorability and strong AI complementarity (e.g. platform delivery and livestreaming) cross the threshold at far lower AI intensity than occupations AI augments only weakly (e.g. manufacturing line work), and this ordering is broadly consistent with independent Chinese firm-panel evidence on digitalization and wage growth.

The model provides a unified explanation for heterogeneous adoption of output‑based pay across industries and offers policy insights on labor regulation, AI‑skills training, and the future of incentive design in AI‑enabled workplaces.

---

## Keywords

AI‑augmented production
principal–agent model
risk‑sharing
incentive design
contract transformation
piece‑rate compensation
time‑rate compensation
human–AI complementarity
minimum‑wage regulation
comparative statics

---

## Notation

| Symbol | Definition |
|---|---|
| $A$ | AI utilization intensity (firm/task-level), $A \in [0, \bar A]$ |
| $C$ | Human–AI complementarity |
| $\theta$ | AI amplification coefficient |
| $h$ | Baseline human capital |
| $\tilde H$ | Effective human capital, $\tilde H = h + \theta AC$ |
| $a$ | Worker effort |
| $a_0$ | Minimum enforceable effort under time-rate (Mode T) |
| $k$ | Effort-cost convexity parameter, $\psi(a) = \tfrac12 k a^2$ |
| $r$ | Worker absolute risk aversion (CARA) |
| $\sigma^2$ | Output noise variance, $\varepsilon \sim N(0,\sigma^2)$ |
| $\bar U$ | Reservation utility |
| $F$ | Fixed monitoring cost under piece-rate (Mode P) |
| $\alpha$ | Piece-rate base wage |
| $\gamma$ | Piece-rate incentive slope |
| $\gamma^*$ | Optimal piece-rate slope |
| $W_0$ | Fixed wage under time-rate |
| $\Pi_T(A)$ | Firm profit under time-rate contract |
| $\Pi_P^*(A)$ | Firm profit under optimal piece-rate contract |
| $A^*$ | Contract transformation threshold, $\Pi_T(A^*) = \Pi_P^*(A^*)$ |
| $W_{\min}$ | Minimum-wage floor |
| $G(A)$ | Profit difference, $G(A) = \Pi_P^*(A) - \Pi_T(A)$ |

*Symbols are listed in order of first appearance in Sections 4.1–4.3.*

**A note on units.** All monetary quantities ($\Pi$, $W$, $\alpha$, $\bar U$) are expressed in standardized units — multiples of a representative monthly base-wage benchmark for the calibrated occupations, consistent with the reservation-utility normalization $\bar U = 1.0$ in Section 3.4. AI intensity $A$ is likewise a standardized index on $[0,3]$, constructed to span the empirical range of enterprise digital-tool penetration reported by CAICT (Section 3.1), rather than a directly observable physical quantity. This normalization follows standard practice in stylized principal–agent calibration exercises; numerical thresholds such as $A^*\approx0.65$ should not be read as directly comparable to indices constructed on different scales elsewhere (see the caveat in Section 3.5 regarding Chen and Guo, 2023).

---

# 1. Introduction

Artificial intelligence (AI) is transforming how firms organize production, monitor performance, and design compensation systems. In China, this transformation is particularly salient: more than 84 million workers were engaged in platform‑based flexible employment in 2023, accounting for roughly 15 percent of urban employment. Since the 2021 *Guiding Opinions on Safeguarding the Labor Rights of New Employment Forms*, platform labor has become a regulated category, and the shift from traditional time‑rate compensation to output‑based pay has accelerated across logistics, content creation, and digital services.

Yet this transition presents a fundamental economic paradox. AI technologies increase productivity by augmenting workers' effective human capital, but they also amplify output volatility and expose workers to greater income risk. Under piece‑rate compensation, workers bear both effort costs and output risk, whereas under time‑rate compensation, firms shoulder the risk while enforcing minimum effort through observable inputs. This raises a central question:

**Under what conditions should firms switch from time‑rate to piece‑rate compensation, and how does AI adoption shift this boundary?**

Existing research provides important foundations but leaves this question open. Classical principal–agent theory establishes that optimal linear contracts balance incentives against risk exposure. Recent work on AI and labor markets documents productivity gains from AI adoption but does not analyze how AI changes contract design. Emerging studies argue that AI may shift firms toward output‑based pay, yet they do not provide a closed‑form characterization of the transformation threshold or its comparative statics.

This paper fills that gap by embedding AI into a tractable principal–agent model. We introduce an AI‑augmented effective human capital function:

$$
\tilde{H} = h + \theta AC
$$

derive closed‑form expressions for optimal effort and incentives, and show that a unique transformation threshold $A^*$ exists. Comparative statics reveal how noise, risk aversion, and human–AI complementarity shape this threshold. We further incorporate China's minimum‑wage regulation and show that binding wage floors substantially delay — roughly doubling to tripling the required AI intensity, though not categorically preventing — contract transformation within the empirically relevant AI-intensity range.

The remainder of the paper proceeds as follows. Section 2 reviews the related literature. Section 3 presents stylized facts and parameter calibration, together with suggestive evidence from independent Chinese firm-panel data supporting the threshold mechanism. Section 4 introduces the model. Section 5 derives equilibrium outcomes. Section 6 presents the main theoretical results. Section 7 provides numerical simulations, including a sensitivity and sector-heterogeneity analysis. Section 8 concludes with policy implications. Appendices contain additional proofs, calibration details, and a formal unification of the two contract modes.

---

# 2. Literature Review

## 2.1 Principal–Agent Models of Incentives and Risk‑Sharing

The theoretical foundation of this paper lies in the canonical principal–agent framework. Holmstrom (1979) establishes that under CARA utility and normally distributed noise, optimal contracts are linear in output and balance incentives against risk exposure. Holmstrom and Milgrom (1991) extend this insight to multi‑task environments, showing that high‑noise tasks favor fixed wages because incentives distort effort allocation.

Subsequent work has refined these insights. Lazear (2000) documents empirically how piece‑rate compensation increases productivity but also raises income volatility. Prendergast (2002) emphasizes the role of uncertainty in shaping incentive strength. These studies highlight the tradeoff between incentives and risk, but they do not incorporate AI as a productivity‑augmenting force nor analyze how AI shifts the optimal contract boundary.

This paper contributes to this literature by embedding AI‑augmented production into the Holmstrom–Milgrom framework. By modeling effective human capital as $\tilde{H}=h+\theta AC$, we show that AI amplifies the incentive effect of piece‑rate contracts and generates a unique transformation threshold $A^*$ at which firms optimally switch from time‑rate to piece‑rate compensation.

**On the specific functional form $\tilde H = h + \theta AC$.** We adopt an additively separable, linear-in-$A$ augmentation of human capital rather than alternative forms considered in adjacent literatures — e.g., a multiplicative form $\tilde H = h\cdot(1+\theta A)^C$, or a CES-aggregator combining human and AI-derived effective labor as in task-based automation models (Acemoglu and Restrepo, 2018). Three considerations motivate this choice. First, tractability: the additive form keeps $\tilde H$ linear in $A$, which is what allows $\Pi_T(A)$ to remain exactly linear (Section 4.2) — the source of the linear-versus-convex asymmetry driving Theorem 1's existence result; a multiplicative or CES form would make both branches nonlinear in $A$, obscuring the clean mechanism this paper isolates. Second, interpretability: $\theta C$ has a direct reading as "the marginal human-capital return to a unit of AI intensity, scaled by task complementarity" — closer to an elasticity than the corresponding parameter under a CES specification. Third, this scope boundary matters for what the paper does *not* claim: because Theorem 1 rests on a linear-versus-convex profit comparison, robustness of the qualitative existence-and-uniqueness result to alternative augmentation functions is an open question we do not resolve here. We conjecture, but do not prove, that any augmentation function increasing and unbounded in $A$ would preserve existence of some threshold; the exact elasticity results of Appendix A.5, which rely specifically on the additive-linear form, would not carry over unchanged to a multiplicative specification. We flag this as a scope boundary rather than resolve it (see also Section 8.2, point 5, on endogenizing $C$).

## 2.2 AI, Automation, and Labor Markets

A second strand of literature examines how AI and automation reshape labor markets. Acemoglu and Restrepo (2018) develop a task‑based model in which automation reallocates labor across tasks and affects wages and employment. Brynjolfsson, Li, and Raymond (2025) provide empirical evidence that AI tools significantly increase individual productivity in knowledge‑intensive occupations. Other studies document how AI affects monitoring, prediction, and managerial decision‑making.

However, this literature focuses primarily on employment, productivity, and task allocation—not on compensation design. While Shin and Kang (2026) argue conceptually that AI may shift firms toward output‑based pay, they do not provide a closed‑form characterization of the transformation threshold or its comparative statics. No existing model formally links AI adoption to the optimal allocation of risk and incentives within the firm.

## 2.3 Platform Labor, Flexible Employment, and Chinese Labor Regulation

A third strand of literature examines the rise of platform labor and flexible employment in China. Government reports indicate that platform‑based flexible workers exceeded 84 million in 2023, reflecting rapid growth in gig‑economy sectors such as logistics, ride‑hailing, and digital content creation. Scholars have analyzed how platform algorithms shape labor supply, monitoring, and compensation, and how regulatory frameworks attempt to balance flexibility with worker protection.

A central regulatory instrument is the minimum‑wage system, which imposes binding constraints on base wages even in flexible employment arrangements. Recent policy documents emphasize the need to protect workers from excessive income volatility, but they do not analyze how such regulations interact with incentive design or AI adoption.

## 2.4 Contribution Relative to the Literature

Relative to these three strands, the paper makes four contributions:

1. **A closed‑form transformation threshold.**
   We derive a unique $A^*$ at which firms optimally switch from time‑rate to piece‑rate compensation, and an exact closed-form expression $A^* = x^*/(\theta C)$ for how this threshold depends on the AI amplification coefficient and complementarity (Appendix A.5).

2. **Comparative statics linking risk, uncertainty, and AI complementarity.**
   Using the implicit function theorem, we show how noise, risk aversion, and human–AI complementarity jointly determine the transformation threshold, and derive exact elasticity results (Appendix A.5–A.6).

3. **Integration of Chinese labor regulation.**
   By incorporating minimum‑wage constraints, we show that regulatory frictions substantially delay — though, once the firm's incentive slope is correctly re-optimized under the constraint, do not categorically block — contract transformation in China's rapidly digitalizing labor markets (Section 7.3).

4. **Sector heterogeneity linked to independent empirical evidence, with open, reproducible code.**
   We show that $A^*$ differs systematically across occupations with different monitorability and AI complementarity (Section 7.5), and we relate this ordering to independent Chinese firm-panel evidence on digitalization and wage growth (Section 3.5). All calibration and simulation code is publicly released for reproducibility.

# 3. Stylized Facts and Parameter Calibration

This section presents three stylized facts that motivate the model and guide the calibration of key parameters. The goal is to anchor the theoretical framework in empirical patterns observed in China's rapidly digitalizing labor markets and to justify the numerical values used in the simulations in Section 7. The facts correspond directly to the model's core parameters: AI intensity $A$, human–AI complementarity $C$, output noise $\sigma^2$, and worker risk aversion $r$.

---

## 3.1 Stylized Fact 1: Rising AI Penetration in Chinese Firms

China has experienced a rapid increase in enterprise‑level digitalization and AI adoption. According to the China Academy of Information and Communications Technology (CAICT), the penetration rate of digital tools among Chinese firms rose from roughly 18 percent in 2018 to nearly 40 percent in 2022. Industries such as logistics, e‑commerce operations, content creation, and customer service have adopted AI‑based workflow tools, automated monitoring systems, and algorithmic decision‑making at scale.

This motivates modeling AI intensity $A$ as a continuous variable capturing the degree of AI integration into production. The simulation range $A \in [0,3]$ corresponds to the empirical transition from low to high AI penetration.

---

## 3.2 Stylized Fact 2: Expansion of Flexible and Output‑Based Employment

China's platform economy has expanded dramatically. Government statistics indicate that platform‑based flexible workers exceeded 84 million in 2023, a 50 percent increase from 2019. These workers include couriers, ride‑hailing drivers, livestream hosts, and digital content creators—occupations where output‑based compensation is increasingly prevalent.

This fact supports the model's focus on contract transformation from time‑rate to piece‑rate pay. It also motivates the inclusion of a fixed monitoring cost $F$, reflecting the digital infrastructure required to implement output‑based compensation.

---

## 3.3 Stylized Fact 3: Empirical Estimates of Worker Risk Aversion

Labor economics provides empirical guidance on the magnitude of worker risk aversion. Chetty (2006) and subsequent studies estimate absolute risk aversion parameters in the range $r \in [0.2,2.0]$ for typical workers facing income volatility. This range is consistent with observed behavior in gig‑economy occupations.

We therefore set $r = 1.0$ as the baseline value and explore the full empirical range in comparative statics.

---

## 3.4 Calibration of Remaining Parameters

To ensure internal consistency and empirical plausibility, the remaining parameters are calibrated as follows:

- Baseline human capital: $h = 2.0$
- AI amplification coefficient: $\theta = 1.5$
- Human–AI complementarity: $C = 1.0$
- Effort cost parameter: $k = 1.0$
- Minimum enforceable effort: $a_0 = 1.0$
- Reservation utility: $\bar{U} = 1.0$
- Output noise: $\sigma^2 = 1.0$
- Monitoring cost: $F = 1.5$

These values jointly produce a baseline transformation threshold:

$$
A^* \approx 0.65
$$

which aligns with mid‑range AI penetration levels in Chinese digital service industries. (See the units note following the Notation table for how these standardized values map to the empirical ranges of Sections 3.1–3.3.)

---

## 3.5 Suggestive Evidence for the Threshold Mechanism

While this paper does not conduct firm-level regression, existing Chinese panel-data evidence is consistent with the threshold logic of Theorem 1. Using a text-based digitalization index for 2,846 Chinese A-share firms (2010–2020), Chen and Guo (2023) find that the relationship between digital transformation and average wages is non-monotonic: below a digitalization threshold of 2.773, labor-substitution effects dominate and wage growth is suppressed, but above this threshold, productivity and market-competition effects dominate and wages rise significantly — an effect strongest in labor-intensive and knowledge-intensive industries. This empirical wage-side threshold is the mirror image of the profit-side threshold $A^*$ derived in Section 6: both point to AI/digital intensity producing a discontinuous rather than gradual shift in how firms compensate labor. On the institutional side, ILO survey evidence confirms that location-based platform work in China (delivery, ride-hailing) is already overwhelmingly compensated by piece rate rather than time rate (International Labour Organization, 2021), consistent with this paper's premise that AI-intensive, easily-monitored tasks are where the transformation predicted by Theorem 1 is empirically observed first.

**A caveat on comparability.** The numerical threshold reported by Chen and Guo (2023) — a digitalization index value of 2.773 — and this paper's $A^*\approx0.65$ are constructed on entirely different scales (a firm-level text-based digitalization index versus this paper's standardized AI-intensity parameter) and are not directly comparable in magnitude. The parallel drawn here is qualitative only: both studies point to a discontinuous, threshold-crossing pattern in how digital/AI intensity relates to labor compensation, not a claim that the two threshold values coincide or should be benchmarked against one another. We also note that Chen and Guo's panel-fixed-effects design addresses some, but not all, endogeneity concerns — firms with faster wage growth may also invest more in digitalization, a reverse-causality channel this paper does not independently resolve and treats their finding as suggestive corroboration rather than causal validation of this paper's specific mechanism.

# 4. Model

This section presents the formal environment of the model. We consider a one‑period principal–agent framework in which a risk‑neutral firm hires a single worker whose effort is not contractible. The firm chooses between two compensation modes—time‑rate and piece‑rate—and AI technology enters the production process by augmenting the worker's effective human capital.

---

## 4.1 Environment

### Effective human capital

AI augments human capital according to:

$$
\tilde{H} = h + \theta AC
$$

where:

- $h > 0$ is baseline human capital
- $A \ge 0$ is AI utilization intensity
- $C > 0$ is human–AI complementarity
- $\theta > 0$ is the amplification effect of AI

---

### Production technology

Output is:

$$
y = a\tilde{H} + \varepsilon
$$

where $\varepsilon \sim N(0,\sigma^2)$.

---

### Effort cost

Effort incurs convex cost:

$$
\psi(a) = \frac{1}{2}ka^2
$$

---

### Worker preferences

The worker has CARA utility with absolute risk aversion $r > 0$.
Certainty equivalent:

$$
CE = E[w] - \frac{1}{2}r\,\mathrm{Var}(w) - \psi(a)
$$

---

### Moral hazard

Effort $a$ is not observable or contractible.

---

### Participation constraint

Competitive labor markets imply:

$$
CE = \bar{U}
$$

---

## 4.2 Time‑Rate Contract (Mode T)

Under time‑rate compensation:

- Worker receives fixed wage $W_0$
- Firm enforces minimum effort $a_0$

Participation constraint:

$$
W_0 - \frac{1}{2}ka_0^2 = \bar{U}
$$

Thus:

$$
W_0 = \bar{U} + \frac{1}{2}ka_0^2
$$

Firm profit:

$$
\Pi_T(A)
= a_0(h+\theta AC) - \bar{U} - \frac{1}{2}ka_0^2
$$

This is **linear** in AI intensity $A$:

$$
\frac{d\Pi_T}{dA} = a_0\theta C
$$

---

## 4.3 Piece‑Rate Contract (Mode P)

Compensation:

$$
w = \alpha + \gamma y
$$

---

### Worker's effort choice

Worker solves:

$$
\max_a\; \gamma a\tilde{H} - \frac{1}{2}ka^2
$$

Thus:

$$
a^* = \frac{\gamma\tilde{H}}{k}
$$

---

### Participation constraint

Certainty equivalent:

$$
CE = \alpha
+ \gamma a^*\tilde{H}
- \frac{1}{2}r\gamma^2\sigma^2
- \frac{1}{2}k(a^*)^2
$$

Substitute $a^*$:

$$
CE = \alpha
+ \frac{1}{2k}\gamma^2\tilde{H}^2
- \frac{1}{2}r\gamma^2\sigma^2
$$

Set $CE = \bar{U}$:

$$
\alpha
= \bar{U}
+ \frac{1}{2}r\gamma^2\sigma^2
- \frac{1}{2k}\gamma^2\tilde{H}^2
$$

---

### Firm profit

Expected profit:

$$
\Pi_P(\gamma)
= (1-\gamma)a^*\tilde{H} - \alpha - F
$$

Substitute $a^*$ and $\alpha$:

$$
\Pi_P(\gamma)
= \frac{\gamma\tilde{H}^2}{k}
- \frac{1}{2k}\gamma^2\tilde{H}^2
- \frac{1}{2}r\gamma^2\sigma^2
- \bar{U} - F
$$

---

### Optimal piece‑rate

FOC yields:

$$
\gamma^*
= \frac{\tilde{H}^2}{\tilde{H}^2 + rk\sigma^2}
$$

Optimal profit:

$$
\Pi_P^*(A)
= \frac{\tilde{H}^4}{2k(\tilde{H}^2 + rk\sigma^2)}
- \bar{U} - F
$$

---

## 4.4 Timing

1. Firm chooses contract mode.
2. Under piece‑rate, firm chooses $(\alpha,\gamma)$.
3. Worker chooses effort $a$.
4. Output realized; wage paid.

**Figure 4: Model timing.** The four-stage sequence of the one-period principal–agent game: the firm's contract-mode choice (Section 6's $A^*$ threshold) is made before the piece-rate parameters, which are set before the worker's effort choice, which is made before output and payment are realized. *(See `simulation/fig4_timing.png` in the code repository.)*

---

## 4.5 Discussion

The model embeds AI into the Holmstrom–Milgrom linear contracting framework by allowing AI intensity $A$ and complementarity $C$ to scale effective human capital. AI amplifies both productivity and the returns to effort, altering the firm's optimal risk‑sharing arrangement and potentially triggering contract transformation.

A natural question is whether Mode T and Mode P can be viewed as two points on a single contract family, with $\gamma=0$ recovering Mode T exactly. A naive reading does not work: setting $\gamma=0$ in the worker's first-order condition $a^*=\gamma\tilde H/k$ gives zero effort, not the enforced effort $a_0>0$ that defines Mode T. The two modes rely on structurally different enforcement technologies — attendance-based supervision versus output-contingent digital monitoring — and cannot be unified by varying $\gamma$ alone. Appendix C formalizes a genuine unification by introducing a second contract instrument (an enforced effort floor implemented through attendance supervision) and shows that the firm's optimum in this extended space is always a corner — either pure time-rate or pure piece-rate, never a blend of the two mechanisms. We flag there, and note here for visibility, that this corner-solution prediction sits in tension with commonly observed hybrid compensation schemes (base pay plus commission) in China's platform economy, and we discuss the specific cost-structure assumption responsible for that prediction, along with the extension that would relax it.

# 5. Equilibrium Analysis

This section derives the equilibrium outcomes under the two compensation modes introduced in Section 4. We first characterize the firm's profit under the time‑rate contract, which is linear in AI intensity. We then solve the worker's incentive problem under the piece‑rate contract, derive the optimal piece‑rate parameter, and obtain the firm's optimal profit. The comparison of these two profit functions forms the basis for the contract transformation threshold analyzed in Section 6.

---

## 5.1 Time‑Rate Contract (Mode T)

Under the time‑rate contract, the firm enforces a minimum effort level $a_0$ through attendance monitoring. The worker receives a fixed wage $W_0$, and her certainty equivalent is:

$$
CE_T = W_0 - \frac{1}{2}ka_0^2
$$

The participation constraint $CE_T = \bar{U}$ implies:

$$
W_0 = \bar{U} + \frac{1}{2}ka_0^2
$$

The firm's expected profit is therefore:

$$
\Pi_T(A)
= a_0(h+\theta AC) - \bar{U} - \frac{1}{2}ka_0^2
$$

This profit is **linear** in AI intensity $A$:

$$
\frac{d\Pi_T}{dA} = a_0\theta C
$$

---

## 5.2 Piece‑Rate Contract (Mode P)

Under the piece‑rate contract:

$$
w = \alpha + \gamma y
$$

The firm chooses $(\alpha,\gamma)$ to satisfy incentive compatibility (IC) and individual rationality (IR), and to maximize expected profit.

---

### Step 1: Incentive Compatibility (IC)

Worker chooses effort $a$ to maximize:

$$
CE_P(a)
= \alpha + \gamma a\tilde{H}
- \frac{1}{2}r\gamma^2\sigma^2
- \frac{1}{2}ka^2
$$

FOC yields:

$$
a^* = \frac{\gamma\tilde{H}}{k}
$$

The second-order condition is $\partial^2 CE_P/\partial a^2 = -k < 0$ for all $k>0$, confirming $a^*$ is a strict global maximum (see also Appendix A.0).

---

### Step 2: Participation Constraint (IR)

Substitute $a^*$:

$$
CE_P
= \alpha
+ \frac{1}{2k}\gamma^2\tilde{H}^2
- \frac{1}{2}r\gamma^2\sigma^2
$$

Set $CE_P = \bar{U}$:

$$
\alpha
= \bar{U}
+ \frac{1}{2}r\gamma^2\sigma^2
- \frac{1}{2k}\gamma^2\tilde{H}^2
$$

---

### Step 3: Firm Profit Maximization

Expected profit:

$$
\Pi_P(\gamma)
= (1-\gamma)a^*\tilde{H} - \alpha - F
$$

Substitute $a^*$ and $\alpha$:

$$
\Pi_P(\gamma)
= \frac{\gamma\tilde{H}^2}{k}
- \frac{1}{2k}\gamma^2\tilde{H}^2
- \frac{1}{2}r\gamma^2\sigma^2
- \bar{U} - F
$$

FOC yields optimal piece‑rate:

$$
\gamma^*
= \frac{\tilde{H}^2}{\tilde{H}^2 + rk\sigma^2}
$$

The second-order condition $\partial^2\Pi_P/\partial\gamma^2 = -\tilde H^2/k - r\sigma^2 < 0$ holds for all $\tilde H, k, r, \sigma^2 > 0$, confirming $\Pi_P(\gamma)$ is strictly concave and $\gamma^*$ is the unique global maximizer, so $\gamma^*\in(0,1)$ (Appendix A.0).

Optimal profit:

$$
\Pi_P^*(A)
= \frac{\tilde{H}^4}{2k(\tilde{H}^2 + rk\sigma^2)}
- \bar{U} - F
$$

---

## 5.3 Comparison of the Two Modes

Define profit difference:

$$
G(A) = \Pi_P^*(A) - \Pi_T(A)
$$

Section 6 shows:

- $G(0) < 0$ due to fixed cost $F$
- $G(A) \to +\infty$ as $A \to \infty$
- $G(A)$ is strictly convex on the entire domain (Appendix A.1), not merely for large $A$

Thus a unique threshold $A^*$ exists.

# 6. Main Results

This section presents the core theoretical results of the paper. We show that AI‑augmented production generates a unique threshold in AI utilization intensity at which firms optimally switch from time‑rate to piece‑rate compensation. We then characterize how this threshold responds to changes in output noise, worker risk aversion, and human–AI complementarity.

---

## 6.1 Existence and Uniqueness of the Contract Transformation Threshold

Define:

$$
G(A) = \Pi_P^*(A) - \Pi_T(A)
$$

---

### **Theorem 1 (Existence and uniqueness of $A^*$).**

*Domain and regularity.* $A$ ranges over $[0, \bar{A}]$ for some arbitrarily large $\bar{A}$ (the simulations in Section 7 use $\bar{A}=3$, matching the empirical AI-penetration range from Section 3.1); $k>0$ ensures the effort-cost function $\psi(a)=\tfrac{1}{2}ka^2$ is strictly convex, which is what guarantees a well-defined interior optimum $a^*$ in Sections 4.3 and 5.2. Given these regularity conditions:

There exists a **unique** threshold $A^* > 0$ such that:

- For $A < A^*$: $\Pi_T(A) > \Pi_P^*(A)$
- For $A > A^*$: $\Pi_P^*(A) > \Pi_T(A)$

---

### Proof

#### Step 1: Existence

At $A = 0$:

$$
G(0) < 0
$$

because piece‑rate profit includes fixed monitoring cost $F$.

As $A \to \infty$:

Time‑rate profit grows linearly:

$$
\Pi_T(A) \sim a_0\theta C A
$$

Piece‑rate profit grows quadratically:

$$
\Pi_P^*(A) \sim \frac{(\theta C)^2}{2k}A^2
$$

Thus:

$$
G(A) \to +\infty
$$

By continuity, at least one root exists.

---

#### Step 2: Uniqueness

$\Pi_T(A)$ is linear (affine) in $A$. $\Pi_P^*(A)$ can be shown to be strictly convex on the *entire* domain $[0,\bar A]$ — not merely in the asymptotic sense used above — via an explicit closed-form second derivative (Appendix A.1). Given this, $G(A)$ is itself strictly convex, being the difference of a convex and an affine function. A strictly convex function's lower level set $\{A : G(A)<0\}$ is an interval; since this interval contains $A=0$ (Step 1) and is bounded (since $G(A)\to+\infty$), it takes the form $[0,A^*)$ for a unique finite $A^*$, giving existence and uniqueness simultaneously. The complete argument, including the closed-form global convexity verification, is given in Appendix A.1–A.2.

$\blacksquare$

---

## 6.2 Comparative Statics of the Transformation Threshold

### **Theorem 2 (Comparative statics of $A^*$).**

The threshold $A^*$ satisfies:

$$
\frac{\partial A^*}{\partial \sigma^2} > 0, \qquad \frac{\partial A^*}{\partial r} > 0, \qquad \frac{\partial A^*}{\partial C} < 0
$$

That is, $A^*$ rises with output noise and worker risk aversion, and falls with human–AI complementarity. In fact (Appendix A.5–A.6), $A^*$ is exactly inversely proportional to $\theta C$, and the elasticities of $A^*$ with respect to $r$ and $\sigma^2$ are exactly equal.

### Proof

Using the implicit function theorem:

$$
\frac{\partial A^*}{\partial x}
= -\frac{\partial G/\partial x}{\partial G/\partial A},
\qquad x \in \{\sigma^2, r, C\}
$$

Denominator:

$$
\frac{\partial G}{\partial A}(A^*) > 0
$$

Thus the sign of each comparative static depends on the numerator.

---

### (i) Output noise $\sigma^2$

Piece‑rate profit:

$$
\Pi_P^*(A)
= \frac{\tilde{H}^4}{2k(\tilde{H}^2 + rk\sigma^2)}
- \bar{U} - F
$$

Differentiate:

$$
\frac{\partial \Pi_P^*}{\partial \sigma^2}
= -\frac{r\tilde{H}^4}{2(\tilde{H}^2 + rk\sigma^2)^2}
< 0
$$

Thus:

$$
\frac{\partial A^*}{\partial \sigma^2} > 0
$$

Interpretation:
More noise makes piece‑rate less attractive → firms require higher AI intensity to switch.

---

### (ii) Risk aversion $r$

$$
\frac{\partial \Pi_P^*}{\partial r}
= -\frac{\sigma^2\tilde{H}^4}{2(\tilde{H}^2 + rk\sigma^2)^2}
< 0
$$

Thus:

$$
\frac{\partial A^*}{\partial r} > 0
$$

Interpretation:
More risk‑averse workers require higher compensation under piece‑rate → delaying transformation.

---

### (iii) Human–AI complementarity $C$

Effective human capital:

$$
\tilde{H} = h + \theta AC
$$

Thus:

$$
\frac{\partial \tilde{H}}{\partial C} = \theta A > 0
$$

Higher $C$ increases both $\tilde H$ and the convexity of piece‑rate profit through it, making piece‑rate attractive earlier:

$$
\frac{\partial A^*}{\partial C} < 0
$$

The full derivation — including the calibration-dependent inequality this sign relies on — is given in Appendix A.4, since (unlike the sign for $r$ and $\sigma^2$) this result is not a pure algebraic identity independent of parameter values.

Interpretation:
Stronger complementarity accelerates transformation.

---

## 6.3 Implications for Contract Design

The results imply:

1. **Risk and uncertainty delay transformation.**
   High noise or high risk aversion pushes firms to remain in time‑rate mode.

2. **Human–AI complementarity accelerates transformation.**
   Training that improves complementarity lowers $A^*$.

3. **AI amplifies incentives.**
   As $A$ grows, piece‑rate becomes increasingly profitable due to convex productivity gains.

These insights form the theoretical foundation for Section 7's numerical simulations.

# 7. Numerical Simulation

This section presents numerical simulations that illustrate the theoretical results derived in Sections 5 and 6. Using the calibrated parameters from Section 3, we evaluate firm profit under the time‑rate and piece‑rate contracts, compute the contract transformation threshold $A^*$, and examine how risk, uncertainty, and regulation affect the profitability of output‑based compensation. An interactive version of the simulations below — allowing readers to vary $\sigma^2$, $r$, $C$, and $W_{\min}$ in real time and see $A^*$ recomputed on the fly — is available at https://danghaosheng2028.github.io/ai-contract-transformation/ (source: `docs/index.html` in the code repository).

All simulations use the baseline parameter set:

$$
(h,\theta,C,k,a_0,\bar{U},r,\sigma^2,F)
= (2.0,1.5,1.0,1.0,1.0,1.0,1.0,1.0,1.5)
$$

---

## 7.1 Baseline Profit Comparison and the Transformation Threshold

We compute:

- Time‑rate profit:

$$
\Pi_T(A)
= a_0(h+\theta AC) - \bar{U} - \frac{1}{2}ka_0^2
$$

- Piece‑rate profit:

$$
\Pi_P^*(A)
= \frac{\tilde{H}^4}{2k(\tilde{H}^2 + rk\sigma^2)}
- \bar{U} - F
$$

where:

$$
\tilde{H} = h + \theta AC
$$

Plotting $\Pi_T(A)$ and $\Pi_P^*(A)$ for $A \in [0,3]$ yields a unique intersection at:

$$
A^* \approx 0.65
$$

**Figure 1: Contract transformation threshold.** Plots calibrated time-rate profit $\Pi_T(A)$ against piece-rate profit $\Pi_P^*(A)$ for $A \in [0, 3]$. Time-rate profit rises only linearly because a fixed wage cannot capture the convex incentive gains AI-augmented effort makes possible; piece-rate profit rises convexly because higher $A$ raises effective human capital $\tilde{H}$, compounding through the $\tilde{H}^4$ term in $\Pi_P^*(A)$. The curves cross exactly once, at $A^* \approx 0.65$ under baseline calibration. Below the threshold, monitoring cost $F$ outweighs incentive gains and firms retain fixed wages; above it, convex gains dominate and output risk shifts onto workers. *(See `simulation/fig1_threshold.png` in the code repository, or explore this relationship interactively at the link above.)*

![Figure 1: Contract transformation threshold](fig1_threshold.png)

### Interpretation

- For $A < A^*$: fixed monitoring cost $F$ makes piece‑rate unprofitable.
- For $A > A^*$: convex productivity gains dominate, making piece‑rate optimal.

This confirms **Theorem 1**.

---

## 7.2 Comparative Statics: Threshold Surface $A^*(r,\sigma^2)$

We compute $A^*$ over a grid:

- $r \in [0.1,2.0]$
- $\sigma^2 \in [0.1,2.0]$

For each pair, solve:

$$
G(A) = 0
$$

### Results

- $A^*$ increases in worker risk aversion $r$
- $A^*$ increases in output noise $\sigma^2$
- $A^*$ decreases in human–AI complementarity $C$

These match **Theorem 2**.

---

## 7.3 Regulatory Friction: Minimum Wage Constraint

Introduce a minimum-wage floor on the base wage:

$$
\alpha \ge W_{\min}
$$

Because the worker's effort choice $a^*=\gamma\tilde H/k$ depends only on $\gamma$ (the base wage $\alpha$ enters the worker's problem as an additive transfer with no effect on the first-order condition), the floor does not change $a^*$ directly. What it changes is the firm's *optimal choice of $\gamma$ itself*, once $\alpha$ can no longer be driven arbitrarily negative to subsidize a high $\gamma$.

**Constrained profit.** For a given $\gamma$, IR requires

$$
\alpha(\gamma) = \max\left\{ W_{\min},\; \bar U + \frac{1}{2}r\gamma^2\sigma^2 - \frac{\gamma^2\tilde H^2}{2k} \right\}.
$$

When the unconstrained IR-wage already exceeds $W_{\min}$, the constraint is slack and profit is the unconstrained $\Pi_P(\gamma)$ of Section 5.2. When it falls short, $\alpha=W_{\min}$ and profit becomes

$$
\Pi_P^{MW,\text{bind}}(\gamma) = \frac{\gamma\tilde H^2}{k} - \frac{\gamma^2\tilde H^2}{k} - W_{\min} - F.
$$

**Optimal response under the constraint.** This binding-constraint branch is a downward-opening parabola in $\gamma$, with vertex at

$$
\gamma_c^* = \frac{1}{2}
$$

— an exact result independent of $\tilde H$, $\sigma^2$, $r$, or $W_{\min}$, since the risk-cost and incentive-cost terms shaping the unconstrained $\gamma^*$ have both been absorbed into the now-fixed $\alpha=W_{\min}$. A firm facing a binding wage floor optimally moves its incentive slope toward $1/2$, not toward the unconstrained $\gamma^*$ (which can approach 1 as $A$ grows). The firm's true optimal profit under the constraint, $\Pi_P^{MW}(A)$, is obtained by maximizing over $\gamma\in[0,1]$ with $\alpha(\gamma)$ as defined above.

**Threshold values.** Solving $\Pi_P^{MW}(A^*_{MW}) = \Pi_T(A^*_{MW})$ numerically for $A\in[0,50]$:

| $W_{\min}$ | $A^*_{MW}$ |
|---|---|
| 0.0 ($\alpha\ge0$ only) | 1.333 |
| 0.02 | 1.347 |
| 0.1 | 1.398 |
| 0.5 | 1.633 |
| 1.0 | 1.886 |
| 1.5 | 2.108 |

Every value remains within the empirically relevant range $A\in[0,3]$ (Section 3.1). The unconstrained baseline is $A^*\approx0.65$; even requiring only a non-negative base wage ($W_{\min}=0$) roughly doubles the threshold to $\approx1.33$, and $W_{\min}=1.5$ pushes it to $\approx2.11$ — over three times the frictionless benchmark, but still finite.

**Figure 2: Minimum-wage floor delays, but does not block, transformation over the empirically relevant AI-intensity range.** Plots $\Pi_T(A)$, the unconstrained $\Pi_P^*(A)$, and the correctly re-optimized $\Pi_P^{MW}(A)$ for $A\in[0,3]$ under $W_{\min}=0.5$, together with the optimal incentive slope $\gamma$ chosen at each $A$ under the binding constraint (converging to $\gamma_c^*=0.5$). $\Pi_P^{MW}(A)$ grows more slowly than $\Pi_P^*(A)$ — since it forgoes the negative-base-wage channel — but remains strictly convex and crosses $\Pi_T(A)$ at a finite point within the plotted range. *(See `simulation/fig2_minimum_wage.png` and `simulation/minimum_wage.py` in the code repository; the interactive tool above lets readers verify this directly by sweeping $W_{\min}$ from 0 to 2.)*

![Figure 2: Minimum-wage floor delays but does not block transformation](fig2_minimum_wage.png)

### Interpretation

- A binding minimum wage **substantially delays, but does not categorically block**, contract transformation within the empirically relevant range, once the firm's incentive slope $\gamma$ is correctly re-optimized under the constraint rather than held at its unconstrained value.
- The regulatory-friction narrative of Sections 2.3, 6, and 8.1 survives in qualitative form — minimum-wage protection roughly doubles to triples the AI intensity required before piece-rate becomes optimal — but the mechanism is dampened, not eliminated.

### 7.3.1 Robustness: convexity survives even under a stricter limited-liability constraint

A natural follow-up question is whether Theorem 1's central mechanism — piece-rate profit's convex growth eventually dominating time-rate's linear growth — survives once negative base wages are ruled out altogether ($\alpha\ge0$), a stricter and more institutionally realistic constraint than any specific statutory $W_{\min}$. Under the binding-constraint branch with $W_{\min}=0$, profit at the optimal $\gamma_c^*=1/2$ is

$$
\Pi_P^{MW,\text{bind}}(A)\Big|_{\gamma=1/2} = \frac{\tilde H^2}{4k} - F,
$$

which is still quadratic in $A$ (since $\tilde H$ is linear in $A$), with leading coefficient $(\theta C)^2/(4k)$ — one quarter of the unconstrained asymptotic coefficient $(\theta C)^2/(2k)$, but still strictly convex. We confirmed numerically that this constrained-branch profit overtakes $\Pi_T(A)$ at $A\approx1.33$ and continues to grow quadratically thereafter (the profit gap widens from $-1.0$ at $A=0$ to $+224$ at $A=20$). This is a reassuring robustness result: the paper's headline convexity mechanism does not depend on the unrealistic feature of allowing arbitrarily negative wages — it survives, with a higher but still finite threshold, under the strictest realistic limited-liability constraint.

---

## 7.4 Summary of Simulation Results

1. Piece‑rate profit is **convex** in AI intensity $A$, on the entire domain, not merely asymptotically (Appendix A.1).
2. Time‑rate profit is **linear** in $A$.
3. A unique transformation threshold $A^*$ exists, and is exactly proportional to $1/(\theta C)$ (Appendix A.5).
4. Noise and risk aversion **delay** transformation, with identical elasticities (Appendix A.6).
5. Human–AI complementarity **accelerates** transformation.
6. Minimum‑wage regulation **substantially delays** transformation — roughly doubling to tripling the required AI intensity across realistic floor levels (Section 7.3) — though it does not categorically block transformation within the empirically relevant AI-intensity range. This mechanism survives even under the stricter constraint of ruling out negative base wages entirely (Section 7.3.1).

These numerical results reinforce the theoretical findings and quantify the economic forces driving contract transformation in AI‑augmented production environments.

---

## 7.5 Sector Heterogeneity

Because $A^*$ depends on $(C,\sigma^2,r)$, occupations differ systematically in how early they cross the transformation threshold. Holding all other parameters at baseline, Table 2 reports illustrative calibrations for four occupation types, reflecting qualitative differences in AI complementarity, output monitorability, and typical risk exposure discussed in Sections 2–3.

**Table 2. Sector-heterogeneous transformation thresholds**

| Occupation | Representative real-world examples | $C$ | $\sigma^2$ | $r$ | $A^*$ |
|---|---|---|---|---|---|
| Delivery / ride-hailing riders | Meituan, Ele.me couriers | 1.2 | 0.5 | 0.8 | 0.466 |
| Livestream hosts | Douyin, Kuaishou livestream sellers | 1.5 | 1.8 | 1.0 | 0.500 |
| Designers / knowledge workers | Software engineers, graphic designers | 1.3 | 1.3 | 1.5 | 0.591 |
| Manufacturing line workers | Assembly-line factory workers | 0.4 | 0.7 | 1.0 | 1.516 |

*Note: only $(C, \sigma^2, r)$ vary by row; all other parameters use the Section 3.4 baseline. The "representative examples" column names commonly recognized occupation categories purely for illustration, not as claims about any specific company's actual compensation structure. Calibrations are illustrative rather than estimated from worker-level data (see Section 8.2). See `simulation/fig3_heterogeneity.png` and `simulation/simulate.py` in the code repository for the full computation.*

![Figure 3: Sector-heterogeneous transformation thresholds](fig3_heterogeneity.png)

Riders and livestream hosts, whose tasks are both highly monitorable (low $\sigma^2$) and strongly complemented by AI routing or recommendation algorithms (high $C$), cross the threshold at roughly two-thirds of the baseline AI intensity — consistent with the empirical observation (Section 3.5) that these occupations are already overwhelmingly piece-rate. Manufacturing line workers, whose tasks AI augments only weakly, require more than double the baseline AI intensity to reach $A^*$, and under many realistic parameter ranges may never cross it, explaining the persistence of time-rate compensation in that sector even as AI adoption rises economy-wide.

---

## 7.6 Joint Sensitivity of $A^*$ to $\theta$ and $k$

Section 7.2 varies $r$ and $\sigma^2$ while holding all else at baseline. Here we additionally vary the AI amplification coefficient $\theta$ and the effort-cost convexity parameter $k$ jointly, since $\theta$ and $k$ are calibrated more loosely than $r$ and $\sigma^2$ (which have established empirical ranges from Chetty, 2006).

**Table 3. $A^*(\theta, k)$ sensitivity grid** (all other parameters at Section 3.4 baseline)

| $\theta \backslash k$ | 0.70 | 0.85 | 1.00 | 1.15 | 1.30 |
|---|---|---|---|---|---|
| 1.20 | 0.291 | 0.558 | 0.812 | 1.057 | 1.295 |
| 1.35 | 0.259 | 0.496 | 0.722 | 0.940 | 1.151 |
| **1.50** | 0.233 | 0.446 | **0.650** | 0.846 | 1.036 |
| 1.65 | 0.212 | 0.406 | 0.591 | 0.769 | 0.942 |
| 1.80 | 0.194 | 0.372 | 0.541 | 0.705 | 0.863 |

The baseline cell ($\theta=1.50$, $k=1.00$) recovers $A^*\approx0.650$. Consistent with the exact elasticity result of Appendix A.5 ($\partial\ln A^*/\partial\ln\theta=-1$), moving along a row shows $A^*$ falling roughly in proportion to $1/\theta$. $A^*$ is comparably sensitive to $k$ (elasticity $\approx2.05$, the most sensitive parameter calibrated). Even at the most conservative corner of the grid ($\theta=1.20$, $k=1.30$), $A^*$ remains within the empirically plausible range $[0,3]$, so the qualitative conclusion is not an artifact of the point calibration in Section 3.4.

**Table 4. Elasticities of $A^*$ at baseline calibration** (finite-difference, $\pm1\%$ perturbation)

| Parameter | Elasticity $\partial\ln A^*/\partial\ln x$ | Note |
|---|---|---|
| $\sigma^2$ | +0.213 | = elasticity w.r.t. $r$ exactly (Appendix A.6) |
| $r$ | +0.213 | = elasticity w.r.t. $\sigma^2$ exactly (Appendix A.6) |
| $C$ | $-1.000$ | exact, closed form (Appendix A.5) |
| $\theta$ | $-1.000$ | exact, closed form (Appendix A.5) |
| $k$ | +2.048 | largest sensitivity of any parameter |
| $F$ | +0.792 | monitoring-cost pass-through |

# 8. Conclusion and Policy Implications

This paper develops a principal–agent model of compensation design under AI‑augmented production. By embedding AI intensity $A$ and human–AI complementarity $C$ into effective human capital:

$$
\tilde{H} = h + \theta AC
$$

we derive closed‑form expressions for optimal effort, optimal piece‑rate incentives, and firm profit under time‑rate and piece‑rate contracts.

A central theoretical result is the existence of a unique transformation threshold $A^*$ at which firms optimally switch from time‑rate to piece‑rate compensation, with an exact closed form $A^*\propto 1/(\theta C)$. Comparative statics show that the threshold increases in output noise and worker risk aversion (with identical elasticity for both) and decreases in human–AI complementarity. Numerical simulations confirm these results and show that minimum‑wage regulation substantially delays — roughly doubling to tripling the required AI intensity, though not categorically blocking — contract transformation within the empirically relevant AI-intensity range, and that the threshold varies systematically across occupations with different AI complementarity and monitorability.

---

## 8.1 Policy Implications

### (1) Differentiated labor regulation across industries

Industries with high AI penetration and strong complementarity (e.g., digital content creation) are likely above $A^*$ and benefit from output‑based pay.
Low‑AI or high‑noise industries remain below $A^*$, where time‑rate compensation is optimal.

### (2) Human–AI complementarity training

Because $A^*$ decreases in $C$ — and, in fact, is exactly inversely proportional to $\theta C$ (Appendix A.5) — policies that enhance workers' ability to collaborate with AI tools can accelerate beneficial contract transformation, and are, at the margin, an exact substitute for technology upgrades that raise $\theta$.

### (3) Minimum‑wage design for flexible employment

Binding wage floors raise the required base wage under piece‑rate compensation and, under baseline calibration, substantially delay transformation — roughly doubling to tripling the AI intensity required across the range of floors tested (Section 7.3) — rather than blocking it outright. Hybrid systems (minimum income guarantees, earnings smoothing) may protect workers with a smaller efficiency cost than a flat floor, though this paper's formal unification of the two contract modes (Appendix C) predicts that base-guarantee-plus-commission schemes are only optimal under monitoring-cost structures somewhat richer than the one calibrated here — a caveat discussed there in detail.

### (4) An efficiency–equity tradeoff, not a one-sided cost

Section 7.3's finding should not be read as a case against minimum-wage protection. From an efficiency standpoint, delaying contract transformation forgoes the productivity gains that convex, AI-augmented incentive pay could deliver at a given AI intensity. But from an equity and welfare standpoint, the same mechanism protects risk-averse workers from exactly the income volatility that unconstrained piece-rate contracts would impose as $\sigma^2$ and $A$ rise (Section 6.2(i)) — and, as Section 8.2 notes, may also mitigate multitasking harms (e.g., speed-versus-safety tradeoffs) that this paper's single-task framework does not itself model, meaning the equity case sketched here should be read as a lower bound. The model does not take a stance on how a regulator should weigh these effects; it only shows that the tradeoff is structural, not incidental — a wage floor cannot be fine-tuned to preserve the efficiency gains of AI-driven incentive pay while also serving its worker-protection purpose, because both effects flow from the same constraint on $\alpha$.

---

## 8.2 Limitations and Future Research

1. Noise is assumed Gaussian; AI prediction errors may be heavy‑tailed.
2. Multi‑agent extensions could analyze team production under AI.
3. Dynamic models could incorporate learning about AI tools.
4. Social-insurance contributions (工伤保险、社保) mandated alongside wage floors under China's 2021 Guiding Opinions are not modeled as a separate firm-side cost; incorporating them as an additional fixed cost under piece-rate compensation would plausibly strengthen the delaying effect documented in Section 7.3 further, not weaken it.
5. Complementarity $C$ is treated as exogenous and time-invariant. In practice, workers may endogenously invest in AI-collaboration skills to raise $C$ over time, which would make $A^*$ itself a dynamic, path-dependent object rather than a static threshold — a natural direction for future dynamic extensions of this model. Relatedly, the sector calibrations in Section 7.5 are illustrative, drawn from qualitative task characteristics rather than estimated from worker-level data; replacing them with data-informed values (e.g. platform-reported income variance by occupation) is a natural next step.
6. The baseline piece-rate contract in Sections 4.3 and 5.2 permits an arbitrarily negative base wage $\alpha$ in the unconstrained case. Section 7.3.1 shows the paper's central convexity mechanism survives even under the stricter institutional constraint $\alpha\ge0$, though with a higher threshold — a robustness check we view as resolving, rather than merely flagging, this earlier concern.
7. **From moral hazard to hidden information: screening under unobserved $(r, C)$.** The model in Sections 4–5 treats worker risk aversion $r$ and human–AI complementarity $C$ as parameters the firm can effectively condition on when setting $(\alpha, \gamma)$. In practice, a platform typically cannot observe an individual worker's risk aversion or her capacity to complement AI-assisted tasks before contracting with her; these are private information. This connects the paper's single-threshold framework to the broader theory of incentives under hidden information developed by Laffont and Tirole (1993), who show that when an agent's type is unobserved, the principal generally cannot implement the full-information contract $(\alpha^*, \gamma^*)$ derived in Section 5.2 for every worker, and instead must offer a menu of contracts $\{(\alpha_i, \gamma_i)\}$ designed to induce self-selection. Extending the present model in this direction would replace the single transformation threshold $A^*$ of Theorem 1 with a *separation condition*: for a given AI intensity $A$, the platform would need to determine whether the gain from screening — offering low-$\gamma$ contracts that retain risk-averse or low-$C$ workers alongside high-$\gamma$ contracts that extract surplus from risk-tolerant, high-$C$ workers — exceeds the informational rents such a menu must concede to induce truthful revelation. This would generalize $A^*$ from a scalar cutoff into a *region* in $(A, r, C)$-space, and offers a natural bridge between this paper's aggregate-firm framing and worker-level heterogeneity of the kind documented in Section 7.5. We leave the formal characterization of this screening extension to future work.
8. **Single-task framework and the multitasking blind spot.** This paper cites Holmstrom and Milgrom (1991) for its general theory of linear contracting under CARA-normal uncertainty, but does not apply that same paper's central substantive insight — that high-powered incentives on measurable tasks induce agents to systematically neglect unmeasured tasks — to its own setting. This is a first-order omission for the platform-labor context motivating this paper: piece-rate compensation for delivery riders, for instance, is widely associated in policy discussion with speed-versus-safety tradeoffs that a single-task effort model cannot represent. Extending the model to a multitask setting (a₁ = measurable output, a₂ = unmeasured quality/safety, with a joint cost function $\psi(a_1,a_2)$) would very plausibly strengthen — not weaken — the paper's regulatory conclusion in Section 8.1: minimum-wage protection's welfare case would gain an additional channel beyond risk-sharing, since dampening the incentive slope $\gamma$ under a binding floor (Section 7.3.1) would also mitigate multitasking distortions. We do not model this extension here but flag it as the most substantively important direction for future work, and note explicitly that the current efficiency-equity tradeoff in Section 8.1(4) should be read as a lower bound on the equity case for regulation, since it omits this channel entirely.

---

# Appendix A. Additional Proofs

This appendix provides complete derivations for (i) the second-order conditions underlying the worker's effort choice and the firm's optimal piece rate (Section A.0); (ii) an explicit global-convexity verification of $\Pi_P^*(A)$ completing the proof of Theorem 1, which the main text only established asymptotically (Sections A.1–A.2); (iii) the comparative-statics proofs of Theorem 2, with a corrected derivation for $\partial A^*/\partial C$ (Sections A.3–A.4); and (iv) two exact structural corollaries not stated in the main text (Sections A.5–A.6).

## A.0 Second-Order Conditions (SOC)

**Worker's effort choice.** The worker's problem is $\max_a\{\gamma a\tilde H - \tfrac12 ka^2\}$. The second derivative with respect to $a$ is $-k<0$ for all $k>0$, so $a^*=\gamma\tilde H/k$ characterizes a strict global maximum.

**Firm's piece-rate choice.** From Section 5.2,

$$
\Pi_P(\gamma) = \frac{\gamma\tilde H^2}{k} - \frac{\gamma^2\tilde H^2}{2k} - \frac{1}{2}r\gamma^2\sigma^2 - \bar U - F.
$$

This is quadratic in $\gamma$ with leading coefficient

$$
\frac{\partial^2\Pi_P}{\partial\gamma^2} = -\frac{\tilde H^2}{k} - r\sigma^2 < 0
$$

for all $\tilde H, k, r, \sigma^2 > 0$. Hence $\Pi_P(\gamma)$ is strictly concave everywhere on its domain, and $\gamma^*=\tilde H^2/(\tilde H^2+rk\sigma^2)$ characterizes the unique global maximizer, confirming $\gamma^*\in(0,1)$.

## A.1 Global Convexity of $\Pi_P^*(A)$ (completing the proof of Theorem 1)

The main text establishes $G(A)\to+\infty$ as $A\to\infty$ via the asymptotic orders of $\Pi_T$ (linear) and $\Pi_P^*$ (quadratic), and states uniqueness from "a strictly convex function minus a linear function." This requires $\Pi_P^*(A)$ to be convex on the *entire* domain $[0,\bar A]$, not merely asymptotically. We verify this directly.

Write $H=\tilde H(A)=h+\theta AC$ and $b=rk\sigma^2$ (a positive constant). Then

$$
\Pi_P^*(A) = \frac{H^4}{2k(H^2+b)} - \bar U - F.
$$

Differentiating twice with respect to $A$ (using $dH/dA=\theta C$, a constant) and simplifying yields

$$
\frac{d^2\Pi_P^*}{dA^2} = (\theta C)^2\cdot\frac{H^2(H^4+3bH^2+6b^2)}{k(H^2+b)^3}.
$$

Since $H>0$ (as $h>0$ and $A,\theta,C\ge0$) and $b>0$, every term in the bracketed numerator is strictly positive, and the denominator $k(H^2+b)^3>0$. Hence

$$
\frac{d^2\Pi_P^*}{dA^2} > 0 \quad\text{for all } A\ge0,
$$

establishing that $\Pi_P^*(A)$ is strictly convex on the entire domain. (This closed-form expression was verified against direct numerical second differencing at $A\in\{0,0.2,0.5,0.65,1,2,3,5,10\}$ under baseline calibration, matching to five decimal places at every point.)

## A.2 Existence and Uniqueness (completing Theorem 1)

With $\Pi_T(A)$ affine and $\Pi_P^*(A)$ strictly convex on $[0,\bar A]$ (Section A.1), $G(A)=\Pi_P^*(A)-\Pi_T(A)$ is itself strictly convex.

A strictly convex function's lower level set $\{A\in[0,\bar A]:G(A)<0\}$ is an interval: if $G(A_1)<0$ and $G(A_2)<0$ for $A_1<A_2$, convexity implies $G(A)$ lies below the chord connecting these points for all $A\in[A_1,A_2]$, and hence below $0$. Since $G(0)<0$ (Section 6.1, Step 1), this interval contains $0$ and, being an interval, takes the form $[0,A^*)$ for some $A^*$. Because $G(A)\to+\infty$, the interval is bounded, so a finite crossing point $A^*$ exists with $G(A^*)=0$, $G(A)<0$ for $A<A^*$, and $G(A)>0$ for $A>A^*$ (strict convexity precludes $G$ re-entering negative territory once past the first crossing). This gives existence and uniqueness simultaneously, correcting the informal "convex minus linear crosses zero exactly once" statement — which is false in general (a convex function can cross zero twice) but holds here specifically because the level-set argument pins the first crossing to originate from $G(0)<0$. $\blacksquare$

## A.3 Derivative with Respect to Risk Aversion $r$

Piece‑rate profit is:

$$
\Pi_P^*(A)
= \frac{\tilde{H}^4}{2k(\tilde{H}^2 + rk\sigma^2)}
- \bar{U} - F
$$

Differentiate with respect to $r$:

$$
\frac{\partial \Pi_P^*}{\partial r}
= -\frac{\sigma^2\tilde{H}^4}{2(\tilde{H}^2 + rk\sigma^2)^2}
$$

Since all parameters are positive:

$$
\frac{\partial \Pi_P^*}{\partial r} < 0
$$

Time‑rate profit does not depend on $r$, so:

$$
\frac{\partial G}{\partial r}
= \frac{\partial \Pi_P^*}{\partial r} < 0
$$

Using the implicit function theorem:

$$
\frac{\partial A^*}{\partial r}
= -\frac{\partial G/\partial r}{\partial G/\partial A}
$$

The denominator is positive:

$$
\frac{\partial G}{\partial A}(A^*) > 0
$$

Thus:

$$
\frac{\partial A^*}{\partial r} > 0
$$

### Interpretation

More risk‑averse workers require higher compensation under piece‑rate pay, reducing firm profit and delaying contract transformation.

## A.4 Derivative with Respect to Complementarity $C$ (corrected proof)

The claim "the convexity of $\Pi_P^*$ ensures $\partial G/\partial C>0$" does not follow from convexity in $A$ alone; convexity of $\Pi_P^*$ in $A$ says nothing about the sign of its cross-partial with $C$. We instead verify the inequality directly at the equilibrium threshold.

Differentiating $\Pi_P^*(A)$ with respect to $C$ (holding $A$ fixed, using $\partial H/\partial C=\theta A$):

$$
\frac{\partial\Pi_P^*}{\partial C} = \theta A\cdot\frac{H^3(H^2+2b)}{k(H^2+b)^2}
$$

and differentiating $\Pi_T(A)$ with respect to $C$:

$$
\frac{\partial\Pi_T}{\partial C} = a_0\theta A.
$$

Hence

$$
\frac{\partial G}{\partial C} = \theta A\cdot\left\{\frac{H^3(H^2+2b)}{k(H^2+b)^2} - a_0\right\}.
$$

For $A>0$, the sign of $\partial G/\partial C$ matches the sign of the bracketed term. **This is not a universal algebraic identity** — it depends on parameter values at $A=A^*$. Under baseline calibration ($h=2$, $\theta=1.5$, $k=1$, $r=1$, $\sigma^2=1$, $a_0=1$) evaluated at $A^*\approx0.6496$ ($H\approx2.974$, $b=1$):

$$
\frac{H^3(H^2+2b)}{k(H^2+b)^2} \approx 2.944 > a_0 = 1.0,
$$

so $\partial G/\partial C>0$ at the equilibrium threshold under baseline calibration, with a margin of roughly $3\times$ — not a knife-edge result. Given $\partial G/\partial A(A^*)>0$ (Section A.2), the implicit function theorem gives

$$
\frac{\partial A^*}{\partial C} = -\frac{\partial G/\partial C}{\partial G/\partial A} < 0. \quad\blacksquare
$$

**Note.** Because this step depends on calibration rather than being a pure algebraic identity, the precise statement is: this holds whenever complementarity is productive enough, relative to the enforced minimum effort $a_0$ under time-rate pay, that raising $C$ creates more marginal option value under the convex piece-rate branch than under the linear time-rate branch — satisfied comfortably under our calibration, but not a theorem-level universal claim.

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
2. Since $\theta$ and $C$ enter identically, doubling either has an identical effect on $A^*$: AI-complementarity training and technology upgrades that raise $\theta$ are, at the margin, perfect substitutes for accelerating contract transformation (cf. Section 8.1(2)).

## A.6 Corollary: Equal Elasticities for $r$ and $\sigma^2$

By an analogous argument, $r$ and $\sigma^2$ enter the model only through the product $b\equiv rk\sigma^2$. Since $\partial\ln b/\partial\ln r = \partial\ln b/\partial\ln\sigma^2 = 1$ identically, and $A^*$ depends on $r,\sigma^2$ only via $b$, it follows that

$$
\frac{\partial\ln A^*}{\partial\ln r} = \frac{\partial\ln A^*}{\partial\ln\sigma^2}
$$

exactly, for any parameter values. Confirmed numerically: both elasticities equal $0.213$ under baseline calibration. Worker risk aversion and output-noise variance are interchangeable drivers of the transformation threshold — a doubling of either has exactly the same proportional effect on $A^*$.

---

# Appendix B. Parameter Calibration Details

This appendix provides additional justification for the parameter values used in the numerical simulations in Section 7. The calibration is designed to ensure internal consistency, empirical plausibility, and alignment with stylized facts from China's rapidly digitalizing labor markets.

---

## B.1 Human Capital and AI Amplification

Baseline human capital:

$$
h = 2.0
$$

AI amplification coefficient:

$$
\theta = 1.5
$$

Human–AI complementarity:

$$
C = 1.0
$$

These values ensure that effective human capital:

$$
\tilde{H} = h + \theta AC
$$

increases meaningfully with AI intensity $A$ while remaining within empirically plausible ranges.

---

## B.2 Effort Cost and Monitoring

Effort cost parameter:

$$
k = 1.0
$$

Minimum enforceable effort under time‑rate:

$$
a_0 = 1.0
$$

Reservation utility:

$$
\bar{U} = 1.0
$$

Monitoring cost for piece‑rate implementation:

$$
F = 1.5
$$

These values reflect typical magnitudes in principal–agent models and ensure that time‑rate compensation is initially more profitable when AI intensity is low.

---

## B.3 Noise and Risk Aversion

Output noise:

$$
\sigma^2 = 1.0
$$

Worker risk aversion:

$$
r = 1.0
$$

These values lie in the center of empirically estimated ranges for gig‑economy workers (Chetty 2006; subsequent studies).

---

## B.4 AI Intensity Range

The simulation range:

$$
A \in [0,3]
$$

corresponds to the empirical transition from low to high AI penetration in Chinese firms, based on CAICT digitalization statistics.

---

## B.5 Baseline Transformation Threshold

Using the calibrated parameters, the baseline contract transformation threshold satisfies:

$$
A^* \approx 0.65
$$

This value lies within the mid‑range of observed AI adoption levels in digital service industries, providing empirical grounding for the model's predictions.

---

## B.6 Sector Heterogeneity Calibration

Table 2 (Section 7.5) varies $(C, \sigma^2, r)$ by occupation while holding $(h, \theta, k, a_0, \bar{U}, F)$ at their Section 3.4 baseline values. The direction of each adjustment — higher $C$ and lower $\sigma^2$ for platform-mediated, algorithmically-routed tasks; lower $C$ for tasks AI augments only weakly — follows directly from the task characteristics discussed in Sections 2.3 and 3.5, but the specific magnitudes are illustrative rather than estimated. Full reproduction code and numerical output are provided in `simulation/simulate.py` and `simulation/results.json` in the accompanying code repository.

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

# References

Acemoglu, D., & Restrepo, P. (2018). *The Race Between Man and Machine*.

Brynjolfsson, E., Li, Y., & Raymond, L. (2025). *Productivity Effects of AI Tools*.

Chen, D. and Guo, W. (2023) 'Digital Transformation, Wage Growth and Income Gap Across Firms: Also on the Industry-Leading Effect of "Lighthouse Factory"', *Journal of Finance and Economics* (财经研究), 49(4), pp. 50–64.

Chetty, R. (2006). *A New Method for Estimating Risk Aversion*.

Holmstrom, B. (1979). *Moral Hazard and Observability*.

Holmstrom, B., & Milgrom, P. (1991). *Multitask Principal–Agent Problems*.

International Labour Organization (2021). *Digital Labour Platforms in China: Working Conditions, Policy Issues and Future Prospects*. ILO Working Paper 24.

Laffont, J.-J., & Tirole, J. (1993). *A Theory of Incentives in Procurement and Regulation*. MIT Press.

Lazear, E. (2000). *Performance Pay and Productivity*.

Prendergast, C. (2002). *The Tenuous Tradeoff Between Risk and Incentives*.

Shin, J., & Kang, H. (2026). *AI and Compensation Systems*.
