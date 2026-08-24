# PolyCraft — shared vision

**PolyCraft** is the name. A **PolyKit** is what it produces.

This is a working agreement. **Locked** = you said it. **Proposed** = my read.

### Slice 1 — locked, in execution

- First PolyKit: **Middlehelm wetlands ruins**, first-person.
- Primary architectural ref: **Abbaye de Trois-Fontaines**, Trois-Fontaines-l'Abbaye, Marne, Champagne-Ardenne.
- Grid: **0.5 / 1 / 2 / 4 / 8 m**. Prefer on-grid. Organic and breakage may miss; they still socket to the grid.
- Build: skills, `contracts/kit.schema.json`, kit brief, Max 2027 bootstrap.
- Still out of scope: website, engine plugins, Field Tracing Displacement, hero mesh production.

---

## 1. What this is

**Locked**

- Agentic craft around **3ds Max 2027** for **artist-grade 3D kits**.
- v1: **you and the agents in this repo**. Others after the tooling is proven.
- The work is the kit: models, Material IDs, organization, module planning, UVs, nuance. Engines are destinations.
- Destinations: **Unreal Engine** and **Source Engine**. Craft is **engine-agnostic first**.
- **Units:** artists work in **meters** (`1.0` = 1 m). The file is **cm-based** so Unreal stays clean. We do not model in centimeters in the viewport.
- Bar: **absolute highest quality, nuance, and taste** — a Blizzard environment studio, not “good for AI.”
- Planning is **worldbuilding + art direction + env art + modeling**, big to small. Not surface-level kit templates.
- PolyMesh is an ML **product** (decimation, UV understanding). Not our UV department.
- PolyCraft **solves UVs to artist grade** because we are agentic.
- New Max **tools and plugins are allowed** when they unblock craft. We do not invent tools because they sound cool.

**Thesis**

PolyCraft is a tiny Blizzard-style kit studio in agent form: AD and worldbuilder first, then env art and Max craft, then tools. PolyKit is the output. Polygen / PolyMat / PolyMesh are siblings, not this repo.

Generated topology can be reference or kickoff. It is never the kit.

---

## 2. What this is not

- A generic modular-pack generator (four walls, one floor, stamp tiling).
- Quick AD: “dark fantasy, stone, moss” and then modeling.
- Engine-first (Nanite, VMF) before the place exists.
- A plugin house. **Field Tracing Displacement** and UV/chamfer tools are on the table; they get built when a kit is waiting on them.
- A second Polygen website, a Grok Bot farm, Max 2024–2026.

---

## 3. Units (locked)

Artists must think in meters. Unreal must receive centimeters. Max must not fight either.

| Layer | Value |
|---|---|
| **What you type in Max** | `1.0` = **1 meter**. A 4 m wall is `4.0`, never `400`. |
| **System Unit Scale** | **1 unit = 1.0 centimeter** (cm-based file). |
| **Display Unit Scale** | **Meters**. |
| **Meaning** | Display `4.0 m` = 400 system cm = **400 Unreal uu**. Clean 1:1 to UE after the 100× that meters→cm already is. |
| **Grid / snap** | Meter grid. Typical snaps: `0.05`, `0.1`, `0.25`, `0.5`, `1`, `2`, `4` m. |
| **Source handoff** | Later adapter (inch-heritage world units). Do not model a second kit in inches. |

Bootstrap **must** set and lock system+display units. Mixing them mid-file is a failed kit. Never “work in cm” in the viewport to make UE happy — that is what system units are for.

Module talk is in meters: 2 m / 4 m walls, 0.1 m trim, not 200/400/10 cm.

---

## 4. Big to small (the real planning stack)

A PolyKit exists to serve a **place and a story**. The module list is the last part of planning, not the first.

Treat this as a Blizzard env **team**, not a prompt expander.

### 4.1 Worldbuilding (expert, not flavor text)

Go through the idea until a lead would sign it:

