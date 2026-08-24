# PolyCraft — shared vision

**PolyCraft** is the name. A **PolyKit** is what it produces.

This is a working agreement. **Locked** = you said it. **Proposed** = my read. **Open** = still blocking. Until remaining sign-off boxes are checked, agents may only revise this agreement.

---

## 1. What this is

**Locked**

- Agentic craft around **3ds Max 2027**, aimed at **artist-grade 3D kits**.
- v1 users: **you and the agents in this repo**. Other people after the tooling is proven.
- The work is the kit: 3ds models, Material IDs, organization, planning, Blizzard-level nuance, module planning. Not an engine feature checklist.
- Engine destinations are **Unreal Engine** and **Source Engine**. Craft is **engine-agnostic first**. Export adapters come after the kit is true.
- Taste bar: Diablo 4 / Blizzard environment art — modular **and** alive.
- At minimum: a serious partner on **solid base meshes**.
- Rules and skills for how we plan and execute; shared vision with questions answered before geometry.
- Adjacent to Polygen / PolyMesh / PolyMat / Kingdom Crafter — not a rewrite.
- **PolyMesh** is an ML **product**: SOTA decimation + artist-grade UV understanding. Not agentic.
- **PolyCraft is agentic**, so we **do** solve UVs to artist grade here. That is craft + tools, not “defer to PolyMesh.”
- We may **author new 3ds Max tools and plugins** whenever stock Max is the ceiling: UV solvers, chamfer profile control, UI, and anything else the kit ecosystem needs to run at full capability.

**Thesis**

PolyCraft is the agentic Max craft OS. PolyKit is the kit (meshes, IDs, sockets, UVs, assembly proof, briefs). Polygen is concept / style / kit-sheets / PolyMat. PolyMesh is the ML sibling we can call; it is not our UV department. Kingdom Crafter is a destination, not the DCC.

| Layer | Kind | Owns |
|---|---|---|
| **Polygen** | Product + agents | Intent, style, concept, kit *sheets*, extract/refine, generation |
| **PolyMat** | Product | 4K PBR tileables, trims, atlases |
| **PolyMesh** | ML product | Decimation, learned UV understanding |
| **PolyCraft (this)** | Agentic system + Max tools | Kit as a production system: plan, model, IDs, organize, UV *solve*, script, plugin, QA, taste |
| **PolyKit** | Output | The kit itself |
| **Unreal / Source** | Destinations | Handoff after the kit is right |
| **Kingdom Crafter** | Destination | Shipped kits, when we choose to publish |

Generated topology can be reference or kickoff. It is never the kit.

---

## 2. What this is not

- A second Polygen website.
- Engine-first (Nanite settings, VMF quirks) before the kit exists.
- A chatbot that dumps boxes.
- Stale modular: four walls, one floor, obvious tiling.
- Max 2024–2026. Host is **2027 only**.
- A public multi-user product in slice 1.
- A plugin farm in search of a problem. Tools exist because a kit step is blocked.

---

## 3. Kits first (the center)

Everything else is in service of a kit a lead environment artist would trust.

That means:

- **Grid law** — module sizes, snap, pivots as a contract.
- **Socket language** — straight, inner/outer corner, cap, column, floor-to-wall, trim, hero insert.
- **Module plan** — the set, the variants, what is instance vs unique, what is allowed to break the module without breaking the grid.
- **Material IDs** — planned at kit scale before hero detailing, because trims, atlases, and shaders are kit-level.
- **Organization** — naming, layers, XRefs, assembly scene vs source modules.
- **Nuance** — wear story, silhouette, not-stale tiling, concept fidelity, Blizzard restraint + drama.
- **UVs** — artist-grade, kit-aware (trim vs unique vs atlas, stacking, texel, seams that serve the module). Agentic solve in Max; custom solver if stock Unwrap is the ceiling. PolyMesh is optional ML assist, not the owner.
- **Usability** — an LD (or a future engine adapter) can assemble without fighting the assets.

Unreal vs Source changes **handoff** (units scale, lightmap channel, collision flavor, nanite vs cheap meshes). It does not change whether a 400-unit wall is actually 400, whether ID 3 is trim, or whether three modules in a row look like a stamp.

