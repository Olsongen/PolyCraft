# PolyMax (name proposed, not locked)

3ds Max **2027** agent craft for artist-grade modular 3D kits.

This repo is adjacent to [3D Polygen](https://www.3dpolygen.com), PolyMesh, and PolyMat. It is not a second generative website. It is the DCC-side intelligence: how an agent plans, models, organizes, UVs, and QA's a kit the way a senior environment artist would.

**Status:** vision lock. We do not model, script a pipeline, or scaffold a product until the agreement in [`docs/VISION.md`](docs/VISION.md) is signed.

## Host

- Autodesk 3ds Max **2027** (R29, `maxVersion` `29000`)
- Python via **pymxs** (not MaxPlus)
- UI via **PySide6** + `qtmax`
- MAXScript where pymxs cannot carry by-ref / Unwrap / menu registration

## How we work here

1. Read `docs/VISION.md`.
2. Anything unmarked as **Locked** is still a proposal.
3. Do not invent product surface (web app, marketplace, etc.) until the vision says that is the work.
4. Agent rules live in `.cursor/rules`. Skills live in `.cursor/skills`.
