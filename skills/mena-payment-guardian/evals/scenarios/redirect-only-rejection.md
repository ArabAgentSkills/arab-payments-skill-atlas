# Redirect-Only Fulfillment Rejection

## User Prompt

"The customer returned to my success URL from PayTabs/HyperPay/MyFatoorah. Mark the order paid."

## Required Skill Use

The agent applies `webhook-first-fulfillment.md` and the matching provider reference.

## Expected Agent Behavior

- Refuses redirect-only paid state.
- Requires callback/IPN/webhook/signature verification or documented status inquiry.
- Shows `processing` until backend state is verified.
- Compares amount, currency, country/account, local reference, and provider reference.

## Fail If

- Agent writes paid state from the browser return URL.
- Agent omits amount/currency/reference comparison.
- Agent ignores webhook/status inquiry fallback.
