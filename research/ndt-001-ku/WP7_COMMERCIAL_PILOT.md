# CoreSyn — NDT Model Assurance & Localization Validation Pilot

## Buyer problem

NDT and AI-assisted inspection teams can have impressive average metrics while still carrying hidden tail failures, sensitivity to noise/distribution shift, weak reproducibility, or claims that exceed the evidence. CoreSyn provides an independent evidence layer before deployment or procurement decisions.

## Pilot objective

Independently reproduce and stress-test one customer-selected NDT localization/classification pipeline and produce an auditable evidence pack showing what works, where it fails, and what can defensibly be claimed.

## Proposed 6-week scope

### WP1 — Evidence intake & protocol freeze
- Model/pipeline inventory.
- Dataset and ground-truth provenance review.
- Baseline definition.
- Frozen metrics, splits and acceptance criteria.

### WP2 — Independent reproduction
- Reproduce customer baseline in an isolated evaluation harness.
- Environment/seed/version capture.
- Discrepancy register.

### WP3 — Robustness & shift testing
- Noise/SNR sweeps where technically appropriate.
- Distribution-shift tests.
- Missing/corrupted signal checks where appropriate.
- Tail-error and worst-case review.

### WP4 — Challenger & ablation
- Matched generic baselines/challengers where useful.
- Component ablation.
- Attribution: identify which mechanism actually changes performance.

### WP5 — Statistical assurance
- Paired comparisons.
- Bootstrap/confidence intervals as appropriate.
- Sensitivity to splits/cases.
- Failure-mode and confidence diagnostics.

### WP6 — Claim gate & evidence pack
- Approved / prohibited claim matrix.
- Machine-readable metrics and predictions.
- Reproduction scripts/configuration.
- Evidence manifest and cryptographic receipts.
- Executive technical review.

## Deliverables

1. Frozen Evaluation Protocol.
2. Baseline Reproduction Report.
3. Robustness/OOD Matrix.
4. Failure-Mode & Tail-Risk Report.
5. Ablation/Attribution Report.
6. Statistical Validation Report.
7. Claim Gate.
8. Reproducible Evidence Pack.
9. Executive readout for engineering/quality leadership.

## Commercial packaging

### Option A — NDT Assurance Diagnostic
2 weeks. One pipeline, one dataset, reproduction + initial stress test + claim review.
Indicative fee: **EUR 18k–25k**.

### Option B — NDT Model Assurance Pilot
6 weeks. Full WP1–WP6 scope above.
Indicative fee: **EUR 55k–75k**.

### Option C — Deployment Evidence Program
8–12+ weeks. Multiple datasets/conditions, customer-specific validation matrix, reviewer support and expanded evidence pack.
Indicative fee: **EUR 90k–120k+**, scoped after technical intake.

Fees are commercial positioning, not a representation of market-cleared pricing. Travel, specialist test campaigns, proprietary data acquisition, certification-body work and hardware testing are separately scoped.

## Success criteria

The pilot succeeds when the customer has a reproducible answer to:

- Can we reproduce the claimed performance?
- Under which conditions does it degrade?
- Which cases dominate risk?
- Which component causes any measured improvement?
- What evidence is still missing?
- What can engineering, quality and management safely claim?

The pilot does NOT require CoreSyn to make the customer's model look better. Finding a hidden failure mode is a successful assurance outcome.

## Case-study proof point

CoreSyn's public guided-wave case study demonstrates the workflow itself: frozen baseline reproduction, continuous challenger evaluation, noise/OOD testing, paired statistical analysis, ablation, internal blind validation and explicit claim control. See `M9_CLAIM_GATE.md` for exact permitted wording and limitations.

## Positioning line

**Proof before trust. Independent evidence for NDT models before the claim becomes a decision.**
