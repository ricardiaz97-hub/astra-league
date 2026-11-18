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
