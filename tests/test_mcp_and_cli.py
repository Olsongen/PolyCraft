from __future__ import annotations

import json
import os
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from polycraft.mcp_server import call_tool, handle  # noqa: E402


class McpTests(unittest.TestCase):
    def test_initialize_and_tools(self) -> None:
        init = handle({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}})
        assert init is not None
        self.assertEqual(init["result"]["serverInfo"]["name"], "polycraft")
        listed = handle({"jsonrpc": "2.0", "id": 2, "method": "tools/list"})
        assert listed is not None
        names = [t["name"] for t in listed["result"]["tools"]]
        self.assertIn("polycraft_max_bootstrap", names)
        self.assertIn("polycraft_kits_list", names)

    def test_kits_list_tool(self) -> None:
        result = call_tool("polycraft_kits_list", {})
        self.assertFalse(result["isError"])
        kits = json.loads(result["content"][0]["text"])
        self.assertTrue(any(k["id"] == "middlehelm-wetlands-ruins" for k in kits))


class CliTests(unittest.TestCase):
    def _run(self, *args: str) -> subprocess.CompletedProcess[str]:
        env = os.environ.copy()
        env["PYTHONPATH"] = str(ROOT / "src")
        env["POLYCRAFT_ROOT"] = str(ROOT)
        return subprocess.run(
            [sys.executable, "-m", "polycraft", *args],
            cwd=str(ROOT),
            capture_output=True,
            text=True,
            env=env,
            check=False,
        )

    def test_kits_and_validate(self) -> None:
        kits = self._run("kits")
        self.assertEqual(kits.returncode, 0, kits.stderr)
        data = json.loads(kits.stdout)
        self.assertEqual(data[0]["id"], "middlehelm-wetlands-ruins")
        val = self._run("validate")
        self.assertEqual(val.returncode, 0, val.stderr)
        self.assertTrue(json.loads(val.stdout)["ok"])

    def test_max_status_unreachable_here(self) -> None:
        env_port = os.environ.get("POLYCRAFT_MAX_PORT")
        # Isolate from any mock left in this process; the CLI is a subprocess.
        status = self._run("max", "status")
        body = json.loads(status.stdout)
        if env_port:
            self.skipTest("harness mock port leaked into env")
        self.assertFalse(body["reachable"])
        self.assertEqual(body["backend"], "unreachable")
        self.assertEqual(body["v1_host"], "windows-max2027-local")
        self.assertIn("install-harness", body["hint"])


if __name__ == "__main__":
    unittest.main()
