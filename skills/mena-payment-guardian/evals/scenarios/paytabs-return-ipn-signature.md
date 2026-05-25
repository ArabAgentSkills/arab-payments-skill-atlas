# PayTabs Return IPN Signature

## User Prompt

"PayTabs redirected the customer to return URL with a signature. I also have callback/IPN enabled. Can I use the same signature logic everywhere and fulfill from return?"

## Required Skill Use

The agent loads `paytabs.md` and `webhook-first-fulfillment.md`.

## Expected Agent Behavior

- Treats Return URL as browser-dependent UX, not the only fulfillment signal.
- Distinguishes Return URL signature verification from callback/IPN raw-body HMAC verification.
- Verifies callback/IPN `Signature` header over the raw payload using the server key.
- Compares `cart_id`, `tran_ref`, `cart_amount`, and `cart_currency`.
- Processes duplicate callback/IPN deliveries idempotently.

## Fail If

- Agent fulfills from Return URL alone.
- Agent uses Return URL sorted-field verification for callback/IPN raw payloads.
- Agent exposes the PayTabs server key to frontend code.

## Automated Checks

- must: Return URL
- must: browser-dependent UX
- must: raw-body HMAC
- must: `Signature` header
- must: `cart_id`
- must: `tran_ref`
- must-not: same signature logic everywhere
