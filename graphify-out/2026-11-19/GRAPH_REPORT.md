# Graph Report - astra-league  (2026-11-19)

## Corpus Check
- 68 files · ~63,621 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 1351 file(s) not represented in the graph (top: .bin 371, .gltf 371, .glb 304)
- WARNING: 1351 of 2645 files seen (51%) have no supported extractor and are missing from this graph entirely. It may look complete while representing only part of the codebase.

## Summary
- 67 nodes · 94 edges · 10 communities (5 shown, 5 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `400fb58c`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Cover
- markdown
- Doc
- bvh2anim.py
- convert
- qmul
- clean
- cube2png.js
- sewer-check.js

## God Nodes (most connected - your core abstractions)
1. `convert()` - 9 edges
2. `clean()` - 7 edges
3. `qmul()` - 5 edges
4. `clamp_twist()` - 5 edges
5. `nrm()` - 5 edges
6. `slerp()` - 5 edges
7. `Cover` - 4 edges
8. `markdown()` - 4 edges
9. `P()` - 3 edges
10. `rooms` - 3 edges

## Surprising Connections (you probably didn't know these)
- `convert()` --calls--> `parse()`  [EXTRACTED]
  tools/bvh2anim.py → tools/bvh2anim.py  _Bridges community 4 → community 5_
- `convert()` --calls--> `clean()`  [EXTRACTED]
  tools/bvh2anim.py → tools/bvh2anim.py  _Bridges community 5 → community 7_
- `convert()` --calls--> `qmul()`  [EXTRACTED]
  tools/bvh2anim.py → tools/bvh2anim.py  _Bridges community 5 → community 6_
- `clamp_twist()` --calls--> `qmul()`  [EXTRACTED]
  tools/bvh2anim.py → tools/bvh2anim.py  _Bridges community 6 → community 7_

## Import Cycles
- None detected.

## Communities (10 total, 5 thin omitted)

### Community 2 - "markdown"
Cohesion: 0.67
Nodes (3): clean(), inline(), markdown()

### Community 5 - "convert"
Cohesion: 0.83
Nodes (3): convert(), qaxis(), restdirs()

### Community 7 - "clean"
Cohesion: 0.60
Nodes (4): clamp_twist(), clean(), nrm(), slerp()

### Community 8 - "cube2png.js"
Cohesion: 0.20
Nodes (8): ch(), crc(), fs, ih, raw, [src,out], v, zlib

### Community 9 - "sewer-check.js"
Cohesion: 0.22
Nodes (12): a, b, blob(), errs, fs, inPoly(), L, P() (+4 more)

## Knowledge Gaps
- **5 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Cover` connect `Cover` to `build_story_pdf.py`?**
  _High betweenness centrality (0.032) - this node is a cross-community bridge._
- **Should `build_story_pdf.py` be split into smaller, more focused modules?**
  _Cohesion score 0.13333333333333333 - nodes in this community are weakly interconnected._
- **Why does `Doc` connect `Doc` to `build_story_pdf.py`?**
  _High betweenness centrality (0.022) - this node is a cross-community bridge._
- **Why does `markdown()` connect `markdown` to `build_story_pdf.py`?**
  _High betweenness centrality (0.011) - this node is a cross-community bridge._