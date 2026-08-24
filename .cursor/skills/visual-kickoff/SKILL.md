---
name: visual-kickoff
description: Core PolyCraft image-gen step. Use GPT Image 2.0 for concepts, ambiguity, and inspiration. Do not lean on it for trim sheets or tileables yet except a cautious dry-stone albedo kickoff.
---

# Visual kickoff

**Concepts:** always allowed — Cursor **internal image gen** in this session (stills, ambiguity, inspiration). That is the job.

**Textures:** not always. Dry stone was okay; trim/wet/moss were rough. Skip texture gen unless we explicitly want a kickoff. PolyMat owns tiling and PBR.

**GPT Image 2.0** is a preference when we have a picker. This session’s `GenerateImage` is the internal tool we use for concepts.

## When (required)

- Camera, massing, wear, or module read is still verbal.
- A taste argument needs a still, not adjectives.
- Inspiration against **this kit’s** primary refs (paths on that brief / `kits/<id>/ref/`).

## When not

- Trim atlases, wet tiles, moss overlays, “give me PBR.” Skip, or one dry-ashlar kickoff at most, then PolyMat.
- Letting a pretty wrong frame rewrite the brief.
- Using another kit’s refs as if they were this place.

## How — concepts

1. Load the active kit’s refs. Put that brief’s kill list in the prompt.
2. Camera from the brief (do not assume FPS 1.7 m).
3. Save under `kits/<id>/concepts/`. One line in that README: shot, kit job, keep or kill.

## PolyMat

If we ever hand an image over: **dry stone albedo only**, as a kickoff. Not final. Not trim. Not wet/moss until gen quality is there.
