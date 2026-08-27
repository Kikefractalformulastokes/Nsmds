# NDT-001 — M9 CLAIM GATE

Status: FROZEN after M8 internal blind validation
Date: 2026-08-27

## Evidence-supported statements

1. On the frozen 40-case noise-free holdout, the generic two-neighbour inverse-square continuous localizer achieved 8.668 mm MAE versus 15.000 mm for the frozen nearest-neighbour baseline (observed MAE reduction 42.21%).
2. In M6, the challenger beat the 15 mm per-case reference in 36/40 cases and every leave-one-out mean remained below 15 mm.
3. The paired bootstrap CI95% for mean improvement crossed zero (-3.35 to +13.98 mm); therefore statistical superiority at the conventional 95% confidence level is NOT claimed.
4. In the pre-specified M8 internal blind re-split, the frozen continuous challenger achieved 27.93 mm MAE versus 37.50 mm nearest-neighbour MAE (observed reduction 25.51%; 13/16 cases better).
5. M7 attribution shows that the observed improvement is explained by generic continuous two-neighbour interpolation/inverse-distance weighting. It is NOT evidence of canonical NS-MDS causality.
6. OOD robustness is unresolved. The KNN2 continuous challenger degraded on the frozen 10/5 dB OOD condition; adaptive routing reduced some damage but did not solve it.
7. CoreSyn can legitimately present this work as an evidence/model-assurance exercise: benchmark reproduction, challenger construction, blind evaluation, statistical validation, ablation, failure-mode analysis and explicit claim control.

## Approved commercial wording

- "CoreSyn independently stress-tests NDT/AI localization pipelines against frozen baselines, blind splits, perturbations and failure modes."
- "In our public guided-wave benchmark case study, a frozen continuous-localization challenger reduced observed MAE versus the discrete nearest-neighbour reference on both the original holdout and an internal blind re-split."
- "The study also exposed material tail-risk and OOD limitations, demonstrating why headline average accuracy is insufficient for deployment assurance."
- "We deliver reproducible evidence packs designed to help engineering teams understand where a model works, where it fails and what can defensibly be claimed."

## Prohibited wording

Do NOT state or imply:

- "NS-MDS reduced NDT error by 42%."
- "NS-MDS is validated for aircraft NDT."
- "42% statistically proven improvement."
- "Airline-ready", "certified", "approved by Ryanair", or equivalent.
- "Independent external validation" for M8; M8 is an internal blind re-split.
- Transfer of KU/public-benchmark performance to a specific aircraft, inspection procedure, defect class or operator.
- That the current uncertainty diagnostic is a validated safety gate.

## Evidence required to raise the claim

1. Third-party or separately sourced NDT dataset with frozen protocol.
2. Pre-registered evaluation and untouched final test set.
3. Relevant aircraft/material/defect geometry and realistic acquisition variability.
4. Repeated trials across operators, probes, SNRs and environmental conditions.
5. Appropriate statistical power and confidence intervals that support the intended claim.
6. If NS-MDS attribution is desired: canonical NS-MDS implementation must be tested head-to-head against matched generic baselines under the same frozen protocol.
7. For operational/certification claims: domain-owner review and applicable aerospace/NDT qualification and regulatory processes.

## Claim-gate verdict

PASS for a CoreSyn NDT Model-Assurance case study and commercial pilot proposition.

HOLD for canonical NS-MDS performance attribution, operational aircraft performance claims, certification claims, and external-validation claims.
