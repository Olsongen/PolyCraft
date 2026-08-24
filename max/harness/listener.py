"""PolyCraft harness — runs INSIDE 3ds Max 2027.

Starts a localhost HTTP listener on 127.0.0.1:17927. pymxs work is pumped
on the Max main thread via a Qt timer. Agents talk through the PolyCraft
API / CLI / MCP — do not ask artists to drag scripts.

This file is safe to open outside Max: it exits with a clear error.
"""

from __future__ import annotations

import json
import sys
import threading
import traceback
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from queue import Empty, Queue
from typing import Any

REPO = Path(__file__).resolve().parents[2]
SRC = REPO / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from polycraft.harness import DEFAULT_HOST, DEFAULT_PORT, err, ok, parse_request  # noqa: E402
from polycraft.root import repo_root  # noqa: E402

_JOBS: Queue = Queue()


def _in_max() -> bool:
    try:
        from pymxs import runtime as _rt  # noqa: F401

        return True
    except Exception:
        return False


def _run_op(data: dict[str, Any]) -> dict[str, Any]:
    from pymxs import runtime as rt

    op = data["op"]
    if op == "ping":
        ver = int(rt.maxVersion()[1])
        return ok(
            op,
            result={
                "maxVersion": ver,
                "host": "3ds Max 2027" if ver >= 29000 else f"unsupported:{ver}",
            },
        )
    if op == "scene_info":
        names: list[str] = []
        objs = rt.objects
        try:
            for obj in objs:
                names.append(str(obj.name))
        except TypeError:
            for i in range(1, int(objs.count) + 1):
                names.append(str(objs[i].name))
        formatted = str(rt.units.formatValue(400.0))
        return ok(
            op,
            result={
                "nodes": names,
                "systemType": str(rt.units.SystemType),
                "displayType": str(rt.units.DisplayType),
                "format400cm": formatted,
            },
        )
    if op in {"filein", "bootstrap"}:
        path = data.get("path")
        if op == "bootstrap" and not path:
            path = str((repo_root(REPO) / "max" / "polycraft_bootstrap.ms").resolve())
        if not path:
            return err(op, "path required")
        rt.fileIn(path)
        return ok(op, result={"path": path})
    if op == "eval_ms":
        code = data.get("code") or ""
        result = rt.execute(code)
        return ok(op, result=_stringify(result))
    if op == "eval_py":
        code = data.get("code") or ""
        local: dict[str, Any] = {}
        exec(compile(code, "<polycraft-eval>", "exec"), {"rt": rt, "__builtins__": __builtins__}, local)  # noqa: S102
        value = local.get("result", local.get("out"))
        return ok(op, result=_stringify(value))
    return err(op, f"unhandled op {op}")


def _stringify(value: Any) -> Any:
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    return str(value)


def _execute_on_main(data: dict[str, Any]) -> dict[str, Any]:
    try:
        parsed = parse_request(data)
        return _run_op(parsed)
    except Exception as exc:  # noqa: BLE001
        return err(str(data.get("op") or "unknown"), f"{exc}\n{traceback.format_exc()}")


class _Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def log_message(self, fmt: str, *args: Any) -> None:
        sys.stderr.write("PolyCraft harness: " + (fmt % args) + "\n")

    def _send(self, code: int, payload: dict[str, Any]) -> None:
        raw = json.dumps(payload).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def do_GET(self) -> None:  # noqa: N802
        if self.path.rstrip("/") == "/health":
            box: dict[str, Any] = {}
            _JOBS.put(("health", {}, box))
            self._wait(box)
            health = box.get("reply") or err("ping", "no reply")
            self._send(200 if health.get("ok") else 503, health)
            return
        self._send(404, err("ping", "not found"))

    def do_POST(self) -> None:  # noqa: N802
        if self.path.rstrip("/") != "/exec":
            self._send(404, err("unknown", "not found"))
            return
        length = int(self.headers.get("Content-Length") or "0")
        raw = self.rfile.read(length)
        try:
            data = json.loads(raw.decode("utf-8"))
        except json.JSONDecodeError as exc:
            self._send(400, err("unknown", f"bad json: {exc}"))
            return
        box: dict[str, Any] = {}
        _JOBS.put(("exec", data, box))
        self._wait(box)
        reply = box.get("reply") or err(str(data.get("op") or "unknown"), "no reply")
        self._send(200 if reply.get("ok") else 400, reply)

    def _wait(self, box: dict[str, Any], timeout: float = 120.0) -> None:
        event = threading.Event()
        box["event"] = event
        event.wait(timeout)
        if "reply" not in box:
            box["reply"] = err("unknown", "timed out waiting for Max main thread")


def drain_jobs() -> None:
    while True:
        try:
            kind, data, box = _JOBS.get_nowait()
        except Empty:
            return
        if kind == "health":
            box["reply"] = _execute_on_main({"v": 1, "op": "ping"})
        else:
            box["reply"] = _execute_on_main(data)
        event = box.get("event")
        if event is not None:
            event.set()


def _start_pump() -> None:
    try:
        import qtmax
        from PySide6 import QtCore
    except Exception:
        drain_jobs()
        return

    parent = qtmax.GetQMaxMainWindow()

    class Pump(QtCore.QObject):
        def __init__(self) -> None:
            super().__init__(parent)
            timer = QtCore.QTimer(self)
            timer.setInterval(50)
            timer.timeout.connect(drain_jobs)
            timer.start()
            self._timer = timer

    pump = Pump()
    parent._polycraft_harness_pump = pump  # keep alive on the main window


def start(host: str = DEFAULT_HOST, port: int = DEFAULT_PORT) -> None:
    if not _in_max():
        raise RuntimeError("PolyCraft harness listener runs inside 3ds Max 2027 only.")
    from pymxs import runtime as rt

    if int(rt.maxVersion()[1]) < 29000:
        raise RuntimeError("PolyCraft requires 3ds Max 2027 (maxVersion 29000).")

    _start_pump()
    server = ThreadingHTTPServer((host, port), _Handler)
    thread = threading.Thread(target=server.serve_forever, name="polycraft-harness", daemon=True)
    thread.start()
    msg = f"PolyCraft harness listening on http://{host}:{port}  (API/CLI/MCP)\n"
    print(msg, flush=True)
    try:
        rt.format(msg)
    except Exception:
        pass


if __name__ == "__main__":
    if not _in_max():
        sys.stderr.write("This listener must be started inside 3ds Max 2027.\n")
        sys.stderr.write("On the Max box: polycraft max install-harness && start Max 2027.\n")
        raise SystemExit(2)
    start()
