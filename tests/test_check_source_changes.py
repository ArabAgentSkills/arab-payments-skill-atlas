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


if __name__ == "__main__":
    unittest.main()