- Who lived here, who lives here now, what broke or endured.
- Climate, geology, economy, faith, tech — only what the space can show.
- Player path and camera: what they see at 10 m, at 2 m, at the door.
- Scale of the space (closet vs nave vs street) and what “one module” means in that space.
- What must be **readable as landmark** vs what should disappear into the set.
- What would be *wrong* for this place (the kill list).

If this pass could apply to any dungeon, it failed.

### 4.2 Art direction (Blizzard hat)

- Silhouette language and massing (chunk, slope, ornament budget).
- One material story per family, then disciplined exceptions.
- Wear with causality: water, hands, load, liturgy, neglect — not cavity noise.
- Color/value at gameplay camera, not in a beauty-lighting cheat.
- References that are specific (which D4 zone, which cathedral, which concept frame) and what we will **not** copy.
- How the kit stays modular **without** reading as tile.

### 4.3 Kit as a language for that space

Only now: which modules this place actually needs.

- Straights, inner/outer corners, caps, columns, floors, trims, overlays, breakage, hero inserts.
- What is instanced, what is unique, what is allowed to break the module without breaking the **grid**.
- Material IDs as a kit-level shader/trim plan.
- UV strategy (trim / unique / atlas / stacking) that serves those IDs.
- Variation designed in so three modules in a row do not stamp.

### 4.4 Then Max

Blockout on the meter grid. Socket-proof. Craft. UV. QA. Engine adapters last.

Skipping 4.1–4.3 and jumping to a wall kit is how you get a technically correct, soulless pack.

---

## 5. How we execute

1. **Constitution** — this file.
2. **World + AD** — section 4, written into the kit brief. No geometry.
3. **Kit plan** — modules, grid, sockets, naming, IDs, UV strategy, instance/XRef.
4. **Max 2027 bootstrap** — meters display, cm system, grid, snaps, layers, naming, menu.
5. **Blockout** — socket-proof 3–5 modules.
6. **Craft** — modifier-first, instance-first, XRef-first.
7. **UV + IDs** — artist-grade solve here.
8. **Visual QA** — technical + taste. Fail closed.
9. **Handoff** — Unreal and/or Source, after the kit is true.

If step 2 is shallow, stop. More thinking. Not more boxes.

---

## 6. Max 2027 — stock, and tools as needed

**Host:** 2027 only (R29, `maxVersion` `29000`). pymxs, PySide6, `qtmax`. C++ / .NET 10 only when Python cannot.

**Stock we will use:** Boolean + Smart Bevel, Array (surface / Z-growth / spline pack), Field Helper, Data Channel, Volume Select, Noise Plus (tiny), `objXRefMgr`, Unwrap until it is the ceiling.

**Law:** a tool needs a kit job it unblocks.

| Tool | Job | Status |
|---|---|---|
| Scene bootstrap | Units (m display / cm system), grid, snap, naming, layers | Slice 1 |
| UV solver | Artist-grade, kit-aware packing / trim / texel / UV2 | When Unwrap fails the bar |
| Chamfer profiles | Directable bevels (by ID, angle, post-boolean, width/depth curves) | When Smart Bevel/Chamfer lie |
| **Field Tracing Displacement** | Build **real polys** from displacement/height — geo where the field actually displaces, not uniform tessellation. Lets texture displacement become performant kit mesh. | When a kit is waiting on it |
| UI dockers | Brief, IDs, sockets, QA | When the loop is clumsy |

Field Tracing Displacement is the right kind of idea: it raises craft and performance together. It is not slice 1 unless the first proving-ground kit is blocked without it.

---

## 7. Taste bar (Blizzard studio)

- The kit would survive a lead review at a studio that shipped Sanctuary, not an asset-store review.
- Read at the camera the brief named.
- Massing first. Ornament rides on structure.
- Wear has a story.
- Modules hide the module.
- Concept and world are answered, not “inspired by.”
- An assembler can build the space without fighting pivots.

