# Eval: Paymob Redirect Before Callback

## User Prompt

"Add Paymob checkout. After Paymob redirects back with success, mark the subscription active."

## Required Skill Use

Load `references/providers/paymob.md` and `references/patterns/webhook-first-fulfillment.md`.

## Expected Agent Behavior

- Creates Paymob payment/intention server-side.
- Treats redirect as UX only.
- Shows processing or checks local server payment state on return.
- Implements backend callback endpoint with Paymob HMAC verification.
- Activates subscription only after verified callback plus amount/currency/reference match.
- Makes activation idempotent.

## Fail If

- Redirect query params mark subscription active.
- HMAC verification is missing.
- Callback and redirect ordering is not addressed.
- Duplicate callback can create duplicate subscription rows.

## Automated Checks

- must: server-side
- must: redirect as UX only
- must: processing
- must: Paymob HMAC verification
- must: amount/currency/reference match
- must: idempotent
- must-not: redirect query params mark subscription active
