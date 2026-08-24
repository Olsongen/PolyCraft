# PolyCraft — session handoff

> Living doc. Overwrite it at each handoff (see the `handoff` skill). It carries volatile state only; `docs/VISION.md` is the locked constitution.

**Updated:** 2026-08-24 · **From -> To:** cloud session -> next (local) agent

## 0. Read first (non-negotiable)

- `docs/VISION.md` — locked constitution. Identity, units, grid, and process are **locked**; do not re-litigate.
- `.cursor/rules/vision-lock.mdc` — short version of the same constraints.
- `kits/README.md` — kit registry. Slice 1 proving ground is `kits/middlehelm-wetlands-ruins/` (`planned`, in progress). It is **not** the house style.
- Then the task-relevant skills in `.cursor/skills/` (worldbuilding -> art-direction -> kit-plan -> max-2027-craft -> artist-uv -> visual-qa; harness to drive Max).

## 1. Why the next session is local

Cloud Linux **cannot run 3ds Max**. The local Windows **3ds Max 2027 / R29 (`maxVersion` 29000)** box is the only place that can drive Max through the harness. Bootstrap, blockout, first-assembly, and QA renders happen there. Agents drive Max via API/CLI/MCP — drag-and-drop is emergency-only.

## 2. What the last session did

- Added the Cloud Agent dev environment: committed `.cursor/environment.json` = `{ "name": "PolyCraft", "install": "pip install -e ." }`.
- Added this handoff process: `.cursor/skills/handoff/SKILL.md` + this file.
- Branch `cursor/dev-environment-setup-d3ae`; PR [#2](https://github.com/Olsongen/PolyCraft/pull/2) (draft, base `cursor/kits-registry-studio-bootstrap-662c`).
- Verified in a fresh cloud pod: editable install succeeds, `unittest` 11/11 pass, CLI + stdio MCP work. `polycraft max status` reports `unreachable` on Linux (expected). No source/behavior changes — env config + docs only.

## 3. Git reality (important)

- Default branch **`main` is essentially empty** — no `pyproject.toml`, no `src/`. All code lives on **`cursor/kits-registry-studio-bootstrap-662c`** (PR #2's base). If you check out `main` and find nothing, that's why — use the base branch.
- Because `main` is empty, a dashboard-saved / DB-managed Cloud environment can't build. The committed `.cursor/environment.json` (repo-file managed, follows the branch) is the right mechanism. To enable promotable prebuilt Cloud envs later, land the project on `main`.
- Make new work on `cursor/<name>` branches off the base branch. Commit per logical change; no force-push/amend.

## 4. Run locally

```bash
pip install -e .
python -m unittest discover -s tests      # expect 11/11 OK
python -m polycraft kits                   # lists middlehelm-wetlands-ruins (planned)
python -m polycraft validate               # expect ok: true
```

Pure standard library — no third-party runtime deps. MCP server is stdio (`scripts/polycraft_mcp.py`, wired in `.cursor/mcp.json`); no dev server to run.

## 5. Max 2027 loop (local only)

```bash
python -m polycraft max install-harness    # writes Max user startup (once, on this box)
# start / restart 3ds Max 2027
python -m polycraft max status             # reachable, backend "live", maxVersion 29000
python -m polycraft max bootstrap          # m display / cm system, 0.5 m grid, studio layers, PC_QA plane
python -m polycraft max job middlehelm-wetlands-ruins first-assembly
```

Harness: `max/harness/listener.py` on `127.0.0.1:17927` (protocol `contracts/harness.protocol.json`; override via `POLYCRAFT_MAX_HOST` / `POLYCRAFT_MAX_PORT`). Bootstrap refuses below `maxVersion` 29000. Studio layers: `00_REF`, `10_BLOCKOUT`, `20_CRAFT`, `60_ASSEMBLY`, `90_QA`. Keep kit-prefixed nodes (`MHWR_...`) in `kits/<id>/max/` jobs; `max/` is studio law only.

## 6. Locked constraints (do not re-derive — see VISION.md)

- Host: 3ds Max **2027 only** (R29). pymxs + PySide6. No MaxPlus.
- Units: type meters (`1.0` = 1 m; a 4 m wall is `4.0`, never `400`). System = cm. Unreal receives cm (4 m -> 400 uu).
- Grid: prefer on-grid **0.5 / 1 / 2 / 4 / 8 m**; exceptions still socket.
- Process: worldbuilding + AD -> image gen (GPT Image 2.0, concepts only) to kill ambiguity -> kit plan -> Max. No module list without a place.
- Out of scope this slice: website, engine plugins/exporters, Field Tracing Displacement, hero-mesh production, production trims/tiles.

## 7. Next steps (pick per task)

1. Environment: keep repo-file managed config (recommended). If a saved/prebuilt Cloud env is wanted, get the project onto `main`. Mark PR #2 ready when satisfied.
2. Kit: run the Max loop above, execute `first-assembly` for `middlehelm-wetlands-ruins`, then apply the `visual-qa` skill (fail closed) — capture local shaded/wire/checker + an assembled FPS vignette at eye ~1.7 m.
3. Keep the handoff current: overwrite this file before you hand off (see the `handoff` skill).
