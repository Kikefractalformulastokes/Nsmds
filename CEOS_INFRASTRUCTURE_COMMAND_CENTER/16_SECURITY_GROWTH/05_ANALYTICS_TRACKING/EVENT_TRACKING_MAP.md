# Event Tracking Map

Per the brief's minimum event list. None are implemented yet (no site to instrument).

## CoreSyn
`contact_click`, `deck_download`, `one_pager_download`, `demo_view`, `cep_page_view`,
`materials_interest`, `aerospace_interest`

## RiesgoDeObra
`stripe_click`, `tally_open`, `lead_magnet_open`, `demo_view`, `pricing_view`,
`form_submit_confirmed` (if platform exposes it), `checkout_started` (if platform exposes it)

## ModelAssuranceLab
`request_review_click`, `evidence_package_interest`, `enterprise_contact`

## Aerospace
`one_pager_click`, `poc_scope_click`, `contact_alvaro_ready`

## Implementation rule

Every event fires only on an explicit user action (click, view, submit) — no passive
fingerprinting, no third-party data sharing beyond the chosen analytics tool. Event names above
are the agreed vocabulary; implementation maps them to whatever the chosen tool calls its event
API.
