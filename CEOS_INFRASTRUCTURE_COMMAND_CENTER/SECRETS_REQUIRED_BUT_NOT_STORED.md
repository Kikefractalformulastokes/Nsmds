# Secrets / Credentials Required But NOT Stored Here

Per the governing rule ("no toques secretos", "no subas claves API"), **no secret, key, or
credential is stored in this repo or in this command center.** This file only lists what would
be *needed*, by whom, out of band, to unblock the rest of the brief.

| Needed for | Credential/access type | Holder | Where it must live |
|---|---|---|---|
| Auditing CoreSyn/CEOS/ModelAssuranceLab/RiesgoDeObra/Materials/Aerospace repos | GitHub repo access grant (`add_repo`) to this session, or a separate session scoped to each repo | Enrique | Never in this repo — grant via session config only |
| Search Console verification | Google account access (Chrome agent, browser session) | Enrique | Chrome agent's authenticated browser only |
| Stripe review (RiesgoDeObra) | Stripe dashboard login | Enrique | Chrome agent's authenticated browser only |
| Tally review | Tally account login | Enrique | Chrome agent's authenticated browser only |
| DNS changes (any `coresyn.io`, `riesgodeobra.es` record) | Registrar/DNS provider login | Enrique | Chrome agent, with explicit per-change approval |
| Analytics install | GA4/Plausible property + install approval | Enrique | Explicit approval required before any snippet is added |

No API keys, tokens, `.env` values, or passwords were found anywhere in the `nsmds` repo during
this audit (verified via pattern scan for `api_key`, `secret`, `token`, `password`, PEM headers).
