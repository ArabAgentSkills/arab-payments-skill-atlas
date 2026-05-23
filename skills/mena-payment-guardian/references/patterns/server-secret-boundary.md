# Server Secret Boundary

Use this pattern whenever an integration needs merchant credentials, HMAC secrets, server keys, SHA phrases, secure hash secrets, bearer credentials, or service role keys.

## Server Only

- API secret keys
- Merchant secure keys
- HMAC secrets
- PayTabs server key
- Amazon Payment Services SHA request/response phrases
- PaySky terminal/SecureHash secrets
- Moyasar secret key and webhook secret token
- BNPL bearer tokens and webhook tokens
- Supabase service role keys

## Client Safe Only When Documented

- Hosted checkout URL
- Checkout/session id intended for the browser
- Public/publishable key where provider docs explicitly permit it
- Local order display reference

## Review Questions

1. Can the browser call this endpoint with the credential? If yes, it is a leak.
2. Can a customer change amount/currency/reference before payment creation? If yes, move creation server-side.
3. Does the callback handler need raw body? If yes, do not JSON-parse before verification.
4. Are logs capturing signatures, tokens, or credentials? If yes, redact them.
