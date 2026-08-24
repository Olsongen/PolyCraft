import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "contracts" / "kit.schema.json"
BRIEF_PATH = ROOT / "kits" / "middlehelm-wetlands-ruins" / "brief.json"


def require_fields(obj: dict, spec: dict, path: str, errors: list[str]) -> None:
    required = spec.get("required", [])
    props = spec.get("properties", {})
    for key in required:
        here = f"{path}.{key}" if path else key
        if key not in obj:
            errors.append(f"missing {here}")
            continue
        child_spec = props.get(key)
        if isinstance(obj[key], dict) and isinstance(child_spec, dict):
            require_fields(obj[key], child_spec, here, errors)
    if spec.get("minItems") and isinstance(obj, list) and len(obj) < spec["minItems"]:
        errors.append(f"{path} has {len(obj)} items, min {spec['minItems']}")


def main() -> int:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    brief = json.loads(BRIEF_PATH.read_text(encoding="utf-8"))
    errors: list[str] = []
    require_fields(brief, schema, "", errors)

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

    if errors:
        print("brief invalid:")
        for e in errors:
            print(f"  - {e}")
        return 1

    print(f"OK  {BRIEF_PATH.relative_to(ROOT)}  ({len(mods)} modules)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
