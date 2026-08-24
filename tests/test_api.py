from __future__ import annotations

import json
import py_compile
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from polycraft.api import get_kit, list_kits, validate_briefs  # noqa: E402
from polycraft.root import repo_root  # noqa: E402


class ApiTests(unittest.TestCase):
    def test_repo_root(self) -> None:
        self.assertEqual(repo_root(ROOT / "src" / "polycraft"), ROOT)

    def test_list_kits_includes_middlehelm_as_a_kit(self) -> None:
        kits = list_kits(ROOT)
        ids = [k.id for k in kits]
        self.assertIn("middlehelm-wetlands-ruins", ids)
        mh = get_kit("middlehelm-wetlands-ruins", ROOT)
        self.assertEqual(mh.status, "planned")
        self.assertIn("first-assembly", mh.jobs)
        self.assertTrue(mh.jobs["first-assembly"].resolve(mh.path).is_file())

    def test_validate_all_briefs(self) -> None:
        report = validate_briefs(ROOT)
        self.assertTrue(report.ok, json.dumps(report.to_dict(), indent=2))

    def test_listener_compiles_without_max(self) -> None:
        py_compile.compile(str(ROOT / "max" / "harness" / "listener.py"), doraise=True)


if __name__ == "__main__":
    unittest.main()
