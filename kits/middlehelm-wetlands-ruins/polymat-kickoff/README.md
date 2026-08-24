# PolyMat kickoffs

Albedo / layout **starts** from Cursor image gen. **PolyMat** does the real tiling solve and the rest of the PBR set (normal, height, roughness, AO). Do not ship these as final materials.

| File | Intent | Verdict |
|---|---|---|
| `mhwr_trimsheet_kickoff.png` | 2D trim atlas (courses, moldings, rubble, moss) | **Usable kickoff.** Not a packed studio sheet. |
| `mhwr_tile_ashlar_dry.png` | 4-edge tile dry ashlar | **Best tile candidate.** Verify wrap in PolyMat. |
| `mhwr_tile_ashlar_wet.png` | Uniform wet tile | **Failed as a tile** — vertical waterline gradient. Use as trim/unique, or re-prompt: no gradient, four-edge wrap. |
| `mhwr_tile_moss_overlay.png` | Sparse ID 6 overlay | **Partial.** Drifted toward mossy paving. Re-prompt if we need overlay-only. |

See `.cursor/skills/visual-kickoff/SKILL.md`.
