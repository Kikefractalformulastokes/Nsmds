# SEO Technical Audit

## nsmds (the only page this session can inspect)

| Check | Result |
|---|---|
| `<title>` tag | FAIL — duplicated (`NS-MDS \| Airbus Demo` outside `<head>`, then `NS-MDS \| Airbus` inside `<head>`); browsers/crawlers will use the malformed markup unpredictably |
| Meta description | MISSING |
| Valid HTML structure | FAIL — script before `<head>`, content nested inside `<style>` (see `12_QA_REPORTS/QA_MASTER_REPORT.md`) |
| Mobile viewport meta | PRESENT (`width=device-width, initial-scale=1.0`) |
| `robots.txt` | MISSING (not found in repo) |
| `sitemap.xml` | MISSING (not found in repo) |
| Semantic headings | Only one `<h1>` (`NS-MDS`), no `<h2>`/structure beyond that |
| Alt text on images | N/A — no images, only a canvas chart |

## All other properties (CoreSyn, RiesgoDeObra, ModelAssuranceLab, Materials, Aerospace)

NOT_ACCESSIBLE_THIS_SESSION — no live crawl performed, no Search Console connected.
