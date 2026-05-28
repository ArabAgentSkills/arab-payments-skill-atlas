# Geidea

- Provider: Geidea
- Scope: Saudi Arabia / Egypt / UAE PSP with hosted checkout, Pay API, Pay by Link, callbacks, direct operations, refunds, cancel, void, capture, and BNPL method support.
- Priority: P0
- Readiness: A
- Public docs status: public
- Last checked: 2026-05-29
- Source confidence: High for official Geidea docs.
- Sources: Geidea docs home, overview, Checkout v2, Pay v2, sample callback responses, Pay by Link APIs, refund, cancel order, void, capture transaction, and official Geidea `llms.txt` index.

## Use When

Use for Geidea hosted checkout, direct Pay API, Pay by Link, callbacks, valU/Souhoola routing, and Geidea back-office payment operations.

## Source Map

- Docs home: `https://docs.geidea.net/`
- Checkout v2: `https://docs.geidea.net/docs/geidea-checkout-v2`
- Pay v2: `https://docs.geidea.net/docs/pay-v2`
- Callbacks: `https://docs.geidea.net/docs/sample-callback-responses`
- Refund/cancel/void/capture docs under official Geidea docs.
- Agent-readable docs: `https://docs.geidea.net/llms.txt`

## Integration Paths

- Geidea Checkout for hosted payment pages.
- Pay API/direct APIs where merchant PCI and account setup permit.
- Pay by Link for payment-link flows.
- BNPL methods through enabled Geidea payment methods.

## Setup Prerequisites

- Merchant public key/API password or equivalent credentials, country endpoint, merchant account configuration, callback URL, payment method enablement, and sandbox/live separation.
- Egypt integrations should load `egypt-payment-guardian` for Egypt endpoint, currency, signature, callback, and BNPL specifics.

## Auth And Secret Boundary

- Keep API password/secret credentials and signature material server-side.
- Public keys and session ids may be client-visible only where Geidea docs say so.

## Callback Or Webhook Contract

- Verify Geidea callback authenticity and compare order, amount, currency, and payment operation fields.
- Use callback as server-side signal; redirects are UX only.
- Store Geidea order id/payment id, merchant order reference, transaction id, status, and operation type.

## Signature Or HMAC

- Geidea operation signatures are field-order specific. Use the exact documented operation signature rules for the API/callback type in use.
- Do not reuse checkout signature rules for refund/cancel/capture unless the docs say the field list is identical.

## Idempotency Keys

- Use merchant order reference plus Geidea order/payment/transaction id.
- Back-office operations should use local operation ids and provider operation ids to avoid repeated capture/refund/cancel.

## Amount And Currency

- Compare decimal amount and ISO currency exactly.
- Reject fulfillment or capture/refund updates when provider amount/currency differs from local order.

## Status Mapping

- Map successful payment/capture only after signature verification.
- Keep authorization, captured, refunded, cancelled, voided, failed, and pending as distinct states.
- Never let a late failed callback overwrite a previously verified paid/captured state.

## Refunds Voids And Subscriptions

- Refund, cancel order, void, and capture are separate Geidea operations with different allowed states.
- Capture applies to authorized payments; cancel/void/refund semantics depend on current provider state.
- Subscription-related work should be implemented only from current official docs and merchant enablement.

## Sandbox And Test Notes

- Use Geidea sandbox/test environment and country endpoint.
- Test invalid signature, amount mismatch, duplicate callback, and refund/cancel/capture state mistakes.

## Unknowns And Do Not Invent

- Do not invent country endpoint, signature fields, BNPL method parameters, or operation status names.
- Ask for merchant docs when the account has custom payment methods or local acquirer settings.
- Fetch the current Geidea `llms.txt` index before endpoint-level or signature work, then keep Egypt-specific findings in the Egypt skill.

## Agent Checklist

- Confirm country endpoint and integration path.
- Keep credentials server-side.
- Verify signature.
- Compare order id, amount, currency, and status.
- Keep operation states separate.

## Fail If

- You fulfill on redirect alone.
- You skip callback signature validation.
- You capture a non-authorized transaction.
- You refund/void/cancel from the wrong state.
