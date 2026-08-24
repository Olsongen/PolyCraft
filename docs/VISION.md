# PolyMax — proposed shared vision

This is a working agreement, not a pitch deck. Items are **Locked** (said by you) or **Proposed** (my read, waiting on you). Nothing in this repo should execute past planning until the Proposed lines are accepted, rewritten, or killed.

---

## 1. What this is

**Locked**

- Super-smart AI agent tooling **around 3ds Max 2027**.
- The job is **artist-grade 3D kits**, not “a mesh from a prompt.”
- The skill bar is professional: grid, snapping, modularity that is **not stale**, modifier literacy, instancing, references, organization, custom scripts, studio UV solving, kit-level planning, Material IDs.
- QA has to be real: usability, art direction, taste, nuance — Diablo 4 / Blizzard environment-art equivalent, not stock-kit tidy.
- At minimum the agent is a serious partner on **solid base meshes for kits**.
- This repo needs **rules and skills** for how we plan and execute, including a shared vision with questions actually answered.
- Adjacent to the 3D Polygen ecosystem (Polygen, PolyMesh, PolyMat, Kingdom Crafter), not a rewrite of it.

**Proposed**

PolyMax is the **Max craft operating system** in that ecosystem.

| Layer | Owns |
|---|---|
| **Polygen** | Intent, style, concept, kit *sheets*, extract/refine, generation spend |
| **PolyMat** | 4K PBR tileables, trims, atlases |
| **PolyMesh** | Mesh/topology language (exact charter TBD — private repo not readable from this session) |
| **PolyMax (this)** | 3ds Max 2027 craft: how a kit is *built* as a production system |
| **Kingdom Crafter** | The shipped-kit taste destination: premium, Unreal-ready, hand-authored fidelity |

Polygen already has the right *order* for generation (bind style → read contracts → elevate → generate). PolyMax needs the equivalent order for **modeling**: lock vision → plan the kit as a system → blockout on grid → craft with modifiers/instances/XRefs → UV/MatID as kit decisions → Visual QA that can fail taste.

This is not Hunyuan-in-Max. Generated topology can be a *reference* or a *kickoff*. It is never the kit.

---

## 2. What this is not

**Proposed — kill anything that smells like these**

- A second Polygen web workspace.
- A generic “AI 3D” dashboard.
- A chatbot that dumps MAXScript cubes.
- Auto-retopo as the product.
- A stale modular pack: 4 walls, 1 floor, obvious tiling, no wear logic, no hero exceptions.
- Supporting Max 2024/2025/2026. Host is **2027 only**.

The earlier Next.js scaffold in this session was exactly the wrong instinct (empty-repo default: “browser UI → Next app”). That is **not** the product unless we later decide a briefing room needs a UI.

---

## 3. The actual problem

AI 3D today can make an object. It cannot make a **kit**.

A kit a Blizzard environment artist would trust has:

- A grid law everyone can snap to at 2am.
- A socket language (straight, inner/outer corner, cap, column, floor-to-wall, trim).
- Pivots that are a contract, not a vibe.
- Instancing and XRefs so a trim change propagates.
- Material IDs planned *before* the hero mesh, because shaders and trim sheets are kit-level.
- UVs solved as a *sheet strategy*, not per-asset unwrap-and-pray.
- Variation designed in: ruin, wear, asymmetry **inside** the module, so it does not read as tile.
- Silhouette and massing that hold at gameplay camera (D4 isometric-ish or whatever the brief locks).
- Custom Max scripts as first-class studio tools, not leftovers.

Diablo 4 kits are the named bar because they are modular **and alive**. That is harder than either pure unique hero or pure kitbash.

---

## 4. How we execute (the law)

**Proposed operating sequence. Agents in this repo must not skip steps.**

1. **Vision lock** — questions below answered in writing. No geometry.
2. **Kit plan** — module list, grid, sockets, naming, MatIDs, UV strategy, instance/XRef map, LOD/collision intent.
3. **Scene bootstrap (Max 2027)** — units, grid, snaps, layers, naming, script menu.
4. **Blockout** — boxes/splines on grid. Socket proofs. Assembly test of 3–5 modules before any detailing.
5. **Craft** — modifier-first, instance-first, reference-first. Smart Bevel after Booleans. Array / Data Channel / Field Helper / Noise Plus used on purpose, not as decoration.
6. **UV + IDs** — execute the kit-level sheet plan. No island soup.
7. **Visual QA** — technical gates *and* taste grading. Fail closed.
8. **Handoff** — UE/USD/FBX as the brief specified. Polygen/PolyMat only if the brief says the kit re-enters that pipeline.

If step 1 is incomplete, the only valid work is more questions, more reference, or rewriting this document.

---

## 5. 3ds Max 2027 craft stance

**Locked:** host is Max 2027.

**Proposed implementation stance**

| Topic | Stance |
|---|---|
| Release | R29. Gate scripts with `(maxVersion())[1] >= 29000`. |
| Python | `pymxs.runtime` only. MaxPlus is dead. |
| UI | PySide6 + `qtmax`. Python actions in the Max menu are valid in 2027+. |
| C++ / .NET | Only if pymxs cannot do the job. SDK is .NET 10, C++20, Qt 6.8.3. |
| Booleans | Boolean modifier + **Smart Bevel** for post-boolean transitions. Do not hand-chamfer spaghetti if Smart Bevel will hold. |
| Repetition | **Array** (including 2027 surface / Z-growth / spline pack) before copy-paste. |
| Wear / selection | **Field Helper** + Volume Select, Data Channel, vertex color — planned, not painted as an afterthought. |
| Noise | **Noise Plus** for controlled, tileable, seedable variation. Tiny amplitude. If you can see the noise before you see the architecture, it failed. |
| References | `objXRefMgr` for source modules. Instances in the assembly scene. |
| Interchange | USD for 3ds Max 0.14.0 is the modern path; FBX only when a downstream tool still demands it. |
| Units | Propose **1 generic unit = 1 cm** (Unreal). Must be locked per kit. |