---

## 4. Engines: destinations, not the craft

**Locked:** Unreal and Source are the main targets. Initial work is engine-agnostic.

**Proposed defaults**

| Topic | Stance |
|---|---|
| Canonical Max units | **1 generic unit = 1 cm** in the scene. Artists think metric. |
| Unreal handoff | 1:1 (uu = cm). |
| Source handoff | Scale adapter later (Source world units are inch-heritage). Do not model a second kit in inches. |
| Lightmaps | Source cares about UV2. That is a handoff channel, planned in the kit UV strategy, not a reason to unwrap twice in a panic at export. |
| Collision / LOD / Nanite | Per-kit, mostly per-engine. Deferred until a brief names them. Blockout does not wait on Nanite. |

---

## 5. How we execute

1. **Vision lock** — this file, then a per-kit brief. No geometry.
2. **Kit plan** — modules, grid, sockets, naming, MatIDs, UV strategy, instance/XRef map.
3. **Scene bootstrap (Max 2027)** — units, grid, snaps, layers, naming, PolyCraft menu.
4. **Blockout** — on grid. Socket-proof 3–5 modules before detailing.
5. **Craft** — modifier-first, instance-first, reference-first. Smart Bevel after Booleans. Custom chamfer/profile tools when stock bevels lie.
6. **UV + IDs** — artist-grade solve here. Call PolyMesh if ML decimation/UV insight helps. Write a solver if Unwrap_UVW cannot hit the bar.
7. **Visual QA** — technical + taste. Fail closed.
8. **Handoff** — Unreal and/or Source adapters, only after the kit is true.

If step 1 is incomplete, the only valid work is more agreement.

---

## 6. 3ds Max 2027 — stock craft and our tools

**Locked:** host is Max 2027 (R29, `maxVersion` `29000`). We may ship new tools and plugins.

**Stock we will actually use**

- pymxs (no MaxPlus). PySide6 + `qtmax`. Python menu actions are valid in 2027+.
- Boolean + **Smart Bevel**. Array (surface / Z-growth / spline pack). Field Helper, Data Channel, Volume Select. Noise Plus at tiny amplitude.
- `objXRefMgr` for source modules. Instances in assembly.
- USD 0.14 and FBX as interchange — engine adapter problem, not the kit problem.

**Tools we are allowed to author** (when stock is the ceiling)

| Class | Examples | When |
|---|---|---|
| UV | Packer, trim-aware layout, texel lock, stacked modular UVs, UV2 lightmap, seam policy | Stock Unwrap cannot hit studio grade on the kit |
| Mesh ops | Chamfer **profiles** (width/depth curves, by-ID, by-angle, post-boolean), smarter than Chamfer/Smart Bevel alone | Bevels are ugly, inconsistent, or un-directable |
| UI | PySide6 dockers: kit brief, ID painter, socket/pivot HUD, QA report | Scripts exist but the artist/agent loop is clumsy |
| Scene | Naming, grid, layer, XRef, instance audit | Always in slice 1 bootstrap |
| C++ / .NET | Modifiers, mesh algos Max Python cannot do at speed | Only if pymxs is actually too slow or too closed. SDK: .NET 10, C++20, Qt 6.8.3 |

**Law:** a new tool needs a kit job it unblocks. We do not start PolyCraft by writing a chamfer product. We start by making kits possible; we extend Max the first time the kit is waiting on the tool.

Keep the modifier stack alive until the plan says collapse.

---

## 7. Taste bar

- Read at the camera the brief named (per-kit, not per-engine).
- Massing first. Ornament rides on structure.
- Wear has a story. Cavity noise is not weathering.
- Modules hide the module.
- One strong material story per kit family.
- Answer the concept/sheet.
- An assembler can build a room without fighting pivots.

Pass/fail plus a written note. “Pretty good” is not a grade.

---

## 8. Visual QA

**Technical:** grid, names, pivots, on-grid dimensions, mating sockets, density, MatID coverage, UV policy (including whether UV2 is required for a Source handoff), instance/XRef vs illegal copies.

