# Sitemap / Robots Plan

## nsmds (this repo)

- No `sitemap.xml` exists.
- No `robots.txt` exists.
- Given this repo currently serves one demo page, a minimal `robots.txt` allowing indexing and a
  one-URL `sitemap.xml` would be trivial to add — **not added in this session** pending the
  Claims QA decision on the "Airbus" reference (no point indexing a page that's about to change).

## Other properties

NOT_ACCESSIBLE_THIS_SESSION. Once in scope, standard rules apply:
- One `sitemap.xml` per property, submitted to Search Console by the Chrome agent.
- `robots.txt` disallows internal/staging paths, allows public marketing paths.
- No `noindex` left on a page that's meant to rank (common accidental SEO killer — check
  explicitly).
