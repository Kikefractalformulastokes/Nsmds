# Incident Response — Lite

For a small team, this is a checklist, not a 24/7 SOC.

## If a secret leaks (key, token, password committed or exposed)

1. Rotate the credential immediately at the source (Stripe/Supabase/GitHub/etc.) — this comes
   before cleanup.
2. Remove it from the current file in a new commit.
3. Scrub git history if it's a shared/public repo (requires Enrique approval — history rewrite is
   destructive).
4. Note the incident in `SECURITY_RISK_REGISTER.md` with date and remediation.

## If a false/risky public claim is discovered live (e.g. an unverified "Airbus" reference)

1. Flag in `CLAIMS_QA_REPORT.md` / `GROWTH_CLAIMS_QA.md`.
2. Get Enrique's ruling on the underlying fact.
3. CODE prepares the copy fix as a small PR; do not edit production directly.
4. Publish the correction once approved.

## If a form starts collecting more data than declared, or data looks mishandled

1. Pause the form (Chrome agent, with approval) or take it offline if severe.
2. Identify what was collected and why.
3. Notify affected individuals if required by applicable data-protection law (Enrique + legal
   judgment call — out of scope for this session to determine).
4. Fix the form's data collection scope before reactivating.

## Contacts

Not populated — no incident contact list exists in this repo. Enrique to supply.
