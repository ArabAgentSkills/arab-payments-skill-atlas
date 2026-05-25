#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_HEADINGS = [
    "User Prompt",
    "Required Skill Use",
    "Expected Agent Behavior",
    "Fail If",
]

CHECK_RE = re.compile(r"^-\s*(must|must-not)\s*:\s*(.+?)\s*$", re.IGNORECASE)


@dataclass(frozen=True)
class AutomatedCheck:
    kind: str
    phrase: str


@dataclass(frozen=True)
class Scenario:
    path: Path
    skill: str
    slug: str
    sections: dict[str, str]
    automated_checks: list[AutomatedCheck]

    @property
    def response_filename(self) -> str:
        return f"{self.skill}__{self.slug}.md"


@dataclass(frozen=True)
class EvalResult:
    scenario: Scenario
    passed: bool
    missing_required: list[str]
    present_forbidden: list[str]


def normalize_text(value: str) -> str:
    value = value.translate(str.maketrans("", "", "`\"'"))
    return re.sub(r"\s+", " ", value.lower()).strip()


def parse_sections(text: str) -> dict[str, str]:
    sections: dict[str, list[str]] = {}
    current: str | None = None
    for line in text.splitlines():
        if line.startswith("## "):
            current = line[3:].strip()
            sections.setdefault(current, [])
            continue
        if current is not None:
            sections[current].append(line)
    return {heading: "\n".join(lines).strip() for heading, lines in sections.items()}


def parse_automated_checks(section: str) -> list[AutomatedCheck]:
    checks: list[AutomatedCheck] = []
    for line in section.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        match = CHECK_RE.match(stripped)
        if not match:
            raise ValueError(f"invalid automated check line: {line}")
        kind = match.group(1).lower()
        phrase = match.group(2).strip()
        if not phrase:
            raise ValueError("automated check phrase cannot be empty")
        checks.append(AutomatedCheck(kind=kind, phrase=phrase))
    return checks


def infer_skill(path: Path, root: Path) -> str:
    relative = path.relative_to(root)
    parts = relative.parts
    if len(parts) >= 5 and parts[0] == "skills":
        return parts[1]
    return path.parents[2].name


def parse_scenario(path: Path, root: Path = ROOT) -> Scenario:
    text = path.read_text(encoding="utf-8")
    sections = parse_sections(text)
    automated = parse_automated_checks(sections.get("Automated Checks", ""))
    return Scenario(
        path=path,
        skill=infer_skill(path, root),
        slug=path.stem,
        sections=sections,
        automated_checks=automated,
    )


def scenario_paths(root: Path = ROOT) -> list[Path]:
    return sorted((root / "skills").glob("*/evals/scenarios/*.md"))


def validate_scenario(scenario: Scenario, require_automated_checks: bool = False) -> list[str]:
    errors: list[str] = []
    display = scenario.path.relative_to(ROOT) if scenario.path.is_relative_to(ROOT) else scenario.path
    for heading in REQUIRED_HEADINGS:
        if heading not in scenario.sections:
            errors.append(f"{display} missing ## {heading}")
    if require_automated_checks and "Automated Checks" not in scenario.sections:
        errors.append(f"{display} missing ## Automated Checks")
    if "Automated Checks" in scenario.sections and not scenario.automated_checks:
        errors.append(f"{display} has empty ## Automated Checks")
    return errors


def validate_scenarios(root: Path = ROOT, require_automated_checks: bool = False) -> list[str]:
    errors: list[str] = []
    paths = scenario_paths(root)
    if not paths:
        return [f"{root} has no eval scenarios"]
    for path in paths:
        try:
            scenario = parse_scenario(path, root)
        except ValueError as exc:
            errors.append(f"{path}: {exc}")
            continue
        errors.extend(validate_scenario(scenario, require_automated_checks))
    return errors


def score_response(scenario: Scenario, response: str) -> EvalResult:
    normalized_response = normalize_text(response)
    missing_required: list[str] = []
    present_forbidden: list[str] = []
    for check in scenario.automated_checks:
        normalized_phrase = normalize_text(check.phrase)
        if check.kind == "must" and normalized_phrase not in normalized_response:
            missing_required.append(check.phrase)
        elif check.kind == "must-not" and normalized_phrase in normalized_response:
            present_forbidden.append(check.phrase)
    return EvalResult(
        scenario=scenario,
        passed=not missing_required and not present_forbidden,
        missing_required=missing_required,
        present_forbidden=present_forbidden,
    )


def score_response_dir(root: Path, response_dir: Path, strict_response_files: bool) -> tuple[list[EvalResult], list[str]]:
    results: list[EvalResult] = []
    errors: list[str] = []
    for path in scenario_paths(root):
        scenario = parse_scenario(path, root)
        if not scenario.automated_checks:
            continue
        response_path = response_dir / scenario.response_filename
        if not response_path.exists():
            message = f"missing response file: {response_path}"
            if strict_response_files:
                errors.append(message)
            else:
                print(f"SKIP {scenario.skill}/{scenario.slug}: {message}")
            continue
        results.append(score_response(scenario, response_path.read_text(encoding="utf-8")))
    return results, errors


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate and score Arab Payments Skill Atlas eval scenarios.")
    parser.add_argument("--root", type=Path, default=ROOT, help="Repository root.")
    parser.add_argument("--validate", action="store_true", help="Validate eval scenario structure.")
    parser.add_argument("--require-automated-checks", action="store_true", help="Require ## Automated Checks in every scenario.")
    parser.add_argument("--response-dir", type=Path, help="Directory of saved agent responses named skill__scenario.md.")
    parser.add_argument("--strict-response-files", action="store_true", help="Fail when a checked scenario has no response file.")
    args = parser.parse_args()

    if args.validate or not args.response_dir:
        errors = validate_scenarios(args.root, args.require_automated_checks)
        if errors:
            print("Eval scenario validation failed:")
            for error in errors:
                print(f"- {error}")
            raise SystemExit(1)
        print("Eval scenario validation passed")

    if args.response_dir:
        results, errors = score_response_dir(args.root, args.response_dir, args.strict_response_files)
        for result in results:
            marker = "PASS" if result.passed else "FAIL"
            print(f"{marker} {result.scenario.skill}/{result.scenario.slug}")
            for phrase in result.missing_required:
                print(f"  missing must: {phrase}")
            for phrase in result.present_forbidden:
                print(f"  present must-not: {phrase}")
        if errors or any(not result.passed for result in results):
            for error in errors:
                print(f"ERROR {error}")
            raise SystemExit(1)


if __name__ == "__main__":
    main()
