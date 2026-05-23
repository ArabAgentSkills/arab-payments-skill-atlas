# Paymob

- Provider: Paymob
- Scope: Egypt hosted checkout, embedded checkout, payment intentions, no-code links, plugins, local methods, callbacks, refunds, voids, captures, and token events.
- Priority: P0
- Readiness: A
- Public docs status: public docs; automated fetches may require JavaScript verification.
- Last checked: 2026-05-23
- Source confidence: High for public documentation, transaction HMAC field order supplied from public Paymob docs, and card-token HMAC checklist; re-check endpoint request/response details before coding.
- Sources:
  - https://developers.paymob.com/paymob-docs/getting-started/overview.md
  - https://developers.paymob.com/paymob-docs/getting-started/integration-checklist.md
  - https://developers.paymob.com/paymob-docs/integration-paths/apis.md
  - https://developers.paymob.com/paymob-docs/integration-paths/no-code/payment-links.md
  - https://developers.paymob.com/paymob-docs/integration-paths/plugins.md
  - https://developers.paymob.com/paymob-docs/payments-and-features/payment-methods.md
  - https://developers.paymob.com/paymob-docs/payments-and-features/core-features.md
  - https://developers.paymob.com/paymob-docs/payments-and-features/managing-payments.md
  - https://developers.paymob.com/paymob-docs/payments-and-features/managing-payments/refund.md
  - https://developers.paymob.com/paymob-docs/payments-and-features/managing-payments/void.md
  - https://developers.paymob.com/paymob-docs/payments-and-features/managing-payments/capture.md
  - https://developers.paymob.com/paymob-docs/developers/webhook-callbacks-and-hmac/overview.md
  - https://developers.paymob.com/paymob-docs/developers/webhook-callbacks-and-hmac/transaction-callbacks.md
  - https://developers.paymob.com/paymob-docs/developers/webhook-callbacks-and-hmac/hmac/hmac-transaction-callback.md
  - https://developers.paymob.com/paymob-docs/developers/webhook-callbacks-and-hmac/hmac/hmac-for-card-tokens.md
  - https://developers.paymob.com/paymob-docs/developers/webhook-callbacks-and-hmac/webhook-testing-tool.md

## Use When

Use for Paymob Egypt or regional Paymob flows involving hosted checkout, embedded checkout, payment intentions, Paymob payment links, plugins, cards, mobile wallets, BNPL/installments, kiosk, bank installments, token callbacks, transaction callbacks, and payment management.

## Source Map

- Getting started and checklist docs explain onboarding, dashboard configuration, and integration readiness.
- API integration docs cover custom integration paths and should be consulted before implementing payment creation.
- Payment method docs cover region-specific method availability such as cards, wallets, BNPL, installments, and kiosk.
- Managing payment docs cover refund, void, and capture behavior.
- Webhook/callback and HMAC docs cover server result handling, HMAC verification, card-token callback signing, and the webhook testing tool.
- Paymob markdown pages are public, but simple HTTP fetches can receive a JavaScript verification page. Treat that as `JS_CHALLENGE`, not as proof the docs are private or broken.

## Integration Paths

- Hosted/unified checkout from a backend-created payment intention or equivalent official API flow.
- Embedded checkout or Pixel flow initialized from backend-created payment data.
- Mobile SDK checkout initialized by backend-created payment data.
- No-code payment links when a merchant does not need custom checkout.
- Plugins for WordPress, Shopify, Odoo, OpenCart, PrestaShop, WHMCS, CS-Cart, Zen Cart, Joomla, Bagisto, osCommerce, Drupal, and StaaH.
- Payment management APIs for refunds, voids, captures, and transaction inquiry where documented.

## Setup Prerequisites

- Merchant account and dashboard access.
- Active test and live environments separated.
- Correct country/region, currency, and payment method enablement.
- API credentials and integration identifiers configured server-side.
- HMAC secret available to the backend callback verifier.
- Backend callback endpoints reachable over HTTPS where Paymob requires it.
- Local order table has expected amount, currency, provider, order reference, and payment attempt ID before checkout is created.

## Auth And Secret Boundary

Create payment intentions, transaction management requests, refunds, voids, captures, and token operations on the server. HMAC secrets, API keys, integration credentials, and merchant secrets never go to browser code, mobile public bundles, logs, screenshots, or GitHub.

Frontend code may receive only official public checkout initialization values needed to render or redirect to Paymob checkout. It must not receive raw merchant secrets or HMAC material.

## Callback Or Webhook Contract

Paymob can redirect the buyer back to the merchant and also send backend callbacks. The redirect is a UX event only. The local paid state must come from a server-side callback/webhook or trusted server-side inquiry after HMAC verification and order reconciliation.

For transaction callbacks:

