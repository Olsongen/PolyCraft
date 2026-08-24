from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

from polycraft.kits import get_kit, list_kits
from polycraft.root import repo_root


@dataclass
class ValidationReport:
    ok: bool
    results: list[dict] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {"ok": self.ok, "results": self.results}


def _require_fields(obj: dict, spec: dict, path: str, errors: list[str]) -> None:
    required = spec.get("required", [])
    props = spec.get("properties", {})
    for key in required:
        here = f"{path}.{key}" if path else key
        if key not in obj:
            errors.append(f"missing {here}")
            continue
        child_spec = props.get(key)
        if isinstance(obj[key], dict) and isinstance(child_spec, dict):
            _require_fields(obj[key], child_spec, here, errors)
    if spec.get("minItems") and isinstance(obj, list) and len(obj) < spec["minItems"]:
        errors.append(f"{path} has {len(obj)} items, min {spec['minItems']}")


def validate_one(brief: dict, schema: dict) -> list[str]:
    errors: list[str] = []
    _require_fields(brief, schema, "", errors)
    for field, spec in schema.get("properties", {}).items():
        if spec.get("type") == "array" and spec.get("minItems") and field in brief:
            if len(brief[field]) < spec["minItems"]:
                errors.append(
                    f"{field} has {len(brief[field])} items, min {spec['minItems']}"
                )
    mods = brief.get("modules", [])
    ids = [m.get("id") for m in mods]
    if len(ids) != len(set(ids)):
        errors.append("duplicate module ids")
    return errors


def validate_briefs(root: Path | None = None, kit_id: str | None = None) -> ValidationReport:
    root = root or repo_root()
    schema = json.loads((root / "contracts" / "kit.schema.json").read_text(encoding="utf-8"))
    kits = [get_kit(kit_id, root)] if kit_id else list_kits(root)
    if not kits:
        return ValidationReport(ok=False, results=[{"id": None, "errors": ["no kits found"]}])
    results = []
    ok = True
    for kit in kits:
        errors = validate_one(kit.brief, schema)
        results.append(
            {
                "id": kit.id,
                "path": str(kit.path / "brief.json"),
                "modules": len(kit.brief.get("modules") or []),
                "errors": errors,
            }
        )
        if errors:
            ok = False
    return ValidationReport(ok=ok, results=results)
