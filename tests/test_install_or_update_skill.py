from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "install_or_update_skill.py"

spec = importlib.util.spec_from_file_location("install_or_update_skill", MODULE_PATH)
assert spec is not None
install_or_update_skill = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(install_or_update_skill)


class GitHubHeaderTests(unittest.TestCase):
    def test_github_headers_uses_available_token(self) -> None:
        with mock.patch.dict("os.environ", {"GH_TOKEN": "test-token"}, clear=True):
            headers = install_or_update_skill.github_headers()

        self.assertEqual(headers["Authorization"], "Bearer test-token")
        self.assertEqual(headers["Accept"], "application/vnd.github+json")

    def test_github_headers_does_not_require_token(self) -> None:
        with mock.patch.dict("os.environ", {}, clear=True):
            headers = install_or_update_skill.github_headers()

        self.assertNotIn("Authorization", headers)


if __name__ == "__main__":
    unittest.main()
