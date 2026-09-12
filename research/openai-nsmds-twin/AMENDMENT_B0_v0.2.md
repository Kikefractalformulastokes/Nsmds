# NS-MDS Twin Study — B0 Control Amendment v0.2

**Date:** 13 September 2026  
**Status:** preregistration amendment before B0/B1 production runs  
**Scope:** corrects the control dynamics in v0.1; no outcome data were inspected before this amendment.

## Reason for amendment

Version 0.1 wrote the experimental dynamics as

\[
D_1u+\mathbb P[(u\cdot\nabla)u]
=\nu\Delta u+\mathbb Pf+\gamma(D_1u-D_2u),
\]

while also requiring the control condition \(\gamma=0\) to recover the ordinary Navier–Stokes baseline.

Those two statements are inconsistent when \(\alpha\neq 0\), because

\[
D_1u=\partial_tu+\alpha\frac{u-\bar u_{\tau_1}}{\tau_1}
\]

still contains a memory term at \(\gamma=0\).

## Corrected experimental dynamics

For B0 onward, the frozen experimental branch is therefore

\[
\partial_tu+\mathbb P[(u\cdot\nabla)u]
=\nu\Delta u+\mathbb Pf+\gamma\,(D_1u-D_2u).
\]

The twin-memory objects remain

\[
D_1u=D_{\tau_1,\alpha}u,\qquad
D_2u=D_{\tau_2,\beta}u,
\]

and

\[
S_{\rm twin}(t)=\|D_1u-D_2u\|_X.
\]

With the corrected dynamics, \(\gamma=0\) removes the augmentation identically and recovers the frozen baseline equation by construction.

## B0 acceptance gate

B0 passes only if all of the following hold:

1. the augmentation term evaluates identically to zero for \(\gamma=0\);
2. the corrected residual equals the baseline residual to machine precision on the manufactured test suite;
3. a deliberately nonzero \(\gamma\) produces a detectable difference on at least one nontrivial smooth trajectory;
4. no target-construction data are used to tune the B0 test.

## B1 acceptance gate

Before any singular-target experiment, the causal exponential memory implementation must be tested on smooth manufactured trajectories with known analytic convolution. The numerical memory error must decrease under time-step refinement and remain finite/stable over the frozen test interval.

## Claim boundary

This amendment does not establish any physical, predictive, or mathematical advantage of NS-MDS. It only repairs the control definition required for a valid baseline comparison.
