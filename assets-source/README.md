# User-provided source assets

Copied from the user's `MAP ASSETS` and `WEAPONS, VEHICLES AND SHIPS` folders on 2026-11-17 at the user's request. Original Tripo UUID filenames are preserved. Large GLB and PNG files use Git LFS.

## Contents
- `market/props/unclassified/`: 25 Tripo-exported GLB source models for Mercado props.
- `market/characters/rigged-candidate/`: 1 skeletal GLB that was in the Mercado source folder; structural inspection found one skin and zero animation clips. It is kept separate as a character candidate, not treated as a prop.
- `sewer/props/unclassified/`: 11 Tripo-exported GLB source models for sewer assets.
- `market-gear/unclassified/`: 27 Tripo-exported GLB source models grouped as Mercado weapons, vehicles, and ships. Individual objects have not yet been visually identified.
- `textures/`: 14 floor/wall variants plus three market and three sewer wall/trim/decal sheets.
- `MANIFEST.csv`: file sizes and SHA-256 hashes for this source collection.

A basic GLB v2 header and embedded JSON check passed for all 64 models. This is not a geometry, texture, scale, rig quality, gameplay, or visual review. The files are source assets; they are not wired into gameplay or runtime asset libraries.

No separate license or per-file provenance manifest was present in the supplied folders when copied. Confirm applicable Tripo terms and project redistribution rights before distributing the repository or shipping these assets. The original texture ZIP was not copied because its PNG contents are included in the organized folders above.
