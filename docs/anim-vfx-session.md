# SUNBURNT: animation + VFX pass (session summary)

File: `index.html` · branch `codex/market-map-level` · **nothing committed yet**

## Kept (live in the game)

### Hand-drawn VFX (`CEL:` block, just before `function fxWord`)
- Flipbook sheets drawn once on canvas at load; fixed pool of 90 planes (no objects created per hit).
- API: `celFx`, `celLand`, `celSpark`, `celSlash`, `celCharge`, `celFlare`, `celTrail`, `updCel` (runs in `step()`).
- **Ki effects** (sparks, flashes, charge-up, lightning, ki rings, dash trail, sword crescent): additive glow, white core, team-color halo, no dark outline.
- **Dust, ground cracks, speed lines**: drawn shapes, soft same-color borders.
- Brackeys CC0 sprites used: `textures/vfx/cel/slash.png` (slash_02), `textures/vfx/cel/bolt.png` (spark_05). Full bundle extracted to `assets-source/incoming/brackeys-vfx-bundle/`.
- Mobile uses smaller sheets (128 px cells instead of 256).

### Where the effects appear
| Event | Effect |
|---|---|
| Any hit (bullets and melee, via `fxHit`) | `celSpark` (big hits add ring + speed lines) |
| Landing from a fall | crack, ring, dust, radial speed lines |
| Hero slam landing | big version + hitstop |
| Jump / double jump | dust puff / ki ring |
| Sword strike | crescent in the real swing plane, at the strike frame |
| Dash | ki trail streaks |
| Ki charge (V), heavy-charge levels, ultimate start | `celCharge` (converging spikes + lightning) |
| Ki beam | charge flipbook at source, flare + ring at tip |

### Animation feel
- Smooth blending between all states (idle, run, aim, jump, land, attacks).
- Attacks: short anticipation, fast strike, slow recovery. The strike frame is detected from each clip (`ATK`, `atkPeaks`, `atkFrac`).
- Attacking while running: torso attacks, legs keep running (`UPPER` / `LOWER` bone masks).
- Weight: legs bend and body squashes on landing, stretches on jump (`vrmWeight`).
- Sword smear: blade stretches on the fastest frames.

### Impact
- Hitstop lands on the strike frame, not on the click (`stopQ`).
- Camera shake scales with hit strength.
- Combo input buffer widened (`p.cd < .5`).

## Removed
- **Motifect packs** (combat + fantasy/magic, 80 BVH clips): looked wonky on the Tripo rigs, even after per-bone retargeting, twist limits and jitter smoothing. All wiring was taken out of `index.html`.
- Leftovers on disk, not loaded by the game: `anims/motifect-combat.json`, `anims/motifect-magic.json`, `tools/bvh2anim.py`, `tools/motifect-magic.json`, `assets-source/incoming/motifect-*`.
- Note for a retry: the retarget math checked out (rest pose differs by 21° or less). Do it in Blender with visual checks per clip.

## Not changed
- Bullet tracers (`tracer`) and the muzzle flash.
- Gameplay values, controls, models.
- The story-mode block (`MODO HISTORIA`), which belongs to another session.

## Pending
- Ricardo fights with no sword; his berserk form uses no weapons at all. Needs bare-hand clips. Ask before changing weapons.

## How to test
1. Run `python -m http.server 8000` (launch config `astra`), open http://localhost:8000, hard reload with Ctrl+F5.
2. Jump and land, combo with the sword, attack while running, dash, hold V, fire the ultimate beam, shoot something.
