# Moyasar

- Provider: Moyasar
- Scope: Saudi PSP with Payments API, hosted/forms, invoices, Apple Pay/Samsung Pay/STC Pay where enabled, purchase, authorization, capture, void, refund, and webhooks.
- Priority: P0
- Readiness: A
- Public docs status: public
- Last checked: 2026-05-24
- Source confidence: High for official Moyasar docs and helpdesk webhook docs.
- Sources: Moyasar docs home, Payments API, authentication, payment operations, dashboard webhooks, webhook reference.

## Use When

Use for Moyasar payments, payment operations, webhook state changes, capture/void/refund, and Saudi SAR payment integrations.

## Source Map

- Docs: `https://docs.moyasar.com/`
- Payments API: `https://docs.moyasar.com/category/payments-api/`
- Authentication: `https://docs.moyasar.com/api/authentication/`
- Payment operations: `https://docs.moyasar.com/guides/payment-operations/`
- Webhooks: `https://docs.moyasar.com/guides/dashboard/setting-up-webhooks/`
- Webhook reference: `https://docs.moyasar.com/api/other/webhooks/webhook-reference`

## Integration Paths

- Purchase flow authorizes and captures immediately, producing `paid` when successful.
- Authorization flow sets manual capture and returns `authorized`; later capture or void is required.
- Webhooks notify state transitions such as paid, failed, refunded, voided, authorized, captured, verified, and abandoned.

## Setup Prerequisites

- Publishable key, secret key, callback URL, webhook endpoint, webhook secret token, enabled payment methods, and sandbox/live separation.
- Confirm capture windows for Mada vs other card schemes.

## Auth And Secret Boundary

- Publishable key may be used where docs allow client-side payment creation.
- Secret key and webhook secret token must remain server-side.

## Callback Or Webhook Contract

- Webhooks are configured in the Moyasar dashboard with HTTPS endpoint, secret token, HTTP method, and selected events.
- Validate secret token before processing.
- Callback URL is UX/status-return support; server-side fetch/webhook remains authoritative.

## Signature Or HMAC

- Moyasar webhook docs describe a Secret Token used by the merchant server to validate notifications.
- Reject webhook notifications that do not include the expected token or do not match the configured method/event contract.

## Idempotency Keys

- Use Moyasar payment id plus local order/reference.
- For capture/void/refund, use local operation ids and provider operation response references.

## Amount And Currency

- Moyasar operations use smallest currency units for capture/refund amounts.
- Compare payment amount, captured/refunded amount, and currency such as `SAR`.

## Status Mapping

- `paid` maps to paid for purchase after verification.
- `authorized` maps only to authorized; capture is needed for captured settlement.
- `captured`, `voided`, `refunded`, `failed`, `verified`, and `abandoned` stay distinct.

## Refunds Voids And Subscriptions

- Capture applies to authorized payments and may be partial.
- Void releases authorized holds or reverses paid/captured payments within allowed window.
- Refund applies to paid/captured amounts and can be partial within documented limits.
- Recurring/subscription-like flows need explicit current docs before implementation.

## Sandbox And Test Notes

- Use Moyasar test keys and dashboard webhooks.
- Test capture failure, void fallback, refund retry, and status fetch after failure.

## Unknowns And Do Not Invent

- Do not invent capture windows beyond the current docs.
- Do not invent webhook signature headers; use the configured secret token validation and current merchant docs.

## Agent Checklist

- Distinguish publishable vs secret key.
- Verify webhook secret token.
- Compare amount/currency/order reference.
- Separate paid, authorized, captured, voided, and refunded.
- Use payment fetch after operation failure.

## Fail If

- You expose secret key in frontend.
- You treat `authorized` as fulfilled/captured.
- You refund more than captured/paid amount.
- You process webhook without token validation.
