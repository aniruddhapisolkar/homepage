---
title: "Chapter 34 — Invent a Problem Worth Solving"
description: "Chapter 34 of The Structure of Mathematical Thought."
---

[Guide contents](/homepage/portfolio/tsmt/) · [Part V](/homepage/portfolio/tsmt/part-v/)

## Start here

Start with a solved problem. Any 11 distinct integers from 1 through 20 include two that sum to 21. What changes if you want the pair to sum to 20? Changing one number can reveal which part of the original argument mattered.

## Worked example

For sum 21, the boxes are ten pairs, $(1,20),(2,19),\dots,(10,11)$. For sum 20, there are nine pairs, $(1,19),(2,18),\dots,(9,11)$, and two unpaired numbers, 10 and 20. The two chosen integers must be distinct, so 10 cannot pair with itself.

You can avoid a sum of 20 by taking one number from each pair plus both unpaired numbers. That gives 11 choices. Any 12 must take a full pair. The change produced a new sharp threshold and explained why it moved.

To invent a problem, change one rule, predict which step of the solution will break, and see whether the new version has a clean answer or an interesting obstruction.

## Try it

- **Practice.** In the same range, find the smallest number of distinct choices that guarantees a pair summing to 19.
- **Stretch.** For choices from 1 through $N$, give a rule for the threshold for any target sum $s$ for which at least one distinct pair exists.

## Check your work

**Practice.** There are nine pairs $(1,18),\dots,(9,10)$, plus unpaired 19 and 20. One from each pair plus the two unpaired numbers gives 11. The guarantee begins at 12.

**Stretch.** Each number has at most one distinct partner, namely $s-x$, so the valid pairs are disjoint. If there are $p$ pairs, the largest pair-free selection has $N-p$ elements, one from each pair plus every unpaired number. The threshold is $N-p+1$. Count $p$ by counting allowed $x$ with $x<s-x$ and $1\le s-x\le N$.

---

Previous: [Chapter 33 — Run an Experiment That Can Surprise You](/homepage/portfolio/tsmt/chapter-33/)

Next: [Chapter 35 — Decide What to Work On Next](/homepage/portfolio/tsmt/chapter-35/)
