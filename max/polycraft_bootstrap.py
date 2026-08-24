"""PolyCraft bootstrap wrapper for 3ds Max 2027.

Run inside Max (Scripting > Run Script, or python.execfile).
Delegates to polycraft_bootstrap.ms so units/grid stay one source of truth.
"""

from __future__ import annotations

from pathlib import Path

from pymxs import runtime as rt


def max_version_code() -> int:
    # MAXScript maxVersion() is 1-indexed; [1] is the release id (29000 for 2027).
    return int(rt.maxVersion()[1])


def require_2027() -> None:
    code = max_version_code()
    if code < 29000:
        raise RuntimeError(
            f"PolyCraft requires 3ds Max 2027 (29000). This session reports {code}."
        )


def bootstrap() -> None:
    require_2027()
    ms = Path(__file__).resolve().parent / "polycraft_bootstrap.ms"
    if not ms.is_file():
        raise FileNotFoundError(ms)
    rt.fileIn(str(ms))


if __name__ == "__main__":
    bootstrap()
