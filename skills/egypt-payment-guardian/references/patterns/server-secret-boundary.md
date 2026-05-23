# Server Secret Boundary

## Principle

Payment secrets belong in trusted server code only. Frontend code may receive only public checkout data explicitly allowed by the provider.

## Server-Side Only

Keep these out of browsers, mobile clients, public repos, logs, and analytics:

- merchant secret keys
- HMAC secrets
- API secret keys
- service role keys
- Basic Authorization secrets
- terminal secrets
- private keys
- webhook signing secrets
- raw provider signatures
- raw card data unless PCI scope is intentionally owned

## Safe Client Data

Client code may receive:

- hosted checkout URL
- public checkout key if provider documents it as public
- client secret/reference intended for checkout initialization
- local payment attempt id that cannot be used as a credential
- non-sensitive display status from the local server

## Logging

Log only safe identifiers:

- local order id
- local user id if not sensitive in context
- provider transaction/reference id
- status
- timestamp
- verification outcome

Do not log tokens, full card data, signatures, HMAC strings, Authorization headers, or request bodies containing secrets.

## Supabase Boundary

If using Supabase, service role writes belong in Edge Functions or server routes. Browser code must use anon/authenticated client keys only and must not be able to update paid state directly.

## Fail The Review If

- Any `VITE_`, `NEXT_PUBLIC_`, mobile config, or frontend bundle variable contains a secret.
- Client code calls provider payment APIs with secret credentials.
- The app updates paid state from browser code.
- Logs print full callback payloads without redaction.
