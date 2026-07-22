# Website Architecture Map (target)

Per the brief — this is the **target** structure, not a confirmed live state. Only the `nsmds`
row has any direct evidence; the rest is copied from the brief as the design intent.

| Property | Purpose | Status |
|---|---|---|
| `coresyn.io` | Company, technology, Assurance Core, CEP, verticals, research | NOT_ACCESSIBLE_THIS_SESSION |
| `modelassurancelab.coresyn.io` | Enterprise/commercial product | NOT_ACCESSIBLE_THIS_SESSION |
| `app.coresyn.io` | Future app/API/verification, referenced once in `research/paper-01-dual-observable/README.md` as hosting a whitepaper PDF | NOT_VERIFIED (URL text found, not fetched) |
| `docs.coresyn.io` | Future documentation | NOT_ACCESSIBLE_THIS_SESSION |
| `coresyn.io/aerospace` | CoreSyn Aerospace Assurance Lab / Airbus PoC (public-safe framing) | NOT_ACCESSIBLE_THIS_SESSION — `nsmds`'s `index.html` is the closest existing artifact (a standalone Aerospace demo page, not this path) |
| `coresyn.io/materials` | Materials Assurance | NOT_ACCESSIBLE_THIS_SESSION |
| `riesgodeobra.es` | Active commercial experiment | NOT_ACCESSIBLE_THIS_SESSION; external QA reported via Enrique (see `08_RIESGODEOBRA/`) |
| Demos (`/demos/*`) | Atomic Forest, Moiré Graphene, Exoplanets, Solar UV, Dark Chemistry, Digital Twins | NOT_ACCESSIBLE_THIS_SESSION — planned in `09_SCIENTIFIC_DEMOS/` |

This map should be re-verified against real DNS/hosting once Chrome-agent access exists
(`SEO_TASK_LIST_FOR_CHROME.md` in `11_SEO_ANALYTICS/`).
