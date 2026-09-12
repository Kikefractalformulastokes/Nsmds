# OpenAI × NS-MDS Twin-Derivative Study v0.1

**Status:** public preregistration / research preprint draft — **not a claim of solving the Millennium Prize problem**  
**Date:** 12 September 2026  
**Author:** Enrique Sánchez Lorenzo · CoreSyn / NS-MDS

## Abstract

OpenAI reported on 8 September 2026 an analytical and Lean-formalized finite-time singularity construction for three-dimensional incompressible Navier–Stokes with smooth forcing and finite energy. This preregistration defines a separate NS-MDS research program whose purpose is not to restate that proof but to test whether causal multi-scale memory observables can (i) anticipate the singular regime, (ii) classify perturbations that preserve, delay, advance, or destroy the singular mechanism, and (iii) generate new falsifiable propositions about stability around the reported construction.

The study freezes a baseline Navier–Stokes branch, a memory-augmented branch, a twin-derivative observable, a perturbation atlas, explicit null tests, and failure criteria before outcome inspection. Any future statement that NS-MDS improves, extends, or explains the OpenAI construction requires independent reproduction and preregistered quantitative success.

## 1. Baseline equation

We use the incompressible forced Navier–Stokes system

\[
\partial_t u + \mathbb P[(u\cdot\nabla)u] = \nu \Delta u + \mathbb P f,\qquad \nabla\cdot u=0,
\]

where \(\mathbb P\) denotes the Leray projection onto divergence-free vector fields.

The OpenAI result is treated only as an external target construction until the CoreSyn audit independently verifies the relevant proof, assumptions, formalization, and reproducibility artifacts.

## 2. Memory-augmented experimental branch

Define an exponential causal memory kernel

\[
K_\tau(r)=\tau^{-1}e^{-r/\tau},\qquad r\ge 0,
\]

and a causal velocity memory

\[
\bar u_\tau(t)=\int_0^t K_\tau(t-s)u(s)\,ds.
\]

Define the family

\[
D_{\tau,\alpha}u=\partial_tu+\alpha\frac{u-\bar u_\tau}{\tau}.
\]

Two frozen scales are used:

\[
D_1u=D_{\tau_1,\alpha}u,\qquad D_2u=D_{\tau_2,\beta}u,\qquad \tau_1<\tau_2.
\]

The first twin observable is

\[
S_{\rm twin}(t)=\|D_1u-D_2u\|_X,
\]

with the norm \(X\) to be fixed before production runs.

The corresponding experimental dynamics are

\[
D_1u+\mathbb P[(u\cdot\nabla)u]
=\nu\Delta u+\mathbb Pf+\gamma(D_1u-D_2u).
\]

The control condition \(\gamma=0\) must recover the frozen baseline branch to declared numerical tolerance.

## 3. Primary hypothesis

The primary hypothesis is **not** that NS-MDS solves Navier–Stokes. It is:

> For a reproduced singular target construction and preregistered perturbations, the twin-memory observable \(S_{\rm twin}\) contains predictive or classificatory information about approach to the singular regime that is not reducible to the chosen classical diagnostics and does not trigger comparably on matched smooth controls.

## 4. Perturbation atlas

For a reproduced target field \(u^*(x,t)\), define perturbations

\[
u_\varepsilon=u^*+\varepsilon v.
\]

For each perturbation family, measure at minimum:

- energy \(E(t)=\frac12\int|u|^2dx\),
- enstrophy \(\Omega(t)=\frac12\int|\omega|^2dx\),
- \(\|\omega(t)\|_\infty\),
- divergence residual,
- PDE residual,
- \(S_{\rm twin}(t)\),
- estimated event time under the frozen event criterion.

Each perturbation is classified as preserving, advancing, delaying, or destroying the target event only after convergence and null-test gates pass.

## 5. Success criteria

A positive NS-MDS result requires all of the following:

1. baseline reproduction succeeds independently;
2. the result survives grid/time-step refinement;
3. the signal survives frozen parameter choices and multiple seeds where randomness is used;
4. matched smooth controls do not show the same signal at a comparable rate;
5. the claimed lead time is positive under a frozen definition;
6. the effect is not explained by trivial rescaling, norm growth, or numerical instability;
7. code, environment, seeds, data, and hashes are published;
8. the result survives an adversarial clean-room rerun.

## 6. Failure criteria

The hypothesis is rejected or downgraded if any of the following holds:

- the baseline cannot be independently reproduced;
- the twin signal appears only after the classical event indicator;
- apparent anticipation disappears under refinement;
- false positives on smooth/null controls are not acceptably bounded;
- the result depends on post-hoc tuning of \(\tau_1,\tau_2,\alpha,\beta,\gamma\);
- divergence or PDE residuals invalidate the compared trajectories;
- the signal is equivalent to a simpler existing diagnostic under the tested regime.

## 7. Audit separation

The OpenAI audit and the NS-MDS extension remain separate evidence chains.

**Audit chain:** source claim → theorem statement → assumptions → analytical proof → Lean correspondence → clean build → adversarial review → disposition.

**Extension chain:** reproduced baseline → frozen NS-MDS operator → null tests → perturbation atlas → statistical/analytic comparison → independent rerun → bounded claim.

No failure or success in the NS-MDS extension can be used to retroactively validate or refute the OpenAI theorem unless it addresses the theorem itself.

## 8. Claim boundary

Version 0.1 makes no claim that NS-MDS solves the Navier–Stokes Millennium Prize problem, no claim that it is superior to the OpenAI proof, and no claim that a twin-memory diagnostic is novel or predictive until the preregistered tests are executed.

The strongest admissible future claim will be determined by evidence. Candidate outcomes range from `NO EFFECT`, through `BOUNDED EARLY-WARNING RESULT`, to a new mathematically stated stability proposition requiring independent proof.

## 9. External reference

OpenAI, “On the Navier–Stokes Millennium Prize Problem,” 8 September 2026. https://openai.com/index/navier-stokes-solution/
