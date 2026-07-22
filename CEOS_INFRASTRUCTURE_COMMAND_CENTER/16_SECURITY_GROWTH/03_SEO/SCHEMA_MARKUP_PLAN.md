# Schema Markup Plan

Recommended structured-data types per page type (JSON-LD), to be added once each page exists:

| Page type | Schema.org type |
|---|---|
| Organization / homepage | `Organization` |
| Technical/whitepaper pages | `TechArticle` or `ScholarlyArticle` (paper already has DOI-ready metadata in `metadata.json` — reuse those fields) |
| Product pages (ModelAssuranceLab) | `Product` or `SoftwareApplication`, only with real, non-inflated claims |
| RiesgoDeObra service pages | `Service` |
| FAQ sections | `FAQPage` |
| Contact page | `ContactPage` |

**Rule:** schema must match visible page content exactly — no schema claim (rating, price,
availability) that isn't also shown and true on the page. This is a Google spam-policy
requirement, not just good practice.

**Status:** not implemented anywhere — no page exists in an accessible repo yet.
