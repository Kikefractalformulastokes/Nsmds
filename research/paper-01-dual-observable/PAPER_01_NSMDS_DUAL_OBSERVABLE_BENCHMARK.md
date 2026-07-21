---
title: "Avoiding single-observable calibration failure in NACA 0012"
subtitle: "A dual-observable benchmark protocol for a memory-regularised flow-model extension"
author:
  - "Enrique Sanchez — CoreSyn Lab, independent research programme"
date: "21 July 2026"
lang: en
geometry: margin=25mm
fontsize: 11pt
colorlinks: true
linkcolor: blue
urlcolor: blue
header-includes:
  - |
    \usepackage{fancyhdr}
    \pagestyle{fancy}
    \fancyhead[L]{CoreSyn Lab — Paper 01}
    \fancyhead[R]{Public draft v0.1}
    \fancyfoot[C]{\thepage}
---

> **PUBLIC DRAFT v0.1 — NOT PEER REVIEWED.** Numerical findings described as historical internal observations have not been independently reproduced from the original execution package. This document does not claim NASA validation, NASA or Airbus endorsement, production CFD readiness, certification, or independent scientific validation.

## Abstract

Calibration against a single aerodynamic observable can produce apparently strong agreement while degrading physically connected quantities. This manuscript defines a dual-observable NACA 0012 benchmark for an experimental, memory-regularised flow-model extension referred to as NS-MDS. The protocol uses public pressure-distribution observations associated with Gregory and O'Reilly and public lift-polar observations from Ladson. Recovered project records describe a pressure-only calibration that improved the fitted pressure observable while substantially degrading the integrated lift polar. A spatially constrained, “lift-preserving” configuration was then proposed to act only near the localised baseline failure while preserving the remainder of the baseline solution. The contribution of this public draft is a falsifiable evaluation design: one baseline, frozen conditions, two connected observables, an explicit degradation gate, provenance controls, execution hashes and a clean-room reproduction requirement. Numerical improvement claims remain provisional until the complete executable package, environment and raw outputs are recovered or reconstructed and reproduced.

**Keywords:** NACA 0012; aerodynamic validation; pressure coefficient; lift polar; multi-objective calibration; model assurance; reproducibility; NS-MDS.

## 1. Introduction

Model calibration is often reported against the quantity used to tune the model. That practice can hide a structural failure when a second physical observable is coupled to the first. For an airfoil, chordwise pressure distribution and integrated lift are not independent marketing metrics: the latter is derived from the pressure field. A candidate method that improves local pressure shape while degrading lift has not achieved a general aerodynamic improvement.

The recovered NS-MDS project history contains exactly this failure pattern. An internal pressure-only calibration was reported to improve agreement with a selected NACA 0012 pressure reference while producing a much worse lift polar than the unmodified baseline. Subsequent multi-objective tuning did not fully remove the conflict. The project then introduced a structural constraint: confine the correction to a small chordwise region associated with the baseline's localised failure, leaving the remainder of the baseline unchanged.

This manuscript does not present that historical result as independently established. Instead, it converts the episode into a preregisterable benchmark protocol designed to answer a narrower question:

> Can a constrained candidate configuration reduce pressure-distribution error without degrading the lift polar relative to the same frozen baseline?

## 2. Evidence boundary

### 2.1 Established for this draft

- Two public NACA 0012 reference reports exist and are identifiable through stable institutional repositories.
- Recovered CoreSyn project records document the pressure-only failure, the multi-objective attempt and the later spatial constraint.
- A public, non-proprietary protocol can be specified without exposing protected equations, calibrated values or implementation details.

### 2.2 Not established for this draft

- The original solver scripts, complete environment, meshes/configurations and raw numerical outputs are not present in the current publication package.
- Historical numerical values have not been rerun independently.
- No third party has reproduced the full aerodynamic benchmark.
- Use of NASA-hosted data does not mean NASA validated, endorsed or reviewed NS-MDS.

## 3. Reference evidence

The benchmark uses two public evidence families:

1. **Pressure and low-speed aerodynamic characteristics.** Gregory and O'Reilly reported NACA 0012 measurements at low speed, including the effects of upper-surface roughness. The report is preserved by Cranfield's Aeronautical Research Council archive.
2. **Lift-polar and operating-condition evidence.** Ladson's NASA TM-4074 provides a comprehensive low-speed NACA 0012 database covering independent variation of Mach and Reynolds numbers and transition fixing.

The final benchmark must document the exact series, angles, conditions and any digitisation or preprocessing used. Data from different facilities or operating conditions must not be silently treated as a single ground-truth experiment.

## 4. Failure mechanism under test

### 4.1 Single-observable calibration

The historical configuration was tuned against pressure-distribution shape. Recovered records report that the local pressure fit improved while integrated lift degraded. This is a failure even if the fitted observable looks visually superior.

### 4.2 Why scalar reweighting may be insufficient

Adding a lift-error term to a weighted objective can move a solution along a trade-off surface without removing the structural cause. If a correction acts over regions where the baseline is already adequate, parameter tuning alone may be unable to preserve the coupled integral.

### 4.3 Spatially constrained hypothesis

The candidate hypothesis is architectural rather than purely parametric: apply the correction only inside a preregistered region linked to the localised baseline error, and recover the frozen baseline outside that region. The public manuscript identifies the constraint class but does not disclose protected parameter values.

## 5. Preregistered benchmark design

### 5.1 Configurations

Three configurations must be evaluated:

