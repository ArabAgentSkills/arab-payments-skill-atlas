# Kashier

- Provider: Kashier
- Scope: Egypt hosted checkout, iframe/payment UI demos, official plugins, cards, wallets, installments, and callback signature review.
- Priority: P1
- Readiness: B for official demos/plugins; conservative for endpoint-level custom API work.
- Public docs status: partially public through official site and official GitHub; developer portal endpoint-level docs were not accessible in this crawl.
- Last checked: 2026-05-23
- Source confidence: Medium. Official demos/plugins are useful, but endpoint-level merchant docs are required for custom API and signature implementation.
- Sources:
  - https://www.kashier.io/
  - https://github.com/Kashier-payments
  - https://github.com/Kashier-payments/NodeJs-Checkout-Demo
  - https://github.com/Kashier-payments/Php-Checkout-Demo
  - https://github.com/Kashier-payments/Kashier-WooCommerce-UI-Plugin

## Use When

Use for Kashier Egypt checkout review, iframe or hosted payment UI integration, official Node/PHP demo review, WooCommerce/Odoo/plugin behavior, callback signature requirements, and conservative payment-flow safety checks when full merchant docs are not available.

## Source Map

- Kashier public site provides product-level capabilities and official brand/source ownership.
- Official GitHub organization provides demos and plugins that can be inspected for current public examples.
- Node.js and PHP checkout demos provide sample checkout structure and callback handling patterns.
- WooCommerce plugin source can help confirm plugin-level behavior.
- Endpoint URLs, signature formulas, and API contracts must come from official merchant docs, current portal docs, or official demo/plugin source, not memory or third-party snippets.

## Integration Paths

- Iframe or Payment UI checkout through official demo/plugin patterns.
- Hosted Payment Page redirect where documented by official sources.
- Official Node.js and PHP checkout demos.
- WooCommerce and other official plugin paths.
- Mobile SDKs, tokenization, subscriptions, refunds, and dashboard actions only where official docs or plugin source expose them clearly.

## Setup Prerequisites

- Kashier merchant account and portal access.
- Test and live credentials obtained from official merchant portal.
- Official docs or merchant docs for the exact integration path.
- Callback/return URLs configured according to official docs.
- Local order stores expected amount, currency, merchant order reference, provider transaction/reference, and checkout mode.
- If only demos are available, review the demo source before coding and document any remaining unknowns.

## Auth And Secret Boundary

Merchant ID, API key, secret key, hash/signature secret, and live/test credentials stay server-side or in secure plugin configuration. Do not expose secrets in frontend code, public mobile bundles, logs, screenshots, GitHub issues, or README examples.

Kashier public checkout identifiers may be used client-side only when official docs require them and they are explicitly non-secret.

## Callback Or Webhook Contract

Official demos mention callback handling for checkout completion. Treat callbacks/webhooks as mandatory server-side verification points. Redirect or iframe completion is UX only until callback signature, amount, currency, and reference are verified.

If a merchant doc or demo does not expose callback contract details, ask for the official merchant documentation rather than inventing payload fields.

## Signature Or HMAC

Official demo references indicate callbacks include signature material that must be verified. Do not invent the signature algorithm, field order, hash function, or endpoint. Implement signature verification only from official Kashier merchant docs or current official demo/plugin source.

If the signature cannot be verified from official sources, the agent must stop and request the merchant docs or choose an official plugin that already handles verification.

## Idempotency Keys

Use local order ID, local payment attempt ID, merchant order/reference, Kashier transaction/reference from the verified callback, and callback event type where available. Add uniqueness around provider references to prevent duplicate paid state.

## Amount And Currency

Kashier public materials mention EGP and other payment methods, but amount formatting and unit rules must be confirmed from merchant docs or official source for the chosen integration. Reject callbacks with amount/currency mismatch. Do not infer decimal/minor-unit handling from unrelated providers.

## Status Mapping

Map only documented statuses from the chosen official source. At minimum, keep pending/processing, paid/success, failed/declined, cancelled, refunded, and duplicate/ignored states separate when exposed. Unknown statuses should remain `pending_review` or `unmapped_provider_status` and should not fulfill.

## Refunds Voids And Subscriptions

Public product pages may mention subscriptions, dashboard, or plugin features. Custom refund, void, subscription, or tokenization work requires official merchant docs or direct review of official plugin source. Do not invent endpoint URLs or request shapes.

## Sandbox And Test Notes

Use Kashier test mode and official demo/plugin examples during development. Test wrong signature, missing signature, amount mismatch, currency mismatch, duplicate callback, redirect without callback, failed callback after paid, and live/test credential separation.

## Unknowns And Do Not Invent

- Do not invent endpoint URLs.
- Do not invent signature algorithms or field order.
- Do not copy third-party code as official behavior.
- Do not treat inaccessible portal pages as proof no API exists.
- Do not use demo credentials, screenshots, or merchant-specific values in public docs.

## Agent Checklist

- Prefer official plugin/demo source when public endpoint docs are unavailable.
- Ask for merchant docs before endpoint-level custom API work.
- Keep credentials server-side or inside secure plugin configuration.
- Verify callback signature before fulfillment.
- Compare amount, currency, and merchant reference.
- Process duplicate callbacks idempotently.
- Document unknowns instead of guessing.

## Fail If

- The agent invents endpoint URLs, payload fields, or signature algorithms.
- The agent fulfills from iframe/redirect success alone.
- The agent skips signature verification because the docs are incomplete.
- The agent exposes merchant secrets in frontend code or public examples.
- The agent treats unofficial packages or blog posts as primary source without clear labeling.
