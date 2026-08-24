---
name: handoff
description: Write a session handoff for the next PolyCraft agent (cloud <-> local). Use at the end of a work session or before handing off — always cloud->local, since Max 2027 only runs on the local Windows box. Keeps docs/HANDOFF.md current.
---

# Handoff

The next agent starts cold. `docs/VISION.md` is locked and travels with the repo; the handoff carries the **volatile** state that code and the constitution can't: what this session did, the git/branch reality, and the exact next move.

## When

- End of a session, or before handing work to another agent.
- **Always cloud -> local.** Cloud Linux cannot run 3ds Max; the local agent inherits the whole Max loop, so it needs the state written down.
- After anything that changes branch/PR state, environment setup, or a kit's status.

## Where

`docs/HANDOFF.md` — one living file. **Overwrite** it so it reflects *now*. Do not append a running log; a stale handoff misleads worse than none. Update the `Updated` / `From -> To` header every time.

## What it must carry

1. **Session summary** — what changed, on which branch, the PR link, and whether it is verified (tests/build) or not.
2. **Git reality** — current branch, base branch, clean vs dirty, and any surprise (e.g. `main` is empty; the code lives on the base branch). Never assume the reader knows this.
3. **Run locally** — `pip install -e .`, `python -m unittest discover -s tests` (expect 11/11), `python -m polycraft kits | validate`.
4. **Max loop** (if the next session is local) — `max install-harness` -> start Max 2027 -> `max status` -> `max bootstrap` -> `max job <kit> <name>`. Host is **2027 / R29 / `maxVersion` 29000** only; harness on `127.0.0.1:17927`.
5. **Locked constraints** — link `docs/VISION.md` and `.cursor/rules/vision-lock.mdc`; do not re-derive them. Units (m display / cm system), grid 0.5-8 m, world+AD before modules.
6. **Next steps** — the smallest concrete next action, open questions, and known caveats.

## Rules

- Self-contained: assume the reader has zero memory of this session.
- Short and current beats complete. Link the constitution; don't paste it.
- Never claim Max ran in the cloud. Never introduce out-of-scope work (website, engine plugins, Field Tracing Displacement, production trims) as a "next step" unless a kit is blocked on it.
- Validate before handing off: `python -m polycraft validate` and the test suite pass, or the handoff says why not.
