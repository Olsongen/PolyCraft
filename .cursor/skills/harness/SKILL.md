---
name: harness
description: Drive PolyCraft through the API, CLI, and MCP from a local Windows agent. Run Max 2027 via the localhost harness. Use whenever a scene must be bootstrapped, a kit job run, or a brief validated. Do not ask the user to drag scripts.
---

# PolyCraft harness

You are a **local agent on the Windows PC that has 3ds Max 2027**. Artists review the viewport. **Do not ask anyone to drag a `.ms` into Max.**

If you are not on that PC, stop. Do not invent Linux Max, Wine, or a cloud workaround.

## Surfaces (one API)

| Surface | How |
|---|---|
| Python API | `from polycraft import list_kits, max_bootstrap, max_job, …` |
| CLI | `python -m polycraft <cmd>` or `scripts/polycraft` |
| MCP | server `polycraft` — tools `polycraft_*` |
| Max listener | inside 2027, `127.0.0.1:17927` (`contracts/harness.protocol.json`) |

## Commands

```bash
python -m polycraft kits
python -m polycraft kit middlehelm-wetlands-ruins
python -m polycraft validate
python -m polycraft max status
python -m polycraft max install-harness    # once
python -m polycraft max bootstrap          # studio units/grid — not a kit
python -m polycraft max job <kit-id> first-assembly
python -m polycraft max eval --ms "units.formatValue 400.0"
```

## Order

1. Confirm you are local (`max status` can see 127.0.0.1:17927, or `3dsmaxbatch` exists).
2. `validate` — briefs must pass.
3. If harness down: `max install-harness`, start Max 2027, status again.
4. `max bootstrap` then the **active** kit job from `kits/README.md`.
5. Do not detail until the briefed camera walks.

## Law

- Studio bootstrap creates `PC_` nodes only. Kit prefixes stay in `kits/<id>/max/`.
- A new kit is a new folder + `brief.json` + optional `max/jobs.json`. Not a change to studio law.
- Drag-and-drop is emergency only, if the harness is down and install failed.

## Protocol

`POST /exec` JSON `{ "v": 1, "op": "ping|bootstrap|filein|eval_ms|eval_py|scene_info" }`  
`GET /health`
