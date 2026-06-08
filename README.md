# Arab Payments Skill Atlas

[![Release](https://img.shields.io/github/v/release/ArabAgentSkills/arab-payments-skill-atlas?label=release)](https://github.com/ArabAgentSkills/arab-payments-skill-atlas/releases)
[![Validate](https://github.com/ArabAgentSkills/arab-payments-skill-atlas/actions/workflows/validate.yml/badge.svg)](https://github.com/ArabAgentSkills/arab-payments-skill-atlas/actions/workflows/validate.yml)
[![GitHub Repo](https://img.shields.io/badge/repo-GitHub-181717?logo=github)](https://github.com/ArabAgentSkills/arab-payments-skill-atlas)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Agents](https://img.shields.io/badge/agents-Codex%20%7C%20Claude%20%7C%20Cursor%20%7C%20Copilot-111827)
![Coverage](https://img.shields.io/badge/coverage-Egypt%20%2B%20MENA%20Payments-0f766e)
![Safety First](https://img.shields.io/badge/payments-webhook--first-critical)

Payment integrations in our region deserve better than guesswork.

مصمم لمساعدة المطورين في مصر والمنطقة العربية على بناء تكاملات دفع أكثر أمانا.

Arab Payments Skill Atlas is a payment-safety skill project for AI coding agents. V1.0.0 ships two installable skills: Egypt Payment Guardian for Egypt-only work, and MENA Payment Guardian for broader Arab/MENA PSP and BNPL work.

Created by Mohamed Waleed and Fady Azzouny with the help of Codex GPT-5.5.

Public repo: `https://github.com/ArabAgentSkills/arab-payments-skill-atlas`

## Why This Exists

Payment work breaks products when agents guess. A success redirect is not a paid order. A frontend SDK callback is not final settlement. A copied secret in browser code can turn a weekend MVP into a production incident.

This project gives coding agents a source-backed field guide for safer regional payment integrations. Egypt Payment Guardian remains stable for existing users, while MENA Payment Guardian expands the Atlas into Arab/MENA PSP and BNPL coverage without turning it into a whole-business API atlas.

## Quick Install

### Install With `npx skills`

List the skills discovered in this repository:

```powershell
npx skills add ArabAgentSkills/arab-payments-skill-atlas --list
```

Install Egypt Payment Guardian:

```powershell
npx skills add ArabAgentSkills/arab-payments-skill-atlas --skill egypt-payment-guardian
```

Install MENA Payment Guardian:

```powershell
npx skills add ArabAgentSkills/arab-payments-skill-atlas --skill mena-payment-guardian
```

Install Egypt globally for Codex:

```powershell
npx skills add ArabAgentSkills/arab-payments-skill-atlas --skill egypt-payment-guardian -g -a codex -y
```

Install MENA globally for Codex:

```powershell
npx skills add ArabAgentSkills/arab-payments-skill-atlas --skill mena-payment-guardian -g -a codex -y
```

Install for Claude Code in the current project:

```powershell
npx skills add ArabAgentSkills/arab-payments-skill-atlas --skill mena-payment-guardian -a claude-code -y
```

Update later:

```powershell
npx skills update egypt-payment-guardian
npx skills update mena-payment-guardian
```

`npx skills` follows the GitHub source. Updates are not silent; users must run `npx skills update` to refresh an installed copy. The `skills` CLI may collect anonymous install telemetry by default; set `DISABLE_TELEMETRY=1` before the command if you want to opt out.

### Full Adapter Install

The `npx skills` path installs a native skill. Use the repo updater when you also want project adapters: `AGENTS.md`, `CLAUDE.md`, Cursor rules, Copilot instructions, and generic prompts.

Install project-local adapters for common agents:

```powershell
python .\scripts\install_or_update_skill.py --agent all --target C:\path\to\your-project
```

Install only one skill through the updater:

```powershell
python .\scripts\install_or_update_skill.py --agent all --skill egypt-payment-guardian --target C:\path\to\your-project
python .\scripts\install_or_update_skill.py --agent all --skill mena-payment-guardian --target C:\path\to\your-project
```

Pull the latest approved public release:

```powershell
python .\scripts\install_or_update_skill.py --agent codex --use-latest-release
```

The Python updater follows approved GitHub releases, while `npx skills` follows the GitHub source.

Dry-run first if you are installing into an active project:

```powershell
python .\scripts\install_or_update_skill.py --agent all --target C:\path\to\temp-project --dry-run
python .\scripts\install_or_update_skill.py --agent codex --dry-run
```

The updater refuses to overwrite local user changes unless `--force` is provided. Installed copies cannot be updated remotely without user consent.

To also update the global Codex skill when installing all project adapters, opt in explicitly:

```powershell
python .\scripts\install_or_update_skill.py --agent all --target C:\path\to\your-project --include-global-codex
```

## What Agents Learn

Agents are instructed to:

- identify the provider, country, integration path, environment, and payment method before writing code
- never fulfill from a browser redirect, SDK success callback, hosted checkout event, BNPL approval page, or frontend-only status
- verify provider authenticity first: HMAC, signature, SecureHash, encrypted webhook, webhook secret token, or documented status inquiry
- compare amount, currency, country/account context, local order reference, and provider transaction/order reference
- process callbacks, webhooks, retries, redirects, status pulls, captures, refunds, voids, and refreshes idempotently
- keep merchant secrets, HMAC secrets, API passwords, terminal secrets, SHA phrases, bearer tokens, and service role keys server-side
- refuse to invent endpoints, fields, signatures, test cards, status names, capture windows, or local payment method support when docs are gated or partial

## Coverage

V1.0.0 remains payment-focused: PSPs plus BNPL only. Non-payment workbook rows such as tax/e-invoicing, logistics, communications, identity, HR/payroll, open banking, commerce/POS/accounting, and Arabic NLP are deferred to future packs.

| Skill | Scope | Coverage |
| --- | --- | --- |
| `egypt-payment-guardian` | Egypt-only payment work | Paymob, FawryPay, Geidea Egypt, EasyKash, PaySky, Kashier, valU, Souhoola. Stable for existing users. |
| `mena-payment-guardian` | Arab/MENA PSP and BNPL work | Paymob, FawryPay, Geidea, PayTabs, Tap Payments, MyFatoorah, HyperPay, Moyasar, Amazon Payment Services, EasyKash, Kashier, PaySky, Tabby, Tamara, valU, Souhoola. |

### MENA V1.0.0 Provider Tiers

| Tier | Providers and methods | What the skill covers |
| --- | --- | --- |
| Full-depth | Paymob, FawryPay, Geidea, PayTabs, Tap Payments, MyFatoorah, HyperPay, Moyasar, Amazon Payment Services, EasyKash, PaySky, Tabby, Tamara | Hosted/API paths, callbacks/webhooks/IPN, signature/HMAC/SecureHash/webhook validation, amount/currency/country checks, status mapping, idempotency, capture/refund/void/cancel/inquiry where documented. |
| Method-depth | valU, Souhoola | PSP-routed BNPL method guidance. Not treated as standalone direct APIs unless official merchant docs exist. |
| Conservative | Kashier | Official site, official GitHub demos, and plugins only until endpoint-level public docs or merchant docs are available. The skill tells agents not to invent missing API details. |

## Supported Agents

| Agent or runtime | Adapter | How to use |
| --- | --- | --- |
| Codex, OpenCode, AGENTS.md-compatible agents | `AGENTS.md` | Keep the repo root adapter or copy it into the target project root. |
| Claude Code | `CLAUDE.md` and `skills/*/` | Copy the selected skill folder into `.claude/skills/` or use the repo memory shim. |
| Cursor | `.cursor/rules/egypt-payment-guardian.mdc`, `.cursor/rules/mena-payment-guardian.mdc` | Copy the relevant rule into the target project's `.cursor/rules/` directory. |
| GitHub Copilot | `.github/copilot-instructions.md` | Copy or merge the instructions into the target repository's Copilot instructions file. |
| OpenClaw, Hermes, custom agents | `adapters/generic/` prompts | Paste the matching prompt into the agent's system, project, or memory instructions. |

Manual fallback for any agent:

```text
Paste adapters/generic/EGYPT_PAYMENT_GUARDIAN_PROMPT.md for Egypt-only work or adapters/generic/MENA_PAYMENT_GUARDIAN_PROMPT.md for broader MENA work, then keep this repo available as reference material.
```

See `docs/agent-compatibility.md` for full compatibility notes.

## Repository Layout

```text
AGENTS.md
CLAUDE.md
.cursor/rules/
.github/copilot-instructions.md
adapters/generic/
docs/
skill-version.json
skills/
  egypt-payment-guardian/
    SKILL.md
    references/
    evals/scenarios/
  mena-payment-guardian/
    SKILL.md
    references/
    evals/scenarios/
scripts/
  validate_skill.py
  validate_adapters.py
  validate_source_watch.py
  secret_scan.py
  check_source_links.py
  check_source_changes.py
  install_or_update_skill.py
```

## For Maintainers

Run the local checks before publishing, installing, or changing payment guidance:

```powershell
python .\scripts\validate_skill.py
python .\scripts\validate_adapters.py
python .\scripts\eval_scenarios.py --validate --require-automated-checks
python -m unittest discover -s tests
python .\scripts\validate_source_watch.py
python .\scripts\secret_scan.py
python .\scripts\check_source_links.py
python .\scripts\check_source_changes.py --check
python .\scripts\install_or_update_skill.py --agent all --target C:\path\to\temp-project --dry-run
python .\scripts\install_or_update_skill.py --agent codex --dry-run
git diff --cached --check
```

`check_source_links.py` uses the network. It reports `JS_CHALLENGE` when a public docs page requires browser or JavaScript verification, `TLS_VERIFY` when a public docs site is browser-accessible but the simple Python fetch cannot verify its certificate chain, and `SERVER_ERROR` for transient provider-side HTTP errors such as `408`, `429`, or `5xx`. It exits `2` for `SERVER_ERROR` so source-watch maintainers review the finding with private artifacts, and exits `1` only on clear breakage such as missing hosts, `404`, or `410`.

`eval_scenarios.py` validates the Markdown pressure scenarios and can score saved agent responses when they are named `skill__scenario.md` under a response directory.

### Release Checklist

Before announcing a new approved release:

1. Confirm the public repository is `ArabAgentSkills/arab-payments-skill-atlas`.
2. Run the validation commands in this README.
3. Push `main`.
4. Run `npx skills add ArabAgentSkills/arab-payments-skill-atlas --list` and confirm both skills appear.
5. Create a version tag such as `v1.0.0`.
6. Publish a GitHub release from that tag.
7. Run `python .\scripts\install_or_update_skill.py --agent codex --use-latest-release --dry-run`.
8. Announce the release only after GitHub Actions and release dry-run succeed.

Latest-release updates are enabled only for human-approved GitHub releases. Do not point users at private watcher artifacts or unreviewed branches.

### Source Watch And Approval

Provider documentation monitoring is split into public-safe metadata and private review evidence.

- Public repo: stores hashes, statuses, timestamps, short excerpts, and curated summaries only.
- Private watcher repo: may store full fetched snapshots as short-retention private workflow artifacts.
- Public guidance changes: published only after human review through a normal PR and approved release.

Use these local commands:

```powershell
python .\scripts\check_source_changes.py --check
python .\scripts\check_source_changes.py --update-baseline
```

See `docs/source-watch.md` and `docs/private-watcher-setup.md` for the full workflow.

## Source Policy

This repository stores original summaries, provider contracts, source links, and eval scenarios. It does not vendor or republish full provider documentation.

Private merchant PDFs, screenshots, dashboards, credentials, onboarding emails, or portal exports must stay out of git. Put local-only materials under `private-docs/` or `local-docs/`; both are ignored.

Every provider update must include:

- official or provider-controlled source URLs
- `last_checked` date in `provider-index.json`
- concise source-backed summaries, not copied docs
- clear unknowns and "do not invent" notes
- eval updates when provider behavior changes

Private watcher findings and full fetched snapshots must not be published. Only human-approved summaries, baseline metadata, changelog entries, and releases belong in the public repo.

## Credits

- Co-creators and maintainers: Mohamed Waleed and Fady Azzouny
- Organization home: ArabAgentSkills
- Built with AI implementation assistance from Codex GPT-5.5

## Disclaimer

This project is not affiliated with any listed payment provider. It is a safety-oriented agent skill and does not replace official provider documentation, merchant agreements, legal advice, PCI DSS guidance, acquirer certification, or production payment certification.
