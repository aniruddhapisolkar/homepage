---
title: "Chapter 18 — Generalize Without Breaking the Argument"
description: "Chapter 18 of The Structure of Mathematical Thought."
---

[Guide contents](/homepage/portfolio/tsmt/) · [Part III](/homepage/portfolio/tsmt/part-iii/)

## Start here

A $3\times5$ rectangular grid has 15 cells. The same argument gives $ab$ cells for any grid with $a$ rows and $b$ columns. **Generalizing** means finding a family of problems that share an argument.

## Worked example

With three positive numbers, each at most 5, the sum is at most 15. For $n$ numbers, each at most $M$, the sum is at most $nM$. Add the $n$ individual inequalities. The reasoning never used positivity, so the bound also holds for negative numbers and negative $M$. It does use the upper bound on every term. Knowing that only the first term is at most $M$ is insufficient.

To generalize a result, look at the steps of its proof. Replace the specific quantities by variables and keep the conditions that make each step legal.

## Try it

- **Practice.** A $4\times4$ grid has 16 cells. Generalize the number of cells to a rectangular grid and then to a stack of such grids.
- **Stretch.** A tournament with six players has 15 games if every pair plays once. Give a formula for $n$ players. Then adapt it when each pair plays exactly twice and some of the games are canceled. What extra information determines the new total?

## Check your work

**Practice.** There are $ab$ cells in an $a\times b$ grid and $abc$ cells in a stack of $c$ such grids.

**Stretch.** Each player contributes $n-1$ game ends, giving $n(n-1)/2$ games. Two games per pair give $n(n-1)$ scheduled games. Subtract the number canceled. If you know only which players had cancellations, you may still need the cancellation count.

---

Previous: [Chapter 17 — Work Backwards From the Goal](/homepage/portfolio/tsmt/chapter-17/)

Next: [Chapter 19 — Recognize the Same Structure in Disguise](/homepage/portfolio/tsmt/chapter-19/)
