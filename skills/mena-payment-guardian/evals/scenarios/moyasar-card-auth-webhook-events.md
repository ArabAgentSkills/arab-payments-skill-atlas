# Moyasar Card Authentication Webhook Events

## User Prompt

"Moyasar sent a `card_auth_authenticated` webhook for standalone 3D Secure. Can we mark the order paid and ship? Also handle `card_auth_failed` the same way as a failed payment."

## Required Skill Use

The agent loads `moyasar.md`, `webhook-first-fulfillment.md`, and `idempotency-state-transitions.md`.

## Expected Agent Behavior

- Validates the Moyasar webhook secret token before processing any `card_auth_*` event.
- Treats `card_auth_authenticated` and `card_auth_failed` as standalone card-authentication outcomes, not `payment_*` fulfillment events.
- Keeps the card authentication id and webhook event id idempotent and separate from payment id, capture id, refund id, and order fulfillment state.
- Does not mark the order paid, authorized, captured, shipped, or fulfilled from card authentication alone.
- Requires a verified payment, capture, or documented server-side payment state before fulfillment.

## Fail If

- Agent treats `card_auth_authenticated` as paid, authorized, captured, shipped, or fulfilled.
- Agent maps `card_auth_failed` directly to payment failure without checking linked payment state.
- Agent processes the webhook without Moyasar secret token validation.

## Automated Checks

- must: webhook secret token
- must: card_auth_authenticated
- must: card_auth_failed
- must: standalone card-authentication
- must: idempotent
- must: verified payment
- must-not: mark paid and ship
- must-not: failed payment the same way
