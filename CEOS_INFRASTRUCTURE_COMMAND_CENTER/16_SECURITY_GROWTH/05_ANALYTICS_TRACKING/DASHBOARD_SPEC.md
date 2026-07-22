# Dashboard Spec

Metrics per the brief, to be built once real events flow (no live data exists to build this
against yet):

- Visitors (by property)
- Conversion rate (top → bottom of funnel, per `CONVERSION_FUNNEL_MAP.md`)
- CTA clicks (by event, per `EVENT_TRACKING_MAP.md`)
- Lead source (via `UTM_POLICY.md` attribution)
- Qualified leads (per `LEAD_SCORING_RULES.md` once CRM exists)
- Payment attempts / revenue confirmed (RiesgoDeObra only, from Stripe)
- Funnel drop-off (stage-to-stage per vertical)

Candidate home: a CEOS module (`03_CEOS/CEOS_MODULE_MAP.md` — "Commercial Execution" module) or a
lightweight Azure-hosted dashboard per `AZURE_ARCHITECTURE_OPTIONS.md`, decided once there's real
data volume to justify either.
