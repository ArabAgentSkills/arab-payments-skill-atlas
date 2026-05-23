# Eval: Geidea Amount Currency Mismatch

## User Prompt

"The Geidea callback says paid, but the amount is 100 EGP and my order is 120 EGP. Should I mark it paid?"

## Required Skill Use

Load `references/providers/geidea-egypt.md` and `references/patterns/idempotency-state-transitions.md`.

## Expected Agent Behavior

- Rejects fulfillment because amount differs.
- Records a verified event only if signature is valid.
- Marks local attempt as mismatch/review or failed according to project state model.
- Does not create paid state.
- Recommends safe logging and manual investigation.

## Fail If

- The order is marked paid because provider status says success.
- The agent ignores currency/amount comparison.
- The agent recommends editing the order amount to match the provider after the fact.
