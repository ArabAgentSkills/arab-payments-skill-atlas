# Kashier

- Provider: Kashier
- Scope: Egypt PSP with public product pages, official GitHub demos/plugins, and partially public/gated endpoint-level docs.
- Priority: P1
- Readiness: B
- Public docs status: partially-public-official-github
- Last checked: 2026-05-24
- Source confidence: Medium. Official site and GitHub repos are public; endpoint-level merchant docs should be requested before custom API work.
- Sources: Kashier official site, Kashier API blog, official GitHub organization, Node.js demo, PHP demo, WooCommerce plugin.

## Use When

Use for Kashier checkout planning, plugin/demo-based integration review, and conservative guidance when endpoint-level docs are not available.

## Source Map

- Site: `https://www.kashier.io/`
- API product page/blog: `https://www.kashier.io/blog-posts/kashier-api---power-flexibility-simplicity`
- GitHub: `https://github.com/Kashier-payments`
- Node demo: `https://github.com/Kashier-payments/NodeJs-Checkout-Demo`
- PHP demo: `https://github.com/Kashier-payments/Php-Checkout-Demo`

## Integration Paths

- Use official plugins and demos where they match the stack.
- For custom endpoint-level integration, ask for current merchant docs/API reference.

## Setup Prerequisites

- Merchant account, mode/environment, merchant identifier, secret/signature material, callback/redirect configuration, and current official docs.

## Auth And Secret Boundary

- Keep all merchant ids that are sensitive in the project, API keys, secret/signature material, and payment creation credentials server-side.
- Do not place demo secrets in public frontend bundles.

## Callback Or Webhook Contract

- Use only documented callback/webhook behavior from official demos or merchant docs.
- Redirect/checkout page result remains UX only until server verifies through documented callback or inquiry.

## Signature Or HMAC

- Do not infer signature algorithms from partial snippets.
- If a demo includes a signature helper, validate it against current merchant docs before production.

## Idempotency Keys

- Use local order reference plus Kashier transaction/payment reference where documented.
- Duplicate callback/retry handling remains mandatory even when docs are partial.

## Amount And Currency

- Compare amount, currency, merchant order reference, and provider reference before paid state.
- Egypt flows should explicitly confirm EGP and smallest/decimal unit from official docs.

## Status Mapping

- Map statuses only from official docs or demo responses that are current.
- Unknown statuses must go to pending/manual-review, not paid.

## Refunds Voids And Subscriptions

- Use official plugin or merchant docs for refunds/voids/capture; do not invent endpoints.
- Subscriptions/tokenization require direct official docs.

## Sandbox And Test Notes

- Test only with official demo/plugin instructions or merchant-provided sandbox docs.
- Keep merchant docs local/private if licensing or access terms require it.

## Unknowns And Do Not Invent

- Endpoint URLs, signature algorithm, status enum, amount units, test cards, and refund/capture APIs are unknown unless current official docs are provided.

## Agent Checklist

- Prefer official plugin/demo.
- Ask for merchant docs before custom API code.
- Keep secrets server-side.
- Verify callback/inquiry before fulfillment.
- Mark unknowns explicitly.

## Fail If

- You invent endpoint URLs.
- You infer signature rules from memory.
- You treat product marketing text as endpoint documentation.
- You claim full-depth custom API support without merchant docs.
