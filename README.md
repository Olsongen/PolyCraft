# PolyCraft

Agentic 3ds Max **2027** craft for artist-grade kits. v1 is Ethan + agents in this repo.

**First PolyKit:** Middlehelm wetlands ruins — first person — grid 0.5 / 1 / 2 / 4 / 8 m.  
**Primary ref:** Abbaye de Trois-Fontaines (church ruin, not the 18th-century gate).

Units: **display meters** (`1.0` = 1 m), **system centimeters** (Unreal 4 m → 400 uu).

## Repo map

| Path | What |
|---|---|
| [`docs/VISION.md`](docs/VISION.md) | Locked constitution |
| [`kits/middlehelm-wetlands-ruins/`](kits/middlehelm-wetlands-ruins/) | World/AD brief + JSON contract |
| [`contracts/kit.schema.json`](contracts/kit.schema.json) | What a PolyKit brief must contain |
| [`max/`](max/) | 2027 bootstrap (units, grid, layers, menu) |
| [`.cursor/skills/`](.cursor/skills/) | Worldbuilding, AD, kit-plan, Max, UV, QA |

## Local Max

Cloud cannot run 3ds Max. On your box, in **2027**:

1. Run `max/polycraft_bootstrap.ms`
2. Read `kits/middlehelm-wetlands-ruins/BRIEF.md`
3. First assembly test is in that brief — do not detail before it walks at 1.7 m

```bash
python scripts/validate_brief.py
```

## Not this slice

No website. No Field Tracing Displacement plugin yet. No Unreal/Source exporter. No hero mesh production.
