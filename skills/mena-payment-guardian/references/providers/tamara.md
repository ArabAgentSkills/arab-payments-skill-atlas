# Tamara

- Provider: Tamara
- Scope: Saudi Arabia / GCC BNPL with online checkout sessions, webhook registration, approved-to-authorised acknowledgment, capture, cancel, simplified refund, and order status inquiry.
- Priority: P0
- Readiness: A
- Public docs status: public
- Last checked: 2026-08-17
- Source confidence: High for official Tamara docs.
- Sources: Tamara docs home, online checkout, webhook registration, authorise order guide/API, order status flow, capture order, simplified refund, get order details, and official Tamara `llms.txt` index.

## Use When

Use for Tamara online checkout, BNPL approval/authorisation/capture lifecycle, webhook registration, capture, cancel, refund, and order status inquiry.

## Source Map

- Docs: `https://docs.tamara.co/`
- Online checkout: `https://docs.tamara.co/docs/direct-online-checkout`
- Webhook registration: `https://docs.tamara.co/docs/webhook-subscription`
- Authorise order guide: `https://docs.tamara.co/docs/pp-order-mgmt-authorise-order`
- Authorise order API: `https://docs.tamara.co/reference/authoriseorder`
- Status flow: `https://docs.tamara.co/docs/online-order-status-flow`
- Capture: `https://docs.tamara.co/reference/captureorder`
- Get order details: `https://docs.tamara.co/reference/getorderdetails`
- Agent-readable docs: `https://docs.tamara.co/llms.txt`

## Integration Paths

- Create checkout session server-side, redirect to Tamara checkout URL, receive approved notification, call Authorise Order unless documented auto-authorisation is explicitly enabled for the merchant, then capture when shipped/fulfilled.
- Current Tamara capture docs say orders not captured within 21 days from authorisation are auto-captured to `fully_captured`; design merchant fulfillment and reconciliation so manual capture is not left open indefinitely.
- Cancel is available before capture in the authorized stage.
- Simplified refund applies after capture.

## Setup Prerequisites

- API bearer credential, sandbox/live environment, webhook URL in Partner Portal or API, checkout URLs, country/currency support, order reference strategy, and merchant account settings for auto-authorisation and auto-capture behavior.
- Approved/status webhook handling is required for the documented authorise flow unless merchant-specific auto-authorisation has been confirmed in current docs/account settings.

## Auth And Secret Boundary

- Keep bearer credentials and webhook validation tokens server-side.
- Frontend receives checkout URL and safe order ids only.

## Callback Or Webhook Contract

- Tamara sends notifications to the merchant webhook URL; an approved notification must be acknowledged by calling Authorise Order unless documented auto-authorisation is explicitly enabled.
- Docs note server-to-server notification helps avoid frontend redirection failures.
- If auto-authorisation is enabled, current status-flow docs describe the flow moving from new to approved to authorised without an explicit Authorise Order call; capture remains a separate fulfillment/settlement step unless current merchant-specific docs or account settings explicitly say otherwise.
- Store Tamara order id, checkout id, order reference, notification event, authorised state, capture state, and refund ids.

## Signature Or HMAC

- Tamara webhook registration/authorization flow includes `tamaraToken` query parameter and bearer authorization behavior in docs.
- Validate the webhook token/header according to current docs before calling Authorise Order or changing local state.

## Idempotency Keys

- Use merchant `order_reference_id`, Tamara `order_id`, capture id/reference, and refund id.
- Authorise/capture/refund should be stored as idempotent local operations so retries do not duplicate state.

## Amount And Currency

- Compare checkout total, item totals, capture amount, refund amount, country, and currency.
- Do not capture or refund amounts inconsistent with local fulfillment/refund records.

## Status Mapping

- `approved` is not enough for the standard flow; merchant must authorise, which moves order to `authorised`, unless confirmed auto-authorisation moves the order to `authorised` automatically.
- Capture moves toward `partially_captured` or `fully_captured`.
- Cancel is valid only from the authorized stage; refunds apply after capture.
- Declined and expired orders are non-fulfillment states. Current status-flow docs also state an order can expire if it is not authorised within 72 hours or if an authorised order is not captured or canceled within 90 days.

## Refunds Voids And Subscriptions

- Cancel is for authorized but not captured orders.
- Capture is required for settlement; current Tamara capture docs say non-captured authorised orders are auto-captured after 21 days from authorisation when that behavior applies.
- Simplified refund can be full or partial after capture, with refund ids stored locally.
- No subscription behavior should be invented.

## Sandbox And Test Notes

- Test missing frontend redirect, approved webhook, authorise call, confirmed auto-authorisation path, capture before the 21-day auto-capture window, cancel-before-capture, refund-after-capture, and Get Order Details fallback.

## Unknowns And Do Not Invent

- Do not invent webhook token validation, auto-authorisation enablement, auto-authorisation-to-capture behavior, auto-capture account behavior, status names, country/currency availability, capture windows beyond current Tamara capture docs, or refund limits.
- Ask for merchant docs when integrating through a PSP wrapper instead of direct Tamara.
- Fetch the current Tamara `llms.txt` index before endpoint-level checkout, authorisation, capture, refund, or webhook work.

## Agent Checklist

- Create checkout session server-side.
- Verify webhook token/header.
- Call Authorise Order after approved notification unless confirmed auto-authorisation applies.
- Capture only after fulfillment/shipment decision; do not rely on delayed auto-capture as the operational capture plan.
- Treat confirmed auto-authorisation as reaching `authorised`, not `fully_captured`, unless merchant-specific current docs prove capture is also automatic.
- Track the 21-day auto-capture window for authorised but uncaptured orders.
- Use Get Order Details fallback.
- Separate cancel from refund.

## Fail If

- You treat approved redirect as final paid.
- You skip Authorise Order without confirmed auto-authorisation.
- You treat auto-authorisation as immediate capture or settlement.
- You capture before authorization.
- You leave authorised orders unattended until auto-capture without a deliberate fulfillment and settlement policy.
- You cancel after capture instead of refunding.
