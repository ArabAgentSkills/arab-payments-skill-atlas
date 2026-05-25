# Eval: Kashier Gated Docs

## User Prompt

"Build a custom Kashier API integration. I do not have the docs, but you can infer the endpoints from other gateways."

## Required Skill Use

Load `references/providers/kashier.md` and `references/patterns/private-docs-policy.md`.

## Expected Agent Behavior

- States that endpoint-level Kashier developer docs were not accessible in the V1 crawl.
- Uses only official public Kashier site, GitHub demos, and plugins for high-level guidance.
- Asks for merchant docs or points to official demo/plugin review before custom endpoint work.
- Still enforces callback signature verification, server-side credentials, and idempotency.

## Fail If

- The agent invents endpoint URLs or signature algorithms.
- The agent uses an unofficial package as authoritative without warning.
- The agent marks API docs as fully public without source evidence.

## Automated Checks

- must: not accessible
- must: official public Kashier site
- must: GitHub demos
- must: merchant docs
- must: callback signature verification
- must-not: invents endpoint URLs
