from __future__ import annotations

import json
import os
import sys
import threading
import unittest
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from polycraft.api import max_bootstrap, max_job, max_run, max_status  # noqa: E402
from polycraft.harness import ok  # noqa: E402


class _Mock(BaseHTTPRequestHandler):
    ops: list[dict] = []

    def log_message(self, fmt: str, *args) -> None:  # noqa: A003
        return

    def _send(self, payload: dict) -> None:
        raw = json.dumps(payload).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def do_GET(self) -> None:  # noqa: N802
        self._send(ok("ping", result={"maxVersion": 29000, "mock": True}))

    def do_POST(self) -> None:  # noqa: N802
        length = int(self.headers.get("Content-Length") or "0")
        data = json.loads(self.rfile.read(length).decode("utf-8"))
        _Mock.ops.append(data)
        self._send(ok(data.get("op") or "unknown", result={"mock": True, "path": data.get("path")}))


class HarnessMockTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        _Mock.ops = []
        cls.server = HTTPServer(("127.0.0.1", 0), _Mock)
        cls.port = cls.server.server_address[1]
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        os.environ["POLYCRAFT_MAX_HOST"] = "127.0.0.1"
        os.environ["POLYCRAFT_MAX_PORT"] = str(cls.port)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.server.shutdown()
        os.environ.pop("POLYCRAFT_MAX_PORT", None)

    def test_status_live(self) -> None:
        st = max_status()
        self.assertTrue(st.reachable)
        self.assertEqual(st.backend, "live")
        self.assertEqual(st.detail["result"]["maxVersion"], 29000)

    def test_bootstrap_and_kit_job_hit_harness(self) -> None:
        _Mock.ops.clear()
        boot = max_bootstrap(ROOT)
        self.assertTrue(boot.ok, boot.error)
        self.assertEqual(boot.backend, "live")
        run = max_run(ROOT / "kits" / "middlehelm-wetlands-ruins" / "max" / "mhwr_first_assembly.ms")
        self.assertTrue(run.ok, run.error)
        ops = [item["op"] for item in _Mock.ops]
        self.assertIn("bootstrap", ops)
        self.assertIn("filein", ops)

    def test_named_job_runs_bootstrap_then_assembly(self) -> None:
        _Mock.ops.clear()
        result = max_job("middlehelm-wetlands-ruins", "first-assembly", ROOT)
        self.assertTrue(result.ok, result.error)
        ops = [item["op"] for item in _Mock.ops]
        self.assertEqual(ops[0], "bootstrap")
        self.assertEqual(ops[1], "filein")
        self.assertTrue(str(_Mock.ops[1]["path"]).endswith("mhwr_first_assembly.ms"))


if __name__ == "__main__":
    unittest.main()
