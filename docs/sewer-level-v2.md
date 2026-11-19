# Sewer Level v2 — Rumbo al Hotel Aurora

Replaces the old plan (entry tutorial → one canal with three identical lift holds → short straight chase). That plan was one long line with the same beat three times. This version is a **hub with two branches that loop back**, a **deep descent**, and a chase that **climbs out** under Hotel Aurora. Target length: **25–35 minutes**.

Map: [`../art/sewers/sewer-v2-layout.svg`](../art/sewers/sewer-v2-layout.svg) (plan + depth profile).

## The goal the player understands

The city's drainage is dead. The only way to Hotel Aurora is under the **Cisterna Mayor**, which is flooded. To drain it, the squad must bring power back to the hub (**La Rotonda**) from two substations, then run the cistern pumps. Draining the cistern exposes the beast's nest, and the beast.

## Route and beats

| # | Area | Depth | What the player does | Time |
|---|------|-------|----------------------|------|
| ① | **Pozo de entrada** | 0 → −18 m | Spiral stair down a round shaft, daylight above. Squad banter. No enemies. | 1 min |
| ② | **Colector Viejo** | −18 m | ~180 m of winding brick S-curves, ankle-deep water, side alcoves with loot. First ceiling crawlers in two spots. One checkpoint. | 4 min |
| ③ | **La Rotonda** (hub) | −20 m | Irregular round chamber with a balcony ring and a sealed central drain pit. Three gates: west (open), east (open), pit (needs power). A wall board shows both substations. | 1 min |
| ④A | **Los Sifones** (west) | −16 m | Sludge catwalk, then a 30 m crouch crawl pipe into a pump house. **Lever 1** starts a **90 s pressure hold**: bugs from three vents. When it locks, a flood gate opens a **shortcut straight back to the hub**. | 6 min |
| ④B | **Galería de Filtros** (east) | −20 → −6 m | Tall modern filter hall. Climb across five stacked tanks (jumps, one wall-run). Turn **3 valves** on top of three tanks while bugs climb after you (spread-out defense, not one circle). Then ride the **lift down** while it's attacked (waiting under pressure). The lift bottom is a **shortcut back to the hub**. | 7 min |
| ③ | Back at **La Rotonda** | −20 m | Both substations on → the pit opens. Short breather and squad dialogue. | 1 min |
| ⑤ | **Cisterna Mayor** | −40 m | Ladder down the pit into a huge pillar forest, half flooded. Start the drain: **3 pump consoles (P1, P2, P3) on different sides** must stay alive for ~3 min. Consoles get attacked one at a time, then together, so the squad has to split and rotate. Trapped workers on a platform must be reached once (rescue). As the water drops from −36 to −44 m, **ripples and a huge shape** move between the pillars: the beast, glimpsed and never fought. | 8 min |
| ⑥ | **El Nido** | −46 m | The drained floor reveals a tunnel into the nest: eggs, slime, silence. **Crouch walk**, no shooting (squad whispers). One egg hatches by itself and wakes it. | 2 min |
| ⑦ | **La Persecución** | −46 → 0 m | **RUN.** Up the aqueduct while it collapses behind you, wall-run a broken span, slide under a closing gate, then **crank a slow gate** while the beast closes in (the squad holds it off for seconds). Ladders up into the Hotel Aurora basement. Two checkpoints. | 4 min |

## What makes it not one shape

- **Loop structure:** hub → branch → shortcut back to hub, twice. The player sees each shortcut gate locked on the way in and opens it on the way out.
- **Vertical:** about 46 m from top to bottom, plus a 14 m climb inside the filter hall. The profile goes down, up, down hard, then up all the way out.
- **Five different spaces:** round shaft, winding tunnel, round hub, tall industrial hall, pillar cathedral, cave nest, rising aqueduct. No two rooms share a footprint.
- **Five different "wait" moments**, never the same beat twice: a single-point hold (Sifones), spread-out valves (Filtros), a moving lift (Filtros), rotating between 3 points (Cisterna), and a crank under chase pressure (Persecución).

## Space: from cramped to huge

The level squeezes the player first, then opens up. Tunnels are **round or arched**, not square (reference: `../art/sewers/inspo/tunnel-catwalks.jpg`). The cistern is a pillar hall like a flood-control reservoir (reference: `../art/sewers/inspo/cistern-pillars.jpg`).

| Area | Cross-section | Width × height | Feel |
|------|---------------|----------------|------|
| ① Shaft | Round, spiral stair | 6 m across | Closed in, light from above |
| ② Old collector | Low brick arch | 3 × 2.6 m | Cramped, ceiling crawlers right overhead |
| ④A Crawl pipe | Round pipe | 1.4 m | Most uncomfortable point: crouch only |
| ③ Hub | Dome | 30 m across, 12 m tall | First breath of space |
| Corridors between areas | Round tube with side catwalks over green sludge (like the reference) | 6 × 5 m | Mid-size, lights strung on cables |
| ④B Filter hall | Tall vault | 50 × 25 m, 20 m tall | Big and vertical |
| ⑤ Cistern | Flat ceiling on rows of huge pillars | 110 × 70 m, 25 m tall, pillars 4 m wide | The biggest space in the game |
| ⑥ Nest | Organic cave | 30 m | Tight again before the run |
| ⑦ Chase | Aqueduct arch, then shafts | 5 m, rising | Opens as you escape upward |

Curved walls are only a visual question. The game's collision uses axis-aligned boxes, so each curved tunnel gets a smooth arched mesh for the look and a chain of small invisible boxes (about 1 m apart) along its walls and floor for collision.

## Building it with what the game already has

| Need | Existing system in `index.html` |
|------|---------------------------------|
| Lever, valve, crank | Level 1 lever phase (`STORY.openShutter`, "Abre la cortina") |
| Timed hold | Level 1 `hold` phase (`STORY.hold`, spawn timer, "Resiste") |
| Bugs | `mob` (acechador), `crawler` (rastrero on ceilings), `brute` |
| Workers to rescue | `civRun` civilians |
| Climb, wall-run, slide, crouch | Existing parkour (`climb`, `wallrun`, `slide`, `crouch`) |
| Objectives, markers, checkpoints | `obj`, `markAt`, `STORY.cp` |
| Dialogue | `say` / `storyLater` and `story/*.json` lines |
| Textures | The ivory/charcoal/orange set from `docs/texture-prompts.tsv` |

New things this level needs: a moving lift platform, water that lowers in stages, and the beast (model in `art/sewers/sewer-beast-tpose-*.png`, still to be made into a 3D model).

## Rules for the blockout

- Every branch is readable: one main path, side alcoves only for loot.
- The next objective is always lit in warm orange; the cistern uses cold teal so the drop feels deeper.
- No timed failure on holds; enemy waves are the pressure. The chase uses checkpoints, never instant death on a missed jump.
- The beast is only seen in pieces (ripples, a shape, a tail) until the nest.

## Build notes (v3, big scale)

- Pipes are 14 m wide and 10 m tall (shortcuts 10 × 8 m) with a 6 m water channel sunk 1.5 m between two walkways. Crosswalk model (`props/sewer/catwalk.glb`) bridges the channel every ~45 m in the Sifones corridor and the chase.
- Rooms are 14–22 m tall with a sunken pool; the cistern is mostly water with pillars and console islands linked by grating walkways.
- Water shader is a WebGL port of Renka's stylized forest water (MIT, renka-exe.itch.io): vertex waves, voronoi caustics, noise foam, fresnel. The Godot version's screen-depth refraction is not ported.
- Portra 400 LUT and film grain are on for every map.
