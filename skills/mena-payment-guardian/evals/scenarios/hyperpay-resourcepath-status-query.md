# HyperPay ResourcePath Status Query

## User Prompt

"HyperPay redirected the shopper back with resourcePath. The page says success, so I want the frontend to unlock access immediately."

## Required Skill Use

The agent loads `hyperpay.md` and `webhook-first-fulfillment.md`.

## Expected Agent Behavior

- Treats the shopper redirect as UX only.
- Uses the server to call `baseUrl + resourcePath` with HyperPay auth and retrieve transaction status.
- Decrypts/authenticates encrypted webhooks before using them.
- Compares amount, currency, brand/type, merchant reference, and provider ids.
- Handles multiple final or out-of-order webhook messages idempotently.

## Fail If

- Agent fulfills only because the shopper reached the result page.
- Agent lets the frontend call authenticated HyperPay status APIs.
- Agent ignores encrypted webhook authentication or duplicate final messages.

## Automated Checks

- must: redirect as UX only
- must: `baseUrl + resourcePath`
- must: HyperPay auth
- must: encrypted webhooks
- must: amount, currency
- must: out-of-order webhook messages
- must-not: frontend to unlock access immediately
