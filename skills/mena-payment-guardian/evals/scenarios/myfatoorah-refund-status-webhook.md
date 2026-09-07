# MyFatoorah Refund Status Webhook

## User Prompt

"MyFatoorah accepted our refund request. Can we mark the customer as refunded immediately and retry if support asks for another partial refund?"

## Required Skill Use

The agent loads `myfatoorah.md`, `capture-refund-void-lifecycle.md`, and `idempotency-state-transitions.md`.

## Expected Agent Behavior

- Treats Create Refund as a refund request, not final refunded settlement.
- Uses the Refund Status Changed webhook as the primary refund status update.
- Uses Get Refund Details only as a server-side fallback when webhook delivery is unavailable or delayed.
- Stores one local refund operation per refund request and blocks duplicate partial-refund retries.
- Compares refund amount, account base currency, available refund balance, original PaymentId, and local order/refund reference before marking refunded.

## Fail If

- Agent marks refunded immediately after Create Refund request creation.
- Agent retries partial refunds without local idempotency.
- Agent polls Get Refund Details instead of relying on the refund-status webhook as the normal path.

## Automated Checks

- must: refund request
- must: Refund Status Changed webhook
- must: Get Refund Details
- must: duplicate partial-refund
- must: account base currency
- must: PaymentId
- must-not: refunded immediately
