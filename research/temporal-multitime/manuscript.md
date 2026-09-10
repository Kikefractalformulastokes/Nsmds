# Adversarial Reproducibility Benchmark for Multi-Time Dynamics

**Stability, modal energy, interaction closure, and numerical boundary sensitivity in a minimal (3,3) scalar model**

**Enrique Sánchez Lorenzo** · CoreSyn, Madrid, Spain  
Corresponding author: enrique@coresyn.io  
ORCID: 0009-0000-5362-6507  
Public preprint release: 10 September 2026

## Abstract

Theories with multiple temporal dimensions face strong requirements concerning well-posed evolution, energy positivity, interaction preservation, and, for fields with spin, removal of ghost degrees of freedom by adequate constraint or gauge structure. We present a reproducible adversarial benchmark for a deliberately narrower question using a minimal scalar model with signature (3,3), with one temporal coordinate selected for evolution. Unrestricted modal evolution contains an exponentially growing sector, while a non-trivial spectral region has oscillatory free modes and non-negative modal Hamiltonian. The broad safe region is not closed under generic mode addition: an analytic counterexample family and eight random seeds produce safe inputs whose sums can be unstable. A narrower same-sign one-dimensional massless subcone is pairwise-addition closed. Near the stability surface, seven of 96 probes disagree between binary floating-point and high-precision sign classification. Ten primary computational outputs were reproduced byte-for-byte in an independent clean-room rerun. The contribution is a frozen adversarial scalar benchmark, not a ghost-free or unitary multi-time theory. The results isolate mathematical, numerical, and scope obligations for stronger constructions.

**Keywords:** multiple time dimensions; ultrahyperbolic dynamics; reproducibility; stability; interaction closure; numerical precision

## 1. Introduction

Multiple-time frameworks make unusually strong mathematical commitments. Once more than one time-like direction is admitted, statements about causality, stability, energy positivity, dimensional reduction, and quantum consistency cannot be inferred from metric signature alone. The recent Three-Dimensional Time proposal makes explicit claims in precisely this territory and motivates the present bounded stress-test setting [1]. A useful evaluation therefore requires claims to be converted into bounded tests that can fail, be repaired, and be attacked again.

This study develops such a benchmark around a minimal scalar realization with signature (3,3). The goal is not to validate a particular fundamental theory. Instead, we ask four narrower questions: (i) when does modal evolution remain oscillatory; (ii) when is the modal Hamiltonian non-negative; (iii) is a linearly safe spectral region preserved under mode composition representative of nonlinear interactions; and (iv) how reliable is numerical classification close to the stability boundary? The benchmark is intentionally small enough for analytic checks, deterministic sweeps, adversarial counterexamples, and clean-room reproduction.

### 1.1 Related work and novelty boundary

Ultrahyperbolic evolution is not generically equivalent to an ordinary Cauchy problem. Craig and Weinstein showed that, although unrestricted mixed-signature evolution is ill-posed in general, explicit nonlocal constraints on codimension-one initial data can yield global unique solutions with continuous dependence in appropriate Sobolev phase spaces [2]. Their Fourier analysis separates oscillatory and exponentially growing sectors using the same norm competition that appears in the present minimal benchmark. This prior result is essential: the existence of a restricted stable sector is not, by itself, a new theorem of this work.

Multi-time consistency can also be pursued through gauge structure rather than a simple spectral cutoff. In Two-Time Physics, Bars formulated field-theoretic constructions in d+2 dimensions whose kinematic constraints arise from underlying gauge symmetries and permit reductions to one-time descriptions [3]. Subsequent supersymmetric 2T constructions explicitly argue that additional gauge symmetries and kinematic constraints remove ghost degrees of freedom and yield unitary theories in those models [4]. This distinction is crucial for the present manuscript: a scalar modal restriction does not test whether time-like components of spin-1, spin-2, or higher-spin fields are removed from the physical spectrum. Consequently, non-negative modal energy in the scalar benchmark must not be promoted into a statement of ghost freedom or unitarity for a complete multi-time field theory. The 2T constructions are not equivalent to the scalar (3,3) benchmark studied here, but they demonstrate that constraints, gauge structure, and reduction maps are central rather than optional ingredients in serious extra-time theories.

