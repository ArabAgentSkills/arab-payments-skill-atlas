# Tabby Country Webhook Capture Race

## User Prompt

"We use Tabby in Kuwait with KWD. The success redirect and webhook can both call capture, so I will use a timestamp reference for each capture and grab `web_url` from the top-level checkout response."

## Required Skill Use

The agent loads `tabby.md`, `webhook-first-fulfillment.md`, and `capture-refund-void-lifecycle.md`.

## Expected Agent Behavior

- Does not assume Kuwait/KWD support from older Tabby docs; checks current country/currency support and merchant confirmation.
- Uses the nested hosted-checkout URL from `configuration.available_products.installments[0].web_url`.
- Registers payment webhooks for the right `merchant_code` and verifies the configured static auth header.
- Retrieves payment before fulfillment or capture.
- Prevents duplicate capture attempts with a local capture-in-progress guard plus the same stable `reference_id` across redirect and webhook paths.

## Fail If

- Agent assumes Kuwait/KWD is supported without current merchant confirmation.
- Agent redirects from an unverified top-level `web_url`.
- Agent captures separately from redirect and webhook handlers with timestamp-based `reference_id` values.
- Agent fulfills without retrieving payment and checking amount/currency/reference.

## Automated Checks

- must: Kuwait/KWD
- must: current country/currency support
- must: `configuration.available_products.installments[0].web_url`
- must: `merchant_code`
- must: static auth header
- must: retrieves payment
- must: capture-in-progress
- must: stable `reference_id`
- must-not: timestamp reference
