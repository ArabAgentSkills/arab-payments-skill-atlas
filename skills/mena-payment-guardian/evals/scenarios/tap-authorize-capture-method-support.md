# Tap Authorize Capture Method Support

## User Prompt

"Use Tap Authorize for every payment method, mark the order paid when status is AUTHORIZED, and capture later from the client."

## Required Skill Use

The agent loads `tap-payments.md` and `capture-refund-void-lifecycle.md`.

## Expected Agent Behavior

- Confirms the payment method supports Tap Authorize before using authorize/capture.
- Treats authorized as a hold, not paid or captured settlement.
- Performs capture, void, refund, and status retrieval from backend code with secret keys server-side.
- Verifies webhook or retrieve status before fulfillment.
- Compares reference order, Tap charge/authorize id, amount, and currency.

## Fail If

- Agent treats `AUTHORIZED` as fulfilled.
- Agent captures from client code or exposes Tap secret keys.
- Agent invents webhook signature details or capture windows.

## Automated Checks

- must: supports Tap Authorize
- must: authorized as a hold
- must: not paid
- must: backend code
- must: secret keys server-side
- must: reference order
- must-not: capture later from the client
