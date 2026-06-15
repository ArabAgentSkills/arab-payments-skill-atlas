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
    def test_semantic_html_navigation_chrome_does_not_change_normalized_text(self) -> None:
        first = b"""
        <html><body>
          <nav>Home Guides API Reference Login</nav>
          <aside>Payments API Create Payment Fetch Payment</aside>
          <main><h1>Webhook Reference</h1><p>Payment Event payment_paid requires server verification.</p></main>
          <footer>Copyright 2026 Provider</footer>
        </body></html>
        """
        second = b"""
        <html><body>
          <nav>Home Guides API Reference Login Card Authentication API</nav>
          <aside>Payments API Create Payment Fetch Payment Card Authentication API</aside>
          <main><h1>Webhook Reference</h1><p>Payment Event payment_paid requires server verification.</p></main>
          <footer>Copyright 2026 Provider</footer>
        </body></html>
        """

        self.assertEqual(
            check_source_changes.normalize_text(first, "text/html"),
            check_source_changes.normalize_text(second, "text/html"),
        )

    def test_agent_readable_index_notice_does_not_change_normalized_text(self) -> None:
        first = (
            b"Webhook For AI agents: visit https://docs.example.com/llms.txt for an index "
            b"of all pages formatted in Markdown and endpoints in OpenAPI. "
            b"Payment Event payment_paid requires server verification."
        )
        second = b"Webhook Payment Event payment_paid requires server verification."

        self.assertEqual(
            check_source_changes.normalize_text(first, "text/plain"),
            check_source_changes.normalize_text(second, "text/plain"),
        )

    def test_relative_updated_age_does_not_change_normalized_text(self) -> None:
        first = b"Webhook V2 Updated 3 months ago Webhook Signature Payment Status Data Model"
        second = b"Webhook V2 Updated 4 months ago Webhook Signature Payment Status Data Model"

        self.assertEqual(
            check_source_changes.normalize_text(first, "text/plain"),
            check_source_changes.normalize_text(second, "text/plain"),
        )

    def test_approximate_relative_updated_age_does_not_change_normalized_text(self) -> None:
        first = b"API Actions Updated about 1 year ago Capture Payment"
        second = b"API Actions Updated about 2 years ago Capture Payment"

        self.assertEqual(
            check_source_changes.normalize_text(first, "text/plain"),
            check_source_changes.normalize_text(second, "text/plain"),
        )

    def test_gitbook_llms_markdown_notice_does_not_change_normalized_text(self) -> None:
        first = (
            b"Pay API For the complete documentation index, see llms.txt . "
            b"This page is also available as Markdown . Callback response verification"
        )
        second = b"Pay API Callback response verification"

        self.assertEqual(
            check_source_changes.normalize_text(first, "text/plain"),
            check_source_changes.normalize_text(second, "text/plain"),
        )

    def test_recent_requests_widget_chrome_does_not_change_normalized_text(self) -> None:
        first = (
            b"Capture Transaction Recent Requests Log in to see full request history "
            b"Time Status User Agent Retrieving recent requests... Loading Loading Body amount currency"
        )
        second = b"Capture Transaction Body amount currency"

        self.assertEqual(
            check_source_changes.normalize_text(first, "text/plain"),
            check_source_changes.normalize_text(second, "text/plain"),
        )

    def test_recent_requests_widget_with_ellipsis_does_not_change_normalized_text(self) -> None:
        first = (
            "Capture Transaction Recent Requests Log in to see full request history "
            "Time Status User Agent Retrieving recent requests\u2026 Loading\u2026 Body amount currency"
        ).encode()
        second = b"Capture Transaction Body amount currency"

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


class GitHubRepoApiUrlTests(unittest.TestCase):
    def test_github_repo_root_uses_api_url(self) -> None:
        self.assertEqual(
            check_source_changes.github_source_api_url("https://github.com/Kashier-payments/NodeJs-Checkout-Demo"),
            "https://api.github.com/repos/Kashier-payments/NodeJs-Checkout-Demo",
        )

    def test_github_org_root_uses_api_url(self) -> None:
        self.assertEqual(
            check_source_changes.github_source_api_url("https://github.com/Kashier-payments"),
            "https://api.github.com/orgs/Kashier-payments",
        )

    def test_github_deeper_path_is_not_rewritten(self) -> None:
        self.assertIsNone(
            check_source_changes.github_source_api_url(
                "https://github.com/Kashier-payments/NodeJs-Checkout-Demo/blob/main/README.md"
            )
        )


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

    def test_ok_baseline_with_current_js_challenge_is_not_a_change(self) -> None:
        url = "https://github.com/Kashier-payments/NodeJs-Checkout-Demo"
        baseline = {
            url: {
                "url": url,
                "provider_ids": ["egypt-payment-guardian:kashier", "mena-payment-guardian:kashier"],
                "status": "OK",
                "sha256": "abc123",
            }
        }
        current = [
            {
                "url": url,
                "provider_ids": ["egypt-payment-guardian:kashier", "mena-payment-guardian:kashier"],
                "status": "JS_CHALLENGE",
                "sha256": "",
                "http_status": 403,
                "excerpt": "GitHub API verification requires retry or manual browser verification.",
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

    def test_ok_baseline_with_current_transient_http_error_is_not_a_change(self) -> None:
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
                "http_status": 429,
                "sha256": "",
                "excerpt": "HTTP error 429.",
            }
        ]

        self.assertEqual(check_source_changes.compare_records(current, baseline), [])

    def test_ok_baseline_with_current_non_transient_http_error_is_a_change(self) -> None:
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
                "http_status": 404,
                "sha256": "",
                "excerpt": "HTTP error 404.",
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
