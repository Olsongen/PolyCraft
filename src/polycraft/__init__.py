"""PolyCraft — agentic kit studio for 3ds Max 2027."""

from polycraft.api import (
    KitRecord,
    MaxStatus,
    ValidationReport,
    get_kit,
    list_kits,
    max_bootstrap,
    max_eval,
    max_job,
    max_run,
    max_status,
    validate_briefs,
)

__version__ = "0.1.0"

__all__ = [
    "KitRecord",
    "MaxStatus",
    "ValidationReport",
    "get_kit",
    "list_kits",
    "max_bootstrap",
    "max_eval",
    "max_job",
    "max_run",
    "max_status",
    "validate_briefs",
]
