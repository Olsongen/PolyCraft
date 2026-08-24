# Max 2027 — studio + harness

PolyCraft does not run 3ds Max in the cloud. Agents on the **Windows Max box** drive 2027 through the harness.

This folder is **studio law only**. Kit-prefixed nodes (`MHWR_…`, and later kits) are created by `kits/<id>/max/` jobs.

## Harness

`max/harness/listener.py` listens on `127.0.0.1:17927` inside Max. Protocol: `contracts/harness.protocol.json`.

```bash
python -m polycraft max install-harness   # writes Max user startup
# start 3ds Max 2027
python -m polycraft max status
python -m polycraft max bootstrap
```

Emergency only: fileIn `max/harness/startup.ms` or `max/polycraft_bootstrap.ms`.

## What bootstrap does

- Refuses to run below `maxVersion` **29000** (R29 / 2027)
- **System units:** centimeters (`SystemScale` 1.0)
- **Display units:** metric **meters** — you type `4.0`, not `400`
- **Home grid:** 0.5 m (50 cm), major lines every 1 m
- **Snap:** 3D on
- **Studio layers:** `00_REF`, `10_BLOCKOUT`, `20_CRAFT`, `60_ASSEMBLY`, `90_QA`
- **QA plane:** `PC_QA_meter_plane` — 1 m × 1 m at the origin

Kit briefs may add layers (`20_ARCH`, `30_VAULT`, …). Those come from the kit job, not from bootstrap.

## Grid while modeling

Prefer **0.5 / 1 / 2 / 4 / 8 m** unless the active brief names a different step. Organic overlays may miss; they still snap to sockets.
