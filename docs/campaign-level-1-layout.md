# Campaign Level 1 — Olocuilta Market Evacuation

## Goal

The player is the squad member separated when the invasion begins. Rescue the civilians trapped in Olocuilta Market, guide them to the Ferris-wheel evacuation zone, reunite with the squad, and hold the fairground until the evac ship arrives.

This level is an authored, two-story campaign route—not a reused multiplayer arena. Use `olocuilta-market-map-guide.md` and the concept images in `art/markets/` as layout references.

## Level flow

| Beat | Space | Gameplay |
|---|---|---|
| 1. Invasion begins | Cathedral-side forecourt and columned front entrance | Player starts separated from the squad and enters the market after seeing survivors trapped inside. |
| 2. Rescue | Front-middle ground-floor stalls | Regular mobs surround the survivors. Clear the encirclement and open a route into the central aisle. |
| 3. Learn vault | Ground-floor stall rows | Knocked-over stalls block the route. Teach vault-over with a low, obvious obstacle, then use a few more as traversal and cover. |
| 4. Overhead threat | Main aisle and market rows | Ranged mobs hang from roof beams and crawl overhead. Telegraph attacks; keep civilians and player routes legible. |
| 5. Vertical traversal | East/right-side ramp to second-floor gallery | Ramp remains intact at the lower-right/front end. Player follows a long intact gallery toward the back. |
| 6. Wall movement | Broken upper gallery near the rear | Player wall-runs along the intact marked wall and wall-jumps to the far ledge. This gap is well separated from the ramp. |
| 7. Cross the fairground | Long open approach behind the market | From the rear market doors, the squad is visible roughly 200 meters away at the far barricade line. Sparse stalls, planters, carts, and vehicles create separated cover islands so the player can cross while hordes advance behind. |
| 8. Reach the team | Distant barricade line | The player reaches the squad. A teammate calls them over and reports that the evac ship is five minutes out. |
| 9. Civilian passage | Barricade line and safe cover lanes | Squad members hold a controlled gap while civilians pass behind the defenders and move to cover along the north/east and north/west edges. The central landing zone stays clear. |
| 10. Five-minute hold | Huge Ferris-wheel fairground | Defend civilians and the barricades against escalating waves advancing from the market and both side streets. Use regular mobs, ranged crawlers from the market edge, and occasional brawlers. |
| 11. Extraction | Open landing zone near the Ferris wheel | The ship arrives after the five-minute defense. The squad and civilians board and evacuate while the market burns behind them. |

## Spatial rules

- The cathedral and columned entrance are the **front/south** landmark.
- The Ferris wheel is the **back/north** landmark. The squad's barricades and civilian holding area are in the open fairground around it; the ship lands in a separate clear zone.
- Leave roughly **200 meters** of broad open ground between the market's rear exit and the squad's barricade position. Treat 200 m as a target scale for the blockout, not a surveyed real-world measurement.
- Break up the long crossing with a small number of separated cover islands at readable intervals; preserve long sightlines so the advancing hordes are visible.
- Civilians stay on the ground-floor main aisle; the player takes the second-floor traversal section and rejoins them at the rear.
- Keep the ramp landing clear and visibly distinct from the broken gallery crossing.
- Ranged enemies use ceiling beams as their traversal space, not balcony positions.
- Regular enemies surround the survivors during the rescue encounter.
- Stall obstacles teach vaulting. The upper-floor gap teaches wall-run and wall-jump.
- Keep the fairground as the largest open gameplay space in Level 1; put cover and fairground stalls around its perimeter so the landing zone remains open.
- Face the barricade line toward the market's rear doors. Civilians pass through a defended gap and move behind the squad to cover; wave enemies approach from the market and side streets.
- The squad's radio line tells the player to reach them and says the evac ship is five minutes away. Start the defense timer only after the civilians have reached the safe side of the line.
- On ship arrival, stop new waves, stage boarding, and show the market burning in the departure view.
- Keep the fairground defense sequence as the campaign's largest combat space. It should feel much larger than the market interior and the first traversal section.
- Reuse game assets where helpful, but keep this campaign layout separate from all multiplayer layouts.

## Browser-game scope

Build the level as a compact graybox using the existing movement, combat, and enemy systems. Use a small number of encounter groups, objective markers, and clear transitions. Add set dressing only after the front-to-back route, civilian path, ramp, traversal gap, and extraction zone work clearly. The five-minute hold should be one final authored defense sequence, not a multiplayer arena reused unchanged.

## Current implementation (story mode, `index.html`)

Story mode now runs Level 1 on the Olocuilta market map (`MAPS[4]`). The script lives in the `MODO HISTORIA` block of `index.html`; dialogue text lives in `story/nivel1.json`.

