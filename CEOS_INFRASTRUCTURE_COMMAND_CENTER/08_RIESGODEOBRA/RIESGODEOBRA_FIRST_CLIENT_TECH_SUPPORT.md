# RiesgoDeObra — First Client Tech Support Plan

**Status: not yet needed — `commercial.customers` is still 0.**

When the first real client/payment happens:
1. Confirm the Stripe transaction and Tally submission link up correctly (the two currently
   BLOCKED verification items — see `STRIPE_STATUS_REPORT.md`, `TALLY_STATUS_REPORT.md` — should
   be resolved before this point, not discovered during a live client's first payment).
2. Manual check that the client received confirmation (email/receipt).
3. Update CEOS Company State (`commercial.customers` → 1, `revenue` → actual amount) with the
   transaction as evidence.
4. Log the case in `16_SECURITY_GROWTH/09_CRM_LEADOPS/LEAD_PIPELINE.csv` as `PAID`.
5. Only then consider a case study (`16_SECURITY_GROWTH/08_CONTENT_ENGINE/CASE_STUDY_TEMPLATE.md`),
   with the client's explicit consent.
