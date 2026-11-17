# Graph Report - astra-league  (2026-11-17)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 26 nodes · 28 edges · 4 communities (1 shown, 3 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `4435504e`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Cover
- markdown
- Doc

## God Nodes (most connected - your core abstractions)
1. `Cover` - 4 edges
2. `markdown()` - 4 edges
3. `Doc` - 3 edges
4. `clean()` - 3 edges
5. `inline()` - 3 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Import Cycles
- None detected.

## Communities (4 total, 3 thin omitted)

### Community 2 - "markdown"
Cohesion: 0.67
Nodes (3): clean(), inline(), markdown()

## Knowledge Gaps
- **3 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Cover` connect `Cover` to `build_story_pdf.py`?**
  _High betweenness centrality (0.230) - this node is a cross-community bridge._
- **Should `build_story_pdf.py` be split into smaller, more focused modules?**
  _Cohesion score 0.13333333333333333 - nodes in this community are weakly interconnected._
- **Why does `Doc` connect `Doc` to `build_story_pdf.py`?**
  _High betweenness centrality (0.157) - this node is a cross-community bridge._
- **Why does `markdown()` connect `markdown` to `build_story_pdf.py`?**
  _High betweenness centrality (0.080) - this node is a cross-community bridge._