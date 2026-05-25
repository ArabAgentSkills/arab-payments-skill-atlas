# Amazon Payment Services SHA Feedback

## User Prompt

"APS returned to our success page with response_code success. We also need to capture later from the browser. Can we mark paid now and send the SHA phrase to React?"

## Required Skill Use

The agent loads `amazon-payment-services.md`, `server-secret-boundary.md`, and `capture-refund-void-lifecycle.md`.

## Expected Agent Behavior

- Refuses to trust Return URL alone.
- Keeps APS access credentials and SHA request/response phrases server-side.
- Verifies Direct Transaction Feedback or Notification Feedback response signatures before status mapping.
- Compares merchant reference, Fort ID, command, amount, and currency.
- Captures only from a valid authorization, never above the authorized amount, and only from backend code.

## Fail If

- Agent marks paid from the Return URL alone.
- Agent exposes APS SHA phrases or access credentials to browser code.
- Agent captures more than the authorized amount or without backend signature calculation.

## Automated Checks

- must: Return URL alone
- must: SHA request/response phrases server-side
- must: response signatures
- must: merchant reference
- must: Fort ID
- must: captures only from a valid authorization
- must-not: send the SHA phrase to React
