# PolyCraft

Agentic 3ds Max **2027** craft for artist-grade modular kits (**PolyKits**).

v1 is **Ethan + agents in this repo**. Destinations later: **Unreal Engine** and **Source Engine**. The craft itself is kit-first and engine-agnostic: models, IDs, organization, module planning, Blizzard-level nuance, artist-grade UVs.

We may author new Max tools and plugins when stock Max is the ceiling. [PolyMesh](https://www.3dpolygen.com) is a sibling ML product (decimation, UV understanding) — not our UV department.

**Status:** vision lock. [`docs/VISION.md`](docs/VISION.md) is the agreement. Do not model or ship a product until remaining sign-off boxes are checked.

## Host

- 3ds Max **2027** (R29, `maxVersion` `29000`)
- pymxs, PySide6, `qtmax`
- C++ / .NET 10 plugins only when Python cannot do the job
