---
name: kit-plan
description: Turn a signed world/AD brief into modules, sockets, MatIDs, UV strategy, naming. Use only after world and art direction exist.
---

# Kit plan

Do not start here. If `world` or `artDirection` is missing, run those skills first.

## Job

Turn the place into a **language**: grid, sockets, IDs, UV policy, module list, first assembly test.

## Order

1. Grid steps (studio default 0.5 / 1 / 2 / 4 / 8 m) and exception rule.
2. Socket law (pivot, mate, what may break the module without breaking the grid).
3. Material IDs at kit scale.
4. UV strategy (trim vs unique vs stack). Do not unique-unwrap modular walls.
5. Module table with `priority`: blockout / craft / overlay / hero / later.
6. First assembly test — the smallest walkable proof (see Middlehelm brief).

## Active kit

`kits/middlehelm-wetlands-ruins/`. Arcade 4 m + wide 8 m, pier 1 m, aisle 2 m, waterline trim, one standing vault. Hero west front is **not** blockout.

## Output

`brief.json` must still validate against `contracts/kit.schema.json`.
