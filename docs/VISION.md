# PolyCraft — working shared vision

Working name: **PolyCraft**. Alternate you floated: PolyKit. PolyMax is demoted (too host-specific once other people use the tooling).

This is a working agreement, not a pitch deck. **Locked** = you said it. **Proposed** = my read. **Open** = still blocking. Agents may only revise this agreement until the remaining sign-off boxes are checked.

---

## 1. What this is

**Locked**

- Super-smart **agentic** tooling around **3ds Max 2027**, for **artist-grade 3D kits**.
- v1 users: **you and the agents in this repo**. Other people come after the tooling is proven, not before.
- Professional craft: grid, snapping, modularity that is **not stale**, modifiers, instancing, references, organization, custom scripts, kit-level planning, Material IDs.
- QA has to be real: usability, art direction, taste, nuance — Diablo 4 / Blizzard environment-art equivalent.
- At minimum a serious partner on **solid base meshes for kits**.
- This repo needs **rules and skills** for how we plan and execute, including a shared vision with questions actually answered.
- Adjacent to Polygen / PolyMesh / PolyMat / Kingdom Crafter, not a rewrite of them.
- **PolyMesh is not agentic.** It is a product: SOTA decimation + artist-grade UV understanding. We do not fork that work. We call it.
- We can do more than pure ML *because* this is an agent system: planning, Max craft, kit logic, taste, iteration, organization.

**Proposed thesis**

**PolyCraft** is the agentic craft OS. A **PolyKit** is what it produces (a production modular kit + its brief/contract). Kingdom Crafter is where a proven kit can ship. Polygen is where concept / style / kit-sheets / PolyMat live.

| Layer | Kind | Owns |
|---|---|---|
| **Polygen** | Product + agents | Intent, style, concept, kit *sheets*, extract/refine, generation |
| **PolyMat** | Product | 4K PBR tileables, trims, atlases |
| **PolyMesh** | Product (ML) | SOTA decimation, artist-grade UV *understanding / solve* |
| **PolyCraft (this)** | Agentic system | Max 2027 craft: kit as a production system — plan, model, organize, script, QA, taste |
| **PolyKit** | Output | The kit itself: modules, sockets, IDs, UVs, assembly proof |
| **Kingdom Crafter** | Destination | Premium Unreal-ready kits with hand-authored fidelity |

Polygen already has the right *order* for generation (bind style → contracts → elevate → generate). PolyCraft needs the equivalent order for **modeling**: lock vision → plan the kit as a system → blockout on grid → craft with modifiers/instances/XRefs → UV/MatID as kit decisions (solve via Max + PolyMesh, never a competing UV network) → Visual QA that can fail taste.

Generated topology can be a *reference* or a *kickoff*. It is never the kit.

---

## 2. What this is not

**Locked in spirit, proposed in wording**

- A second Polygen web workspace.
- A generic “AI 3D” dashboard.
- A chatbot that dumps MAXScript cubes.
- Auto-retopo or UV-ML as the product (that is PolyMesh).
- A stale modular pack: 4 walls, 1 floor, obvious tiling, no wear logic, no hero exceptions.
- Supporting Max 2024/2025/2026. Host is **2027 only**.
- A public multi-user product in slice 1.

---

## 3. The actual problem

AI 3D today can make an object. ML can decimate and unwrap. Neither makes a **kit**.

A kit a Blizzard environment artist would trust has:

- A grid law everyone can snap to at 2am.
- A socket language (straight, inner/outer corner, cap, column, floor-to-wall, trim).
- Pivots that are a contract, not a vibe.
- Instancing and XRefs so a trim change propagates.
- Material IDs planned *before* the hero mesh.
- UVs as a *sheet strategy* here, solved by Max craft + PolyMesh — not island soup, not a second UV product.
- Variation designed in: ruin, wear, asymmetry **inside** the module.
- Silhouette and massing that hold at the gameplay camera the brief names.
- Custom Max scripts as first-class studio tools.

