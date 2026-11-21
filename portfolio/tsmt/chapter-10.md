---
title: "Chapter 10 — Prove a Pattern by Induction"
description: "Chapter 10 of The Structure of Mathematical Thought."
---

[Guide contents](/homepage/portfolio/tsmt/) · [Part II](/homepage/portfolio/tsmt/part-ii/)

## Start here

Imagine a row of numbered tiles. You know tile 1 can fall and that falling tile $k$ knocks over tile $k+1$. Together those facts cover every tile with a positive integer label. **Induction** uses that same chain of implications.

## Worked example

Show that the sum of the first $n$ odd positive integers equals $n^2$. At $n=1$ the sum is 1. Assume it equals $k^2$ after $k$ terms. The next odd number is $2k+1$, so the sum after the next term is

$$k^2+2k+1=(k+1)^2.$$

The first calculation is the **base case**. The second is the **inductive step**, which proves the next case from the current one. Make sure the step starts where the base case leaves off.

## Try it

- **Practice.** Prove that $2^n\ge n+1$ for every integer $n\ge0$.
- **Stretch.** Prove every integer $n\ge2$ is either prime or a product of primes. Use **strong induction**, where the step can use all earlier cases.

## Check your work

**Practice.** $2^0=1$. If $2^k\ge k+1$, then $2^{k+1}\ge2(k+1)\ge k+2$ for $k\ge0$.

**Stretch.** The base case 2 is prime. If $n$ is composite, write $n=ab$ with $2\le a,b<n$. Apply the assumption to both smaller factors and combine their prime factorizations.

---

Previous: [Chapter 09 — Use Symmetry Without Losing Cases](/homepage/portfolio/tsmt/chapter-09/)

Next: [Chapter 11 — Look at the Smallest or Largest Case](/homepage/portfolio/tsmt/chapter-11/)
