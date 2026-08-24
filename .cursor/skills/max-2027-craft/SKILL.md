---
name: max-2027-craft
description: 3ds Max 2027 craft for PolyCraft. Units (meters display / cm system), grid 0.5–8 m, pymxs, modifiers, instances, XRefs. Use when bootstrapping a scene or modeling a module.
---

# Max 2027 craft

Host is **3ds Max 2027** only. Gate: `(maxVersion())[1] >= 29000`.

## Units (law)

```maxscript
units.SystemType = #centimeters
units.SystemScale = 1.0
units.DisplayType = #Metric
units.MetricType = #meters
```

Artists type `4.0` for 4 m. File is cm. Unreal: 4 m = 400 uu. **Never model in cm in the viewport.**

Run `max/polycraft_bootstrap.ms` (or the pymxs wrapper) on a new scene before blockout.

## Grid

Home grid spacing **50.0** system units = **0.5 m**. Majors every 2 lines = 1 m. Snap 3D. Prefer 0.5 / 1 / 2 / 4 / 8 m. Exceptions socket back to the grid.

## Craft

- Modifier-first. Collapse is a decision.
- Boolean then **Smart Bevel** when stock bevels hold.
- **Array** before copy-paste.
- Instances in assembly; `objXRefMgr` for source modules.
- Field Helper / Data Channel / Noise Plus only on purpose. Tiny noise.
- Naming: kit prefix from the brief (`MHWR_...`). Layers from the brief.

## Plugins

Write a new tool only when this kit is blocked (UV solver, chamfer profiles, Field Tracing Displacement). Do not start those in slice 1.

## Python

`pymxs.runtime` only. UI: PySide6 + `qtmax`. No MaxPlus.