- **B0 — Frozen baseline:** no NS-MDS contribution.
- **C1 — Pressure-only historical class:** included to reproduce the known failure mode.
- **C2 — Constrained candidate:** spatially bounded correction with configuration referenced by an immutable parameter-bundle hash.

### 5.2 Freeze before evaluation

The following items must be fixed before final candidate evaluation:

- geometry and operating conditions;
- source data and preprocessing;
- solver or reduced-order implementation version;
- baseline and candidate configuration hashes;
- mesh or discretisation family;
- convergence criteria and compute budget;
- metric code and acceptance thresholds;
- train/calibration and held-out evaluation partitions.

### 5.3 Primary observables

1. Chordwise pressure-coefficient error by angle and region.
2. Lift-polar error across the fixed angle sweep.

The lift-polar gate is primary, not a secondary descriptive check.

### 5.4 Acceptance rule

C2 passes only if all of the following hold on the frozen evaluation set:

1. pressure-distribution error improves over B0 by the preregistered minimum;
2. lift-polar error does not exceed B0 and meets the preregistered improvement or non-inferiority threshold;
3. convergence, stability and conservation checks pass;
4. the conclusion survives the predefined sensitivity and ablation tests;
5. every reported value can be regenerated from retained outputs.

An improvement in pressure accompanied by unacceptable lift degradation is an explicit failure, regardless of aggregate objective value.

## 6. Metrics and controls

### 6.1 Accuracy

- pressure-coefficient RMSE by angle and chord region;
- lift-polar RMSE across the fixed sweep;
- signed bias and maximum absolute deviation;
- descriptive coefficient of determination, reported only as secondary context.

### 6.2 Numerical controls

- residual histories and convergence decision;
- grid/discretisation sensitivity or an explicitly stated limitation when unavailable;
- divergence/conservation diagnostics where the implementation supports them;
- runtime and compute budget;
- failed and unstable runs, retained rather than discarded.

### 6.3 Robustness

- ablation of the spatial constraint;
- sensitivity to the constraint boundary;
- held-out angle or condition tests;
- comparison with at least one stronger reasonable baseline before any industrial-performance claim.

## 7. Reproducibility contract

Every run must emit:

- code and protocol version;
- dataset identity, provenance and SHA-256;
- environment and dependency metadata;
- mesh/discretisation identifier;
- configuration or parameter-bundle hash;
- start/end time and compute metadata;
- convergence and error logs;
- raw outputs and generated metrics;
- canonical report hash.

The package must include a one-command runner and must work from a clean environment without undocumented manual intervention.

## 8. Historical internal observations

Recovered project records contain numerical values for the pressure-only failure, multi-objective attempts and constrained candidate. They are intentionally excluded from the headline findings of this public draft because the original execution package and raw outputs have not yet been independently reproduced. When the clean-room gate is complete, this section should be replaced by automatically generated tables that trace each value to retained output hashes.

This treatment is deliberate: a transparent missing result is stronger evidence than a precise number whose provenance cannot currently be rerun.

## 9. Independent replication plan

An external reviewer should receive:

- the frozen public datasets and provenance record;
- baseline implementation and expected baseline outputs;
- immutable fixtures and metric code;
- the protocol and acceptance thresholds;
- a blinded candidate bundle or controlled runner;
- a blank result form and SHA-256 manifest.

The reviewer first reproduces B0, then executes C1 and C2 without changing the protocol. The returned record must include environment metadata, deviations, logs, outputs, hashes and conflict/compensation disclosure. A review of the document alone does not constitute reproduction.

## 10. Limitations

- This is a protocol and failure-analysis draft, not a completed CFD validation paper.
- Cross-report operating-condition differences can confound direct comparison and must be reconciled explicitly.
- A reduced-order or illustrative model cannot establish performance in a production CFD solver.
- Agreement on NACA 0012 does not establish generalisation to other geometries, regimes or industrial scenarios.
- Independent replication has not yet occurred.
- Proprietary disclosure boundaries limit the implementation detail available in this public version.

## 11. Conclusion

The central lesson is methodological: calibration success on a single observable can conceal failure of a coupled physical quantity. A defensible NACA 0012 benchmark for the candidate NS-MDS extension must treat pressure distribution and lift polar as simultaneous gates under one frozen baseline and one reproducibility contract. The next scientific result is not another tuned number; it is a clean-room execution package that can regenerate the complete evidence chain.

## Data and code availability

The public reference reports are linked below. The NS-MDS execution package is not included in this draft because the complete original environment and outputs are still being recovered or reconstructed. Release status will be updated only after the publication gate is met.

## Conflict and funding statement

The author is the founder of the CoreSyn research programme and has a direct intellectual-property and commercial interest in NS-MDS. No independent funding or institutional endorsement is claimed in this draft.

## References

1. Gregory, N., and O'Reilly, C. L. (1970). *Low-speed aerodynamic characteristics of NACA 0012 aerofoil section, including the effects of upper-surface roughness simulating hoar frost*. Aeronautical Research Council R&M 3726. <https://reports.aerade.cranfield.ac.uk/handle/1826.2/3003>
2. Ladson, C. L. (1988). *Effects of independent variation of Mach and Reynolds numbers on the low-speed aerodynamic characteristics of the NACA 0012 airfoil section*. NASA Technical Memorandum 4074. <https://ntrs.nasa.gov/citations/19880019495>
3. McCroskey, W. J. (1987). *A critical assessment of wind tunnel results for the NACA 0012 airfoil*. NASA Technical Memorandum 100019. <https://ntrs.nasa.gov/citations/19880002254>

