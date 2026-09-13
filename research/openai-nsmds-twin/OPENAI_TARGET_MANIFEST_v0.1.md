# OpenAI 3D Target Manifest v0.1

**Purpose:** freeze the exact external target that NS-MDS will attempt to reproduce/observe before any B4 perturbation atlas.

**OpenAI source repository:** `openai/NavierStokesAndEuler`  
**Frozen commit:** `f9e8bc5b38b6e212696e8a30e3e91517af887bbd`

## 1. Formal target facts frozen from source

1. The periodic comparator theorem constructs, for every positive viscosity `nu`, zero initial data and a forcing satisfying the comparator force conditions for which no global smooth periodic solution exists.
2. The source states that the full periodic corollary supplies a solution that blows up exactly at time `t = 1`.
3. The bridge normalizes arbitrary positive viscosity to viscosity one by time/amplitude rescaling.
4. The comparator witness uses zero initial velocity.
5. The forcing is smooth, periodic, and obtained from the project candidate with compact future-time support / decay consequences.
6. The exact construction is assembled from the project's physical candidate machinery (`ActualCandidateConstruction`, `ActualCandidateAssembly`, stage/prefix/activation modules) rather than from a short closed-form velocity formula.

## 2. Exact construction identifiers

From `ActualCandidateConstruction.lean`:

- `selectedBudget := 0`
- `selectedThreshold := ActualCarrierGeometry.startingThreshold 0`
- `selectedCycle := cycle selectedBudget selectedThreshold`
- `selectedQbig := qbig selectedBudget selectedThreshold`
- physical prefixes are constructed through `chartVelocity`, `chartPressure`, `chartVelocityStages`, `chartPressureStages`, `chartPotentialParts`, and `chartDirectStages`.

From `ComparatorTheorem.lean`:

- theorem: `NavierStokes.ComparatorBridge.navier_stokes_breakdown_periodic`
- for every `nu > 0`, obtains the periodic paper corollary and transports it to the comparator statement.

## 3. NS-MDS target convention

Primary NS-MDS observation target will use viscosity-one normalization unless a later source-extraction gate proves that another normalization is required for a specific physical prefix.

Frozen event time:

`T_star = 1`.

Frozen initial condition:

`u_0 = 0`.

Frozen primary NS-MDS parameters remain those in B3 and MUST NOT be retuned after target inspection.

## 4. Critical limitation before B4

The Lean source proves properties of a candidate assembled through `noncomputable` definitions and a large constructive hierarchy. The frozen repository does **not** by itself provide a ready-to-run 3D array, CFD checkpoint, mesh field, or short explicit numerical formula for `u(x,t)` that can simply be sampled by the current Python harness.

Therefore:

- B4 MUST NOT start from a guessed surrogate and label it the OpenAI solution.
- An asymptotic toy model may be used only as an explicitly labelled probe, never as target reproduction.
- `BASELINE_REPRODUCED` remains false until an executable representation of the OpenAI candidate (or a rigorously equivalent sampled representation) is produced and checked against its governing equation/residual and source construction.

## 5. Materialization gate M0

Before B4, satisfy one of:

**M0-A — direct extraction**  
Derive executable/samplable field evaluators from the frozen candidate constructors and verify source correspondence.

**M0-B — author-provided executable artifact**  
Use an official numerical evaluator/checkpoint/dataset for the same frozen construction, with hashes and correspondence checks.

**M0-C — independently implemented equivalent representation**  
Implement the published construction from its definitions and prove/verify equivalence to the relevant frozen source objects to declared tolerances.

Required outputs:

- velocity samples `u(x,t)`;
- pressure samples `p(x,t)` where needed;
- forcing samples `f(x,t)`;
- divergence residual;
- Navier-Stokes PDE residual;
- event-time behavior near `t=1`;
- source/hash provenance.

## 6. Claim boundary

Current status after B0/B1/B2/B3:

- memory implementation controls: PASS;
- smooth/null controls: PASS;
- NS-MDS parameters: FROZEN;
- OpenAI Lean comparator clean build: independently reproduced in the separate audit chain;
- OpenAI 3D candidate numerically reproduced: **NOT YET**;
- B4 perturbation atlas: **BLOCKED ON M0**.

No Source = No Claim. No executable target = No B4 target claim.
