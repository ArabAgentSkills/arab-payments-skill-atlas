from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "check_source_links.py"

spec = importlib.util.spec_from_file_location("check_source_links", MODULE_PATH)
assert spec is not None
check_source_links = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(check_source_links)


class HttpStatusClassificationTests(unittest.TestCase):
    def test_provider_5xx_is_transient_not_broken(self) -> None:
        self.assertTrue(check_source_links.is_transient_http_status(500))
        self.assertTrue(check_source_links.is_transient_http_status(503))

    def test_clear_missing_link_is_not_transient(self) -> None:
        self.assertFalse(check_source_links.is_transient_http_status(404))
        self.assertFalse(check_source_links.is_transient_http_status(410))

    def test_rate_limit_style_status_is_transient(self) -> None:
        self.assertTrue(check_source_links.is_transient_http_status(408))
        self.assertTrue(check_source_links.is_transient_http_status(429))


if __name__ == "__main__":
    unittest.main()
