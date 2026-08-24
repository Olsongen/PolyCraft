from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from polycraft.root import repo_root


@dataclass(frozen=True)
class KitJob:
    name: str
    script: str
    requires: tuple[str, ...] = ()
    notes: str = ""

    def resolve(self, kit_dir: Path) -> Path:
        path = kit_dir / "max" / self.script
        if not path.is_file():
            raise FileNotFoundError(f"kit job script missing: {path}")
        return path


@dataclass(frozen=True)
class KitRecord:
    id: str
    title: str
    status: str
    path: Path
    camera: dict[str, Any] = field(default_factory=dict)
    jobs: dict[str, KitJob] = field(default_factory=dict)
    brief: dict[str, Any] = field(default_factory=dict)

    def to_dict(self, *, include_brief: bool = False) -> dict[str, Any]:
        data: dict[str, Any] = {
            "id": self.id,
            "title": self.title,
            "status": self.status,
            "path": str(self.path),
            "camera": self.camera,
            "jobs": {
                name: {
                    "script": job.script,
                    "requires": list(job.requires),
                    "notes": job.notes,
                }
                for name, job in self.jobs.items()
            },
        }
        if include_brief:
            data["brief"] = self.brief
        return data


def _load_jobs(kit_dir: Path) -> dict[str, KitJob]:
    jobs_path = kit_dir / "max" / "jobs.json"
    if not jobs_path.is_file():
        return {}
    raw = json.loads(jobs_path.read_text(encoding="utf-8"))
    jobs: dict[str, KitJob] = {}
    for name, spec in raw.items():
        if isinstance(spec, str):
            jobs[name] = KitJob(name=name, script=spec)
            continue
        jobs[name] = KitJob(
            name=name,
            script=spec["script"],
            requires=tuple(spec.get("requires") or ()),
            notes=spec.get("notes") or "",
        )
    return jobs


def load_kit(kit_dir: Path) -> KitRecord:
    brief_path = kit_dir / "brief.json"
    brief = json.loads(brief_path.read_text(encoding="utf-8"))
    return KitRecord(
        id=brief.get("id") or kit_dir.name,
        title=brief.get("title") or kit_dir.name,
        status=brief.get("status") or "vision",
        path=kit_dir,
        camera=brief.get("camera") or {},
        jobs=_load_jobs(kit_dir),
        brief=brief,
    )


def list_kits(root: Path | None = None) -> list[KitRecord]:
    kits_dir = (root or repo_root()) / "kits"
    found: list[KitRecord] = []
    for brief in sorted(kits_dir.glob("*/brief.json")):
        found.append(load_kit(brief.parent))
    return found


def get_kit(kit_id: str, root: Path | None = None) -> KitRecord:
    root = root or repo_root()
    direct = root / "kits" / kit_id
    if (direct / "brief.json").is_file():
        return load_kit(direct)
    for kit in list_kits(root):
        if kit.id == kit_id:
            return kit
    raise KeyError(f"unknown kit: {kit_id}")
