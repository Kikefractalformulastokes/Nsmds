# Claims QA Rules

Standing rules for any CoreSyn/NS-MDS public-facing copy, derived from the brief and reinforced
by the existing `research/paper-01-dual-observable/PUBLICATION_GATE.md` (which already models
this correctly):

1. No claim of NASA validation, Airbus endorsement, third-party certification, or independent
   scientific validation unless a signed, evidenced review exists.
2. No use of a third-party company name as if it were a confirmed client/partner without written
   permission. **Current finding:** `index.html` badges the page "Airbus · Technical
   Demonstration" and titles it "NS-MDS | Airbus Demo" — this reads as a claim of an Airbus
   relationship. No evidence of an Airbus engagement exists in this repo. Flagged **BLOCK** in
   `12_QA_REPORTS/CLAIMS_QA_REPORT.md` pending Enrique confirmation of what relationship (if any)
   exists and whether "Airbus" may be used in public copy.
3. No third-party logos without permission.
4. Materials claims: "E2 internal" language only — never "E3" or "validated externally" until
   independent reproduction is complete (per brief, no Materials content exists in this repo to
   check yet).
5. Every provisional numerical result must carry a status label (draft / not peer reviewed / not
   independently reproduced) — the one paper in this repo already does this correctly
   (`PAPER_01...md`, `PUBLICATION_GATE.md`, `metadata.json` all label status consistently).
6. No CEOS "Company State" number changes without an audited evidence source.
7. No RiesgoDeObra pricing/design changes without a confirmed bug.
