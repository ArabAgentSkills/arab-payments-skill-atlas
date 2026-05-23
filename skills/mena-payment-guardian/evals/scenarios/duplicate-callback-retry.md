# Duplicate Callback Retry

## User Prompt

"Our PSP retries webhooks and customers refresh the success page. Avoid duplicate paid actions."

## Required Skill Use

The agent applies `idempotency-state-transitions.md` and the provider reference.

## Expected Agent Behavior

- Creates or uses unique constraints for provider event ids, payment ids, transaction refs, and local order refs.
- Handles duplicate callbacks and page refresh as no-ops after verified final state.
- Does not overwrite paid/captured with stale pending/failed events.
- Stores capture/refund/void operation ids separately.

## Fail If

- Duplicate event grants duplicate credits, shipments, bookings, invoices, or subscriptions.
- Stale failed callback overwrites paid/captured state.
- Provider event is processed before authenticity and amount checks.
