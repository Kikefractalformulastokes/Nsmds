# NS-MDS B3 Parameter Freeze v0.1

**Status:** FROZEN BEFORE TARGET INSPECTION  
**Study:** OpenAI x NS-MDS Twin-Derivative Study  
**Date:** 13 September 2026

## Purpose

This file freezes the primary NS-MDS parameters before any production comparison against the OpenAI singular target. Parameters may not be changed to improve target results. Any later change requires a new preregistered branch/version and must not overwrite the results obtained under this freeze.

## Evidence entering B3

- B0 control gate: PASS. The amended experimental formulation recovers the baseline exactly when the NS-MDS coupling is disabled.
- B1 causal-memory manufactured solution: PASS under time-step refinement.
- B2 smooth/null temporal controls: PASS for steady, periodic, decaying, and high-gradient-smooth manufactured controls.
- B2 run: 34724769750.
- B2 source commit: a2c8fa132ca0fb8a6f9b8f29a02d06784e7d46b2.
- B2 evidence artifact digest: sha256:b44d1fde7fc2cb7295827863d619b7fd190cdb7e240d8755d7462518b6d6fe60.

## Frozen primary operator

For exponential causal memory

m_tau(t) = integral_0^t tau^-1 exp(-(t-s)/tau) u(s) ds,

use

D_{tau,a} u = partial_t u + a (u-m_tau)/tau.

The primary twin observable is

T_12[u] = D_{tau1,alpha}u - D_{tau2,beta}u,

S_twin(t) = ||T_12[u](t)||_X.

## Frozen parameters

- tau1 = 0.18
- tau2 = 0.72
- alpha = 1.0
- beta = 1.0
- gamma = 0.0 for the PRIMARY study

The primary study is therefore OBSERVATIONAL: NS-MDS does not modify the Navier-Stokes trajectory. A nonzero-gamma modified-dynamics study, if performed, is a separate secondary experiment and cannot be used to establish a claim about the original Navier-Stokes dynamics.

## Frozen primary norm for a 3D field

Primary norm:

X = L2_x on the declared spatial domain.

Primary normalized signal:

S_norm(t) = ||T_12[u](t)||_L2 / (1 + ||u(t)||_L2).

Secondary diagnostics may be recorded but are not allowed to replace the primary endpoint after target inspection:

- ||T_12[u]||_H1,
- ||curl T_12[u]||_L2,
- energy,
- enstrophy,
- ||omega||_infinity,
- divergence residual,
- PDE residual.

## Frozen temporal refinement set

For dimensionless/manufactured validation runs:

- dt = 0.02
- dt = 0.01
- dt = 0.005

For a target construction with a different natural time scale, these values must be mapped by a declared nondimensionalization before inspection. The ratios 4:2:1 are frozen.

## Frozen null-reference envelope

The B2 smooth/null controls produced the following finest-grid tail maxima of the normalized twin signal:

- steady: 0.012455602407863513
- periodic: 0.4285442207784155
- decaying: 0.017126678421761018
- high-gradient smooth: 0.6011005958872644

These values are reference controls, not universal thresholds for singularity. No target will be labelled singular solely because it exceeds them.

## Frozen primary question

Does the primary L2 twin-memory observable provide reproducible positive lead time or perturbation-classification information about the target event beyond the frozen classical diagnostics, while remaining stable under refinement and without comparable false triggering on matched smooth controls?

## No post-hoc promotion rule

A positive result requires all of:

1. target baseline independently reproduced;
2. PDE and divergence residuals acceptable under a declared tolerance;
3. signal stable under refinement;
4. positive lead time under a criterion fixed before outcome inspection;
5. no comparable false trigger on matched smooth controls;
6. effect not reducible to a trivial rescaling of a classical diagnostic;
7. parameters above unchanged;
8. code, environment, hashes, and outputs preserved;
9. independent clean-room rerun before publication-grade promotion.

## Claim boundary

This freeze does not claim singularity prediction, regularity, proof of blow-up, or a solution of the Navier-Stokes Millennium Prize problem. It exists to prevent post-hoc tuning and to make the next target experiments falsifiable.
