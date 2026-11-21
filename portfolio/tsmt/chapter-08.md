---
title: "Chapter 08 — Track What Stays the Same or Moves One Way"
description: "Chapter 8 of The Structure of Mathematical Thought."
---

[Guide contents](/homepage/portfolio/tsmt/) · [Part II](/homepage/portfolio/tsmt/part-ii/)

## Start here

A row of coins starts all tails. A move flips exactly two coins. Can you get exactly one head? After any move, the head count changes by $-2$, 0, or 2. It remains even, so one head is unreachable.

## Worked example

A value preserved by every legal move is an **invariant**. Here the value is parity, which records whether a count is even or odd. Look for a simpler value when the exact state changes too much to track.

A **monovariant** changes only one way. Start with any pile of stones. If every legal move removes at least one stone, the pile size strictly decreases. Since the count is a nonnegative integer, the process must stop. The lower bound and the strict decrease both matter. A real-valued quantity can halve forever.

## Try it

- **Practice.** Start at 5. Each move adds or subtracts 6. Can you reach 28? Find an invariant that rules it out.
- **Stretch.** Remove opposite corners from an $8\times8$ chessboard. Can you cover all remaining squares with dominoes, each covering two adjacent squares?

## Check your work

**Practice.** The remainder upon division by 6 is always 5. The remainder of 28 is 4.

**Stretch.** The removed corners have the same color. Every domino covers one square of each color, so a tiling would require equal numbers of the two colors. The remaining counts are 30 and 32.

---

Previous: [Chapter 07 — Read the Shape of a Problem](/homepage/portfolio/tsmt/chapter-07/)

Next: [Chapter 09 — Use Symmetry Without Losing Cases](/homepage/portfolio/tsmt/chapter-09/)
