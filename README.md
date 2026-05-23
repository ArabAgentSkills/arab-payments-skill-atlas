# Arab Payments Skill Atlas

[![Release](https://img.shields.io/github/v/release/ArabAgentSkills/arab-payments-skill-atlas?label=release)](https://github.com/ArabAgentSkills/arab-payments-skill-atlas/releases)
[![Validate](https://github.com/ArabAgentSkills/arab-payments-skill-atlas/actions/workflows/validate.yml/badge.svg)](https://github.com/ArabAgentSkills/arab-payments-skill-atlas/actions/workflows/validate.yml)
[![skills.sh](https://skills.sh/b/ArabAgentSkills/arab-payments-skill-atlas)](https://skills.sh/ArabAgentSkills/arab-payments-skill-atlas)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Agents](https://img.shields.io/badge/agents-Codex%20%7C%20Claude%20%7C%20Cursor%20%7C%20Copilot-111827)
![Egypt V1](https://img.shields.io/badge/coverage-Egypt%20V1-0f766e)
![Safety First](https://img.shields.io/badge/payments-webhook--first-critical)

Payment integrations in our region deserve better than guesswork.

مصمم لمساعدة المطورين في مصر والمنطقة العربية على بناء تكاملات دفع أكثر أمانا.

Arab Payments Skill Atlas is a payment-safety skill project for AI coding agents. V1 ships with Egypt Payment Guardian, an Egypt-first provider pack for Paymob, FawryPay, Geidea Egypt, EasyKash, PaySky, Kashier, valU, and Souhoola.

Created by Mohamed Waleed and Fady Azzouny with the help of Codex GPT-5.5.

Public repo: `https://github.com/ArabAgentSkills/arab-payments-skill-atlas`

## Why This Exists

Payment work breaks products when agents guess. A success redirect is not a paid order. A frontend SDK callback is not final settlement. A copied secret in browser code can turn a weekend MVP into a production incident.

This project gives coding agents a source-backed field guide for safer regional payment integrations. It starts with Egypt because that is where the current provider research is deepest. The broader Atlas name is intentional: later releases can add more Arab and MENA payment packs through the same review process.

## Quick Install

### Install With `npx skills`

List the skills discovered in this repository:

```powershell
npx skills add ArabAgentSkills/arab-payments-skill-atlas --list
```

Install Egypt Payment Guardian interactively:

```powershell
npx skills add ArabAgentSkills/arab-payments-skill-atlas --skill egypt-payment-guardian
```

Install globally for Codex:

```powershell
npx skills add ArabAgentSkills/arab-payments-skill-atlas --skill egypt-payment-guardian -g -a codex -y
```

Install for Claude Code in the current project:

```powershell
npx skills add ArabAgentSkills/arab-payments-skill-atlas --skill egypt-payment-guardian -a claude-code -y
```

Update later:

```powershell
npx skills update egypt-payment-guardian
```

`npx skills` follows the GitHub source. Updates are not silent; users must run `npx skills update` to refresh an installed copy. The `skills` CLI may collect anonymous install telemetry by default; set `DISABLE_TELEMETRY=1` before the command if you want to opt out.

### Full Adapter Install

The `npx skills` path installs the skill itself. Use the repo updater when you also want the project adapters: `AGENTS.md`, `CLAUDE.md`, Cursor rules, Copilot instructions, and the generic prompt.

Install the current Egypt V1 skill globally for Codex/AGENTS-compatible skill discovery:

```powershell
Copy-Item -Recurse .\skills\egypt-payment-guardian "$HOME\.agents\skills\egypt-payment-guardian" -Force
```

Install project-local adapters for common agents:

```powershell
python .\scripts\install_or_update_skill.py --agent all --target C:\path\to\your-project
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

## What Agents Learn

The installed skill is `egypt-payment-guardian`. Its canonical source is `skills/egypt-payment-guardian/SKILL.md`.

Agents are instructed to:

- identify the provider, integration path, environment, and payment method before writing code
- never fulfill from a browser redirect, SDK success callback, hosted checkout event, or frontend-only status
- verify provider authenticity first: HMAC, signature, SecureHash, or documented status inquiry
- compare amount, currency, local order reference, and provider transaction/order reference
- process callbacks, retries, redirects, status pulls, and refreshes idempotently
- keep merchant secrets, HMAC secrets, API passwords, terminal secrets, and service role keys server-side
- refuse to invent endpoints, fields, signatures, test cards, or status names when docs are gated or partial

## Egypt V1 Coverage

V1 is Egypt-only. The repository name is intentionally broader because later releases can add more Arab and MENA payment packs after the same source-backed review process.

| Tier | Providers and methods | What the skill covers |
| --- | --- | --- |
| Full-depth | Paymob, FawryPay, Geidea Egypt, EasyKash, PaySky | Hosted checkout/API paths, callbacks/webhooks, HMAC/signature/SecureHash guidance, amount/currency checks, status mapping, idempotency, refunds/voids/capture/inquiry where documented. |
| Method-depth | valU, Souhoola | PSP-routed BNPL method guidance, especially through Geidea and other enabled PSP accounts. Not treated as standalone direct APIs unless official merchant docs exist. |
| Conservative | Kashier | Official site, official GitHub demos, and plugins only until endpoint-level public docs or merchant docs are available. The skill tells agents not to invent missing API details. |
| Deferred | ETA eInvoicing/eReceipt, Daftra, Bosta, ShipBlu, CEQUENS, PayTabs, Tap, MyFatoorah, HyperPay, Moyasar, Amazon Payment Services | Valuable future packs, not claimed as covered in Egypt V1. |

## Supported Agents

| Agent or runtime | Adapter | How to use |
| --- | --- | --- |
| Codex, OpenCode, AGENTS.md-compatible agents | `AGENTS.md` | Keep the repo root adapter or copy it into the target project root. |
| Claude Code | `CLAUDE.md` and `skills/egypt-payment-guardian/` | Copy the skill folder into `.claude/skills/egypt-payment-guardian` or use the repo memory shim. |
| Cursor | `.cursor/rules/egypt-payment-guardian.mdc` | Copy the rule into the target project's `.cursor/rules/` directory. |
| GitHub Copilot | `.github/copilot-instructions.md` | Copy or merge the instructions into the target repository's Copilot instructions file. |
| OpenClaw, Hermes, custom agents | `adapters/generic/EGYPT_PAYMENT_GUARDIAN_PROMPT.md` | Paste the prompt into the agent's system, project, or memory instructions. |

Manual fallback for any agent:

```text
Paste adapters/generic/EGYPT_PAYMENT_GUARDIAN_PROMPT.md into the agent's project instructions and keep this repo available as reference material.
```

To also update the global Codex skill when installing all project adapters, opt in explicitly:

```powershell
python .\scripts\install_or_update_skill.py --agent all --target C:\path\to\your-project --include-global-codex
```

See `docs/agent-compatibility.md` for full compatibility notes.

## Repository Layout

```text
AGENTS.md
CLAUDE.md
.cursor/rules/egypt-payment-guardian.mdc
.github/copilot-instructions.md
adapters/generic/
docs/
skill-version.json
skills/egypt-payment-guardian/
  SKILL.md
  references/provider-index.json
  references/providers/
  references/patterns/
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
python .\scripts\validate_source_watch.py
python .\scripts\secret_scan.py
python .\scripts\check_source_links.py
python .\scripts\check_source_changes.py --check
python .\scripts\install_or_update_skill.py --agent all --target C:\path\to\temp-project --dry-run
python .\scripts\install_or_update_skill.py --agent codex --dry-run
git diff --cached --check
```

`check_source_links.py` uses the network. It reports `JS_CHALLENGE` when a public docs page requires browser or JavaScript verification and fails only on clear breakage such as missing hosts, TLS errors, or `404`.

### Release Checklist

Before announcing a new approved release:

1. Confirm the public repository is `ArabAgentSkills/arab-payments-skill-atlas`.
2. Run the validation commands in this README.
3. Push `main`.
4. Create a version tag such as `v0.1.0`.
5. Publish a GitHub release from that tag.
6. Run `python .\scripts\install_or_update_skill.py --agent codex --use-latest-release --dry-run`.
7. Announce the release only after the release dry-run succeeds.

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

This project is not affiliated with Paymob, FawryPay, Geidea, EasyKash, Kashier, PaySky, valU, Souhoola, or any listed provider. It is a safety-oriented agent skill and does not replace official provider documentation, merchant agreements, legal advice, PCI DSS guidance, or production payment certification.
