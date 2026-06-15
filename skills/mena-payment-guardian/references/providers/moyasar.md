# Moyasar

- Provider: Moyasar
- Scope: Saudi PSP with Payments API, hosted/forms, invoices, Apple Pay/Samsung Pay/STC Pay where enabled, purchase, authorization, capture, void, refund, standalone 3D Secure card authentication where enabled, and webhooks.
- Priority: P0
- Readiness: A
- Public docs status: public
- Last checked: 2026-06-15
- Source confidence: High for official Moyasar docs and helpdesk webhook docs.
- Sources: Moyasar docs home, Payments API, authentication, card authentication API, standalone 3D Secure guide, payment operations, dashboard webhooks, webhook reference.

## Use When

Use for Moyasar payments, standalone 3D Secure card authentication, payment operations, webhook state changes, capture/void/refund, and Saudi SAR payment integrations.

## Source Map

- Docs: `https://docs.moyasar.com/`
- Payments API: `https://docs.moyasar.com/category/payments-api/`
- Authentication: `https://docs.moyasar.com/api/authentication/`
- Card authentication API: `https://docs.moyasar.com/api/card_auths/01-create-card-auth`
- Fetch card authentication: `https://docs.moyasar.com/api/card_auths/02-fetch-card-auth`
- Standalone 3D Secure: `https://docs.moyasar.com/guides/3d-secure/standalone-authentication`
- Payment operations: `https://docs.moyasar.com/guides/payment-operations/`
- Webhooks: `https://docs.moyasar.com/guides/dashboard/setting-up-webhooks/`
- Webhook reference: `https://docs.moyasar.com/api/other/webhooks/webhook-reference`

## Integration Paths

- Purchase flow authorizes and captures immediately, producing `paid` when successful.
- Authorization flow sets manual capture and returns `authorized`; later capture or void is required.
- Standalone 3D Secure card authentication verifies cardholder authentication without charging the card. Its result can support a later payment flow, but it is not a paid, authorized, or captured payment by itself.
- Webhooks notify state transitions such as paid, failed, refunded, voided, authorized, captured, verified, and abandoned.
- Card-authentication webhooks notify standalone 3D Secure outcomes such as `card_auth_authenticated` and `card_auth_failed`; process them separately from `payment_*` fulfillment events.

## Setup Prerequisites

- Publishable key, secret key, callback URL, webhook endpoint, webhook secret token, enabled payment methods, and sandbox/live separation.
- Confirm capture windows for Mada vs other card schemes.

## Auth And Secret Boundary

- Publishable key may be used where docs allow client-side payment creation.
- Secret key and webhook secret token must remain server-side.

## Callback Or Webhook Contract

- Webhooks are configured in the Moyasar dashboard with HTTPS endpoint, secret token, HTTP method, and selected events.
- Validate secret token before processing.
- For `card_auth_*` webhook events, treat `data` as the card authentication object, not a payment object.
- Callback URL is UX/status-return support; server-side fetch/webhook remains authoritative.

## Signature Or HMAC

- Moyasar webhook docs describe a Secret Token used by the merchant server to validate notifications.
- Reject webhook notifications that do not include the expected token or do not match the configured method/event contract.
- Do not accept card-authentication webhook events without the same secret-token validation used for payment webhook events.

## Idempotency Keys

- Use Moyasar payment id plus local order/reference.
- For standalone card authentication, use the webhook event id plus card authentication id.
- For capture/void/refund, use local operation ids and provider operation response references.

## Amount And Currency

- Moyasar operations use smallest currency units for capture/refund amounts.
- Compare payment amount, captured/refunded amount, and currency such as `SAR`.

## Status Mapping

- `paid` maps to paid for purchase after verification.
- `authorized` maps only to authorized; capture is needed for captured settlement.
- `captured`, `voided`, `refunded`, `failed`, `verified`, and `abandoned` stay distinct.
- `card_auth_authenticated` means a standalone 3D Secure card-authentication flow completed successfully; it does not mean payment fulfillment.
- `card_auth_failed` means the standalone card-authentication flow failed or expired; keep it separate from payment failure unless a linked payment attempt is also failed by verified server state.

## Refunds Voids And Subscriptions

- Capture applies to authorized payments and may be partial.
- Void releases authorized holds or reverses paid/captured payments within allowed window.
- Refund applies to paid/captured amounts and can be partial within documented limits.
- Recurring/subscription-like flows need explicit current docs before implementation.

## Sandbox And Test Notes

- Use Moyasar test keys and dashboard webhooks.
- Test `card_auth_authenticated` and `card_auth_failed` webhook handling where standalone 3D Secure is enabled for the merchant.
- Test capture failure, void fallback, refund retry, and status fetch after failure.

## Unknowns And Do Not Invent

- Do not invent capture windows beyond the current docs.
- Do not invent webhook signature headers; use the configured secret token validation and current merchant docs.
- Do not assume standalone 3D Secure card authentication is enabled for every merchant.

## Agent Checklist

- Distinguish publishable vs secret key.
- Verify webhook secret token.
- Keep standalone card authentication separate from paid/captured fulfillment.
- Compare amount/currency/order reference.
- Separate paid, authorized, captured, voided, and refunded.
- Use payment fetch after operation failure.

## Fail If

- You expose secret key in frontend.
- You treat `authorized` as fulfilled/captured.
- You treat `card_auth_authenticated` as paid, authorized, captured, shipped, or fulfilled.
- You refund more than captured/paid amount.
- You process webhook without token validation.