**Taste:** ortho shaded/wire/checker, assembled vignette at gameplay camera, wear/trim/hero closeups, vs concept, three-module stale test.

Cloud cannot run Max. Scripts and plugins run locally. We review contracts + images.

---

## 9. Roles (Cursor, not Grok Bots)

Skills + subagents in this repo. Stronger Grok on taste later; faster Grok on mechanical QA. No parallel Grok Bot org.

| Role | Job |
|---|---|
| Kit planner | Grid, sockets, IDs, module set |
| Max TD | pymxs, plugins, modifiers, XRef |
| UV lead | Artist-grade solve + when to use PolyMesh vs our solver |
| Art director | Taste, stale test, nuance |
| QA | Fail closed |

---

## 10. Questions

### Identity

| # | Question | Status | Answer |
|---|---|---|---|
| I1 | Name? | **Locked** | **PolyCraft**. PolyKit = the kit. |
| I2 | v1 user? | **Locked** | You + agents here. Others after proof. |
| I3 | Slice 1 success? | Proposed | Frozen constitution + Max 2027 bootstrap (menu, grid, naming) + kit schema + one named brief. Tools beyond bootstrap only if that brief is blocked. |

### Ecosystem

| # | Question | Status | Answer |
|---|---|---|---|
| E1 | Polygen? | Proposed | Consume style / kit-sheet. Do not reimplement generate. |
| E2 | PolyMesh? | **Locked** | ML product (decimation + UV understanding). Sibling, not our UV department. |
| E3 | Our UVs? | **Locked** | Agentic artist-grade UV solve is in scope, including new Max UV tools. |
| E4 | PolyMat? | Proposed | Authors sheets. We plan IDs and layouts to use them. |
| E5 | New Max plugins? | **Locked** | Yes, as needed to elevate craft. Not a plugin studio for its own sake. |
| E6 | Kingdom Crafter? | Proposed | One destination for a proven kit. |

### Craft defaults

| # | Question | Status | Answer |
|---|---|---|---|
| C1 | Engines? | **Locked** | Unreal + Source as destinations. Kits first, engine-agnostic. |
| C2 | Canonical units? | Proposed | 1 Max unit = 1 cm. Scale at Source export. |
| C3 | Default module? | Open | 200 / 400 cm is a common start — confirm per first kit |
| C4 | QA camera? | Open | Per-kit. D4-like vs FPS changes massing. |
| C5 | Collision / Nanite / LOD? | Proposed | Engine adapters; not slice 1. |
| C6 | First proving-ground kit? | Open | One interior kit with a real module set, not a platform of kits |
| C7 | Drive Max how? | Proposed | Local pymxs / MAXScript / plugins from git contracts. No pretend-Max in the cloud. |

### Product surface

| # | Question | Status | Answer |
|---|---|---|---|
| P1 | Web app in v1? | Proposed | **No.** |
| P2 | MCP in v1? | Proposed | No. |
| P3 | Bootstrap scripts in v1? | Proposed | Yes. |
| P4 | Custom UV/chamfer plugins in v1? | Proposed | Charter yes. Build when the first kit proves stock Max is the limiter. |

---

## 11. Slice 1 (if you sign the rest)

1. Freeze this document.
2. Skills: kit-plan, max-2027-craft, artist-UV, visual-QA, taste, when-to-plugin.
3. `kit.schema.json`.
4. Max 2027 bootstrap: units/grid/snap/layers/naming/menu.
5. One named PolyKit brief — no hero detailing, no engine export project.

No website. No bot platform. No Unreal/Source plugin as the first artifact.

---

## 12. Sign-off

- [x] Name: PolyCraft
- [x] v1 audience
- [x] PolyMesh = ML sibling, not our UV department
- [x] Agentic UV solve in scope
- [x] New Max tools/plugins allowed
- [x] Engines = Unreal + Source, kits first / agnostic
- [ ] Canonical units (cm proposed)
- [ ] Polygen / PolyMat / Kingdom Crafter remainder
- [ ] Slice 1 scope
- [ ] First proving-ground kit named (world, camera, module size)

Until the empty boxes are checked, agents may only revise this agreement.
