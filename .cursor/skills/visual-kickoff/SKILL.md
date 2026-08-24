---
name: visual-kickoff
description: Use Cursor image generation as a core PolyCraft step — resolve AD ambiguity, FPS camera tests, inspiration, and PolyMat albedo/trim kickoffs. Use whenever look, wear, module read, or materials are unclear, and when starting trim sheets or tileables for PolyMat.
---

# Visual kickoff (image gen is part of the job)

Do not wait for a “make a picture” request. If the brief still has visual ambiguity, **generate**. If a kit needs a material start for PolyMat, **generate**. Kill frames that fight the brief; do not let a pretty wrong image become the new AD.

## When (required)

- World/AD is written but the camera still is not obvious.
- Module language is ambiguous (4 m vs 8 m, collapse-as-bay, waterline).
- Taste argument needs a still, not adjectives.
- PolyMat needs an albedo or trim **kickoff** (this repo does not replace PolyMat’s tile solve or PBR maps).

## How — concepts

1. Load **primary refs** (this kit: `ref/eglise1–3.jpg`, church only).
2. FPS eye ~1.7 m unless the brief says otherwise.
3. Prompt the **grammar**: pale limestone, pointed arcade, round west triplet, temperate wetland, shared 1.0 m stain. Name the kill list in the prompt (no gargoyles, no 18th-c gate, no jungle).
4. Save under `kits/<id>/concepts/`. Write one line in that folder’s README: shot, kit job, keep or kill.

## How — PolyMat kickoffs

Generate **square 1:1** unless the sheet is explicitly wide.

| Kickoff | Prompt for | Hand to PolyMat as |
|---|---|---|
| Trim sheet | Flat 2D atlas, horizontal bands, even light, no 3D scene | Layout + albedo start for courses, moldings, waterline, broken edge |
| Tile albedo | “Seamless, wraps four edges, no border, orthographic, flat light” | Basecolor to tile-solve |
| Overlay | Sparse moss/algae, not a second architecture | Layer / ID 6 start |

**Do not** ask this generator for roughness, normal, or height as the source of truth. PolyMat does tiling solve and the rest of the PBR set.

## What we learned (Middlehelm test)

- Trim sheet: **usable kickoff**. Bands and moldings appeared. Not a packed studio UV sheet; PolyMat / a human still owns layout discipline.
- Dry ashlar tile: **best 4-edge candidate**. Flat light, running bond. Check wrap in PolyMat; do not assume perfect seam.
- Wet ashlar: **failed as a tile** — came back as a **vertical waterline gradient**. Keep as a trim/unique panel, or prompt again with “NO vertical gradient, uniform wetness, four-edge wrap.”
- Moss overlay: drifted toward a mossy **floor**. Re-prompt “sparse overlay on stone, not paving” if we need ID 6.

## Fail

- Letting a baroque or jungle frame rewrite the brief.
- Shipping generated maps as final PBR.
- Generating without the kit refs when refs exist.
