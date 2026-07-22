# Pre-Merge QA Checklist

Run 2026-07-22, against `claude/coresyn-ceos-infrastructure-audit-sthqhh`.

## Build/test command

```
$ find . -iname "*.yml" -o -iname "*.yaml"   # no CI config
$ ls package.json                             # not found
```

No build/test step exists for `nsmds` (static HTML + Markdown, no bundler, no test suite). This
is expected for the repo's current size — not a gap introduced by this session.

## HTML parse result

```
$ python3 -c "
import html.parser
class P(html.parser.HTMLParser): pass
p = P()
with open('index.html') as f: p.feed(f.read())
print('OK: index.html parses without exception')
"
OK: index.html parses without exception
```

**Result: PASS.** (Before the fix, the file had a `<script>` before `<head>`, chart markup nested
inside `<style>`, and a duplicate `<title>` — documented in `12_QA_REPORTS/QA_MASTER_REPORT.md`.)

## Link check

- `https://cdn.jsdelivr.net/npm/chart.js@4` — now version-pinned (was unpinned `.../chart.js`).
- `https://app.coresyn.io/research/coresyn-whitepaper-july-2026.pdf` (referenced in
  `research/paper-01-dual-observable/README.md`) — not fetched this session, NOT_VERIFIED, not
  confirmed broken.
- No other outbound links exist in the repo.

**Result: PASS** (no known-broken link; one link remains unverified pending Chrome-agent fetch).

## Claims check

```
$ grep -ni "airbus" index.html README.md
NO_MATCHES_FOUND
```

**Result: PASS.** Confirmed via direct grep against the two changed public files, run after the
fix (2026-07-22).

## No-secrets scan

```
$ grep -riE "api[_-]?key|secret|token|password|BEGIN (RSA|PRIVATE)|sk-[a-zA-Z0-9]" -r . --exclude-dir=.git
```

Matches found are all inside this session's own documentation *discussing* the secrets policy
(e.g. "no API keys were found," "secrets never enter git history") — no real credential value
matched. **Result: PASS**, re-confirmed after adding ~155 new documentation files this session.

## No Airbus public claim

Covered under "Claims check" above — confirmed **PASS** by direct grep on the two changed public
files. The command-center's own internal docs still discuss "Airbus" as historical audit trail
(the finding and its fix) — that's expected and is INTERNAL-classified, not public-facing.

## No production deploy risk

No deploy was executed. This branch has not been merged to `main`. See
`DEPLOYMENT_RISK_NOTE.md` for the conditional risk if `main` is configured to auto-deploy.

---

**Overall pre-merge QA verdict: PASS.** Ready for human review; merge still requires Enrique's
explicit approval per `DEPLOYMENT_RISK_NOTE.md`.
