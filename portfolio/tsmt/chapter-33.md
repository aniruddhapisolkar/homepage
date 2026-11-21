---
title: "Chapter 33 — Run an Experiment That Can Surprise You"
description: "Chapter 33 of The Structure of Mathematical Thought."
---

[Guide contents](/homepage/portfolio/tsmt/) · [Part V](/homepage/portfolio/tsmt/part-v/)

## Start here

How many pieces can $n$ straight cuts make in a sheet of paper? Sketch several cases. For zero through four cuts, the maximum counts are 1, 2, 4, 7, and 11. The increases are 1, 2, 3, and 4. What mechanism could explain them?

## Worked example

Treat the sheet as a convex region, such as a rectangle, and make each cut a straight line through it. The $k$th cut meets at most $k-1$ earlier cuts at distinct points inside the sheet. These points divide the cut into at most $k$ segments. Each segment splits one existing region. The maximum increase is therefore $k$.

To attain the bound for a fixed number of cuts, draw lines of distinct directions through the center, then move each line by a small distance. Move the lines one at a time. When placing a line, avoid the finitely many shifts that would make it pass through an intersection of two already placed lines. For each pair, a sufficiently small shift keeps its intersection near the center because their directions are distinct. There are only finitely many pairs, so you can keep every intersection inside the sheet. Now the increases attain $1,2,\dots,n$. The maximum count is $1+n(n+1)/2$.

The sketches suggested an exact claim. The intersection argument explains both the upper bound and when it is attainable.

## Try it

- **Practice.** Predict the maximum number of pieces after six cuts. Explain what happens if all six are parallel.
- **Stretch.** Suppose $n\ge1$ cuts all pass through the center with distinct directions. Find the number of pieces and explain exactly where the maximum-count proof loses pieces.

## Check your work

**Practice.** The maximum is $1+6\cdot7/2=22$. Six parallel cuts through the interior give seven pieces because each cut adds only one.

**Stretch.** The first cut makes two pieces. Each subsequent cut meets all earlier cuts at the same point, producing only two segments and two new pieces. The total is $2n$. The loss comes from several intersections occupying one point.

---

Previous: [Chapter 32 — Find Counterexamples and Test the Boundaries](/homepage/portfolio/tsmt/chapter-32/)

Next: [Chapter 34 — Invent a Problem Worth Solving](/homepage/portfolio/tsmt/chapter-34/)
