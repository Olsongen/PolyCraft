---
name: visual-qa
description: Technical and taste QA for PolyKits. Use at every handoff and after the first assembly test. Fail closed.
---

# Visual QA

Both tracks can fail the kit. Cloud cannot run Max; drive a local 2027 session through the harness and review contracts + images.

## Technical

- Display meters, system cm (`python -m polycraft max bootstrap` still applied).
- On-grid per the brief (studio default 0.5 / 1 / 2 / 4 / 8 m), or exception rule honored.
- Pivots per socket law.
- Naming + layers from **this** brief.
- MatIDs match the brief.
- Instances/XRefs vs illegal copies.
- Then the brief’s own `qa.technical` list.

## Taste

- Walk at the camera the brief named. If it only works in ortho, it failed.
- The place in the brief, not a generic dungeon and not another kit.
- Three-module stale test.
- Pass/fail plus a written note. “Pretty good” is not a grade.
- Then the brief’s own `qa.taste` list.

## First assembly

The vignette on the **active** brief must be walkable before detailing. Run it with `python -m polycraft max job <id> first-assembly`.
