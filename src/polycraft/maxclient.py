"""Client for the in-Max harness. Live HTTP first, then 3dsmaxbatch on Windows."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from polycraft.harness import DEFAULT_HOST, DEFAULT_PORT, request
from polycraft.root import repo_root


@dataclass
class MaxStatus:
    reachable: bool
    backend: str
    host: str
    port: int
    detail: dict[str, Any] = field(default_factory=dict)
    hint: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "reachable": self.reachable,
            "backend": self.backend,
            "host": self.host,
            "port": self.port,
            "detail": self.detail,
            "hint": self.hint,
            "v1_host": "windows-max2027-local",
            "platform": sys.platform,
        }


@dataclass
class ExecResult:
    ok: bool
    backend: str
    op: str
    payload: dict[str, Any] = field(default_factory=dict)
    error: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "ok": self.ok,
            "backend": self.backend,
            "op": self.op,
            "payload": self.payload,
            "error": self.error,
        }


class MaxUnreachable(RuntimeError):
    pass


def harness_host() -> str:
    return os.environ.get("POLYCRAFT_MAX_HOST", DEFAULT_HOST)


def harness_port() -> int:
    return int(os.environ.get("POLYCRAFT_MAX_PORT", DEFAULT_PORT))


def _url(host: str, port: int, path: str) -> str:
    return f"http://{host}:{port}{path}"


def live_exec(
    op: str,
    *,
    path: str | None = None,
    code: str | None = None,
    host: str | None = None,
    port: int | None = None,
    timeout: float = 30.0,
) -> dict[str, Any]:
    host = host or harness_host()
    port = port if port is not None else harness_port()
    body = json.dumps(request(op, path=path, code=code)).encode("utf-8")
    req = urllib.request.Request(
        _url(host, port, "/exec"),
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.URLError as exc:
        raise MaxUnreachable(f"Max harness not reachable at {host}:{port}: {exc}") from exc


def live_ping(host: str | None = None, port: int | None = None, timeout: float = 0.6) -> dict[str, Any]:
    host = host or harness_host()
    port = port if port is not None else harness_port()
    try:
        with urllib.request.urlopen(_url(host, port, "/health"), timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.URLError as exc:
        raise MaxUnreachable(f"Max harness not reachable at {host}:{port}: {exc}") from exc


def find_3dsmax_dir() -> Path | None:
    env = os.environ.get("ADSK_3DSMAX_x64_2027")
    if env and Path(env).is_dir():
        return Path(env)
    if sys.platform == "win32":
        programmed = Path(r"C:\Program Files\Autodesk\3ds Max 2027")
        if programmed.is_dir():
            return programmed
    return None


def find_3dsmaxbatch() -> Path | None:
    named = shutil.which("3dsmaxbatch")
    if named:
        return Path(named)
    root = find_3dsmax_dir()
    if root:
        candidate = root / "3dsmaxbatch.exe"
        if candidate.is_file():
            return candidate
    return None


def max_user_startup_dirs() -> list[Path]:
    home = Path.home()
    roots = [
        home / "AppData" / "Local" / "Autodesk" / "3dsMax",
    ]
    found: list[Path] = []
    for root in roots:
        if not root.is_dir():
            continue
        for match in root.glob("2027*/scripts/startup"):
            if match.is_dir():
                found.append(match)
    return found


def install_harness(root: Path | None = None) -> dict[str, Any]:
    root = root or repo_root()
    listener = root / "max" / "harness" / "listener.py"
    if not listener.is_file():
        raise FileNotFoundError(listener)
    posix = listener.resolve().as_posix()
    snippet = (
        "-- PolyCraft harness (generated). Starts the localhost API inside Max 2027.\n"
        f'python.ExecuteFile @"{posix}"\n'
    )
    dirs = max_user_startup_dirs()
    if not dirs:
        return {
            "ok": False,
            "installed": False,
            "startup_ms": snippet,
            "listener": str(listener),
            "error": (
                "Max 2027 user startup folder not found. "
                "On the Windows box with Max installed, run: polycraft max install-harness"
            ),
        }
    written = []
    for folder in dirs:
        target = folder / "polycraft_harness.ms"
        target.write_text(snippet, encoding="utf-8")
        written.append(str(target))
    return {
        "ok": True,
        "installed": True,
        "written": written,
        "listener": str(listener),
        "hint": "Restart 3ds Max 2027. Harness listens on 127.0.0.1:17927",
    }


def batch_filein(script: Path, timeout: float = 180.0) -> dict[str, Any]:
    exe = find_3dsmaxbatch()
    if exe is None:
        raise MaxUnreachable(
            "3dsmaxbatch not found. Install Max 2027 or start Max with the harness."
        )
    script = script.resolve()
    if not script.is_file():
        raise FileNotFoundError(script)
    proc = subprocess.run(
        [str(exe), str(script)],
        capture_output=True,
        text=True,
        timeout=timeout,
        check=False,
    )
    log = (proc.stdout or "") + (proc.stderr or "")
    return {
        "v": 1,
        "ok": proc.returncode == 0,
        "op": "filein",
        "backend": "batch",
        "log": log,
        "returncode": proc.returncode,
    }


UNREACHABLE_HINT = (
    "Max 2027 harness not on localhost. v1 agents run on the Windows PC that has Max. "
    "Start 3ds Max 2027, then: python -m polycraft max install-harness (once) "
    "and python -m polycraft max bootstrap."
)


def status(host: str | None = None, port: int | None = None) -> MaxStatus:
    host = host or harness_host()
    port = port if port is not None else harness_port()
    try:
        detail = live_ping(host, port)
        return MaxStatus(
            reachable=True,
            backend="live",
            host=host,
            port=port,
            detail=detail,
        )
    except MaxUnreachable as exc:
        batch = find_3dsmaxbatch()
        if batch:
            return MaxStatus(
                reachable=False,
                backend="batch",
                host=host,
                port=port,
                detail={"3dsmaxbatch": str(batch), "live_error": str(exc)},
                hint="Harness down; batch fallback is available for filein.",
            )
        return MaxStatus(
            reachable=False,
            backend="unreachable",
            host=host,
            port=port,
            detail={"live_error": str(exc)},
            hint=UNREACHABLE_HINT,
        )


def exec_op(
    op: str,
    *,
    path: str | None = None,
    code: str | None = None,
    allow_batch: bool = True,
    host: str | None = None,
    port: int | None = None,
) -> ExecResult:
    try:
        payload = live_exec(op, path=path, code=code, host=host, port=port)
        return ExecResult(
            ok=bool(payload.get("ok")),
            backend="live",
            op=op,
            payload=payload,
            error=None if payload.get("ok") else payload.get("error"),
        )
    except MaxUnreachable as live_err:
        if allow_batch and op in {"filein", "bootstrap"} and path:
            try:
                payload = batch_filein(Path(path))
                return ExecResult(
                    ok=bool(payload.get("ok")),
                    backend="batch",
                    op=op,
                    payload=payload,
                    error=None if payload.get("ok") else payload.get("log"),
                )
            except MaxUnreachable:
                pass
        return ExecResult(
            ok=False,
            backend="unreachable",
            op=op,
            error=f"{live_err} {UNREACHABLE_HINT}",
        )
