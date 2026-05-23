# Amazon Payment Services

- Provider: Amazon Payment Services
- Scope: MENA PSP formerly PayFort, with Hosted Checkout, custom integration, mobile SDKs, transaction feedback, notification feedback, signature credentials, capture, refund, void/release style operations, installments, and local methods where enabled.
- Priority: P1
- Readiness: A
- Public docs status: public
- Last checked: 2026-05-24
- Source confidence: High for official Amazon Payment Services docs; merchant account configuration controls exact enabled channels.
- Sources: Amazon Payment Services docs home, webhooks, capturing payment, API FAQ.

## Use When

Use for APS/PayFort Hosted Checkout, custom integration, webhook/notification feedback, SHA signature validation, capture, refund, installments, and MENA local payment method integrations.

## Source Map

- Docs: `https://paymentservices.amazon.com/docs/`
- Webhooks: `https://paymentservices.amazon.com/docs/managing-payments/tracking-a-payment/webhooks`
- Capture: `https://paymentservices.amazon.com/docs/managing-payments/capturing-payment`
- FAQ: `https://paymentservices.amazon.com/docs/api/faqs/faq`

## Integration Paths

- Hosted Checkout and custom integration.
- Mobile SDKs and plugins.
- Backend APIs for capture and other managing-payment operations.

## Setup Prerequisites

- Merchant identifier, access code, SHA request phrase, SHA response phrase, channel configuration, Direct Transaction Feedback URL, Notification URL, Return URL, and sandbox/live endpoints.
- URLs must meet APS HTTPS/domain requirements for webhooks and return handling.

## Auth And Secret Boundary

- Keep access code, merchant identifier when sensitive in your architecture, SHA request/response phrases, and API credentials server-side.
- Frontend must not calculate APS signatures or hold SHA phrases.

## Callback Or Webhook Contract

- APS has transaction feedback for immediate payment results and notification feedback for post-payment updates such as capture, refund, and delayed status changes.
- Return URL is a customer flow endpoint and must not be the only fulfillment signal.
- Store merchant reference, Fort ID, command, amount, currency, response code/message, and signature verification status.

## Signature Or HMAC

- Requests and responses use APS signature calculation with configured SHA phrases.
- Verify response/feedback signature before mapping status.
- Do not send capture/refund API calls without correctly calculated backend signature.

## Idempotency Keys

- Use merchant reference plus Fort ID and command/operation id.
- Deduplicate notification feedback and operation responses.

## Amount And Currency

- Compare APS amount and currency to the original merchant reference.
- For capture, merchant reference must match the original authorization and capture amount cannot exceed authorized amount.

## Status Mapping

- Map APS response codes/messages only through official docs and merchant configuration.
- Treat authorized, captured, refunded, voided/released, failed, and pending as distinct states.
- Delayed notification feedback must not create duplicate fulfillment.

## Refunds Voids And Subscriptions

- Capture is used after authorization and must be performed within the allowed timeframe for the payment method/acquirer.
- Refund and other managing-payment operations must be backend-only and signature-verified.
- Installments and tokenization require account enablement and dedicated docs.

## Sandbox And Test Notes

- Use sandbox endpoints and separate SHA phrases.
- Test Direct Transaction Feedback and Notification URL independently.

## Unknowns And Do Not Invent

- Do not invent response code meanings, local method fields, SHA phrase values, or account channel settings.
- Ask for current APS merchant docs when PayFort legacy terminology differs from current APS pages.

## Agent Checklist

- Configure feedback and notification URLs.
- Calculate request signature server-side.
- Verify response signature.
- Compare merchant reference, Fort ID, amount, and currency.
- Fulfill from verified server state only.

## Fail If

- You trust return URL alone.
- You expose SHA phrases or access credentials.
- You skip signature verification.
- You capture more than authorized.