- Processed callbacks are POST callbacks with data received as a JSON object.
- Response callbacks are GET callbacks with data received as query parameters.
- Compare Paymob order/transaction identifiers to the local payment attempt.
- Confirm `success`, `pending`, refund, void, capture, and parent transaction flags before changing local state.

## Signature Or HMAC

Transaction callback HMAC uses SHA-512 with the merchant HMAC secret. Build the HMAC input by concatenating values in this exact field order from the Paymob transaction HMAC docs:

1. `amount_cents`
2. `created_at`
3. `currency`
4. `error_occured`
5. `has_parent_transaction`
6. `obj.id` for Processed POST callbacks, or `id` for Response GET callbacks
7. `integration_id`
8. `is_3d_secure`
9. `is_auth`
10. `is_capture`
11. `is_refunded`
12. `is_standalone_payment`
13. `is_voided`
14. `order.id` for Processed POST callbacks, or `order_id` for Response GET callbacks
15. `owner`
16. `pending`
17. `source_data.pan`
18. `source_data.sub_type`
19. `source_data.type`
20. `success`

Compare the calculated HMAC to the received `hmac` query parameter with a timing-safe comparison where available.

Card-token callback HMAC has a different field list. Use the Paymob card-token docs and concatenate:

1. `card_subtype`
2. `created_at`
3. `email`
4. `id`
5. `masked_pan`
6. `merchant_id`
7. `order_id`
8. `token`

Do not reuse the transaction HMAC list for token callbacks or the token callback list for transactions.

## Idempotency Keys

Use local order ID, local payment attempt ID, Paymob intention/order ID, Paymob transaction ID, integration ID, and event/callback type. Enforce uniqueness so duplicate callbacks, retries, redirects, refreshes, and status polls cannot create more than one paid transition.

## Amount And Currency

Paymob legacy flows commonly expose `amount_cents`; newer intention flows must be checked against the current API docs before coding. Store the expected amount in the exact unit the selected endpoint uses, plus a normalized minor-unit value for internal comparison. Reject callbacks when amount, currency, integration ID, or local order reference does not match.

## Status Mapping

- Local `paid`: HMAC verified, amount/currency/reference match, `success` is true, and `pending` is false.
- Local `pending`: checkout created, redirect returned, callback pending, or Paymob marks the transaction pending.
- Local `failed`: verified callback says not successful and not pending.
- Local `voided`: verified callback or management API confirms void.
- Local `refunded` or `partially_refunded`: verified refund event/response confirms refund state.
- Local `authorized`: authorization-only or auth/capture flow is confirmed but capture has not happened.
- Never downgrade paid from a later redirect, duplicate failed callback, stale browser status, or unverified event.

## Refunds Voids And Subscriptions

Use Paymob managing payment docs for refund, void, and capture. Treat refunds, voids, and captures as separate operations with their own audit records and idempotency keys. For auth/capture, do not fulfill as captured unless capture is confirmed by the documented Paymob flow. For saved cards and subscriptions, use the token callback HMAC rules and keep tokens server-side.

## Sandbox And Test Notes

Use test credentials and Paymob webhook testing tools during development. Exercise success, failure, pending, delayed callback, duplicate callback, refund, void, capture, mobile wallet, kiosk, and token callback cases. Do not commit dashboard screenshots, merchant IDs, HMAC secrets, or sample private credentials.

## Unknowns And Do Not Invent

- Do not invent endpoint fields when the selected API page is unavailable through automated fetch.
- Do not treat a JavaScript verification page as evidence that Paymob docs are blocked or private.
- Do not assume old Accept API behavior matches newer intention APIs.
- Do not invent payment method availability for a merchant account.
- Do not infer refund/capture/void support without the current official page or merchant dashboard enablement.

## Agent Checklist

- Load this file before implementing Paymob.
- Confirm the exact Paymob integration path: API, plugin, payment link, checkout, embedded, SDK, or management operation.
- Keep all credentials and HMAC secrets server-side.
- Create and persist a local payment attempt before redirecting or rendering checkout.
- Verify transaction HMAC or token HMAC with the correct field list.
- Compare amount, currency, local order reference, Paymob order/intention ID, and transaction ID.
- Process callbacks idempotently.
- Fulfill only from verified server state.
- Add tests for delayed callback, duplicate event, bad HMAC, amount mismatch, currency mismatch, refund, void, and stale failure after paid.

## Fail If

- The agent fulfills from browser redirect, checkout success screen, SDK callback, or query parameters alone.
- The agent skips Paymob HMAC verification.
- The agent uses the card-token HMAC field list for transaction callbacks or the transaction list for token callbacks.
- The agent exposes API keys, HMAC secrets, integration secrets, or merchant credentials to frontend code.
- The agent accepts amount/currency/reference mismatch.
- The agent marks a duplicate callback as a second payment.
- The agent overwrites a confirmed paid state from a stale failed or pending event.
