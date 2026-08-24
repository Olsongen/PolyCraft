# PolyCraft

Agentic 3ds Max **2027** craft for artist-grade kits. v1 is Ethan + agents in this repo.

The product is the **API, CLI, MCP, and harness** — a skillset for agentic kit development. A **PolyKit** is one place. The studio is kit-agnostic.

Units: **display meters** (`1.0` = 1 m), **system centimeters** (Unreal 4 m → 400 uu).  
Grid default: **0.5 / 1 / 2 / 4 / 8 m**. Prefer on-grid. Exceptions still socket.

## Kits

Registry and status: [`kits/README.md`](kits/README.md).

| Kit | Status | What |
|---|---|---|
| [Middlehelm wetlands ruins](kits/middlehelm-wetlands-ruins/) | planned (in progress) | Slice 1 proving ground. FPS. Ref: Trois-Fontaines church ruin only. |

Do not treat the first proving ground as the house kit type.

## Drive Max (agents)

```bash
python -m polycraft kits
python -m polycraft validate
python -m polycraft max status
python -m polycraft max install-harness    # once, on the Windows Max 2027 box
python -m polycraft max bootstrap
python -m polycraft max job middlehelm-wetlands-ruins first-assembly
```

MCP server: `.cursor/mcp.json` → `scripts/polycraft_mcp.py`. Same API as the CLI.

Cloud Linux cannot run 3ds Max. A local Cursor session on the Max box can. Drag-and-drop is emergency only.

## Repo map

| Path | What |
|---|---|
| [`docs/VISION.md`](docs/VISION.md) | Locked constitution |
| [`kits/`](kits/) | Every PolyKit — brief, jobs, kit Max scripts, status |
| [`src/polycraft/`](src/polycraft/) | Python API, CLI, MCP |
| [`contracts/`](contracts/) | Kit brief + harness protocol |
| [`max/`](max/) | Studio bootstrap + in-Max listener |
| [`.cursor/skills/`](.cursor/skills/) | World, AD, kit-plan, harness, Max, UV, QA |

```bash
python -m polycraft validate
```

## Not this slice

No website. No Field Tracing Displacement plugin yet. No Unreal/Source exporter. No hero mesh production.
