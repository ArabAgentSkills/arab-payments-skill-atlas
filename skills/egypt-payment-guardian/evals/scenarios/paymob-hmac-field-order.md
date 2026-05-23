# Eval: Paymob HMAC Field Order

## User Prompt

"I verified Paymob by hashing every callback field alphabetically. The redirect says success, so can we activate the order?"

## Required Skill Use

Load `references/providers/paymob.md`.

## Expected Agent Behavior

- Rejects generic alphabetical hashing for Paymob transaction callbacks.
- Uses the exact Paymob transaction HMAC field order from the provider reference.
- Distinguishes Processed POST fields from Response GET fields for `obj.id`/`id` and `order.id`/`order_id`.
- Does not reuse card-token HMAC fields for transaction callbacks.
- Activates only after valid HMAC, matching amount/currency/reference, and paid status.

## Fail If

- The agent says hashing all fields alphabetically is enough for Paymob.
- The agent uses the card-token HMAC list for transaction callbacks.
- The agent fulfills from redirect success before verified callback state.
