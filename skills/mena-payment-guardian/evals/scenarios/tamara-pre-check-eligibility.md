# Tamara Pre-Check Eligibility

## User Prompt

"Show Tamara to every shopper and create the checkout session directly. If Tamara rejects them later, we can handle it after redirect."

## Required Skill Use

The agent loads `tamara.md` and `capture-refund-void-lifecycle.md`.

## Expected Agent Behavior

- Runs the documented pre-check eligibility step before offering Tamara as an available payment method.
- Does not create the final checkout session for customers who fail eligibility.
- Still treats the redirect as UX and relies on approved notification plus Authorise Order unless confirmed auto-authorisation applies.
- Captures only after authorisation and fulfillment policy allow capture.
- Keeps pre-check eligibility, approval, authorisation, capture, cancel, and refund as separate states.

## Fail If

- Agent skips pre-check eligibility and sends every shopper to Tamara checkout.
- Agent treats eligibility or approval as captured settlement.
- Agent skips Authorise Order without confirmed auto-authorisation.
- Agent fulfills from redirect alone.

## Automated Checks

- must: pre-check eligibility
- must: available payment method
- must: final checkout session
- must: approved notification
- must: Authorise Order
- must: captures only after authorisation
- must-not: every shopper
- must-not: captured settlement
