# PolyKits

PolyCraft is the studio. A **PolyKit** is one place. This folder is the registry — not a house style.

Studio law (local Windows Max 2027, display meters / system cm, default 0.5–8 m grid, world+AD before modules, harness) is shared. Place, camera, wear, naming prefix, layers, and assembly nodes are **per kit**. Do not inherit another kit’s founding act, silhouette, or module language.

Status values match `contracts/kit.schema.json`: `vision` → `planned` → `blockout` → `craft` → `qa` → `handoff`.

| Kit | Status | Camera | Notes |
|---|---|---|---|
| [`middlehelm-wetlands-ruins`](middlehelm-wetlands-ruins/) | **planned** (in progress) | FPS, eye 1.7 m | Slice 1 proving ground. First assembly is a harness job, not a studio node. |

## New kit

1. `shared-vision` then worldbuilding + art direction. No module list yet.
2. Copy the schema into `kits/<id>/brief.json` + `BRIEF.md`.
3. Kit-plan only after world/AD can be signed.
4. Optional `max/jobs.json` + scripts. Studio bootstrap stays in `max/`.

## Agents

```bash
python -m polycraft kits
python -m polycraft max bootstrap
python -m polycraft max job <kit-id> first-assembly
```
