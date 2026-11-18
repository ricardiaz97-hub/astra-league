# Claude Handoff - Astra League Story Mode

Use this folder as the campaign design source of truth. Read this brief first, then `HISTORY_MODE.md`, then the detailed level documents linked below. The `art/` folder contains the actual visual references and grayboxes; inspect them while planning or changing a level. Do not rely on text descriptions alone.

## Current story order

1. **Olocuilta Market - evacuation and reunion.** The player is separated when the invasion starts. Enter from the cathedral-facing front, rescue civilians surrounded by regular bugs, teach vaulting over fallen stalls, and face ranged bugs crawling on the ceiling beams. The player uses the intact front/east ramp to reach the upper gallery, then wall-runs and wall-jumps across a separate collapsed section far toward the back. Civilians stay on the ground-floor aisle. At the Ferris-wheel fairground, the squad waits behind barricades roughly 200 meters from the market exit. Civilians pass through a defended gate behind the squad; hold against waves for five minutes, board the evac ship, and see the market burning as it leaves.
2. **The Sewers - infiltration and escape.** The full squad takes a clear sewer route to Hotel Aurora to avoid attracting the city horde. It is a full level, but never a maze. The route changes across clean, rusty, and overgrown sections. Opening section is calm and has no enemies: enter through a lit manhole, wade in shallow water, vault a low pipe, climb a small ledge, optionally take an obvious loot shortcut that immediately rejoins, hop a narrow gap, and reveal the enormous primary canal. At the canal, the squad glimpses a giant creature across the water, then activates three noisy lift/pump platforms. Each activation raises the water/platform, attracts a swarm, and requires a hold before crossing. Escalate the attack directions and enemy mix across the three holds. After the third, the creature bursts through and triggers a continuous RUN chase: sprint, vault, wall-run, wall-jump, climb out through a sewer outlet three city blocks from the hotel. No combat arenas or side routes during the chase.
3. **Hotel Aurora - intel and ambush.** Search for information left by a former squad member. The hotel is an ambush: fight through waves in the courtyard, drained pool, balconies, and service areas, recover the intel, and escape.
4. **Counterattack - assault the invasion ship.** Begin with the squad in flying mechs attacking the enemy ship, then continue with a boarding action, enemy waves, and the final boss.

## Design rules to preserve

- This is an anime-style team shooter with a warm orange, cream, and charcoal visual identity. Keep the established Astra League roster recognizable.
- Use `art/character-select-transparent/character-select-menu.png` as the roster identity reference; use character sheets in `art/character-sheets/` for details. Do not replace the cast with generic anime soldiers. Known accent examples: Connie purple, Diego green, Gaby orange, Julio gray (eyes closed because he is blind), Jenny yellow, Rebecca pink.
- Make campaign maps authored for their story beats rather than reusing a multiplayer arena unchanged. Keep primary routes easy to read and objectives clear for an HTML game.
- Treat the market's 200-meter approach as a gameplay scale target, not a surveyed measurement. The aerial market illustration's roof cutaway only shows the interior; the real roof remains intact.
- SVG grayboxes are conceptual layouts, not engineering plans. Preserve their orientation, landmark placement, route order, and gameplay intent when translating them into the game.
- `docs/story-mode-outline.md` is explicitly an earlier, compact three-level draft. The current expanded four-level order is in `HISTORY_MODE.md` and in this brief.

## Key files

- `HISTORY_MODE.md` - current expanded campaign synopsis.
- `docs/campaign-level-1-layout.md` and `docs/olocuilta-market-map-guide.md` - Level 1 flow, orientation, and layouts.
- `docs/sewer-level-section-01.md` - enemy-free sewer entrance tutorial.
- `docs/sewer-level-primary-canal.md` - three lift defenses and escalation.
- `docs/sewer-level-chase.md` - beast chase and outlet.
- `art/markets/` - market maps, concepts, and evacuation sequence art.
- `art/sewers/` - sewer concepts and SVG blockouts.
- `art/mechs/` and `art/bosses/` - counterattack and final-boss visuals.
- `art/civilians/`, `art/mobs/`, and `art/character-sheets/` - supporting cast and enemy references.

When continuing design, first summarize the existing route and identify any conflict with these references. Keep the documentation and visual references together when proposing changes.
