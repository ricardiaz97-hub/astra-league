# Handoff — 2026-11-19 (part 2): robot enemies, cover system, finished market level

Branch: `codex/market-map-level`. This file arrives in the same commit as the work it describes. Not merged to `main`. Read `docs/HANDOFF-2026-11-19.md` first: the sewer level, weapons, Ricardo, and how we work.

## Run it

```
python -m http.server 8000
```

Open `http://localhost:8000/`. **Level 1:** HISTORIA → SIGUIENTE → COMENZAR. Hard-reload (Ctrl+Shift+R) after every change.

## Status

**Level 1 (Mercado de Olocuilta) is finished.** The user approved it on 2026-11-19. Don't rework it unless they ask.

## Rules learned the hard way

- **Never insert a `// comment` mid-line in `index.html`.** Lines are very long, and a mid-line comment silently comments out the code after it. `new Function` syntax checks still pass, but the game throws every frame: the image freezes while audio keeps playing.
  - Use `/* */`, or put the comment at the true end of the line.
  - After a patch, grep the new comments and check nothing follows them.
- **`index.html` uses LF line endings.** Patch scripts must use `'\n'`.
- **Runtime check** (allowed; it isn't play-testing): open the preview pane and start story mode from JS by clicking HISTORIA → SIGUIENTE → COMENZAR. Then add a `window.addEventListener('error',…)` listener, wait about 15 s and read the errors. Stale console messages can survive a reload, so trust the listener instead.

## Enemies: robots (replaced the bug mobs)

- **Models (placeholders):**
  - Robots (final, Tripo + Mixamo rig): looks `24` gunner M, `25` gunner F, `26` brawler M, `27` brawler F in `VRMS` (`chars/robot-gunner-m.glb` … `robot-brawler-f.glb`). `mob()` picks male or female at random; `brute()` uses `26` scaled up.
  - Drone: `props/drone.json` now holds the user's final drone (Tripo `tripo_convert_14cc4824-…(1).glb`, no rig, base64). `attachCreature` scales it to height, so its size in the file doesn't matter.
  - Still missing: the heavy with the shield (Tripo keeps exporting a Character Creator skeleton, not Mixamo: `Hip`, `Waist`, `L_Thigh`; needs an unrigged FBX through Mixamo) and the level 2 beast (Tripo quadruped rig, needs its own clips).
- **Spawn:** `mob()` picks a gunner (60%) or a brawler (40%) and sets `f.robot`. `brute()` is a brawler with `f.big=1.45`, 260 HP, slower and harder hitting. `crawler()`/`sniper()` are the drone.
- **AI:** `robotAI` → `brawlAI` / `gunAI`, next to `mob()`.
  - **Brawler (Arkham style):** one attacker at a time (the token in `RB`), the rest circle at 4.5–6.5 m. A blue `!` warns 0.6 s before each 1–3 punch combo. Pressing **F** after the `!` counters (`player.parryAt`). Hitting the brawler during the wind-up interrupts it.
  - **Gunner (COD style):** finds cover with `coverSpot` (low cover, 0.72–1.55 m). It hides, then pops up with the `cv_Gunplay` clip and only fires while standing. It ducks when hit and advances 6 m every 7–11 s. It only shoots with line of sight (`los`), and its shots stop at walls.
  - **Drone:** circles its target 10–18 m out at 5–9 m altitude. Velocity is set directly, because in the air AI movement input barely moves it. Since 2026-11-19 every drone flies (no more ceiling rails), and they are called "Dron".
- **Spawn drop:** `sDrop(f)` drops robots from 38 m, or 9 m inside the market (the ceiling), with a landing burst.
- **Damage:** in `damage()` robots deal ×0.35 and brutes ×0.6.
- **Bullets:** all guns (player, squad, bots) use `bullet()`, a thin streak moving at 220 m/s (`BUL`, `updBul`). Hits show small sparks only. `tracer()` remains for power/ki beams.

## Player systems (whole game)

- **Crouch:** **C** while standing or walking; running + C still slides. The flag is `CROUCH`.
- **Low cover (contextual):** walk up to cover 0.72–1.55 m tall to auto-crouch. Aim to pop up. Space vaults (`p.vaultQ` → `tryLedge`). Moving along cover plays `cv_Crouch_Cover_To_Cover`.
- **High cover:** `HC`, `updHigh`. Push into a wall taller than 1.55 m to put your back to it. Aim near a corner to step out past the edge.
- **Camera:**
  - **In cover:** it pulls to the side (`COV.k`/`HC.k`).
  - **Melee:** it rises 1.2 m and tilts down (`CUP`/`CUPm`).
  - **Skills, ult or charging:** it rises without tilting.
- **New clips:** `anims/cover2.json`, `cover3.json` (vault, freehang climb), `crouchhit.json` (hit reactions, crouch locomotion) and `highcover.json`.
  - `hitAct()` picks the light or heavy reaction.
  - A parried attacker plays `cr_Getting_Hit_Backwards`.
- **Converting Mixamo FBX files:** copy the FBXs plus `Ch44_nonPBR.fbx` (renamed `character_orange.fbx`, used as the T-pose reference) into `tmp/<dir>/`. Run `node tools/anim-recv.js anims`, then open `tools/fbx2anim.html?dir=<dir>&out=<file>.json&pre=<prefix>&files=…&loop=…`.

## Level 1 layout (market → street → defense zone)

- **Street:** 100 m (was 200). `MK.line=-97`, `MK.lz=[0,-125]`.
  - Eight hand-placed cover rows plus textured blocks.
  - The street narrows (walls at |x| 28–62) for the last 14 m before the line.
  - The side alleys beside the market are walled off.
  - A row of buildings at z −160 closes off the back.
- **Rear of the market:** it uses the model's three openings (x −17.5…−7.5, −4…4, 9…19), measured by raycasting the GLB in Blender.
  - Shutters sit in those openings (`STORY.shutters`).
  - The lever is on the rear gallery.
  - The gallery runs around the market, but both rear corners are collapsed (`galBroken`, `galBrokenW`). The east wall-run is the only way to the lever.
- **Hold phase, "Espera la evacuación":**
  - Wave cap is 12 → 18.
  - About 35% of robots go after the civilians (`wantCiv`).
  - Civilians sit in two barricaded sectors (x ±42, z −115) and share one group HP bar (`STORY.civBar`, `civHit`, `civAlert`). If it empties, the ship takes 30 s longer; there's no fail state.
  - At 45 s, three trapped civilians appear mid-street (`STORY.trap`).
- **Squad classes:** Bastión, Sanador, Destello, Sanador, Impacto ×2 (the brawlers), Destello. Each uses its skill every 7–11 s.
- **Ending:**
  - Mothership: the `ship` model at 7× scale, hovering (`STORY.mother`, `motherTick`).
  - The evac shuttle is a 9 m pod (`rover` model, `buildShip`). Four 5.5 m pods land beside it.
  - Civilians board the pods; the squad boards the shuttle.
  - `STORY.depart`: the shuttle and pods fly up into the mothership, then it leaves.
- **Lighting:** the original gloomy night. Street lamps every 17–23 m, and every other one gives real light. The pad floodlights are dimmed. An old mid-line comment had broken their aim; that's fixed.

## Next work

1. **Melee VFX (the user's next ask):** turn most of it down to thin, subtle, flowing effects. Keep VFX for powers, used with taste.
2. **Robots:** final models from the user (gunner, brawler, heavy with a shield, a dog — Mixamo can't rig quadrupeds — and the drone). Then swap the placeholder files.
3. **Robots in high cover:** `coverSpot` only finds low cover.
4. **Check in the arena:** the camera rise, the bullets and the cover changes are global but haven't been checked there.
5. **Sewer level beats:** still open (see the first handoff).

## Sprite VFX (started 2026-11-19, P1 in)

- Style: 2D painted sprite sheets (Marvel Rivals / Deadlock look) plus 3D from code (real light flash, flat shock rings on the floor, ground cracks, orientation along swing/barrel). All old procedural VFX is to be scrapped as each event gets its sprite.
- Prompts: `docs/fx-prompts.tsv` (28 effects, P1–P3). The user makes the art in ChatGPT (real transparency) or Gemini (magenta background).
- Sheets: `fx/sprites/<name>.webp`, 1024 px, 4×4 grid of 256 px frames. 36 sheets, 5.4 MB. Extras with guessed names: `burst_white`, `geyser_white`, `fire_b`, `fire_ring`, `fire_pillar`, `muzzle_b`, `muzzle_c`, `ink_burst_b`, `slash_arc_b`. `ult_start` is missing.
- Player: `celImg(name,img,n)` registers a sheet in `CEL.sheets` (`img` 1 = alpha, 2 = additive glow on black). `celFx` and the `CELF` shader play it in full color (`tint:1` multiplies by `col`).
- P1 wiring:
  - `celSpark` → `hit_light` / `hit_heavy` + `ink_burst`.
  - `fxHit` → light flash + `celSpark` (old star/spark sprites removed).
  - `damage` → `spark_metal` on robots; `robot_boom` + ground shock on robot/drone death.
  - `parried` → `counter_flash` + cyan ring.
  - `celSlash` → `slash_arc`.
  - `fxDecal` → `impact_dust` (old bullet sparks removed).
  - `muzzleFlash(p,col,k,to)` → `muzzle`, rolled along the barrel.
  - `celLand` → `land_ring` over the crack and the flat shock.
- P2/P3 wiring (same day):
  - `img` 3 = white on black, where brightness becomes alpha and `col` tints it. Used by `smoke`, `ring`, `aura_loop` and `beam_hit`.
  - Shared helpers now draw sheets, so every caller changed:
    - `fxSmoke` → `smoke`
    - `fxShock` → `ring`
    - `fxBoom` → `explosion`
    - `fxDust` → `jump_puff`
    - `fxAura` → `aura_loop`
    - `celFlare` → `beam_hit`
    - `celTrail` → `dash`
    - the jump puff → `jump_puff`
  - Heroes: `slapHit` → `mau_slap`, `quakeHit` → `mau_quake`, `heartHit` → `ricardo_cry`, and Ira's aura loop → `ricardo_rage`.
  - Squad: Bastión wall → `shield_hit`, Sanador → `heal`, Destello blink → `flash` (both ends), and `slam()` / `allyPower` → `slam`.
  - Story fires (`flameFrames`) play `fire.webp` (4×4, additive). `fx/flame-atlas.png` is now unused.
  - Not wired yet: `splash` (there's no water-entry hook), bullets hitting a Bastión wall, the extras, and `ult_start` (art missing). Old `burst()` particles, `kBlast`, `kPillar`, `kStreak`, `gRing` and `sprA` remain as the 3D/energy layer.
- Sprite list v2 (2026-11-20): `docs/fx-prompts-v2.tsv`, 58 rows. 8 are REDO, sheets that touch their cell edge (`mau_quake`, `land_ring`, `dash`, `burst_white`, `geyser_white`, `aura_loop`, `mau_slap`, `ricardo_rage`). 50 are NEW, mostly replacing the leftover code effects that look messy: `fxRune`, `kStreak`, `kBlast`, `kPillar`, `kDome`, `sprA`, `fxBolt`, `fxStars` and `fxWord`.
  - Every prompt has a CROP RULE: 12% empty margin in every cell.
  - New layouts: `tall` (2:3 image, 4×3, cells 1:2), `wide` (3:2 image, 3×4, cells 2:1) and `strip` (4 tiling bands for beam bodies).
  - Code to do: `celImg` must take cols/rows and the cell aspect (scale `ax`) for tall/wide sheets.

## Sprite VFX v2 wired (2026-11-20)

- All 87 sheets in `fx/sprites/` are used; `fx/flame-atlas.png` was removed. Sources are in `Downloads/SPRITES` (files with no extension). The import script resized them to the layouts and removed the magenta.
- `celImg(name,img,lay,n)`: `lay` 0 = square 4×4, 1 = wide 3×4 (cell 2:1), 2 = tall 4×3 (cell 1:2), 3 = 4 strips. `celFx` scales the width by the cell aspect (`S.ar`).
- `celAtt(parent,name,o)` puts a looping sprite on an object and moves with it (`updAtt`, called from `updCel`). Used for the drone thruster, item glow, jump pads, beam body (crossed quads) and start, projectile orbs, robot sparks below 35% life, and fire smoke columns and embers.
- Old code effects now drawn as sheets: `sprA` (charge/vortex → `charge_in`, eRing, hit, boom, star), `kBlast`, `kDome`, `kPillar`, `kStreak` (→ `buff_up`), `fxRune` (→ `cast_circle`), `fxStars` (→ `stun`), `fxBolt`, `fxRingB` (→ `e_ring`) and `fxBurst`.
- New events:
  - combat: block, parry glint, robot warn "!", death, respawn, headshot, `ult_start`
  - drones: charge and shot
  - robots: `drop_trail` on the way down, `celLand` when they land
  - items: glow and take, plus `buff_up` for buffs
  - zones: kiField → `zone_ki` / `zone_burn`, Sanador zone → `zone_heal`, Bastión wall → `shield_wall` / `_b` (team)
  - movement: double jump, wall-run, slide, sprint wind
  - vehicles: exhaust, tire dust, crash
  - sewer: drips, ripples, steam, splash, slime
  - story: lever short, `pod_land`, `tractor` + `rescue` on boarding, `warp` when the mothership leaves
  - variants: muzzle, ink and slash pick a random sheet
- The 3D layer stays under the sprites: `lightFlash`, `ring` / `gRing` floor rings, `celLand` cracks and shocks, shake.
- Still missing art: comic `words` (`fxWord` is still text). Sizes and timing get tuned at the end.

## Grayscale sprites + palettes (2026-11-20)

- Direction from the user: every sheet is painted in grayscale with no black outlines and no halftone, and code colors it. Prompts: `docs/fx-prompts-gray.tsv` (89 effects, P1–P3, with default colors per effect). `docs/fx-prompts-v3.tsv` holds the earlier no-outline redos.
- `img` 4 = gradient map: each grey takes a color from `[dark, mid, bright, opacity, additive]`. `celImg` detects a grayscale sheet when it loads (average saturation < 8), so a new gray file dropped in with the same name just works.
- `DEFPAL` holds the defaults per sheet: fire orange, smoke = scene fog color + warm grey at 50%, water teal at 60%, slime green, sparks, drones purple and so on. Anything not listed uses the team color or `o.col`. `o.pal` picks a named palette (`blood`, `tea`, `sewage`, `bluefire`, `water`) or takes an array, e.g. `celFx('splash',x,y,z,{pal:'blood'})`.
- Removed for looking bad: `burst()` square particles, `fxRune` floor circles, `gRing` dashed floor rings, the aura bubble (`m.aura`), the marker gem, and the outlined sheets (hit_heavy, ink_*, robot_boom, explosion, headshot, stun, smoke_column), now covered by clean stand-ins.
