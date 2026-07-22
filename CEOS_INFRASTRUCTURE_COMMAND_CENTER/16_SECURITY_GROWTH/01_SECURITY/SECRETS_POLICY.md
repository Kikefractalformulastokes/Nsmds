# Secrets Policy

1. No secret, API key, token, password, or private key is ever committed to any CoreSyn/CEOS
   repository, public or private.
2. Secrets live only in: (a) the deploy platform's environment-variable store (Vercel/Netlify/
   Azure App Settings), (b) a password manager for human-held credentials, or (c) a secret
   manager (Azure Key Vault) for service-to-service credentials.
3. Frontend bundles may only ever contain "publishable" keys explicitly designed to be public
   (Stripe publishable key, Supabase anon key + RLS enforced). Never a secret key, service-role
   key, or webhook signing secret.
4. Every new repo gets a secret-pattern scan (same method used in this audit: grep for
   `api_key|secret|token|password|BEGIN (RSA|PRIVATE)|sk-[a-zA-Z0-9]`) before its first commit to
   a shared branch, and CODE re-runs it before every PR that touches config.
5. If a secret is ever accidentally committed: rotate it immediately, then scrub history — do
   not just delete the file in a new commit (history still contains it). This requires Enrique
   approval before a force-push/history-rewrite, per the destructive-action rules.
6. This command center itself will never contain a real secret — see
   `SECRETS_REQUIRED_BUT_NOT_STORED.md` at the command-center root for the "what's needed, held
   where" list.
