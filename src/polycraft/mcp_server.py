"""stdio MCP server. Surfaces the same API as the CLI."""

from __future__ import annotations

import json
import sys
from typing import Any

from polycraft import api

PROTOCOL_VERSION = "2024-11-05"

TOOLS: list[dict[str, Any]] = [
    {
        "name": "polycraft_kits_list",
        "description": "List PolyKits with status, camera, and harness jobs.",
        "inputSchema": {"type": "object", "properties": {}},
    },
    {
        "name": "polycraft_kit_get",
        "description": "Get one kit record. Set include_brief to attach brief.json.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "include_brief": {"type": "boolean"},
            },
            "required": ["id"],
        },
    },
    {
        "name": "polycraft_validate",
        "description": "Validate kit briefs against contracts/kit.schema.json.",
        "inputSchema": {
            "type": "object",
            "properties": {"kit": {"type": "string"}},
        },
    },
    {
        "name": "polycraft_max_status",
        "description": "Ping the 3ds Max 2027 harness (localhost:17927).",
        "inputSchema": {"type": "object", "properties": {}},
    },
    {
        "name": "polycraft_max_bootstrap",
        "description": "Run studio bootstrap in Max (units, grid, PC_ QA plane). Agent-driven; do not ask the user to drag a script.",
        "inputSchema": {"type": "object", "properties": {}},
    },
    {
        "name": "polycraft_max_run",
        "description": "fileIn a MAXScript or path relative to the repo inside Max.",
        "inputSchema": {
            "type": "object",
            "properties": {"script": {"type": "string"}},
            "required": ["script"],
        },
    },
    {
        "name": "polycraft_max_job",
        "description": "Run a named kit job (e.g. first-assembly) through the harness.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "kit": {"type": "string"},
                "job": {"type": "string"},
            },
            "required": ["kit", "job"],
        },
    },
    {
        "name": "polycraft_max_eval",
        "description": "Evaluate MAXScript or Python in the live Max session.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "lang": {"type": "string", "enum": ["ms", "py"]},
                "code": {"type": "string"},
            },
            "required": ["lang", "code"],
        },
    },
]


def _text(payload: Any, is_error: bool = False) -> dict[str, Any]:
    text = payload if isinstance(payload, str) else json.dumps(payload, indent=2)
    return {"content": [{"type": "text", "text": text}], "isError": is_error}


def call_tool(name: str, arguments: dict[str, Any] | None) -> dict[str, Any]:
    args = arguments or {}
    try:
        if name == "polycraft_kits_list":
            return _text([k.to_dict() for k in api.list_kits()])
        if name == "polycraft_kit_get":
            kit = api.get_kit(args["id"])
            return _text(kit.to_dict(include_brief=bool(args.get("include_brief"))))
        if name == "polycraft_validate":
            report = api.validate_briefs(kit_id=args.get("kit"))
            return _text(report.to_dict(), is_error=not report.ok)
        if name == "polycraft_max_status":
            return _text(api.max_status().to_dict())
        if name == "polycraft_max_bootstrap":
            result = api.max_bootstrap()
            return _text(result.to_dict(), is_error=not result.ok)
        if name == "polycraft_max_run":
            result = api.max_run(args["script"])
            return _text(result.to_dict(), is_error=not result.ok)
        if name == "polycraft_max_job":
            result = api.max_job(args["kit"], args["job"])
            return _text(result.to_dict(), is_error=not result.ok)
        if name == "polycraft_max_eval":
            result = api.max_eval(args["code"], lang=args["lang"])
            return _text(result.to_dict(), is_error=not result.ok)
        return _text({"error": f"unknown tool: {name}"}, is_error=True)
    except Exception as exc:  # noqa: BLE001 — surface to the agent
        return _text({"error": str(exc)}, is_error=True)


def handle(message: dict[str, Any]) -> dict[str, Any] | None:
    method = message.get("method")
    msg_id = message.get("id")
    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {
                "protocolVersion": PROTOCOL_VERSION,
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "polycraft", "version": "0.1.0"},
            },
        }
    if method == "notifications/initialized":
        return None
    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": msg_id, "result": {"tools": TOOLS}}
    if method == "tools/call":
        params = message.get("params") or {}
        result = call_tool(params.get("name"), params.get("arguments"))
        return {"jsonrpc": "2.0", "id": msg_id, "result": result}
    if method == "ping":
        return {"jsonrpc": "2.0", "id": msg_id, "result": {}}
    if msg_id is None:
        return None
    return {
        "jsonrpc": "2.0",
        "id": msg_id,
        "error": {"code": -32601, "message": f"method not found: {method}"},
    }


def _read_message(stdin) -> dict[str, Any] | None:
    headers: dict[str, str] = {}
    while True:
        line = stdin.readline()
        if line == b"":
            return None
        if line in (b"\r\n", b"\n"):
            break
        decoded = line.decode("utf-8")
        if ":" not in decoded:
            continue
        key, value = decoded.split(":", 1)
        headers[key.strip().lower()] = value.strip()
    length = int(headers["content-length"])
    body = stdin.read(length)
    return json.loads(body.decode("utf-8"))


def _write_message(stdout, message: dict[str, Any]) -> None:
    raw = json.dumps(message, separators=(",", ":")).encode("utf-8")
    stdout.write(f"Content-Length: {len(raw)}\r\n\r\n".encode("ascii") + raw)
    stdout.flush()


def serve() -> None:
    stdin = sys.stdin.buffer
    stdout = sys.stdout.buffer
    while True:
        try:
            message = _read_message(stdin)
        except Exception:
            return
        if message is None:
            return
        reply = handle(message)
        if reply is not None:
            _write_message(stdout, reply)


def main() -> None:
    serve()


if __name__ == "__main__":
    main()
