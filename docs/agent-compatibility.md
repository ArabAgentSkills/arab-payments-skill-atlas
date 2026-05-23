# Agent Compatibility

Arab Payments Skill Atlas ships two installable skills:

- `skills/egypt-payment-guardian/SKILL.md` for Egypt-only payment work.
- `skills/mena-payment-guardian/SKILL.md` for broader Arab/MENA PSP and BNPL work.

Every adapter is a thin loader. Provider knowledge belongs in the skill folders, not in adapter files.

## Compatibility Matrix

| Agent or runtime | Native file | Confidence | Notes |
| --- | --- | --- | --- |
| Codex | `AGENTS.md` | High | Codex-style agents can read root project instructions and choose the correct skill. |
| OpenCode and AGENTS.md-compatible agents | `AGENTS.md` | High | Keep this file at the target project root. |
| Claude Code | `CLAUDE.md` plus `.claude/skills/*/SKILL.md` | High | Use `CLAUDE.md` as project memory and copy the skill folders when native skills are available. |
| Cursor | `.cursor/rules/egypt-payment-guardian.mdc` and `.cursor/rules/mena-payment-guardian.mdc` | High | Agent Requested rules; the agent loads the relevant one when payment work is mentioned. |
| GitHub Copilot | `.github/copilot-instructions.md` | Medium | Copilot instructions are concise; keep provider detail in the skill files. |
| OpenClaw, Hermes, and custom agents | `adapters/generic/EGYPT_PAYMENT_GUARDIAN_PROMPT.md` and `adapters/generic/MENA_PAYMENT_GUARDIAN_PROMPT.md` | Medium | Paste the matching generic prompt into the agent's project, memory, or system instructions. |

## Install Snippets

Codex or AGENTS.md-compatible project:

```powershell
$target = "C:\path\to\your-project"
Copy-Item .\AGENTS.md "$target\AGENTS.md" -Force
```

Claude Code project-local skills:

```powershell
$target = "C:\path\to\your-project"
New-Item -ItemType Directory -Force "$target\.claude\skills" | Out-Null
Copy-Item -Recurse .\skills\egypt-payment-guardian "$target\.claude\skills\egypt-payment-guardian" -Force
Copy-Item -Recurse .\skills\mena-payment-guardian "$target\.claude\skills\mena-payment-guardian" -Force
Copy-Item .\CLAUDE.md "$target\CLAUDE.md" -Force
```

Cursor:

```powershell
$target = "C:\path\to\your-project"
New-Item -ItemType Directory -Force "$target\.cursor\rules" | Out-Null
Copy-Item .\.cursor\rules\egypt-payment-guardian.mdc "$target\.cursor\rules\egypt-payment-guardian.mdc" -Force
Copy-Item .\.cursor\rules\mena-payment-guardian.mdc "$target\.cursor\rules\mena-payment-guardian.mdc" -Force
```

GitHub Copilot:

```powershell
$target = "C:\path\to\your-project"
New-Item -ItemType Directory -Force "$target\.github" | Out-Null
Copy-Item .\.github\copilot-instructions.md "$target\.github\copilot-instructions.md" -Force
```

macOS/Linux generic skill install:

```bash
mkdir -p "$HOME/.agents/skills"
cp -R ./skills/egypt-payment-guardian "$HOME/.agents/skills/egypt-payment-guardian"
cp -R ./skills/mena-payment-guardian "$HOME/.agents/skills/mena-payment-guardian"
```

Manual fallback:

```text
Paste adapters/generic/EGYPT_PAYMENT_GUARDIAN_PROMPT.md for Egypt-only work or adapters/generic/MENA_PAYMENT_GUARDIAN_PROMPT.md for broader MENA payment/BNPL work, then tell the agent where this repository lives.
```

All project-local adapters at once:

```powershell
$target = "C:\path\to\your-project"
python .\scripts\install_or_update_skill.py --agent all --target $target
```

This command installs project-local adapters and both Claude skill folders by default. It does not update the global Codex skill unless `--include-global-codex` is supplied. Use `--agent codex` for a dedicated global Codex install, or add `--skill egypt-payment-guardian` / `--skill mena-payment-guardian` to install only one skill.

## Adapter Rules

- Adapters are not the source of truth.
- Adapters must point to `skills/egypt-payment-guardian/SKILL.md` and/or `skills/mena-payment-guardian/SKILL.md`.
- Adapters must stay short and avoid copied provider docs.
- Provider-specific details stay under each skill's `references/providers/` folder.
- Unknown or custom agents should use `AGENTS.md` first, then the matching generic prompt if they cannot read project files automatically.

## Compatibility Promise

This repository provides native adapters where common agents support them and generic prompts for everything else. It does not guarantee that every proprietary runtime auto-discovers every file. If an agent cannot auto-load the adapter, paste the matching generic prompt into that agent's project instructions and keep the skill folder available as reference material.
