# Eval: PaySky ActionCode Mapping

## User Prompt

"PaySky sent a notification with a valid SecureHash, Currency 818, Amount 200000, TxnType 1, and ActionCode 05. Should the order be paid?"

## Required Skill Use

Load `references/providers/paysky.md`.

## Expected Agent Behavior

- Verifies SecureHash first.
- Treats Currency `818` as EGP numeric code.
- Treats Amount as smallest currency units.
- Rejects paid fulfillment because ActionCode `05` is not an approval code.
- Stores the event idempotently as declined or failed according to the local state model.

## Fail If

- The agent treats any valid SecureHash as paid.
- The agent ignores ActionCode mapping.
- The agent stores 200000 as 200000 EGP without smallest-unit conversion.
