"""PolyCraft public API. CLI and MCP are thin surfaces over this."""

from __future__ import annotations

from pathlib import Path

from polycraft.brief import ValidationReport, validate_briefs
from polycraft.kits import KitRecord, get_kit, list_kits
from polycraft.maxclient import ExecResult, MaxStatus, exec_op, install_harness, status as max_status
from polycraft.root import repo_root


def studio_bootstrap_path(root: Path | None = None) -> Path:
    return (root or repo_root()) / "max" / "polycraft_bootstrap.ms"


def max_bootstrap(root: Path | None = None) -> ExecResult:
    path = studio_bootstrap_path(root)
    return exec_op("bootstrap", path=str(path.resolve()))


def max_run(script: str | Path) -> ExecResult:
    path = Path(script).expanduser()
    if not path.is_file():
        root = repo_root()
        alt = root / path
        path = alt if alt.is_file() else path
    if not path.is_file():
        return ExecResult(
            ok=False,
            backend="none",
            op="filein",
            error=f"script not found: {script}",
        )
    return exec_op("filein", path=str(path.resolve()))


def max_job(kit_id: str, job_name: str, root: Path | None = None) -> ExecResult:
    kit = get_kit(kit_id, root)
    job = kit.jobs.get(job_name)
    if job is None:
        known = ", ".join(sorted(kit.jobs)) or "(none)"
        return ExecResult(
            ok=False,
            backend="none",
            op="filein",
            error=f"kit {kit_id} has no job {job_name!r}. jobs: {known}",
        )
    if "bootstrap" in job.requires:
        boot = max_bootstrap(root)
        if not boot.ok:
            return boot
    return max_run(job.resolve(kit.path))


def max_eval(code: str, *, lang: str) -> ExecResult:
    if lang not in {"ms", "py"}:
        return ExecResult(ok=False, backend="none", op="eval_ms", error="lang must be ms or py")
    op = "eval_ms" if lang == "ms" else "eval_py"
    return exec_op(op, code=code, allow_batch=False)


__all__ = [
    "ExecResult",
    "KitRecord",
    "MaxStatus",
    "ValidationReport",
    "get_kit",
    "install_harness",
    "list_kits",
    "max_bootstrap",
    "max_eval",
    "max_job",
    "max_run",
    "max_status",
    "studio_bootstrap_path",
    "validate_briefs",
]
