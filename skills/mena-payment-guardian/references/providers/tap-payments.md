# Tap Payments

- Provider: Tap Payments
- Scope: Kuwait / GCC / MENA PSP with hosted checkout, Charge API, Authorize API, Payment Request, SDKs, webhooks, recurring, capture, void, and refunds.
- Priority: P0
- Readiness: A
- Public docs status: public
- Last checked: 2026-05-25
- Source confidence: High for official Tap developer docs; webhook `hashstring` details are public but must be checked against the exact webhook/API version in use.
- Sources: Tap get started, webhook, authentication, API actions, recurring payments.

## Use When

Use for Tap checkout, charges, authorizations, captures, voids, webhooks, and regional payment method integrations.

## Source Map

- Get started: `https://developers.tap.company/docs/get-started`
- Webhook: `https://developers.tap.company/docs/webhook`
- Authentication: `https://developers.tap.company/docs/authentication`
- API actions: `https://developers.tap.company/reference/api-actions`
- Recurring: `https://developers.tap.company/docs/recurring-payments`

## Integration Paths

- Hosted checkout through Charge API for direct capture.
- Authorize API for hold-then-capture/void flows where the payment method supports authorization.
- Mobile SDKs and encrypted card/payment request flows where supported.

## Setup Prerequisites

- Tap account, secret key, environment selection, redirect URL, post/webhook URL, merchant/country setup, and enabled methods.
- Confirm whether a method supports authorize/capture before using the Authorize API.

## Auth And Secret Boundary

- Keep secret keys and API credentials server-side.
- Frontend must not call server-key operations directly.

## Callback Or Webhook Contract

- Tap webhook payloads include object type, status, amount, currency, transaction/reference fields, redirect/post information, and merchant identifiers.
- Tap docs say the POST URL is the reliable fallback when browser redirect fails after capture; accept raw posted data only on a reachable HTTPS endpoint.
- Use webhook or server-side retrieve/action response as the authoritative signal; redirect status is UX.
- Store charge/authorize id, reference order, transaction id, amount, currency, and status.

## Signature Or HMAC

- Verify Tap webhook authenticity using the `hashstring` header and current official webhook signing rules for the account/API version.
- Public docs describe HMAC-SHA256 over operation-specific `x_` fields with the Tap secret API key: charge/authorize/refund responses use id, amount, currency, gateway/payment references, status, and created timestamp; invoice responses use id, amount, currency, updated, status, and created timestamp.
- Round amount according to the documented ISO currency decimal precision before computing `hashstring`.
- If the public page or merchant account docs differ for the operation in use, ask for merchant docs or use documented retrieve/status API to confirm before fulfillment.

## Idempotency Keys

- Use merchant `reference.order`, Tap charge/authorize id, and transaction references.
- Store webhook delivery/event ids if present; otherwise deduplicate by object id plus status/action timestamp.

## Amount And Currency

- Tap webhook payloads carry decimal `amount` and ISO currency.
- Compare amount, currency, and reference order before local paid/captured state.

## Status Mapping

- Charge success/captured maps to paid only after verification.
- Authorized maps to authorized, not paid/captured.
- Failed/cancelled/declined remain non-fulfillment.
- Pending/asynchronous statuses stay pending until confirmed by webhook or retrieve.

## Refunds Voids And Subscriptions

- Authorize flows can be captured or voided according to Tap docs and payment-method support.
- Recurring and saved-card flows require payment agreement/customer/card ids; keep those server-side and scoped.
- Refunds must use backend APIs and local refund idempotency.

## Sandbox And Test Notes

- Use Tap test keys/environment and configured webhook endpoints.
- Test authorize/capture/void paths separately from direct charge.

## Unknowns And Do Not Invent

- Do not invent supported local methods, capture window, or status names.
- Do not reuse one `hashstring` field set for every object type.
- Ask for current Tap merchant docs when the account uses custom/local payment methods.

## Agent Checklist

- Choose Charge vs Authorize intentionally.
- Keep secret keys backend-only.
- Verify webhook or retrieve status server-side.
- Compare reference, amount, and currency.
- Separate authorized from captured/paid.

## Fail If

- You treat `AUTHORIZED` as fulfilled.
- You trust redirect status without server confirmation.
- You skip `hashstring` verification or reuse the wrong operation field set.
- You capture/void a payment method that does not support authorization.
