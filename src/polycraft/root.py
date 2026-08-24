from __future__ import annotations

import os
from pathlib import Path


def repo_root(start: Path | None = None) -> Path:
    """Walk up from start (or this file) until kits/ + contracts/ exist."""
    env = os.environ.get("POLYCRAFT_ROOT")
    if env:
        p = Path(env).expanduser().resolve()
        if (p / "kits").is_dir() and (p / "contracts").is_dir():
            return p
    here = (start or Path(__file__).resolve()).parent
    for candidate in (here, *here.parents):
        if (candidate / "kits").is_dir() and (candidate / "contracts").is_dir():
            return candidate
    raise FileNotFoundError(
        "PolyCraft repo root not found (need kits/ and contracts/). Set POLYCRAFT_ROOT."
    )
