---
title: "Chapter 19 — Recognize the Same Structure in Disguise"
description: "Chapter 19 of The Structure of Mathematical Thought."
---

[Guide contents](/homepage/portfolio/tsmt/) · [Part III](/homepage/portfolio/tsmt/part-iii/)

## Start here

Two road maps can look different and still connect towns in exactly the same way. If you can rename the towns and preserve precisely which pairs have roads, every conclusion about connectivity carries over.

## Worked example

Consider a graph with edges $AB,BC,CD,DA$. Another graph has edges $24,41,13,32$. Match $A\leftrightarrow2$, $B\leftrightarrow4$, $C\leftrightarrow1$, and $D\leftrightarrow3$. The four edges match in both directions. This is a graph **isomorphism**, a one-to-one correspondence that preserves adjacency and non-adjacency.

A **duality** can swap roles instead. Think of a seating chart as a table with people as rows and seats as columns. Turn the chart sideways. “Each person has exactly one seat” says each original row has one mark. In the turned chart, each column has one mark. The turned chart also lets you ask a different question about its rows, which now represent seats. A seat shared by two people would appear as a row with two marks. A duality is useful when you have checked the dictionary of what swaps and what stays true.

## Try it

- **Practice.** Can a four-vertex chain and a four-vertex star (one center joined to three leaves) be isomorphic? Use the number of neighbors at a vertex.
- **Stretch.** Can a six-vertex ring be isomorphic to two separate triangles? Every vertex has two neighbors. Find a property the graphs do not share and explain why any isomorphism would preserve it.

## Check your work

**Practice.** The star has a vertex with three neighbors. The chain has none.

**Stretch.** In the ring, there is a path between every pair of vertices. There is no path between vertices in different triangles. Renaming vertices while preserving all edges preserves paths, so it preserves this property.

---

Previous: [Chapter 18 — Generalize Without Breaking the Argument](/homepage/portfolio/tsmt/chapter-18/)

Next: [Chapter 20 — Prove an Answer Is Best](/homepage/portfolio/tsmt/chapter-20/)
