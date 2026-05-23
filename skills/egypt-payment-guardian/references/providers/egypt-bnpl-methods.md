# Egypt BNPL Methods

- Provider: valU and Souhoola as Egypt BNPL payment methods.
- Scope: PSP-routed BNPL/installment methods, primarily through Geidea and other enabled PSP integrations.
- Priority: P1
- Readiness: B for method-level guidance; not a direct-provider API reference in V1.
- Public docs status: PSP-routed public docs; direct merchant API docs not confirmed in V1.
- Last checked: 2026-05-23
- Source confidence: Medium. Geidea docs provide public PSP-routed valU/Souhoola method coverage; direct provider API details require separate official sources.
- Sources:
  - https://docs.geidea.net/docs/buy-now-pay-later-bnpl
  - https://docs.geidea.net/docs/valu
  - https://docs.geidea.net/docs/souhoola
  - https://easykash.gitbook.io/easykash-apis-documentation/direct-payment-hosted/pay-api

## Use When

Use when an Egypt PSP integration exposes valU, Souhoola, or similar BNPL/installment methods as checkout options, payment link options, Direct API method options, or merchant-dashboard enabled payment methods.

## Source Map

- Geidea BNPL overview explains BNPL as a payment method family handled through the PSP checkout flow.
- Geidea valU and Souhoola docs cover method-specific PSP-routed setup and behavior.
- EasyKash Pay API publicly lists valU and Souhoola-like payment option codes when enabled on the EasyKash merchant account.
- This file intentionally does not define direct valU or direct Souhoola API endpoints.

## Integration Paths

- PSP-hosted checkout method option.
- PSP payment link method option.
- PSP Direct API method option where explicitly documented.
- Merchant dashboard enablement through the routing PSP.
- Provider-specific direct API only if official direct merchant docs are provided later.

## Setup Prerequisites

- Identify the routing PSP first: Geidea, EasyKash, Kashier, Paymob, PayTabs, or another merchant-enabled PSP.
- Confirm BNPL method is enabled for the merchant account.
- Confirm eligible currency, amount, installment terms, customer data fields, and item/order details from the routing PSP docs.
- Store local order amount, currency, line items, customer reference, PSP reference, and BNPL method name.

## Auth And Secret Boundary

Use the routing PSP credentials and secret boundary. Do not invent direct valU or Souhoola credentials unless official direct API docs are provided. BNPL-specific eligibility or financing details must stay within the routing PSP or direct official provider contract.

## Callback Or Webhook Contract

The routing PSP owns the callback/webhook contract. Verify the PSP callback signature/HMAC/SecureHash, amount, currency, local order reference, PSP transaction reference, and final paid status before fulfillment. BNPL approval screens, eligibility checks, and installment selection UI are not paid-state proof.

## Signature Or HMAC

Use the routing PSP signature logic:

- Geidea: operation-specific HMAC SHA-256 Base64 signatures and callback verification.
- EasyKash: callback HMAC SHA-512 with documented field order.
- Paymob: Paymob transaction callback HMAC SHA-512.
- PaySky: SecureHash if PaySky routes a BNPL-like method.
- Kashier: official merchant docs or demo/plugin source only.

Do not invent a BNPL-specific signing algorithm.

## Idempotency Keys

Use local order ID, PSP order/transaction reference, PSP payment attempt ID, BNPL method name, and any BNPL provider reference returned inside the verified PSP payload. Idempotency belongs to the PSP callback plus local order transition, not the BNPL UI event.

## Amount And Currency

BNPL methods often have eligibility, amount range, currency, customer, phone, national ID, item detail, and installment-term constraints. Enforce only constraints documented by the routing PSP or direct official provider docs. Reject callbacks whose final amount/currency differ from the local order.

## Status Mapping

- Local `eligible`: customer/method appears eligible, not paid.
- Local `pending`: BNPL flow started or approval pending.
- Local `paid`: routing PSP verified callback confirms paid/success with amount/currency/reference match.
- Local `failed`: routing PSP verified failure/decline.
- Local `cancelled`: verified cancellation.
- Local `expired`: verified expiry.
- Local `refunded`: routing PSP refund flow confirms refund.

Keep BNPL eligibility and approval separate from paid fulfillment.

## Refunds Voids And Subscriptions

Use the routing PSP refund/void/cancel behavior unless direct official BNPL docs are available. BNPL refunds and settlement can have provider-specific rules; do not invent them. Subscriptions or recurring BNPL need direct official docs before implementation.

## Sandbox And Test Notes

BNPL availability usually depends on merchant enablement and test account setup. Test method hidden/disabled cases, eligibility failure, customer cancellation, approved-but-not-paid state, callback amount mismatch, duplicate callback, refund, and fallback when the method is not available for the order.

## Unknowns And Do Not Invent

- Do not treat valU or Souhoola as standalone direct API providers in V1.
- Do not invent eligibility endpoints, refund endpoints, settlement timing, or signature rules.
- Do not fulfill from BNPL approval screens without PSP backend confirmation.
- Do not assume every PSP exposes the same BNPL fields.

## Agent Checklist

- Identify and load the routing PSP reference first.
- Confirm merchant method enablement and constraints.
- Keep PSP secrets server-side.
- Verify routing PSP callback signature.
- Compare amount, currency, PSP reference, local order reference, and method.
- Keep eligibility/approval separate from paid.
- Ask for direct official docs if the user wants direct valU or Souhoola APIs.

## Fail If

- The agent invents direct valU or Souhoola APIs.
- The agent fulfills from BNPL eligibility, installment selection, or approval UI alone.
- The agent skips the routing PSP callback signature check.
- The agent ignores BNPL amount/currency/customer constraints documented by the PSP.
- The agent treats PSP-routed refund behavior as direct BNPL settlement rules without sources.
