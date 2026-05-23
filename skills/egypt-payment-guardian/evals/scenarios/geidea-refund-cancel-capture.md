# Eval: Geidea Refund Cancel Capture

## User Prompt

"For Geidea, use one endpoint for cancel, refund, void, and capture. They all mean reverse the payment, right?"

## Required Skill Use

Load `references/providers/geidea-egypt.md` and `references/patterns/idempotency-state-transitions.md`.

## Expected Agent Behavior

- Explains that cancel, refund, void, and capture are distinct Geidea operations.
- Uses cancel only before Pay API completion where documented.
- Uses refund only for paid, captured, or settled transactions.
- Uses void only for authorized/uncaptured transactions and confirms region/account support.
- Treats capture as completing an authorization, not reversing payment.
- Adds separate idempotency keys and state transitions for each operation.

## Fail If

- The agent treats refund, cancel, void, and capture as interchangeable.
- The agent refunds an uncaptured authorization instead of using the documented void path.
- The agent captures without checking authorized amount and operation support.
