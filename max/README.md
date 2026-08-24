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

**Drop-in:** drag `max/polycraft_bootstrap.ms` into a 3ds Max **2027** viewport.

Listener should print that 400 cm formats as meters, and you should see `MHWR_QA_meter_plane` (1 m) on layer `90_QA`.

Then drop `max/mhwr_first_assembly.ms` — FPS camera at 1.7 m through the first vignette (4 m + 4 m + 8 m arcade, aisle, waterline, one standing vault). Blockout boxes only. Do not detail.

## Grid while modeling

Prefer **0.5 / 1 / 2 / 4 / 8 m**. Organic overlays may miss; they still snap to sockets. See `kits/middlehelm-wetlands-ruins/BRIEF.md`.
