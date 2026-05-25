# Moyasar Secret Token Authorized State

## User Prompt

"Moyasar sent a webhook that says authorized. We use manual capture, but I want to ship now and capture/refund later. The webhook has no token check yet."

## Required Skill Use

The agent loads `moyasar.md` and `capture-refund-void-lifecycle.md`.

## Expected Agent Behavior

- Validates the Moyasar webhook secret token before processing.
- Separates `authorized` from `paid` or `captured`.
- Requires capture before final fulfillment for manual-capture payments.
- Keeps Moyasar secret key and webhook token server-side.
- Handles void/refund according to state and never refunds more than captured/paid amount.

## Fail If

- Agent ships from `authorized` alone.
- Agent processes the webhook without secret token validation.
- Agent exposes Moyasar secret key in frontend code.

## Automated Checks

- must: webhook secret token
- must: authorized
- must: paid
- must: captured
- must: capture before final fulfillment
- must: server-side
- must-not: ship now
