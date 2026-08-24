# Max 2027 bootstrap

PolyCraft does not run 3ds Max in the cloud. These scripts run **on your machine** in Max 2027.

## What it does

- Refuses to run below `maxVersion` **29000** (R29 / 2027)
- **System units:** centimeters (`SystemScale` 1.0)
- **Display units:** metric **meters** — you type `4.0`, not `400`
- **Home grid:** 0.5 m (50 cm), major lines every 1 m
- **Snap:** 3D on
- **Layers:** `00_REF` … `90_QA` (same as the Middlehelm brief)
- **QA plane:** `MHWR_QA_meter_plane` — 1 m × 1 m at the origin

## Run

1. Open 3ds Max **2027**.
2. Drag `max/polycraft_bootstrap.ms` into a viewport, **or** Scripting → Run Script.
3. Optional: run `max/polycraft_menu.ms` once to add a **PolyCraft** menu.

Python (inside Max):

```python
exec(open(r"<repo>/max/polycraft_bootstrap.py", encoding="utf-8").read())
```

Confirm the listener prints that `400` cm formats as meters (expect a `4` m class string).

## Grid while modeling

Prefer **0.5 / 1 / 2 / 4 / 8 m**. Organic overlays may miss; they still snap to sockets. See `kits/middlehelm-wetlands-ruins/BRIEF.md`.
