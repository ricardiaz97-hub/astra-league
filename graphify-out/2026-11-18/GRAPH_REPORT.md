# Graph Report - astra-league  (2026-11-18)

## Corpus Check
- 61 files · ~46,680 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 1459 file(s) not represented in the graph (top: .bin 371, .gltf 371, .glb 300)
- WARNING: 1459 of 2778 files seen (53%) have no supported extractor and are missing from this graph entirely. It may look complete while representing only part of the codebase.

## Summary
- 37 nodes · 45 edges · 7 communities (2 shown, 5 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `420062ed`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Cover
- markdown
- Doc
- convert
- qmul

## God Nodes (most connected - your core abstractions)
1. `convert()` - 6 edges
2. `Cover` - 4 edges
3. `markdown()` - 4 edges
4. `qmul()` - 3 edges
5. `qaxis()` - 3 edges
6. `qrot()` - 3 edges
7. `Doc` - 3 edges
8. `clean()` - 3 edges
9. `inline()` - 3 edges
10. `parse()` - 2 edges

## Surprising Connections (you probably didn't know these)
- `convert()` --calls--> `qmul()`  [EXTRACTED]
  tools/bvh2anim.py → tools/bvh2anim.py  _Bridges community 6 → community 5_

## Import Cycles
- None detected.

## Communities (7 total, 5 thin omitted)

### Community 2 - "markdown"
Cohesion: 0.67
Nodes (3): clean(), inline(), markdown()

### Community 5 - "convert"
Cohesion: 0.67
Nodes (3): convert(), parse(), qaxis()

## Knowledge Gaps
- **5 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Cover` connect `Cover` to `build_story_pdf.py`?**
  _High betweenness centrality (0.110) - this node is a cross-community bridge._
- **Should `build_story_pdf.py` be split into smaller, more focused modules?**
  _Cohesion score 0.13333333333333333 - nodes in this community are weakly interconnected._
- **Why does `Doc` connect `Doc` to `build_story_pdf.py`?**
  _High betweenness centrality (0.075) - this node is a cross-community bridge._
- **Why does `markdown()` connect `markdown` to `build_story_pdf.py`?**
  _High betweenness centrality (0.038) - this node is a cross-community bridge._