Accordingly, the novelty claim of this paper is deliberately narrow. We do not claim to discover that restrictions can regularize multi-time dynamics, nor do we establish a new interacting multi-time field theory. We contribute a reproducibility-first adversarial workflow: freeze a minimal model, derive analytic pass/fail regions, test repairs, attack interaction closure, identify non-universal restricted subcones, audit finite-precision boundary behavior, and reproduce the primary outputs byte-for-byte before manuscript promotion.

## 2. Mathematical setup

Let t1 denote the chosen evolution coordinate, t2 and t3 the additional temporal coordinates, and x ∈ R^3 the spatial coordinates. For the benchmark scalar field, the principal operator is

∂²_t1 φ + ∂²_t2 φ + ∂²_t3 φ − ∇²φ + m²φ = 0.

After Fourier decomposition in x,t2,t3, a mode with spatial wavevector k and extra-temporal frequency vector ω_perp=(ω2,ω3) obeys

d²φ̂/dt1² + q φ̂ = 0,   q = |k|² + m² − |ω_perp|².

Thus q>0 is oscillatory, q=0 is the modal boundary, and q<0 produces exponential behavior in t1. For the free benchmark, the same q appears in the modal Hamiltonian,

H_k = 1/2 (|π_k|² + q|φ_k|²),

so q≥0 is sufficient for non-negative modal energy in this bounded scalar realization. This is only a modal stability/energy statement. It is neither a count of physical degrees of freedom nor a proof that negative-norm states are absent in a theory containing gauge, gravitational, or other spinning fields; therefore it does not establish ghost freedom or unitarity.

## 3. Adversarial benchmark design

The workflow follows a claim → reproduce → perturb → falsify → disposition sequence. M4.11 performs a deterministic phase-space sweep. M4.12 varies mass and orientation and probes the analytic boundary. M4.13 applies rotational and scaling null tests, degenerate controls, high-precision boundary checks, restricted-subcone closure tests, multi-seed interaction attacks, and an analytic counterexample family. M5 then repeats the primary computations in an independent clean-room directory and compares outputs byte-for-byte.

The benchmark uses explicit PASS/FAIL/BOUNDARY dispositions. Near q=0, binary floating-point sign is not treated as authoritative: a declared tolerance or high-precision arithmetic is required. Random search is used only as adversarial evidence; general non-closure is established independently by an analytic counterexample family.

## 4. Results

The benchmark yields a mixed result rather than a universal verdict. Unrestricted free-scalar evolution is not uniformly oscillatory because q<0 modes exist. Nevertheless, q>0 defines a non-trivial free sector with oscillatory evolution and non-negative modal Hamiltonian. For |k|=1, the boundary is r_c=√(1+m²), where r=|ω_perp|/|k|, so nonzero mass shifts rather than removes the boundary.

The sampled classification is rotationally invariant: 25,000 of 25,000 rotation tests passed. The expected scaling law passed 20,000 of 20,000 tests, and all six degenerate controls returned their prescribed classifications. The broad safe cone is not closed under generic mode addition. Across eight independent seeds, every run found counterexamples; among qualifying safe pairs, 31.8–32.8% of sums were unsafe in those sampled distributions. An analytic family supplies a non-random proof of general non-closure. Importantly, a same-sign one-dimensional massless subcone passed 100,000 of 100,000 pairwise-addition tests, showing that interaction failure is not universal for all restricted subsets.

Finally, numerical classification becomes fragile extremely close to q=0. Seven of 96 near-boundary probes produced different signs under standard binary floating-point and high-precision decimal arithmetic. This motivates an explicit tolerance/high-precision policy for any computational study of the boundary.

### Frozen benchmark dispositions

