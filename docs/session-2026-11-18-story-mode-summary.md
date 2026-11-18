# Session summary — Story Mode Level 1 (Olocuilta Market)

Date: 2026-11-17 / 2026-11-18
Branch: `codex/market-map-level` (fast-forwarded to `origin/main` at the start)
Status: **nothing committed**. Earlier local edits (Tefa Mixamo loader, two README lines) are saved in `stash@{0}`.

Main files changed:
- `index.html`: almost all work is in the `MODO HISTORIA` block (`STORY.*`). A few small hooks sit outside it, listed under "Changes outside the story block".
- `story/nivel1.json`: all Level 1 dialogue.
- `docs/campaign-level-1-layout.md`: implementation notes appended.
- `.claude/launch.json`: local server config (`python -m http.server 8000`).

New asset folders (copied from the user's folders, plus derived files):
- `chars/story/civ/civ00–12.glb`: 13 rigged civilians (Tripo + Mixamo skeleton).
- `assets-source/incoming/`:
  - `city/`: brutalist building, storefront, market hall, rubble, street light, tile roof, japan street.
  - `trees/`: 5 stylized trees, converted from `.blend` with Blender.
  - `lod/`: low-poly versions of 4 stalls and the lamp, made with Blender Decimate at 22% / 15%.
  - `rigged/`, `props/`: other models received, not used yet.
  - `zips/`: extracted tree pack, Looming Landmarks, fences.
  - `windturbine.glb`
- `textures/ui/sky-olocuilta-sunset.webp`: the user's skybox.

---

## 1. Dialogue presentation

- The box uses the user's texture `art/ui/dialogue-box-astra.png`. Text types out progressively; the built-in ▼ blinks when the line is complete.
- Portraits come from `art/character-select-transparent/<slug>.png` (`PORTRAITS`, `portraitOf`). They are **full-body**, about 84% of screen height, standing **behind** the box so only the bust shows above it, old-RPG style. Combat barks use a smaller size.
- Radio and civilian lines use a badge instead of a portrait.

## 2. Level 1 flow (`STORY.begin` / `STORY.tick`)

1. **Opening flyover** from behind the cathedral, over the market roof, to the player (skippable).
2. **Enter** through the columned front (porch steps have collision).
3. **Rescue**: 8 civilians surrounded by 10 acechadores.
4. **Vault rows**: three rows of the user's concrete jersey barriers with pallets and drums.
5. **Ceiling crawlers**: 3 Rastreros on the roof beams. They glow purple before spitting.
6. **Ramp**: a custom U-ramp (built geometry, the user's textures) up to the **gallery around the market** (west, front and east sides, built with the user's textures).
7. **Broken gallery**: wall-run along the orange safety-band wall, wall-jump to the far ledge. Falling resets you to the gallery.
8. **Lever** opens the shutter. Civilians come through on their own lanes.
9. **Exit**: camera cut zooms on the squad about 200 m away, then pans to the Ferris wheel.
10. **Crossing**: hordes come from the market doors and the side streets. Drivable vehicles are available.
11. **Barricade line**: 7 squad members hold it; civilians pass behind to shelters by the wheel.
12. **Hold 3:00**: escalating waves, brutes and advancing crawlers. Squad barks count down.
13. **Ship arrives**: a cutscene shot shows the landing, and the ship clears the zone.
14. **Boarding**: the camera sits on the far side of the ship. You, the civilians and the squad run in; the hull hides you as you reach it.
15. **Takeoff**: the ship lifts, then the camera pans to the burning market for the closing lines and the end screen (next: the sewers, toward Hotel Aurora).

## 3. World and art

- Interior floor raised **0.9 m** (`LIFT`) to porch height. Everything inside the market lifts automatically (`inMk`).
- Models are placed **uniformly scaled, never stretched** (`sFit`). Stall collision matches each model's real size.
- The 200 m fairground is crowded with stalls of varied size and angle; a center lane stays clear.
- Uses the user's models: stalls, cart, bench, sign, bollard, Ferris wheel, pickups, hover pod, base ship (end only), fighters in the sky, jersey barriers, pallets, drums, wrecked cars, brutalist buildings, trees, wind turbines, plaster / plackard / brick / metal walls.
- Uses the user's textures: floors 01/02/04/05/07, walls 02–07, market wall base, ramp floor.
- **Horizon**: 2.6 km ground plane, a procedural ring of hills, layered city blocks, tree lines, turbines and street walls, so the map no longer ends like a scale model.
- The multiplayer map's symmetric houses, boundary walls and gray boxes are hidden during story mode and restored afterward (`STORY.hideMap` / `STORY.restoreMap`).

## 4. Lighting and atmosphere

- The user's sunset skybox; sunset fog from 110 m to 1150 m; camera far plane 2600 m.
- The sun's shadow box **follows the player** (it used to cover only ±82 m around the map center). Lower, warmer sun, more contrast, warm rim light.
- The roof darkens the market interior (`setIndoor`).
- Dust motes and light shafts inside; smoke columns over the city that grow with the battle; embers, falling ash, distant explosion flashes with a low boom; fighters and pods crossing the sky.
- Cel shading: ink outlines (`inkOutline`) on the market interior and key props, not on distant objects.

## 5. Camera and presentation

- Cutscene system `STORY.cine` (letterboxed, HUD hidden, skippable with click, SPACE or ESC). Used for the opening, the squad reveal and the ship arrival.
- **Loading screen** (`STORY.loadScreen`, `#sLoad`): concept art, chapter title, a gameplay tip and a progress bar that counts pending models, textures, characters and creatures. It stays until everything has loaded (40 s at most); the flyover starts after it.
- Driving: the camera follows the vehicle from higher up and farther back; the character is hidden and reappears beside the vehicle on exit. FOV widens with speed.
- Ultimates no longer zoom the camera out (this also applies in multiplayer).
- Screen shake on brute hits and ramming; hit-stop on ramming.

## 6. Gameplay and AI

- **Enemies**: acechador 28 HP, brute 120, crawler 45/60. Movement about 50% speed (brutes 38%), no sprint or dash, 40% damage (brutes 50%). They push apart (separation) so they don't stack.
- **Squad (7)**: run on the multiplayer bot AI (`updBot`) with their own target (nearest invader) and a spot on the line that shifts every few seconds. They show full animations, use their real guns and sounds, take cover, dash, melee and use hero skills, plus a Ki area power every 14–20 s. Two of them are melee fighters who rush enemies within 18 m. They can't die and do 30% damage, so enemies still reach the barricade.
- **Civilians**: the user's 13 rigged models. Heights 1.30–1.88 m, each on its own lane, separated, with a stuck-teleport fallback.
- **Vehicles**: 3 pickups and 3 hover pods. `G` gets in and out, `W/S` accelerates, `A/D` steers. Ramming kills invaders.

## 7. Changes outside the story block

- `lowpolySource`: keeps vertex colors; leaves use alpha cutout.
- `useTex`: loads are counted in `LOADQ` (for the loading screen), with an error callback.
- `updCamera`: `window.__camFollow` / `window.__camBack` (driving camera); `window.__fovAdd`; ult zoom disabled.
- `damage`: story invaders deal less damage; the squad can't die and deals 30%.
- `buildMarket`: the procedural Ferris wheel is named `ferrisProc` so story mode can hide it.
- New sound `'boom'` (distant explosion).

## 8. Other session (animation and VFX)

Ran separately as "Anime-grade animation and Ki VFX overhaul". It added hand-drawn Ki VFX (the `CEL:` block: sparks, flares, charge-ups, slashes, dash trails, landing cracks and dust) using Brackeys CC0 sprites, plus animation feel: anticipation and strike timing, run-attack upper/lower body split, landing squash, sword smear, delayed hit-stop. It confirmed bullet impact sparks and tracers are intact. The Motifect animation packs were tried and removed.

## 9. Known pending / not verified

- Nothing committed. `graphify update .` was not run (graphify-out is stale).
- The full level has only been run with scripted teleports and kills, plus the user's own play; there has been no long manual playthrough on a low-end PC.
- Latest fixes not yet confirmed in-game: hidden player while driving, and the boarding cutscene.
- The squad's melee and cover behavior was rarely observed in tests.
- Ricardo should fight with bare hands (berserk with no weapons); this needs unarmed animation clips.
- `stash@{0}` holds the old local edits; decide whether to keep or drop it.
- `.claude/launch.json` is untracked.
