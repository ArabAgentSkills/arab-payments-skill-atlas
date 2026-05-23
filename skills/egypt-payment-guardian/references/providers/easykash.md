# EasyKash

- Provider: EasyKash
- Scope: Egypt Direct Payment Hosted, Pay API, callback service, HMAC verification, payment inquiry, Cash API, plugins, and enabled local payment methods.
- Priority: P2 in seed workbook; promoted to documented V1 provider after public GitBook docs were found.
- Readiness: A for documented Direct Payment and Cash API; account-level method enablement remains merchant-specific.
- Public docs status: public GitBook.
- Last checked: 2026-05-23
- Source confidence: High for Pay API, callback verification, inquiry statuses, amount/currency notes, and cash/direct payment surfaces.
- Sources:
  - https://easykash.gitbook.io/easykash-apis-documentation/
  - https://easykash.gitbook.io/easykash-apis-documentation/direct-payment-hosted/pay-api
  - https://easykash.gitbook.io/easykash-apis-documentation/direct-payment-hosted/callback-service
  - https://easykash.gitbook.io/easykash-apis-documentation/direct-payment-hosted/callback-service/callback-response-verification
  - https://easykash.gitbook.io/easykash-apis-documentation/direct-payment-hosted/payment-inquiry
  - https://easykash.gitbook.io/easykash-apis-documentation/cash-api-cash-only

## Use When

Use for EasyKash direct hosted payment links, cards, wallets, Meeza, Fawry/Aman cash, direct pay callbacks, payment inquiry, Cash API, and enabled installment or BNPL options such as valU/Souhoola when exposed by the merchant's EasyKash account.

## Source Map

- Pay API docs cover direct payment link creation, request fields, amount/currency behavior, redirect behavior, and payment option codes.
- Callback Service docs cover payment-result payloads sent to the merchant.
- Callback response verification docs define HMAC SHA-512 verification and exact field order.
- Payment Inquiry docs provide a server-side fallback and documented statuses.
- Cash API docs cover cash-only payment creation and voucher/reference behavior.

## Integration Paths

- Direct Payment Hosted Pay API creates a direct pay link.
- Buyer is redirected to EasyKash Direct Payment screen and then back to the merchant `redirectUrl`.
- Callback Service sends detailed payment data to the configured merchant callback URL.
- Payment Inquiry checks a transaction by `customerReference`.
- Cash API creates cash-only payments and voucher/reference flows.
- WooCommerce and Shopify plugin paths exist for platform integrations.

## Setup Prerequisites

- EasyKash business account with the required products enabled.
- API key from Integration Settings stored only on the server.
- HMAC secret from Integration Settings stored only on the server.
- Callback URL configured and reachable.
- Local `customerReference` created before Pay API call.
- Local order stores expected amount, currency, customer reference, payment options requested, and EasyKash reference when available.
- Payment options are checked against account enablement before presenting them.

## Auth And Secret Boundary

The Pay API and inquiry API use an API key in the request authorization header. The HMAC secret verifies callbacks. Both are server-side secrets. Do not place API key, HMAC secret, callback verifier code with embedded secrets, or merchant settings in frontend code, public mobile config, logs, screenshots, or GitHub.

## Callback Or Webhook Contract

The redirect back to `redirectUrl` includes basic parameters such as status, provider reference, customer reference, and voucher for cash methods. EasyKash docs say these redirect parameters can be used to display custom messages. They must not be used as fulfillment proof.

For detailed payment information, use the Callback Service or Payment Inquiry. The callback service sends payment details such as product code, amount, payment method, status, EasyKash reference, customer reference, and `signatureHash`. Treat callback payloads as untrusted until HMAC is verified.

## Signature Or HMAC

Callbacks use HMAC SHA-512 with the EasyKash HMAC secret. Concatenate the callback values in this exact documented order, then compare the hex digest to `signatureHash` with timing-safe comparison where available:

1. `ProductCode`
2. `Amount`
3. `ProductType`
4. `PaymentMethod`
5. `status`
6. `easykashRef`
7. `customerReference`

Do not include unrelated fields such as buyer name, voucher, or email in the HMAC input unless the official docs change.

## Idempotency Keys

Use local order ID, `customerReference`, `easykashRef`, provider reference number from redirect, payment method, and callback status. Add uniqueness on `customerReference` and `easykashRef` where possible. Cash voucher/reference creation is not paid proof.

## Amount And Currency

Pay API docs state `amount` is the base amount in the submitted currency and not necessarily EGP; the end user is charged in EGP using the exchange rate at payment time. Available currencies in docs include EGP, USD, SAR, EUR, GBP, QAR, and AED. Store the original amount/currency and compare callback/inquiry values to the local order. For cash-only flows, verify EGP and provider constraints from the Cash API page.

## Status Mapping

- Local `pending`: Pay API link created, redirect returned `pending`, voucher generated, inquiry `NEW`, or callback missing.
- Local `paid`: verified callback status `PAID` or inquiry status `PAID` with matching amount/reference.
- Local `failed`: inquiry `FAILED` or redirect failed plus confirmed inquiry/callback failure.
- Local `expired`: inquiry `EXPIRED`.
- Local `refunded`: inquiry `REFUNDED`.
- Local `cancelled`: inquiry `CANCELED`.
- Local `delivered`: inquiry `DELIVERED` is not automatically a new paid transition; map according to the product and local business flow after payment is already reconciled.

## Refunds Voids And Subscriptions

Public inquiry docs include `REFUNDED` and product docs mention subscriptions as a product type, but endpoint-level refund, void, and subscription management APIs need current official docs or merchant docs before implementation. Do not invent refund or subscription endpoints.

## Sandbox And Test Notes

Direct Payment and Cash API features must be enabled for the EasyKash business account. Test Pay API creation, redirect `success`/`pending`/`failed`, callback HMAC failure, inquiry fallback, delayed callback, duplicate callback, voucher-only cash flow, status mapping, and disabled payment options. Do not commit Integration Settings values.

## Unknowns And Do Not Invent

- Do not mark paid from redirect parameters.
- Do not treat voucher generation as paid.
- Do not invent refund, void, or subscription management endpoints.
- Do not assume every payment option code is enabled for every merchant.
- Do not assume final EGP charged amount without reconciling the callback/inquiry and local order.

## Agent Checklist

- Create direct pay link server-side.
- Persist local `customerReference` before sending the buyer to EasyKash.
- Keep API key and HMAC secret on the server.
- Verify callback HMAC with the documented field order.
- Use Payment Inquiry when callback is delayed, missing, or disputed.
- Compare amount, currency, customer reference, EasyKash reference, and status.
- Process duplicate callbacks idempotently.
- Show processing/pending on redirect until verified.

## Fail If

- The agent fulfills from redirect `success`, `pending`, or voucher values alone.
- The agent skips HMAC SHA-512 verification.
- The agent uses a different HMAC field order without official docs.
- The agent exposes API key or HMAC secret to frontend code.
- The agent accepts amount/currency/reference mismatch.
- The agent invents refund/subscription/cash endpoints not present in official docs.