| Claim/test | Evidence | Disposition |
|---|---|---|
| Uniformly oscillatory unrestricted 3+3 scalar evolution | Existence of q<0 modes | FAIL |
| Non-trivial linearly safe sector | q>0; M4.11–M4.12 | PASS_BOUNDED |
| Orientation dependence | 25,000 rotation tests | REJECTED |
| Broad-cone interaction closure | Analytic family + 8/8 seeds | FAIL |
| All restricted subsets fail closure | 100,000 same-sign 1D tests | REJECTED |
| Float sign reliable arbitrarily near q=0 | 7/96 disagreements | FAIL |
| Validation of source theory / unitarity / nonlinear well-posedness | Outside benchmark scope | NOT CLAIMED |

## 5. Interaction closure and repair attempts

The linear safe region is useful only if a physical dynamics can preserve it. Generic local nonlinearities mix Fourier modes through convolution. If p1=(k1,ω1) and p2=(k2,ω2) are individually safe, p1+p2 need not be safe because spatial components can cancel while extra-temporal components reinforce. The frozen benchmark includes an analytic counterexample with q1=0.84 and q2=0.65 but q_combined=-0.63. This establishes non-closure of the broad region without relying on random search.

The null result is equally important: a narrower same-sign one-dimensional massless subcone is pairwise-addition closed. Consequently, the benchmark does not establish an impossibility theorem. It instead shifts the burden to constructing a dynamically preserved physical state space, together with the constraints or symmetries that select it.

## 6. Numerical precision and reproducibility

Boundary classification is a scientific part of the benchmark rather than an implementation detail. The high-precision audit identified seven disagreements among 96 deliberately near-boundary probes. Results exactly or numerically close to q=0 must therefore be reported with a tolerance policy and, where needed, recomputed at higher precision.

The frozen M5 release records code, data, figures, environment information, governance constraints, and SHA-256 manifests. Ten primary outputs were regenerated in an independent clean-room directory and were byte-identical to their originals. The reproduction environment recorded Python 3.13.5 on Linux x86_64. This establishes computational reproducibility of the bounded benchmark; it does not establish physical validity of a multi-time theory.

## 7. Discussion

The central result is a separation of claims that are often conflated. Multiple time-like directions do not, by metric signature alone, imply either universal instability or automatic consistency. In the minimal benchmark, unrestricted evolution admits exponentially growing modes, while a non-trivial restricted sector avoids that particular instability and has non-negative modal energy. The broad sector then fails generic interaction closure, but a narrower restricted subcone survives pairwise addition.

This pattern is consistent with earlier mathematical and field-theoretic work in which admissible data constraints or gauge constraints are essential to recover controlled evolution [2–4]. The mathematically relevant question is therefore not simply how many time-like coordinates appear in a metric. The decisive issue is whether a theory supplies an explicit physical state space, constraint or gauge mechanism, evolution law, and preservation theorem strong enough to keep dynamics inside an admissible sector. For theories containing spin-1, spin-2, or higher-spin fields, this additionally requires demonstrating that the enlarged component structure does not leave negative-norm physical degrees of freedom. A scalar spectral cutoff cannot substitute for that demonstration. Those obligations become more stringent, not less, once interactions and quantization are introduced.

## 8. Limitations

The study uses a deliberately minimal scalar benchmark. It does not include Yang-Mills fields, gravity, or higher-spin fields, and therefore does not test the component-level ghost problem that arises in spinning sectors when additional time-like directions are introduced. It does not provide a complete constrained Hamiltonian analysis, a gauge-constraint construction, a count of physical versus gauge degrees of freedom, a proof of nonlinear well-posedness, a construction of a positive-definite physical Hilbert space, a proof of unitarity, or a dimensional-reduction theorem from (3,3) to (3,1). Mode addition is a diagnostic proxy for spectral mixing under interactions, not a full nonlinear field-theory solution. The sampled unsafe-sum percentages depend on the sampling distribution and are not universal constants.

