"""Max harness protocol — shared by the studio client and the in-Max listener."""

from __future__ import annotations

from typing import Any

PROTOCOL_V = 1
DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 17927
OPS = frozenset({"ping", "bootstrap", "filein", "eval_ms", "eval_py", "scene_info"})


def request(op: str, *, path: str | None = None, code: str | None = None, id: str | None = None) -> dict[str, Any]:
    if op not in OPS:
        raise ValueError(f"unknown harness op: {op}")
    msg: dict[str, Any] = {"v": PROTOCOL_V, "op": op}
    if path is not None:
        msg["path"] = path
    if code is not None:
        msg["code"] = code
    if id is not None:
        msg["id"] = id
    return msg


def ok(op: str, *, result: Any = None, log: str = "", **extra: Any) -> dict[str, Any]:
    payload: dict[str, Any] = {"v": PROTOCOL_V, "ok": True, "op": op, "log": log}
    if result is not None:
        payload["result"] = result
    payload.update(extra)
    return payload


def err(op: str, error: str, **extra: Any) -> dict[str, Any]:
    payload: dict[str, Any] = {"v": PROTOCOL_V, "ok": False, "op": op, "error": error}
    payload.update(extra)
    return payload


def parse_request(data: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(data, dict):
        raise ValueError("harness request must be a JSON object")
    if data.get("v") != PROTOCOL_V:
        raise ValueError(f"unsupported protocol v: {data.get('v')}")
    op = data.get("op")
    if op not in OPS:
        raise ValueError(f"unknown harness op: {op}")
    return data
