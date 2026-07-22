# Data Classification Policy

| Level | Definition | Examples in this ecosystem |
|---|---|---|
| PUBLIC | Safe for anyone, anywhere | Marketing copy, published paper drafts (with status labels), demo pages, public keyword/SEO plans |
| INTERNAL | Not secret, but not meant for public distribution | Editorial calendars, CRM pipeline, internal QA reports, this command center |
| CONFIDENTIAL | Would create business risk if disclosed | Pricing negotiation notes, unreleased Aerospace PoC scope details, investor decks pre-release |
| SENSITIVE | Personal data requiring consent/purpose limitation | Lead names/emails/phone numbers, RiesgoDeObra client project details, any form submission |
| SECRET | Would create severe/legal/security risk if disclosed | API keys, credentials, NS-MDS core method internals not yet gated for release, unpublished NS-MDS numerical execution package |

## Rules

- Every new document must be classified when created (add a `Classification:` line near the top).
- SENSITIVE data (leads, form data) is collected only with a stated purpose and reasonable
  consent (checkbox/notice at the point of collection) — no silent collection.
- SECRET-level material never enters a public repo, public web path, or unencrypted email.
- This command center is INTERNAL by default; nothing in it should be published to a public site
  verbatim.
