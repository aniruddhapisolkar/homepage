---
title: "Chapter 22 — Estimate Growth With Bounds"
description: "Chapter 22 of The Structure of Mathematical Thought."
---

[Guide contents](/homepage/portfolio/tsmt/) · [Part III](/homepage/portfolio/tsmt/part-iii/)

## Start here

An exact value can be expensive to find. Two simple bounds can still tell you how the value grows when the input gets large. **Asymptotic reasoning** compares growth at large input sizes.

## Worked example

Let $H_k=1+1/2+\cdots+1/k$. At $k=8$, group the terms after 1 in blocks with indices 2, then 3 through 4, then 5 through 8. Each block after 1 adds between $1/2$ and 1. For example, the last block has four terms, each at least $1/8$ and at most $1/4$.

For $k=2^m$ there are $m$ such blocks. Block $j$ has $2^{j-1}$ terms, with denominators greater than $2^{j-1}$ and at most $2^j$. Thus

$$1+m/2\le H_{2^m}\le1+m.$$

Doubling the cutoff adds only one block. Both bounds show logarithmic growth, because $m$ is the number of doublings needed to reach $2^m$. Compare an arbitrary cutoff with the powers of two on either side.

## Try it

- **Practice.** Use the bounds above to put $H_{32}$ in an interval.
- **Stretch.** Prove that $1+1/4+1/9+\cdots+1/n^2\le2$ for every positive integer $n$. Compare $1/k^2$ with $1/(k(k-1))$ when $k\ge2$ and look for cancellation.

## Check your work

**Practice.** Since $32=2^5$, the interval is $[3.5,6]$.

**Stretch.** $1/k^2\le 1/(k(k-1))=1/(k-1)-1/k$. Summing the differences from 2 to $n$ leaves $1-1/n$. Add the first term to get at most $2-1/n$.

---

Previous: [Chapter 21 — Reason With Probability](/homepage/portfolio/tsmt/chapter-21/)

Next: [Chapter 23 — See the Same Fact in Two Ways](/homepage/portfolio/tsmt/chapter-23/)