- **Collision:** the market GLB is visual only, so story mode adds invisible walls around the interior (x −39..39, z −5.5..71.5), with the front arch and the central rear door left open.
- **Models used:** stalls, cart, Ferris wheel, bench, sign, bollard, pickup, rover and the evac transport from `assets-source/`; the U-ramp, straight gallery segments, floor slab, rubble and hanging lamps from `art/markets/models/`. Textures: the ramp texture plus `floor_01`, `wall_04` (wall-run surface) and `wall_07` from `assets-source/textures/`.
- **Route:** cathedral forecourt (z 92) → rescue at the front-middle (z ≈ 50) → three rows of knocked-over stalls (z 40/32/24, vault) → two crawlers on the roof beams (y 12) → U-ramp on the east side → gallery to z 13 → wall-run along the orange wall, then wall-jump to the far ledge (y 4) → lever opens the shutter (z 2) → rear door → fairground crossing → barricades (z −194) → civilians pass → 5:00 hold → ship lands at z −222 → boarding → departure view of the burning market.
- **Failing the gap:** falling under the gap, or into the shaft beside the wall, puts the player back on the gallery.
- **Not modeled yet:** the 16 market civilians in `assets-source` are static T-poses with no rig, so the running civilians still use `chars/story/c_civ1-4`. The broken-gallery piece (`87ce…`) is unused because it would overlap the gallery segments. There is no brawler model, so brawlers are scaled-up acechadores.

### Polish pass (2026-11-17)

- Sky: `textures/ui/sky-olocuilta-sunset.webp` (story mode only). Floors: `floor_02` inside the market, `floor_05` on the fairground, `floor_01` in the forecourt and on the far ledge.
- Models are scaled uniformly and are never stretched. The straight gallery mesh comes tilted (~5° along its length, ~5.6° across), so it is leveled with `rx -0.098, rz -0.087`. Two segments run edge to edge from the ramp to z 14.6. The broken gallery piece is flipped, lined up with the segments, and has fallen to the floor under the gap.
- The shutter is now at z 5. The far ledge sits behind it at y 4.
- Stalls, carts, benches and signs are placed in the cathedral forecourt and along the fairground edges. The center stays clear for crossing and landing.
- Vehicles: 3 pickups and 3 rovers can be driven. Press `G` to get in or out, `W/S` to accelerate, `A/D` to steer. Hitting an invader at speed kills it.
- Squad: 7 teammates hold the line. The Ferris wheel stands behind them at z −236.
- Enemies: acechador 28 HP, brute 120, crawler 45/60. The 3:00 hold allows up to 34 alive, and the crossing spawns larger groups.
- `assets-source/incoming/rigged/`: 17 Mixamo-rigged GLBs (one character in a striped jacket, plus 2 bulky variants) and 2 rigged creatures. They are not wired into the game yet. `assets-source/incoming/props/`: 12 civilians in T-pose with no rig.
- Civilians: the user's 13 Tripo models with Mixamo skeletons, in `chars/story/civ/civ00-12.glb` (`VRMS` keys 40–52). Eight of them are trapped at the rescue. The old `c_civ1-4` VRMs are no longer used. Tripo's batch export drops the skeleton, so export rigged models one at a time.
- Enemy tuning: about 50% move speed (brutes 38%), no sprint or dash, 40% damage (brutes 50%). They push apart so they don't stack (1.5 m apart, 2.6 m for brutes).
- Gallery: now built from in-game boxes textured with the user's textures, not the gallery models. Floor `floor_01`, edge `wall_04`, columns `wall_07`, plus beams and green railings on the open side. The collapsed section uses hanging slabs, rebar, a slab fallen diagonally and rubble (`floor_02` and `wall_07`). Only the U-ramp is still a model.
- Camera: opening flyover (9.5 s), a zoom on the squad at 200 m when leaving the market (6 s), and a shot of the ship arriving (5 s). All three are letterboxed and can be skipped with click, SPACE or ESC (`STORY.cine`). FOV widens while driving (`window.__fovAdd`). Brute hits and ramming shake the camera.
- Atmosphere: dust and light shafts inside the market, smoke columns over the city that grow with the fight, embers, distant ships and drones, sunset fog (`STORY.atmo`).
- Market floor: raised to porch height (`LIFT` 0.9 m). Everything inside the market (z −5.6..69.2) goes up automatically with it (`inMk`). There are steps at the front, the rear door and the side gate on the east front, and that side gate is open.
- Ramp: now built geometry (three sloped runs, landings, columns, railings), using the user's textures. The U-ramp model is no longer used.
- Stalls: collision is taken from each model's real size (no more invisible boxes).
- Squad: invulnerable. They shoot every 0.16–0.32 s for 11 damage, and every 7–12 s one uses an area power (60 damage, 6 m radius).
- Civilians: heights from 1.30 to 1.88 m, each on its own lane, and they push apart from each other.
- Atmosphere: explosions flash on the horizon with a sound, ash falls, there are 12 smoke columns, and the light shafts are stronger.
