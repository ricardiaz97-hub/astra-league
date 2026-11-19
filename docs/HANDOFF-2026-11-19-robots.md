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
  - Robot: `chars/robot-gunner.glb`, look `24` in `VRMS`. It's the Mixamo Ch44 model, converted in Blender with transforms applied. The FBX had a 0.01 armature scale, which made the robot 4× too tall.
  - Drone: `props/drone.json`.
  - The user will send final gunner/brawler/heavy/dog models in T-pose for Mixamo.
- **Spawn:** `mob()` picks a gunner (60%) or a brawler (40%) and sets `f.robot`. `brute()` is a brawler with `f.big=1.45`, 260 HP, slower and harder hitting. `crawler()`/`sniper()` are the drone.
- **AI:** `robotAI` → `brawlAI` / `gunAI`, next to `mob()`.
  - **Brawler (Arkham style):** one attacker at a time (the token in `RB`), the rest circle at 4.5–6.5 m. A blue `!` warns 0.6 s before each 1–3 punch combo. Pressing **F** after the `!` counters (`player.parryAt`). Hitting the brawler during the wind-up interrupts it.
  - **Gunner (COD style):** finds cover with `coverSpot` (low cover, 0.72–1.55 m). It hides, then pops up with the `cv_Gunplay` clip and only fires while standing. It ducks when hit and advances 6 m every 7–11 s. It only shoots with line of sight (`los`), and its shots stop at walls.
  - **Drone:** circles its target 10–18 m out at 5–9 m altitude. Velocity is set directly, because in the air AI movement input barely moves it. Ceiling-rail drones inside the market still crawl.
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
