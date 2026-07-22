# Privacy-Safe Analytics Plan

Principles for whichever tool Enrique selects:

1. Prefer cookieless/first-party analytics where practical (reduces consent-banner friction and
   legal exposure) — e.g. Plausible/Fathom-style tools, or GA4 configured with IP anonymization
   and minimal data retention, per Enrique's choice.
2. No cross-site tracking pixels beyond what's needed for the approved ad platforms once SEM is
   live, and only after a cookie/consent notice is in place for EU visitors (RiesgoDeObra is
   Spain-facing).
3. No session recording / heatmap tool that captures form input by default — if used, mask
   sensitive fields.
4. Data retention: align with `PRIVACY_AND_DATA_RETENTION.md` (§01_SECURITY) — don't keep raw
   event data indefinitely without a reason.
5. No analytics tool is installed without Enrique's explicit sign-off — this file documents the
   decision framework, not a decision.

**Status:** no tool selected yet. `ANALYTICS_DECISION_LOG.md` (once populated) will record the
actual choice and rationale.
