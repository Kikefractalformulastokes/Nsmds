# OpenAI Audit Closure Gate + NS-MDS Twin Execution Matrix v0.1

**Date:** 12 September 2026  
**Status:** active research gate

## A. OpenAI audit closure gate

The OpenAI chain cannot be marked VERIFIED until every mandatory gate below is independently closed.

### A1. Source freeze
- Freeze the exact OpenAI paper version.
- Freeze the exact Lean repository / commit used for the published claim.
- Record SHA-256 / commit identifiers for all source artifacts.

### A2. Statement correspondence
- Map the published theorem statement to the official Clay C/D formulation.
- Verify initial data, forcing, smoothness class, incompressibility, finite-energy condition, domain, and event definition.
- Record any strengthening, weakening, or changed assumption.

### A3. Analytical proof audit
- Build a lemma dependency map.
- Verify each nontrivial inequality and asymptotic step.
- Identify where finite-time loss of regularity is established.
- Check whether any circular dependence or unstated regularity assumption occurs.

### A4. Lean correspondence
- Clean build from frozen dependencies.
- Verify theorem names and final statements correspond to the analytical target.
- Record axioms, admitted statements, classical assumptions, external oracles, or unformalized bridges if any.

### A5. Adversarial checks
- Search for assumption mismatches.
- Test edge cases and parameter boundaries.
- Independently recompute selected critical estimates.
- Attempt counterexamples against intermediate lemmas where mathematically meaningful.

### A6. Disposition
Allowed dispositions:
- VERIFIED_BOUNDED
- VERIFIED_FORMAL_CHAIN_WITH_SCOPE_LIMITS
- CONDITIONAL
- HOLD
- FAIL

`OPENAI SOLUTION VALIDATED BY CORESYN` is prohibited unless the whole frozen chain closes and the wording is scoped exactly to what was independently checked.

---

## B. NS-MDS Twin execution matrix

### B0 — Null baseline
Set memory coupling to zero. Requirement: recover the reference baseline to frozen numerical tolerance.

### B1 — Memory operator sanity
For smooth manufactured solutions:
- convergence under time-step refinement;
- convergence under grid refinement;
- bounded divergence residual;
- bounded PDE residual;
- kernel normalization and causal support checks.

### B2 — Twin observable controls
Compute

\[
S_{twin}(t)=\|D_{\tau_1,\alpha}u-D_{\tau_2,\beta}u\|_X.
\]

Test on:
1. steady smooth flow;
2. periodic smooth flow;
3. decaying vortex control;
4. manufactured high-gradient but globally smooth control;
5. reproduced OpenAI target if A-gate permits.

### B3 — Frozen parameter grid
Before target inspection, freeze a compact grid for:
- tau_1
- tau_2
- alpha
- beta
- gamma

No post-hoc expansion may be counted as confirmatory evidence.

### B4 — Perturbation atlas
Use perturbation families with frozen amplitudes epsilon and seeds. Classify outcome only after numerical-convergence gates pass.

Primary classes:
- PRESERVE
- ADVANCE
- DELAY
- DESTROY
- INDETERMINATE

### B5 — Early-warning criterion
A valid early-warning result requires:
- positive lead time relative to a frozen classical indicator;
- reproducibility across refinement;
- materially lower false-positive rate on matched smooth controls;
- effect size and uncertainty reported;
- superiority over at least one simpler memory-free diagnostic.

### B6 — Clean-room reproduction
A second independent directory/environment reruns all promoted results from a manifest. Promoted outputs must match within declared tolerances; deterministic outputs should hash-match where possible.

---

## C. Promotion ladder

1. PREREGISTERED
2. BASELINE_REPRODUCED
3. NULL_TESTS_PASS
4. TARGET_TESTS_PASS
5. PERTURBATION_ATLAS_REPRODUCED
6. NEW_BOUNDED_CLAIM
7. ANALYTIC_PROPOSITION_CANDIDATE
8. INDEPENDENT_REVIEW
9. PUBLICATION_READY

No step may be skipped.
