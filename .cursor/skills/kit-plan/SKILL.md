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
6. First assembly — the smallest walkable proof named on **this** brief.

## Active kit

`python -m polycraft kits` then read that brief. Assembly jobs live in `kits/<id>/max/jobs.json`. Do not copy another kit’s bays, trims, or prefixes.

## Output

`brief.json` must still validate (`python -m polycraft validate`).
