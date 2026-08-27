# M14 — Journal Target and Submission Strategy

## Primary target
**Journal of Nondestructive Evaluation (Springer Nature)**

## Why this venue
- Direct NDE scope and recent publication history covering guided-wave methods, ultrasonic data and model/data-driven NDE.
- Better fit for an evidence-first assurance/reproducibility study than venues demanding new experimental hardware or mandatory experimental corroboration of simulations.
- Hybrid publishing model: subscription publication is available without mandatory APC; optional open access can be chosen after acceptance.
- The paper's central contribution is NDE evaluation methodology: provenance, frozen benchmarking, tail-risk, OOD stress, blind re-evaluation, attribution control and claim discipline.

## Deliberately not first target
**NDT & E International** is not the first submission target because its current scope states an expectation that modelling/simulation be accompanied by experimental evidence. The present paper intentionally evaluates a public finite-element guided-wave dataset and does not contain a new experimental campaign. This creates unnecessary desk-reject risk despite strong topical relevance.

## Approved title for JNDE submission draft
**Evidence-First Assurance of Ultrasonic Guided-Wave Damage Localization: Blind Re-evaluation, Tail Risk, Distribution Shift, and Claim Control**

## Article positioning
Original research / methodology-oriented NDE evaluation study.

The manuscript must NOT be positioned as:
- canonical NS-MDS performance validation;
- aircraft operational validation;
- airline approval;
- regulatory/certification validation;
- external independent validation;
- conventional 95%-confidence superiority.

## Core results to foreground
1. Primary alternating-position holdout: NN reference 15.000 mm MAE vs generic two-neighbour inverse-square interpolation 8.668 mm MAE (42.21% observed reduction).
2. Paired 20,000-bootstrap 95% interval for mean improvement crosses zero: [-3.351, 13.978] mm; no conventional 95% superiority claim.
3. Tail risk: maximum error 108.315 mm on the primary holdout.
4. Corrected deterministic internal blind subset: 15.000 vs 14.403 mm MAE (3.98% observed reduction), with max error 102.083 mm.
5. Mixed-noise OOD: continuous interpolation degrades relative to nearest neighbour (19.575 vs 6.667 mm MAE).
6. Ablation attributes the observed lift to generic continuous interpolation, not canonical NS-MDS.

## Editorial argument
The novelty is not a new localization architecture. The novelty is a reproducible assurance chain showing how an apparently strong NDE benchmark result changes under statistical uncertainty, tail-risk analysis, distribution shift, ablation and blind re-evaluation. The paper demonstrates why average benchmark improvement alone is insufficient evidence for operational NDE claims.

## Reference verification
Reference 2 verified against publisher metadata:
Lu, H., Cantero-Chinchilla, S., Yang, X., Gryllias, K., & Chronopoulos, D. (2024). Deep learning uncertainty quantification for ultrasonic damage identification in composite structures. Composite Structures, 338, 118087. https://doi.org/10.1016/j.compstruct.2024.118087

## Remaining administrative placeholders
- Final author list and order.
- Corresponding author and email.
- Author affiliations exactly as they should appear in publication.
- ORCID identifiers.
- CRediT contribution statement.
- Funding declaration.

## M14 state
**VENUE SELECTED: JNDE**
**SCIENTIFIC PACKAGE: READY FOR VENUE ADAPTATION**
**PRESS-SUBMIT: HOLD ONLY FOR AUTHORSHIP/IDENTITY METADATA AND FINAL PORTAL ENTRY**
