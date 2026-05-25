from __future__ import annotations

import importlib.util
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "check_source_changes.py"

spec = importlib.util.spec_from_file_location("check_source_changes", MODULE_PATH)
assert spec is not None
check_source_changes = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(check_source_changes)


class SnapshotFilenameTests(unittest.TestCase):
    def test_snapshot_filename_removes_artifact_invalid_characters(self) -> None:
        filename = check_source_changes.snapshot_filename(
            [
                "egypt-payment-guardian:easykash-egypt",
                "mena-payment-guardian:easykash-mena",
            ],
            "https://example.com/docs?country=eg&merchant=demo",
        )

        self.assertTrue(filename.endswith(".txt"))
        self.assertNotRegex(filename, re.compile(r'[<>:"/\\|?*\r\n]'))
        self.assertIn("egypt-payment-guardian-easykash-egypt", filename)
        self.assertLessEqual(len(filename), check_source_changes.MAX_ARTIFACT_FILENAME_CHARS)


class CompareRecordsTests(unittest.TestCase):
    def test_ok_baseline_with_current_tls_verify_is_not_a_change(self) -> None:
        url = "https://hyperpay.docs.oppwa.com/integrations/widget"
        baseline = {
            url: {
                "url": url,
                "provider_ids": ["mena-payment-guardian:hyperpay"],
                "status": "OK",
                "sha256": "abc123",
            }
        }
        current = [
            {
                "url": url,
                "provider_ids": ["mena-payment-guardian:hyperpay"],
                "status": "TLS_VERIFY",
                "sha256": "",
            }
        ]

        self.assertEqual(check_source_changes.compare_records(current, baseline), [])

    def test_ok_baseline_with_current_ok_hash_mismatch_is_a_change(self) -> None:
        url = "https://hyperpay.docs.oppwa.com/integrations/widget"
        baseline = {
            url: {
                "url": url,
                "provider_ids": ["mena-payment-guardian:hyperpay"],
                "status": "OK",
                "sha256": "abc123",
            }
        }
        current = [
            {
                "url": url,
                "provider_ids": ["mena-payment-guardian:hyperpay"],
                "status": "OK",
                "sha256": "def456",
            }
        ]

        changes = check_source_changes.compare_records(current, baseline)

        self.assertEqual(len(changes), 1)
        self.assertEqual(changes[0]["change"], "CHANGED")


if __name__ == "__main__":
    unittest.main()
