# M12 — Internal Review Gate: NDT-001 Evidence-First Assurance

**Manuscript:** M11_MANUSCRIPT_V1.md  
**Gate purpose:** determine whether the evidence supports external manuscript preparation without claim inflation.

## Review checklist

| Gate | Finding | Status |
|---|---|---|
| Source provenance | Public KU Leuven RDR dataset identified by DOI 10.48804/JAIG58; source CSV hashes frozen in workflow | PASS |
| Physical units | Corrected mapping `position_mm = 300 + 400 * normalized_position` used in M8 | PASS |
| Reproducibility | Corrected workflow run 33081098037 completed successfully at commit cefb66e1... | PASS |
| Primary result | 15.000 -> 8.668 mm observed MAE on n=40 original holdout | PASS as observed result |
| Statistical wording | Paired bootstrap CI95 [-3.351, 13.978] mm crosses zero | PASS only with explicit non-superiority caveat |
| Tail-risk reporting | max 108.315 mm and >30 mm failures disclosed | PASS |
| Attribution | M7 identifies generic two-neighbour continuous interpolation as mechanism; no canonical NS-MDS attribution | PASS |
| OOD reporting | OOD degradation disclosed; no robustness claim | PASS |
| Blind gate | Corrected M8: 15.000 -> 14.403 mm, 3.98% observed reduction, n=16, max 102.083 mm | PASS as internal blind re-split |
| External validation | No external/third-party/aircraft validation exists in this chain | HOLD for any such claim |
| Certification | No certification/regulatory/airline approval evidence | HOLD for any such claim |
| Authorship | Final author list/contributions not yet assigned | REQUIRED BEFORE SUBMISSION |
| Venue formatting | Journal/venue not yet selected | REQUIRED BEFORE SUBMISSION |
| Bibliography | Dataset DOI grounded; secondary literature metadata must receive final publisher/Crossref check | REQUIRED BEFORE SUBMISSION |
| Public archival code | GitHub evidence exists; persistent DOI/anonymized archive depends on venue | RECOMMENDED/venue-dependent |

## Reviewer verdict

**CONDITIONAL PASS — READY FOR EXTERNAL MANUSCRIPT PREPARATION, NOT YET READY TO PRESS “SUBMIT”.**

The scientific narrative is defensible if and only if the manuscript preserves the negative/limiting evidence as first-class results. The paper should be positioned as an assurance/reproducibility case study, not as proof of a proprietary localization method.

## Mandatory pre-submission actions
1. Assign authors and CRediT contributions; identify corresponding author.
2. Select a target journal/conference and apply its manuscript template and word/reference limits.
3. Verify every bibliographic field against DOI/publisher records and expand the literature review appropriately for the target venue.
4. Decide whether the repository can be public; if not, create an anonymized reproducibility archive consistent with double-blind rules.
5. Preserve the corrected M8 values everywhere; retire the earlier 0–1000 mm M8 numbers from presentations and manuscripts.
6. Do not add NS-MDS, aircraft, airline, certification, external-validation, or 95%-confidence superiority claims unless new evidence is generated.

## Frozen numerical claims approved for M13
- Original holdout n=40: reference MAE 15.000 mm; generic knn2 inverse-square MAE 8.667762 mm; observed reduction 42.2149%.
- Paired bootstrap improvement CI95: -3.3513 to 13.9778 mm; bootstrap P(improvement>0)=0.92315.
- Original holdout challenger: median 0.2468 mm; P90 4.6078 mm; max 108.3149 mm; 36 better / 4 worse.
- OOD mixed-noise: reference 6.6667 mm; generic continuous 19.5754 mm; max 103.5403 mm.
- Corrected internal blind n=16: reference 15.000 mm; challenger 14.403265 mm; observed reduction 3.9782%; median 0.4063 mm; P90 49.3830 mm; max 102.0825 mm; 12 better / 4 worse.

**M12 state: CONDITIONAL PASS.**