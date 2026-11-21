---
title: "Chapter 13 — Use the Pigeonhole Principle"
description: "Chapter 13 of The Structure of Mathematical Thought."
---

[Guide contents](/homepage/portfolio/tsmt/) · [Part II](/homepage/portfolio/tsmt/part-ii/)

## Start here

If 13 people each choose a favorite month, some month must be chosen by at least two people. If every month were chosen at most once, the total could be at most 12.

## Worked example

Choose six distinct integers from 1 through 10. At least two are consecutive. To see why, put the integers into five boxes.

$$(1,2),\quad(3,4),\quad(5,6),\quad(7,8),\quad(9,10).$$

Six choices in five boxes force one box to contain two choices. Its two members are consecutive. The interesting work was designing boxes that make a collision prove the desired claim.

## Try it

- **Practice.** Prove that among eight integers, some two differ by a multiple of 7.
- **Stretch.** Pick any $n+1$ distinct integers from 1 through $2n$, with $n\ge1$. Prove one picked integer divides another. Try repeatedly dividing each chosen integer by 2 while it is even.

## Check your work

**Practice.** Use the seven possible remainders modulo 7 as boxes. Two integers with the same remainder differ by a multiple of 7.

**Stretch.** Each chosen number has the form $2^k m$, with $m$ odd. There are only $n$ possible odd values of $m$ up to $2n$. Two choices share $m$, so the smaller divides the larger.

---

Previous: [Chapter 12 — Count the Same Objects Two Ways](/homepage/portfolio/tsmt/chapter-12/)

Next: [Chapter 14 — Split Problems and Choose a Standard Form](/homepage/portfolio/tsmt/chapter-14/)
