# FawryPay

- Provider: FawryPay
- Scope: Egypt PSP with online checkout, SDKs, card tokenization, reference payment flows, server notifications, and payment status pull.
- Priority: P0
- Readiness: A
- Public docs status: public
- Last checked: 2026-05-24
- Source confidence: High for official staging developer docs.
- Sources: FawryPay introduction, payment notification, server notification v2, get payment status v2, server APIs, card tokenization overview.

## Use When

Use for FawryPay card/checkout flows, reference payments, merchant-account notification setup, payment status pull, and server notification handling.

## Source Map

- Introduction: `https://developer.fawrystaging.com/docs/introduction`
- Payment notification: `https://developer.fawrystaging.com/docs/card-tokens/payment-notifications/get-payment-notification`
- Server notification v2: `https://developer.fawrystaging.com/docs/card-tokens/payment-notifications/server-notification-v2`
- Status pull v2: `https://developer.fawrystaging.com/docs/card-tokens/payment-notifications/get-payment-status-v2`
- Server APIs overview: `https://developer.fawrystaging.com/docs/server-apis/server-apis-overview`

## Integration Paths

- Online checkout and server APIs.
- Card tokenization and SDK-backed flows where merchant account supports them.
- Reference payment flows with configured notification URL.

## Setup Prerequisites

- Merchant account, merchant code, secure key, configured notification/callback URL in the merchant setup, and sandbox/live credentials.
- Confirm whether notification URL is configured account-side for the chosen flow.

## Auth And Secret Boundary

- Keep merchant code, secure key, signature material, and API auth server-side.
- Browser code must not construct payment verification signatures or status pull signatures.

## Callback Or Webhook Contract

- For the documented notification flow, the notification URL is configured outside the per-order request flow. Do not invent per-order callback behavior.
- Use server notification as the primary signal; use status pull when notification is delayed, missing, or ambiguous.
- Store merchant reference, Fawry reference, order amount, order status, and notification timestamp.

## Signature Or HMAC

- Use FawryPay's documented signature/hash formula for payment requests, notifications, and status pull.
- Verify notification authenticity before mapping status.
- Reject requests where signature validation fails or the local reference does not match.

## Idempotency Keys

- Use merchant reference plus Fawry reference/payment reference.
- Record notification delivery attempts so retries do not create duplicate paid state.

## Amount And Currency

- Compare order amount and expected currency against the notification or status pull result.
- If an amount mismatch appears, keep local state pending/manual-review even when the provider status looks successful.

## Status Mapping

- Map Fawry success/paid status to local paid only after signature verification and amount/reference comparison.
- Failed/cancelled/expired remain non-fulfillment states.
- Pending remains pending and may trigger status pull fallback.

## Refunds Voids And Subscriptions

- Use only documented server APIs for reversal/refund behavior and verify current merchant capabilities.
- Card tokenization and recurring-like behaviors must keep tokens and merchant keys server-side.

## Sandbox And Test Notes

- Use Fawry staging docs and staging credentials for test flows.
- Test delayed notifications and status pull fallback.

## Unknowns And Do Not Invent

- Do not create per-order callback parameters unless the current official docs for that exact flow document them.
- Do not invent status names or signature field order from memory.

## Agent Checklist

- Confirm merchant-level notification setup.
- Generate requests server-side.
- Verify notification/status signatures.
- Compare merchant reference, Fawry reference, amount, and currency.
- Process notification retries idempotently.

## Fail If

- You rely on redirect alone.
- You invent per-order callback behavior.
- You skip signature verification on notification or status pull.
- You fulfill on pending or mismatched amount.