Diablo 4 kits are the named bar because they are modular **and alive**.

---

## 4. How we execute (the law)

**Proposed operating sequence. Do not skip.**

1. **Vision lock** — this file, then a per-kit brief. No geometry.
2. **Kit plan** — module list, grid, sockets, naming, MatIDs, UV *strategy*, instance/XRef map, LOD/collision intent.
3. **Scene bootstrap (Max 2027)** — units, grid, snaps, layers, naming, script menu.
4. **Blockout** — boxes/splines on grid. Socket proofs. Assemble 3–5 modules before detailing.
5. **Craft** — modifier-first, instance-first, reference-first. Smart Bevel after Booleans. Array / Data Channel / Field Helper / Noise Plus on purpose.
6. **UV + IDs** — execute the kit sheet plan in Max; hand meshes to **PolyMesh** for decimation / artist UV solve when that is the right tool; do not reimplement PolyMesh.
7. **Visual QA** — technical gates *and* taste grading. Fail closed.
8. **Handoff** — UE/USD/FBX as the brief specified.

If step 1 is incomplete, the only valid work is more agreement.

---

## 5. 3ds Max 2027 craft stance

**Locked:** host is Max 2027.

**Proposed implementation stance**

| Topic | Stance |
|---|---|
| Release | R29. Gate scripts with `(maxVersion())[1] >= 29000`. |
| Python | `pymxs.runtime` only. MaxPlus is dead. |
| UI | PySide6 + `qtmax`. Python menu actions are valid in 2027+. |
| C++ / .NET | Only if pymxs cannot. SDK: .NET 10, C++20, Qt 6.8.3. |
| Booleans | Boolean modifier + **Smart Bevel**. |
| Repetition | **Array** (2027 surface / Z-growth / spline pack) before copy-paste. |
| Wear / selection | **Field Helper** + Volume Select, Data Channel, vertex color. |
| Noise | **Noise Plus**, tiny amplitude, seedable. If you see noise before architecture, it failed. |
| References | `objXRefMgr` for source modules. Instances in the assembly scene. |
| Interchange | USD 0.14.0 preferred; FBX when downstream still demands it. |
| Units | Propose **1 generic unit = 1 cm** (Unreal). Lock per kit. |

Keep the modifier stack alive until the kit plan says collapse. Collapse is a decision.

---

## 6. Taste bar (proposed)

- **Read at camera.** Grade the camera the brief named.
- **Massing first.** Ornament rides on structure.
- **Wear has a story.** Random cavity noise is not weathering.
- **Modules hide the module.** Grid is for the LD, not the player.
- **Restraint + drama.** One strong material story per kit family.
- **Concept fidelity.** Answer the sheet, do not generic-dungeon it.
- **Usability.** An LD can assemble a room without fighting pivots.

Pass/fail per gate plus a written note. “Pretty good” is not a grade.

---

## 7. Visual QA (proposed)

**Technical (Max / exported JSON)** — units, grid, naming, pivots, on-grid dimensions, mating sockets, density, MatIDs, UV policy, instance/XRef vs illegal copies, collision/LOD if asked.

**Taste (needs images)** — ortho shaded/wire/checker, game-camera assembled vignette, wear/trim/hero closeups, side-by-side vs concept, three-module stale test.

This cloud environment cannot run Max. Scripts run locally. We review contracts + images.

---

## 8. Roles, Cursor agents, and Grok Bots

**Proposed: do not stand up a parallel Grok Bot org chart.**

We already have the right primitive in this repo: **rules + skills + Task subagents**, optionally run on Grok (Pro+). A Grok Bot on grok.com would be a second brain with none of the kit contract, git history, or Max scripts. That is a split we do not want in v1.

Use named roles **inside Cursor**, as skills, when we are executing — not during vision lock:

| Role | Job | When |
|---|---|---|
| Kit planner | System: grid, sockets, IDs, module list | After vision lock |
| Max TD | pymxs / modifiers / XRef / naming | Bootstrap + craft |
| Art director | Taste, silhouette, wear story, stale test | Visual QA |
| UV lead | Kit UV *strategy*; decide when to call PolyMesh | After blockout |
| QA | Technical gates, fail closed | Every handoff |

Pro+ is relevant later: put a stronger Grok on **art director / taste** (nuance), a faster Grok on **mechanical QA** (grid, names, pivots). Same contracts, different temperature of judgment. Not a reason to build a bot platform.

Revisit public Grok Bots only when other users exist and we want a published PolyCraft persona. That is not slice 1.

---

## 9. Questions

### Identity

| # | Question | Status | Working answer |
|---|---|---|---|
| I1 | Name? | Proposed | **PolyCraft** (system). **PolyKit** = a kit we produce. PolyMax dropped. |
| I2 | v1 user? | **Locked** | You + agents here. Other users only after the tooling is proven. |
| I3 | Slice 1 success? | Proposed | Frozen constitution + Max 2027 bootstrap + one named kit brief. No finished cathedral. No website. |

### Ecosystem

| # | Question | Status | Working answer |
|---|---|---|---|
| E1 | Polygen? | Proposed | Consume style / kit-sheet as input. Do not reimplement generate. |
| E2 | PolyMesh? | **Locked** | ML product: SOTA decimation + artist-grade UV. Not agentic. We call it; we do not fork it. |
| E3 | PolyMat? | Proposed | Authors sheets. We assign IDs and layout to *use* them. |
| E4 | Kingdom Crafter? | Proposed | Taste bar + destination for a proven kit. |
| E5 | Agentic vs ML? | **Locked** | Agents here do planning, Max craft, kit logic, taste, iteration. ML products stay products. |

### Craft defaults

| # | Question | Status | Working answer |
|---|---|---|---|
| C1 | Engine? | Proposed | Unreal 5 |
| C2 | Units? | Proposed | 1 Max unit = 1 cm |
| C3 | Default module? | Open | 200 / 400 cm walls — confirm |
| C4 | QA camera? | Open | D4-like vs FPS changes every silhouette decision |
| C5 | Collision / Nanite / LOD? | Open | |
| C6 | First proving-ground kit? | Open | One Kingdom Crafter / Sanctuary-adjacent interior, not a platform |
| C7 | Drive Max how? | Proposed | Local pymxs + MAXScript from a JSON kit contract in git. No pretend-Max in the cloud. |

### Product surface

| # | Question | Status | Working answer |
|---|---|---|---|
| P1 | Web app in v1? | Proposed | **No.** |
| P2 | MCP in v1? | Proposed | No. Polygen already has MCP. |
| P3 | Custom Max scripts in v1? | Proposed | Yes: bootstrap, naming, grid, socket/pivot checks, QA export. |
| P4 | Grok Bots as roles? | Proposed | **No separate bots.** Roles = skills + subagents here. Grok models used when useful. |

---

## 10. Slice 1, if you sign the rest

1. Freeze this document.
2. Skills: kit-plan, max-2027-craft, studio-UV-strategy, visual-QA, taste. UV *solve* remains PolyMesh.
3. `kit.schema.json` — contract a PolyKit brief must satisfy.
4. Max 2027 bootstrap pack.
5. One named kit brief — still no hero detailing.

No mesh generator. No second website. No bot platform. No PolyMesh clone.

---

## 11. Sign-off

- [ ] Name locked (PolyCraft vs PolyKit-as-the-repo)
- [x] v1 audience locked (us first, others after proof)
- [x] PolyMesh boundary locked (ML decimation + UV product, not agentic)
- [x] Agentic vs ML locked
- [ ] Ecosystem remainder (Polygen / PolyMat / Kingdom Crafter) locked
- [ ] Craft defaults locked (units, engine, camera)
- [ ] Slice 1 scope locked
- [ ] First proving-ground kit named

Until the empty boxes are checked, agents may only revise this agreement.
