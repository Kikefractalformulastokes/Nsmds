# CoreSyn / ModelAssuranceLab — Copy Alignment Task

**Trigger:** Chrome agent's external QA (as reported by Enrique) found the CoreSyn/
ModelAssuranceLab site(s) technically live and functional (PASS), but titles/copy read as
outdated relative to current positioning.

**Status:** READY_FOR_CODE — not yet actioned. CODE has no repo access to the CoreSyn web
property in this session, so this is logged as a task for whenever that access exists.

## Scope

- Copy-only alignment: titles, hero text, and positioning language brought in line with current
  CoreSyn/ModelAssuranceLab positioning.
- **No redesign.** No new features. No layout changes. No pricing changes.
- Must pass `CLAIMS_QA_RULES.md` / `16_SECURITY_GROWTH/10_GROWTH_CLAIMS_QA/GROWTH_CLAIMS_QA.md`
  before publishing — outdated copy is not an excuse to introduce a new unverified claim.

## Next action

1. Enrique specifies what "current positioning" actually says (not assumed here — no source copy
   was provided).
2. CODE gets repo access to the CoreSyn web property.
3. CODE drafts the specific title/copy diffs as a small, reviewable PR — no direct edits to
   production.
4. Claims QA + Enrique approval before merge/publish.
