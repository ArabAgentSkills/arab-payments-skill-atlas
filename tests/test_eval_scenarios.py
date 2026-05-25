from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.eval_scenarios import parse_scenario, score_response, validate_scenarios


SCENARIO_BODY = """# Eval: Provider Pressure

## User Prompt

"The return page says success. Can I ship now?"

## Required Skill Use

Load `references/providers/example.md`.

## Expected Agent Behavior

- Verifies the provider signature before processing.
- Compares amount, currency, and merchant reference.

## Fail If

- Agent fulfills from redirect alone.

## Automated Checks

- must: verifies the provider signature
- must: compares amount, currency, and merchant reference
- must-not: fulfills from redirect alone
"""


class EvalScenarioTests(unittest.TestCase):
    def test_parse_automated_checks_and_score_response(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "skills" / "sample-skill" / "evals" / "scenarios" / "provider-pressure.md"
            path.parent.mkdir(parents=True)
            path.write_text(SCENARIO_BODY, encoding="utf-8")

            scenario = parse_scenario(path, Path(tmp))

            self.assertEqual(scenario.skill, "sample-skill")
            self.assertEqual(scenario.slug, "provider-pressure")
            self.assertEqual([check.kind for check in scenario.automated_checks], ["must", "must", "must-not"])

            result = score_response(
                scenario,
                "The answer verifies the provider signature and compares amount, currency, and merchant reference.",
            )

            self.assertTrue(result.passed)
            self.assertEqual(result.missing_required, [])
            self.assertEqual(result.present_forbidden, [])

    def test_score_response_reports_missing_and_forbidden_phrases(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "skills" / "sample-skill" / "evals" / "scenarios" / "provider-pressure.md"
            path.parent.mkdir(parents=True)
            path.write_text(SCENARIO_BODY, encoding="utf-8")
            scenario = parse_scenario(path, Path(tmp))

            result = score_response(scenario, "The agent fulfills from redirect alone.")

            self.assertFalse(result.passed)
            self.assertIn("verifies the provider signature", result.missing_required)
            self.assertIn("compares amount, currency, and merchant reference", result.missing_required)
            self.assertIn("fulfills from redirect alone", result.present_forbidden)

    def test_score_response_ignores_markdown_punctuation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "skills" / "sample-skill" / "evals" / "scenarios" / "provider-pressure.md"
            path.parent.mkdir(parents=True)
            path.write_text(
                SCENARIO_BODY.replace("verifies the provider signature", "`Signature` header"),
                encoding="utf-8",
            )
            scenario = parse_scenario(path, Path(tmp))

            result = score_response(scenario, "The answer checks the Signature header and compares amount, currency, and merchant reference.")

            self.assertTrue(result.passed)

    def test_validate_scenarios_requires_automated_checks(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            scenario_dir = Path(tmp) / "skills" / "sample-skill" / "evals" / "scenarios"
            scenario_dir.mkdir(parents=True)
            (scenario_dir / "missing-checks.md").write_text(
                SCENARIO_BODY.replace("\n## Automated Checks\n\n- must: verifies the provider signature\n- must: compares amount, currency, and merchant reference\n- must-not: fulfills from redirect alone\n", "\n"),
                encoding="utf-8",
            )

            errors = validate_scenarios(Path(tmp), require_automated_checks=True)

            self.assertEqual(len(errors), 1)
            self.assertIn("missing ## Automated Checks", errors[0])


if __name__ == "__main__":
    unittest.main()
