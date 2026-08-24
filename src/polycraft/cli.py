from __future__ import annotations

import argparse
import json
import sys
from typing import Any

from polycraft import api


def _print(data: Any, as_json: bool) -> None:
    if as_json or not isinstance(data, (dict, list)):
        print(json.dumps(data, indent=2))
        return
    print(json.dumps(data, indent=2))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="polycraft",
        description="Agentic kit studio — API / CLI / MCP for 3ds Max 2027.",
    )
    parser.add_argument("--json", action="store_true", help="JSON output (always on for now)")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("kits", help="List kits and status")
    kit = sub.add_parser("kit", help="Show one kit")
    kit.add_argument("id")
    kit.add_argument("--brief", action="store_true")

    val = sub.add_parser("validate", help="Validate kit briefs")
    val.add_argument("--kit")

    mx = sub.add_parser("max", help="Drive Max 2027 through the harness")
    mx_sub = mx.add_subparsers(dest="max_cmd", required=True)
    mx_sub.add_parser("status", help="Ping the live harness")
    mx_sub.add_parser("install-harness", help="Install Max startup listener (Windows)")
    mx_sub.add_parser("bootstrap", help="Run studio units/grid bootstrap in Max")
    run = mx_sub.add_parser("run", help="fileIn a script in Max")
    run.add_argument("script")
    job = mx_sub.add_parser("job", help="Run a named kit job")
    job.add_argument("kit")
    job.add_argument("name")
    ev = mx_sub.add_parser("eval", help="Eval MAXScript or Python in the live session")
    lang = ev.add_mutually_exclusive_group(required=True)
    lang.add_argument("--ms", dest="ms")
    lang.add_argument("--py", dest="py")

    args = parser.parse_args(argv)

    if args.cmd == "kits":
        _print([k.to_dict() for k in api.list_kits()], True)
        return 0
    if args.cmd == "kit":
        _print(api.get_kit(args.id).to_dict(include_brief=args.brief), True)
        return 0
    if args.cmd == "validate":
        report = api.validate_briefs(kit_id=args.kit)
        _print(report.to_dict(), True)
        return 0 if report.ok else 1
    if args.cmd == "max":
        if args.max_cmd == "status":
            st = api.max_status()
            _print(st.to_dict(), True)
            return 0 if st.reachable or st.backend == "batch" else 2
        if args.max_cmd == "install-harness":
            result = api.install_harness()
            _print(result, True)
            return 0 if result.get("ok") else 2
        if args.max_cmd == "bootstrap":
            result = api.max_bootstrap()
            _print(result.to_dict(), True)
            return 0 if result.ok else 2
        if args.max_cmd == "run":
            result = api.max_run(args.script)
            _print(result.to_dict(), True)
            return 0 if result.ok else 2
        if args.max_cmd == "job":
            result = api.max_job(args.kit, args.name)
            _print(result.to_dict(), True)
            return 0 if result.ok else 2
        if args.max_cmd == "eval":
            if args.ms:
                result = api.max_eval(args.ms, lang="ms")
            else:
                result = api.max_eval(args.py, lang="py")
            _print(result.to_dict(), True)
            return 0 if result.ok else 2
    parser.error("unknown command")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
