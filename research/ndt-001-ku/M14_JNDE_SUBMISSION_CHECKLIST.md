# M14 — JNDE Submission Checklist

## Scientific gates
- [x] Public source dataset identified and DOI recorded.
- [x] Source files cryptographically pinned.
- [x] Frozen reference benchmark executed.
- [x] Generic continuous challenger executed.
- [x] ID/OOD stress tests reported.
- [x] Paired bootstrap uncertainty reported.
- [x] Tail errors reported.
- [x] Ablation completed.
- [x] Corrected deterministic internal blind re-evaluation completed.
- [x] Claim gate completed.
- [x] End-to-end CI evidence artifact generated.
- [x] Manuscript v1 written.
- [x] Primary journal selected: Journal of Nondestructive Evaluation.
- [x] Cover-letter draft prepared.
- [x] Reference 2 bibliographic metadata verified.

## Mandatory before portal submission
- [ ] Confirm full author list and exact order.
- [ ] Confirm corresponding author.
- [ ] Confirm publication affiliation(s).
- [ ] Add author email(s) and ORCID(s).
- [ ] Complete CRediT author-contribution statement.
- [ ] Complete funding statement.
- [ ] Decide subscription vs optional open access if/when requested.
- [ ] Produce clean submission manuscript with internal editorial note removed.
- [ ] Produce separate title-page metadata if requested by submission system.
- [ ] Archive or prepare review-safe code/evidence package according to journal policy.
- [ ] Final reference/link audit.
- [ ] Portal metadata entry and final author approval.

## Suggested portal abstract
Data-driven non-destructive evaluation can report strong average localization accuracy while concealing instability, distribution-shift sensitivity, and rare consequential errors. We present an evidence-first assurance study using a public ultrasonic guided-wave dataset for delamination localization in a composite beam. A frozen nearest-neighbour reference is compared with generic continuous localization, followed by paired uncertainty analysis, tail-risk reporting, ablation, distribution-shift stress testing, and deterministic internal blind re-evaluation. On the original noise-free holdout (n=40), mean absolute error decreased from 15.000 to 8.668 mm, an observed 42.21% reduction; however, the paired bootstrap 95% interval for mean improvement crossed zero and maximum error reached 108.315 mm. On an internal blind subset (n=16), the reduction contracted to 3.98% (15.000 vs 14.403 mm) while maximum error remained above 100 mm. Under the studied mixed-noise out-of-distribution condition, continuous localization underperformed the nearest-neighbour reference. Ablation attributes the original improvement to generic two-neighbour interpolation rather than a proprietary mechanism. The results demonstrate that provenance, frozen evaluation, uncertainty, tail-risk analysis, ablation, blind re-evaluation, distribution-shift testing, and explicit claim control materially change what can responsibly be concluded from an NDE benchmark.

## Suggested keywords
Non-destructive evaluation; ultrasonic guided waves; structural health monitoring; damage localization; model assurance; distribution shift; reproducibility; uncertainty; composite structures

## Current gate
**PRESS-SUBMIT HOLD: AUTHORSHIP / CORRESPONDING-AUTHOR / AFFILIATION METADATA ONLY, plus final portal-format checks.**
