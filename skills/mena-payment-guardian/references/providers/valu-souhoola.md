# valU And Souhoola

- Provider: valU and Souhoola
- Scope: Egypt BNPL/consumer finance methods routed through PSPs, especially Geidea, with method-level guidance unless direct merchant API docs are provided.
- Priority: P1
- Readiness: B
- Public docs status: psp-routed
- Last checked: 2026-05-24
- Source confidence: Medium-high for PSP-routed Geidea docs; direct standalone merchant APIs are not documented here.
- Sources: Geidea BNPL overview, Geidea valU, Geidea Souhoola, EasyKash Pay API, Paymob BNPL payment methods.

## Use When

Use when valU or Souhoola appears as a payment method through Geidea, Paymob, EasyKash, or another PSP account, and the task is method routing, callback validation, or local BNPL state handling.

## Source Map

- Geidea BNPL: `https://docs.geidea.net/docs/buy-now-pay-later-bnpl`
- valU through Geidea: `https://docs.geidea.net/docs/valu`
- Souhoola through Geidea: `https://docs.geidea.net/docs/souhoola`
- EasyKash Pay API: `https://easykash.gitbook.io/easykash-apis-documentation/direct-payment-hosted/pay-api`
- Paymob BNPL methods: `https://developers.paymob.com/paymob-docs/payments-and-features/payment-methods/bnpls-egy-ksa-uae.md`

## Integration Paths

- PSP-routed BNPL method in a hosted checkout or direct PSP payment flow.
- Use the PSP's callback/signature/status rules as the authoritative payment contract.
- Direct valU/Souhoola APIs are not covered unless official merchant docs are supplied.

## Setup Prerequisites

- PSP account with valU/Souhoola enabled, method-specific eligibility configuration, callback URLs, and PSP credentials.
- Confirm settlement/capture behavior with the PSP and merchant agreement.

## Auth And Secret Boundary

- Keep PSP credentials and method secrets server-side.
- Do not expose PSP or BNPL merchant secrets in frontend code.

## Callback Or Webhook Contract

- Use the PSP callback/webhook contract, not a guessed standalone BNPL callback.
- For Geidea-routed methods, follow Geidea signature, amount, currency, and status validation.

## Signature Or HMAC

- Signature/HMAC/SecureHash rules come from the PSP path in use.
- Do not invent a valU or Souhoola direct signature algorithm from method pages.

## Idempotency Keys

- Use local order reference plus PSP transaction/payment/order id.
- Store BNPL method name and PSP payment method id for reconciliation.

## Amount And Currency

- Compare total financed amount, EGP currency, PSP amount, and local order total.
- BNPL installment display does not replace backend amount verification.

## Status Mapping

- Map statuses through the PSP provider reference.
- BNPL approval/eligibility screens do not equal paid/captured unless PSP callback/status says so.

## Refunds Voids And Subscriptions

- Refunds, voids, cancellations, and captures must follow the PSP route and merchant agreement.
- Installment cancellation/refund effects can be provider-specific; do not invent customer finance behavior.

## Sandbox And Test Notes

- Test method unavailable, rejected, approved-but-not-confirmed, duplicate callback, and refund/void if documented by the PSP.

## Unknowns And Do Not Invent

- Direct standalone valU/Souhoola endpoint docs, signature rules, and status enums are unknown in this public skill.
- Ask for official merchant docs before direct integration.

## Agent Checklist

- Identify the PSP route.
- Load the PSP provider file.
- Verify PSP callback/signature.
- Compare EGP amount and local reference.
- Keep method-level BNPL state separate from paid state.

## Fail If

- You implement a guessed direct valU/Souhoola API.
- You treat BNPL approval UI as paid.
- You skip the PSP provider signature/callback rules.
- You invent refund/cancellation finance behavior.
