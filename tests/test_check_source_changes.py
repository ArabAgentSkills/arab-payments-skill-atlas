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


class NormalizeTextTests(unittest.TestCase):
    def test_relative_updated_age_does_not_change_normalized_text(self) -> None:
        first = b"Webhook V2 Updated 3 months ago Webhook Signature Payment Status Data Model"
        second = b"Webhook V2 Updated 4 months ago Webhook Signature Payment Status Data Model"

        self.assertEqual(
            check_source_changes.normalize_text(first, "text/plain"),
            check_source_changes.normalize_text(second, "text/plain"),
        )

    def test_hyperpay_greetings_nav_chrome_does_not_change_normalized_text(self) -> None:
        first = b"Products Blogs Board of Directors Greetings Contact us Integration Guides"
        second = b"Products Blogs Board of Directors Contact us Integration Guides"

        self.assertEqual(
            check_source_changes.normalize_text(first, "text/plain"),
            check_source_changes.normalize_text(second, "text/plain"),
        )

    def test_real_provider_content_change_still_changes_normalized_text(self) -> None:
        first = b"Webhook V2 validates webhook signatures before fulfillment"
        second = b"Webhook V2 accepts redirects before fulfillment"

        self.assertNotEqual(
            check_source_changes.normalize_text(first, "text/plain"),
            check_source_changes.normalize_text(second, "text/plain"),
        )


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

    def test_ok_baseline_with_current_transient_urlerror_is_not_a_change(self) -> None:
        url = "https://developer.fawrystaging.com/docs/introduction"
        baseline = {
            url: {
                "url": url,
                "provider_ids": ["egypt-payment-guardian:fawrypay"],
                "status": "OK",
                "sha256": "abc123",
            }
        }
        current = [
            {
                "url": url,
                "provider_ids": ["egypt-payment-guardian:fawrypay"],
                "status": "FAIL",
                "sha256": "",
                "excerpt": "URLError",
            }
        ]

        self.assertEqual(check_source_changes.compare_records(current, baseline), [])

    def test_ok_baseline_with_current_http_error_is_a_change(self) -> None:
        url = "https://developer.fawrystaging.com/docs/introduction"
        baseline = {
            url: {
                "url": url,
                "provider_ids": ["egypt-payment-guardian:fawrypay"],
                "status": "OK",
                "sha256": "abc123",
            }
        }
        current = [
            {
                "url": url,
                "provider_ids": ["egypt-payment-guardian:fawrypay"],
                "status": "HTTP_ERROR",
                "sha256": "",
                "excerpt": "HTTPError",
            }
        ]

        changes = check_source_changes.compare_records(current, baseline)

        self.assertEqual(len(changes), 1)
        self.assertEqual(changes[0]["change"], "CHANGED")

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
