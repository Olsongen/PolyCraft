---
name: visual-kickoff
description: Core PolyCraft image-gen step. Use GPT Image 2.0 for FPS concepts, ambiguity, and inspiration. Do not lean on it for trim sheets or tileables yet except a cautious dry-stone albedo kickoff.
---

# Visual kickoff

**Model:** GPT Image 2.0 until we say otherwise. Cursor `GenerateImage` has no model picker in this session — still treat GPT Image 2.0 as the studio default (concepts, refs in the prompt).

**Primary job: concepts.** FPS stills to answer ambiguity and find the look. That is where this earned its place in the pipeline.

**Textures: not the job yet.** Dry stone albedo was okay-ish. Trim, wet, moss, overlays were rough. Do not spend cycles generating trim sheets or tile sets here until that bar moves. PolyMat still owns tiling solve and PBR.

## When (required)

- Camera, massing, wear, or module read is still verbal.
- A taste argument needs a still, not adjectives.
- Inspiration against primary refs (this kit: Trois-Fontaines **church**, `ref/eglise1–3.jpg`).

## When not

- Trim atlases, wet tiles, moss overlays, “give me PBR.” Skip, or one dry-ashlar kickoff at most, then PolyMat.
- Letting a pretty wrong frame rewrite the brief.

## How — concepts

1. Load church refs. Kill list in the prompt (no 18th-c gate, no gargoyles, no jungle).
2. FPS eye ~1.7 m unless the brief says otherwise.
3. Save under `kits/<id>/concepts/`. One line in that README: shot, kit job, keep or kill.

## PolyMat

If we ever hand an image over: **dry stone albedo only**, as a kickoff. Not final. Not trim. Not wet/moss until gen quality is there.