Modifier literacy means: keep the stack alive until the kit plan says collapse. Collapse is a decision, not a habit.

---

## 6. Taste bar (proposed)

Grade against this, not against “looks 3D.”

- **Read at camera.** D4-like kits fail in the ortho beauty shot and pass in the game camera, or the reverse. We grade the camera the brief named.
- **Massing first.** Chunky, readable silhouettes. Ornament rides on structure; it does not replace it.
- **Wear has a story.** Water path, hand-height grime, load-bearing chips, liturgical vs neglected. Random cavity noise is not weathering.
- **Modules hide the module.** Corners, trims, overlays, breakage, and hero inserts exist so the grid is felt by the LD and not seen by the player.
- **Restraint + drama.** Blizzard env art is not maximalist clutter and not IKEA clean. One strong material story per kit family.
- **Concept fidelity.** If we were given a kit sheet / concept from Polygen, the model must be a sculptural answer to that sheet, not a generic dungeon pack.
- **Usability.** An LD can assemble a room in minutes without fighting pivots, scale, or 45-degree traps.

Taste scoring is pass/fail per gate plus a written note. “Pretty good” is not a grade.

---

## 7. Visual QA (proposed)

Two tracks. Both can fail the kit.

**Technical (automatable from Max / exported JSON)**

- Units, grid, snap
- Naming + layer contract
- Pivot at socket origin
- Module dimensions on grid (no 199.7 cm walls)
- No open sockets that cannot mate
- Quad-majority on deforming / bevelled areas; ngons only where the plan allows
- Density in budget
- MatID coverage matches the plan
- UV: overlap policy, texel density, trim vs unique, no 0-area islands
- Instance/XRef usage vs illegal copies
- Collision / LOD presence if the brief asked

**Taste / art direction (visual, needs images)**

- Ortho: top / front / side, shaded + wire + checker
- Game-camera stills of an assembled vignette (not an isolated wall)
- Wear/trim/hero closeups
- Side-by-side vs concept / kit sheet
- “Stale test”: three-module repeat — if it screams tile, fail

This cloud environment **cannot run 3ds Max**. QA here is rubric + contracts + review of images you (or a local Max agent) provide. Local Max is where scripts execute.

---

## 8. Questions that must be answered

Answer these in this file (or a kit brief that inherits this file). Empty answers mean we are still in vision lock.

### Identity

| # | Question | Status | Working answer |
|---|---|---|---|
| I1 | Product / repo name? | Proposed | **PolyMax** |
| I2 | Who is the user of v1? | Proposed | You + agents in this repo. Not a public Polygen feature yet. |
| I3 | Success for slice 1? | Proposed | A locked constitution + Max 2027 bootstrap + one kit brief that could actually be modeled. Not a finished cathedral. |

### Ecosystem

| # | Question | Status | Working answer |
|---|---|---|---|
| E1 | How does PolyMax talk to Polygen? | Open | Consume style/kit-sheet as input; do not reimplement generate. |
| E2 | What is PolyMesh vs this? | Open | Need your charter. If PolyMesh is topology, PolyMax calls it; it does not fork it. |
| E3 | What is PolyMat vs this? | Proposed | PolyMat authors sheets; PolyMax assigns IDs and UV layout to *use* those sheets. |
| E4 | Kingdom Crafter relationship? | Proposed | Taste + first real kit destination. |

### Craft defaults (per-kit can override, studio needs a default)

| # | Question | Status | Working answer |
|---|---|---|---|
| C1 | Engine target? | Proposed | Unreal 5 |
| C2 | Units? | Proposed | 1 Max unit = 1 cm |
| C3 | Default module? | Open | 200 / 400 cm walls are a common D4-ish start — confirm |
| C4 | Camera for QA? | Open | Third-person / D4-like vs FPS changes every silhouette decision |
| C5 | Collision / Nanite / LOD policy? | Open | |
| C6 | First proving-ground kit? | Open | Recommend one Kingdom Crafter / Sanctuary-adjacent interior kit, not a platform of kits |
| C7 | How does the agent drive Max? | Proposed | Local pymxs + MAXScript, driven by a JSON kit contract in this repo. No pretend-Max in the cloud. |

### Product surface

| # | Question | Status | Working answer |
|---|---|---|---|
| P1 | Is there a web app in v1? | Proposed | **No.** Docs, JSON contracts, Max scripts, Cursor rules/skills. |
| P2 | MCP server in v1? | Proposed | Not until the craft contracts exist. Polygen already has MCP. |
| P3 | Custom Max scripts in v1? | Proposed | Yes: bootstrap, naming, grid, socket/pivot checks, QA export. |

---

## 9. Slice 1, if you sign this

If you accept the Proposed column (or rewrite it), the next work is:

1. Freeze this document (mark Proposed → Locked).
2. Agent skills: vision-lock, kit-plan, max-2027-craft, studio-UV, visual-QA, taste.
3. `kit.schema.json` — the contract a brief must satisfy.
4. Max 2027 bootstrap pack (menu + pymxs): units/grid/snap/layers/naming.
5. One named kit brief filled in as the proving ground — still no hero detailing.

No mesh generation. No second website. No “platform.”

---

## 10. Sign-off

- [ ] Name locked
- [ ] Ecosystem boundaries locked (Polygen / PolyMesh / PolyMat / this)
- [ ] Craft defaults locked (units, engine, camera)
- [ ] Slice 1 scope locked
- [ ] First proving-ground kit named

Until these boxes are checked, agents may only revise this agreement.
