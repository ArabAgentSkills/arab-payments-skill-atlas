# Webhook-First Fulfillment

## Principle

Customer-facing redirects and SDK callbacks are UX signals. Backend callbacks, webhooks, or verified server-side status inquiries are fulfillment signals.

## Default Flow

1. Create a local payment attempt with `status = pending`.
2. Create the provider checkout/session/reference from the server.
3. Redirect or initialize the client checkout with only the public data required by the provider.
4. On client return, show `processing` unless local server state is already `paid`.
5. On callback/webhook/inquiry, verify authenticity.
6. Compare local order reference, amount, currency, and provider reference.
7. In one transaction, record the event and advance state if allowed.
8. Trigger fulfillment only after the durable local state is `paid`.

## When Callback Is Delayed

Use provider inquiry/status APIs when documented. Poll briefly for UX if needed, but do not bypass the verified server confirmation rule.

## When Callback Arrives First

Process the callback normally, update local server state, and let the redirect page read the already-confirmed state.

## When Redirect Arrives First

Do not unlock access. Show a waiting state, then query local server state. Use provider inquiry only through the server if the provider documents it.

## Fail The Review If

- Browser query params set `paid = true`.
- Client SDK success creates subscriptions, bookings, enrollments, invoices, credits, or order fulfillment directly.
- Signature verification is skipped because the callback "comes from the provider."
- Refreshing the success page can trigger fulfillment again.
