# MyFatoorah Webhook And Get Payment Details

## User Prompt

"MyFatoorah redirected back with PaymentId, but the webhook may arrive late. Can the success page mark paid if PaymentId exists?"

## Required Skill Use

The agent loads `myfatoorah.md` and `webhook-first-fulfillment.md`.

## Expected Agent Behavior

- Refuses to mark paid from redirection alone.
- Verifies Webhook v2 using the `myfatoorah-signature` header and webhook secret.
- Uses Get Payment Details server-side as fallback or confirmation.
- Maps `PAID` plus successful transaction state to paid after amount/currency/reference checks.
- Keeps `AUTHORIZE`, pending, failed, in-progress, and canceled states distinct.

## Fail If

- Agent marks paid only because PaymentId exists.
- Agent skips `myfatoorah-signature` verification.
- Agent treats `AUTHORIZE` as captured settlement.

## Automated Checks

- must: redirection alone
- must: `myfatoorah-signature`
- must: webhook secret
- must: Get Payment Details
- must: amount/currency/reference checks
- must: AUTHORIZE
- must-not: PaymentId exists
