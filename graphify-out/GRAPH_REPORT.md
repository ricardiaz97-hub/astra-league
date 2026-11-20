# Graph Report - astra-league  (2026-11-19)

## Corpus Check
- 74 files · ~66,892 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 1354 file(s) not represented in the graph (top: .bin 371, .gltf 371, .glb 306)
- WARNING: 1354 of 2656 files seen (51%) have no supported extractor and are missing from this graph entirely. It may look complete while representing only part of the codebase.

## Summary
- 73 nodes · 100 edges · 8 communities (5 shown, 3 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `acfcf29d`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Cover
- markdown
- Doc
- bvh2anim.py
- anim-recv.js
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
9. `Doc` - 3 edges
10. `clean()` - 3 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Import Cycles
- None detected.

## Communities (8 total, 3 thin omitted)

### Community 2 - "markdown"
Cohesion: 0.67
Nodes (3): clean(), inline(), markdown()

### Community 4 - "bvh2anim.py"
Cohesion: 0.27
Nodes (10): clamp_twist(), clean(), convert(), nrm(), parse(), qaxis(), qmul(), qrot() (+2 more)

### Community 5 - "anim-recv.js"
Cohesion: 0.29
Nodes (3): fs, http, path

### Community 8 - "cube2png.js"
Cohesion: 0.22
Nodes (8): ch(), crc(), fs, ih, raw, [src,out], v, zlib

### Community 9 - "sewer-check.js"
Cohesion: 0.22
Nodes (12): a, b, blob(), errs, fs, inPoly(), L, P() (+4 more)

## Knowledge Gaps
- **3 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Cover` connect `Cover` to `build_story_pdf.py`?**
  _High betweenness centrality (0.027) - this node is a cross-community bridge._
- **Should `build_story_pdf.py` be split into smaller, more focused modules?**
  _Cohesion score 0.13333333333333333 - nodes in this community are weakly interconnected._
- **Why does `Doc` connect `Doc` to `build_story_pdf.py`?**
  _High betweenness centrality (0.018) - this node is a cross-community bridge._
- **Why does `markdown()` connect `markdown` to `build_story_pdf.py`?**
  _High betweenness centrality (0.009) - this node is a cross-community bridge._