---
name: max-2027-craft
description: 3ds Max 2027 craft for PolyCraft. Units (meters display / cm system), grid 0.5–8 m, pymxs, modifiers, instances, XRefs. Use when bootstrapping a scene or modeling a module.
---

# Max 2027 craft

Host is **3ds Max 2027** only. Gate: `(maxVersion())[1] >= 29000`.

Drive Max through the **harness** skill from this Windows PC (`python -m polycraft max …` / MCP). Do not ask the user to drag scripts. If you are a cloud agent, stop.

## Units (law)

```maxscript
units.SystemType = #centimeters
units.SystemScale = 1.0
units.DisplayType = #Metric
units.MetricType = #meters
```

Artists type `4.0` for 4 m. File is cm. Unreal: 4 m = 400 uu. **Never model in cm in the viewport.**

`python -m polycraft max bootstrap` before blockout. That creates studio layers and `PC_QA_meter_plane` only.

## Grid

Home grid spacing **50.0** system units = **0.5 m**. Majors every 2 lines = 1 m. Snap 3D. Prefer 0.5 / 1 / 2 / 4 / 8 m unless the **active brief** names other steps. Exceptions socket back to the grid.

## Craft

- Modifier-first. Collapse is a decision.
- Boolean then **Smart Bevel** when stock bevels hold.
- **Array** before copy-paste.
- Instances in assembly; `objXRefMgr` for source modules.
- Field Helper / Data Channel / Noise Plus only on purpose. Tiny noise.
- Naming and layers come from the **active kit brief**, not from studio bootstrap.

## Plugins

Write a new tool only when this kit is blocked (UV solver, chamfer profiles, Field Tracing Displacement). Do not start those in slice 1.

## Python

`pymxs.runtime` only. UI: PySide6 + `qtmax`. No MaxPlus. In-Max HTTP listener: `max/harness/listener.py`.
