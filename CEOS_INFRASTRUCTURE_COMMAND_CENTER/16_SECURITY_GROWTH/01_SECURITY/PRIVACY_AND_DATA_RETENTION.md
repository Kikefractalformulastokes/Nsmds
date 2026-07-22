# Privacy and Data Retention

## Current state

`nsmds` collects no personal data (no forms, no analytics, no cookies). This is the correct
baseline — nothing to retain, nothing to delete.

## Rules for any future form/tracking (RiesgoDeObra Tally/Stripe, CoreSyn contact forms, CEOS
lead capture)

1. State the purpose of collection at the point of collection (why this field is being asked
   for).
2. Collect the minimum needed — no phone number if email suffices, no company revenue field if
   not used in scoring.
3. Set a retention period per data type in `CRM_LITE_SCHEMA.md` once that system exists — leads
   that go cold (e.g. 12 months no contact) get reviewed for deletion/anonymization.
4. Analytics: prefer privacy-safe/cookieless tools where practical (see
   `PRIVACY_SAFE_ANALYTICS_PLAN.md`); no analytics tool is installed without Enrique's approval.
5. Any EU-based lead (RiesgoDeObra is Spain-facing) falls under GDPR — consent language and a
   privacy policy page are required before the first form goes live commercially. This is a
   legal-review item, not something this session can certify.
