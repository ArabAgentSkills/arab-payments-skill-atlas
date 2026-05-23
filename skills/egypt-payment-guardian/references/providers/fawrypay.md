# FawryPay

- Provider: FawryPay
- Scope: Egypt online checkout, pay-at-Fawry/reference payments, card tokenization, SDKs, server notifications, and status pull.
- Priority: P0
- Readiness: A
- Public docs status: public staging developer docs.
- Last checked: 2026-05-23
- Source confidence: High for notification, callback ownership, status pull, and documented signature formulas; verify the exact product endpoint before coding.
- Sources:
  - https://developer.fawrystaging.com/docs/introduction
  - https://developer.fawrystaging.com/docs/card-tokens/payment-notifications/get-payment-notification
  - https://developer.fawrystaging.com/docs/card-tokens/payment-notifications/server-notification-v2
  - https://developer.fawrystaging.com/docs/card-tokens/payment-notifications/get-payment-status-v2
  - https://developer.fawrystaging.com/docs/server-apis/server-apis-overview
  - https://developer.fawrystaging.com/docs/card-tokens/card-tokenization-overview

## Use When

Use for FawryPay Egypt web checkout, pay-at-Fawry reference payments, Aman/Fawry cash flows exposed by FawryPay, card tokenization, token payments, mobile SDK integrations, server notification callbacks, and payment-status reconciliation.

## Source Map

- Payment notification overview documents the push and pull status model.
- Server Notification V2 documents the preconfigured merchant endpoint, request fields, retry behavior, order statuses, and notification signature.
- Get Payment Status V2 documents the merchant-driven status pull fallback and request signature.
- Introduction and server API docs orient checkout/server-side integration choices.
- Card tokenization docs should be loaded when implementing saved-card or token payment flows.

## Integration Paths

- Hosted checkout or server API charge creation.
- Pay-at-Fawry/reference-number payments where the customer pays later at an outlet or channel.
- Card tokenization and token-based payments.
- Android and iOS SDK flows.
- Server Notification V2 push callback for status updates.
- Get Payment Status V2 pull API for delayed callback or reconciliation jobs.

## Setup Prerequisites

- Merchant account approved by FawryPay.
- Merchant code and secure key available only to backend services.
- Development and production callback notification URLs supplied during merchant onboarding.
- Payment methods and expiry rules enabled for the merchant account.
- Local merchant reference generated before sending the charge request.
- Local status table supports pending, paid, cancelled, expired, refunded, partially refunded, and failed.

## Auth And Secret Boundary

Merchant code, secure key, token payment credentials, and server API credentials stay server-side. Do not include secure key or signature-building material in browser HTML, mobile public bundles, logs, screenshots, or GitHub.

Raw card collection increases PCI scope. Prefer hosted/tokenized/SDK paths unless the merchant has confirmed PCI readiness for the exact flow.

## Callback Or Webhook Contract

FawryPay states the merchant callback URL is configured during merchant account setup and is not received with each order. Do not invent a per-order callback field for flows where the docs say the endpoint is preconfigured.

Server Notification V2 sends HTTP POST status updates to the preconfigured merchant endpoint. The merchant endpoint should return HTTP 200 so FawryPay marks the callback delivered; otherwise FawryPay retries according to its configuration. Treat generated reference numbers and redirect/browser messages as pending until a verified server notification or status pull confirms payment.

## Signature Or HMAC

FawryPay uses SHA-256 signatures. The formula depends on the endpoint:

- Server Notification V2 `messageSignature`: SHA-256 over `fawryRefNumber + merchantRefNumber + paymentAmount(two decimals) + orderAmount(two decimals) + orderStatus + paymentMethod + paymentReferenceNumber(if present) + secureKey`.
- Get Payment Status V2 request `signature`: SHA-256 over `merchantCode + merchantRefNumber + secureKey`.

Use the exact field spelling, decimal formatting, optional payment reference behavior, and endpoint documentation for the product being implemented. Invalid, missing, or mismatched signature means no fulfillment.

## Idempotency Keys

Use local order ID, `merchantRefNumber`, `fawryRefNumber`, `paymentRefrenceNumber` or documented payment reference field, and notification request ID. Add uniqueness on merchant reference and provider reference. Callback retries must not create duplicate paid state.

## Amount And Currency

Use decimal formatting required by the FawryPay endpoint. Compare `paymentAmount`, `orderAmount`, fees, and local expected amount before fulfillment. If the selected product supports only EGP or specific methods, enforce that in the local order and validation layer.

## Status Mapping

- Local `pending`: order created, reference issued, `NEW`, or callback/status pull not yet paid.
- Local `paid`: verified notification or status pull returns `PAID` with matching amount/reference.
- Local `cancelled`: verified `CANCELED`.
- Local `expired`: verified `EXPIRED`.
- Local `failed`: verified `FAILED` or payment failure code.
- Local `refunded`: verified `REFUNDED`.
- Local `partially_refunded`: verified `PARTIAL_REFUNDED`.
- Shipping or delivery statuses are business/order statuses, not payment authorization by themselves.

## Refunds Voids And Subscriptions

Tokenized cards can support saved-card or recurring-like use cases, but the exact token/refund/cancel endpoints must be loaded from the relevant FawryPay page before implementation. Refund events must update payment state explicitly and must not create a second paid transition.

## Sandbox And Test Notes

Fawry public developer docs are under staging domains. Use staging merchant credentials for development and production credentials only in production secret stores. Test callback retry, callback delivery acknowledgement, status pull, reference-number expiry, wrong signature, amount mismatch, duplicate notification, and refund states.

## Unknowns And Do Not Invent

- Do not add a per-order callback URL when the docs say callback URL is configured during account setup.
- Do not invent signature field order for a charge, token, refund, or SDK endpoint.
- Do not treat `NEW`, reference issued, voucher issued, redirect success, or customer screenshot as paid.
- Do not assume card tokenization means the merchant may store raw card data.
- Do not convert shipping or delivery status into payment status.

## Agent Checklist

- Identify the exact FawryPay product path before coding.
- Keep merchant code and secure key on the server.
- Store `merchantRefNumber` before creating the charge.
- Verify notification `messageSignature` or status-pull signature rules.
- Use status pull when callbacks are delayed, missing, or disputed.
- Compare amount, reference, and status.
- Process duplicate notifications idempotently.
- Add tests for preconfigured callback URL, status pull fallback, wrong signature, duplicate callback, and reference expiry.

## Fail If

- The agent invents a per-order callback URL for a flow documented as account-level callback configuration.
- The agent fulfills from generated reference number, redirect page, or browser result alone.
- The agent skips SHA-256 signature verification.
- The agent exposes secure key, merchant signature key, or token credentials to frontend code.
- The agent accepts amount/reference mismatch.
- The agent marks duplicate callback retries as new paid events.