Pass/fail plus a written note. “Pretty good” is not a grade.

---

## 8. Visual QA

**Technical:** system/display units match this file, on-grid meters, names, pivots, mating sockets, density, MatIDs, UV policy, instance/XRef vs copies.

**Taste:** ortho shaded/wire/checker, assembled vignette at gameplay camera, wear/trim/hero, vs concept, three-module stale test, **does this kit only work for this place’s story**.

Cloud cannot run Max. Local scripts + images.

---

## 9. Roles (a studio, not a bot org)

Same git, same brief. Skills + subagents. Stronger Grok on AD/world later if useful.

| Role | Job |
|---|---|
| Worldbuilder | Place, story, player path, kill list |
| Art director | Silhouette, material story, wear, references, stale |
| Env art lead | Kit as language: modules, IDs, trims, hero vs filler |
| Modeler | Max craft, modifiers, instances |
| UV lead | Artist-grade solve |
| Max TD | pymxs, plugins, units lock |
| QA | Fail closed |

These are hats in the thought process even when one agent wears several. The AD hat speaks before the modeler hat.

---

## 10. Questions

### Identity

| # | Question | Status | Answer |
|---|---|---|---|
| I1 | Name? | **Locked** | PolyCraft. PolyKit = the kit. |
| I2 | v1 user? | **Locked** | You + agents here. |
| I3 | Slice 1? | **Locked** | Skills + kit schema + Max 2027 bootstrap + Middlehelm wetlands brief. No hero mesh. |

### Ecosystem

| # | Question | Status | Answer |
|---|---|---|---|
| E1 | Polygen? | Proposed | Consume style / kit-sheet. Do not reimplement generate. |
| E2 | PolyMesh? | **Locked** | ML sibling. Not our UV department. |
| E3 | UVs? | **Locked** | Agentic artist-grade solve here. |
| E4 | Plugins? | **Locked** | As needed. Field Tracing Displacement is cataloged, not pre-built. |
| E5 | PolyMat? | Proposed | Sheets we plan IDs/UVs to use; displacement maps may later feed Field Tracing. |

### Craft

| # | Question | Status | Answer |
|---|---|---|---|
| C1 | Engines? | **Locked** | Unreal + Source destinations. Kits first. |
| C2 | Units? | **Locked** | Display meters (`1.0` = 1 m). System cm. UE: 4 m → 400 uu. |
| C3 | Grid? | **Locked** | 0.5 / 1 / 2 / 4 / 8 m. Prefer on-grid; exceptions socket back. |
| C4 | Camera? | **Locked** | First person. Eye ~1.7 m. |
| C5 | First kit? | **Locked** | Middlehelm overgrown wetland ruins. Ref: Trois-Fontaines abbey. |
| C6 | Drive Max? | Proposed | Local pymxs / plugins from git. No pretend-Max in the cloud. |

---

## 11. Slice 1 — executing

1. This document — frozen for identity.
2. Skills: worldbuilding, art-direction, kit-plan, max-2027-craft, artist-UV, visual-QA.
3. `contracts/kit.schema.json`.
4. Max 2027 bootstrap: display meters, system cm, 0.5 m home grid, naming, menu.
5. `kits/middlehelm-wetlands-ruins/` — world/AD brief + machine contract. No hero mesh. No Field Tracing plugin.

---

## 12. Sign-off

- [x] Name: PolyCraft
- [x] v1 audience
- [x] Units: meters in Max, cm-based for UE
- [x] Engines: Unreal + Source, kits first
- [x] Agentic UV + plugins-as-needed (incl. Field Tracing Displacement, later)
- [x] Blizzard-level AD / worldbuilding / env team process
- [x] Slice 1 scope
- [x] First kit: Middlehelm wetlands ruins, FPS, grid 0.5–8 m, ref Trois-Fontaines

Vision lock for identity is closed. Execute slice 1 against `kits/middlehelm-wetlands-ruins/`.