Accordingly, survival of a restricted scalar sector must not be represented as evidence that a complete multi-time theory is ghost-free, unitary, or physically viable. The results must not be represented as validation or refutation of every multi-time theory, nor as validation of the source Three-Dimensional Time proposal. They are bounded stress tests that identify conditions a stronger theory would need to satisfy, including an explicit mechanism for selecting and preserving the physical state space and, where spinning fields are present, removing unphysical negative-norm degrees of freedom.

## 9. Reproducibility statement

The computational evidence is frozen in `TEMPORAL_M5_FROZEN_BENCHMARK_v1.0`, SHA-256 `8f6fda4ae562b6526e40bf17e04ccb9fde7eef41ec60d2714e11e1b6218e57fa`. The release contains the M4.11–M4.14 code and outputs, publication figures, environment records, governance charter, clean-room comparison, and SHA-256 manifest. Ten primary outputs were regenerated in an independent clean-room directory and were byte-identical to their originals.

A persistent DOI has not yet been assigned. This public GitHub release provides a timestamped public preprint location while a DOI-bearing archival deposit is pursued.

## 10. Conclusion

A minimal (3,3) scalar benchmark exhibits both failure and survival regions. Unrestricted evolution contains exponentially growing modes, whereas a non-trivial spectrally restricted free sector is oscillatory and has non-negative modal energy. The broad safe sector is not closed under generic mode addition, although narrower restricted subsets can be. Near the stability boundary, numerical precision materially affects classification. None of these scalar results establishes ghost freedom or unitarity for a complete theory with spinning fields; those questions require explicit constraint or gauge structure and a demonstrably preserved physical state space. Together, the results argue for evidence-gated evaluation of multi-time dynamics: admissible state spaces, interaction preservation, treatment of spinning-sector degrees of freedom, high-precision boundary policies, and independent reproducibility are prerequisites for stronger physical claims.

## Data and code availability

Code, datasets, figures, manifests, and clean-room comparison are contained in the frozen `TEMPORAL_M5_FROZEN_BENCHMARK_v1.0` package (SHA-256: `8f6fda4ae562b6526e40bf17e04ccb9fde7eef41ec60d2714e11e1b6218e57fa`). The frozen evidence package is being prepared for persistent public archival deposition.

## Declarations

**Generative AI disclosure.** During the preparation of this work, the author used OpenAI ChatGPT to assist with manuscript organization, language refinement, editorial-format preparation, and consistency checks. The author reviewed and edited the content as needed and takes full responsibility for the content of the publication.

**Consent to participate / publish:** Not applicable.  
**Ethics approval:** Not applicable. No human participants, animals, or patient data were involved.  
**Author contributions:** Enrique Sánchez Lorenzo conceived the study, defined the research questions, supervised the evidence-governance workflow, reviewed the computational evidence, and is responsible for the submitted manuscript.  
**Competing interests:** The author declares no competing interests relevant to this manuscript.  
**Funding:** No external funding was received for this study.

## References

1. G. Kletetschka, “Three-Dimensional Time: A Mathematical Framework for Fundamental Physics,” *Reports in Advances of Physical Sciences* 9 (2025), 2550004. DOI: 10.1142/S2424942425500045.
2. W. Craig and S. Weinstein, “On determinism and well-posedness in multiple time dimensions,” *Proceedings of the Royal Society A* 465 (2009), 3023–3046. DOI: 10.1098/rspa.2009.0097. arXiv:0812.0210.
3. I. Bars, “Two-Time Physics in Field Theory,” *Physical Review D* 62 (2000), 046007. DOI: 10.1103/PhysRevD.62.046007. arXiv:hep-th/0003100.
4. I. Bars and Y.-C. Kuo, “N=2,4 Supersymmetric Gauge Field Theory in 2T-physics,” *Physical Review D* 79 (2009), 025001. DOI: 10.1103/PhysRevD.79.025001. arXiv:0808.0537.
