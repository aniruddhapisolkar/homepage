---
title: "Chapter 35 — Decide What to Work On Next"
description: "Chapter 35 of The Structure of Mathematical Thought."
---

[Guide contents](/homepage/portfolio/tsmt/) · [Part V](/homepage/portfolio/tsmt/part-v/)

## Start here

You have tried a proof for 30 minutes. “I am stuck” gives you little to work with. “I can construct a case that reaches 12, but I have no upper bound” tells you what to look for next.

## Worked example

Suppose you ask how many squares a knight can visit on a $3\times3$ chessboard without revisiting a square. You find a path through six squares. Before searching randomly for a longer path, list the legal moves. The center is isolated. From each noncentral square there are exactly two legal moves. Tracing one gives the cycle

$$(1,1),(2,3),(3,1),(1,2),(3,3),(2,1),(1,3),(3,2),(1,1).$$

This supplies a path through eight distinct squares and an upper bound of eight because the center is unreachable from any other square. A failed search became a structural question about which positions connect.

Keep a short research log. Record the precise claim, what you checked, the first gap in the argument, and one action that could close it. If you find a mistake, state which conclusions depend on it and revisit those conclusions.

## Try it

- **Practice.** Write a one-sentence upper bound and a separate one-sentence construction for the knight problem.
- **Stretch.** What changes on a $3\times4$ board? Before searching for a path, identify a property that every knight move preserves or changes. State what your observation proves and what is still open in your own attempt.

## Check your work

**Practice.** The center has no legal moves, so a path visiting more than one square can use only the eight outer squares. Following the displayed cycle and stopping before returning to the start visits all eight.

**Stretch.** Every move flips the square's color, since it changes the sum of the coordinates by an odd number. This forces the two color counts on any path to differ by at most one. On this board there are six of each color, so the coloring alone leaves a full path possible. You still need a construction or a stronger obstruction.

---

Previous: [Chapter 34 — Invent a Problem Worth Solving](/homepage/portfolio/tsmt/chapter-34/)

Next: [Part V checkpoint](/homepage/portfolio/tsmt/part-v/#part-v-checkpoint)
