---
title: "Chapter 17 — Work Backwards From the Goal"
description: "Chapter 17 of The Structure of Mathematical Thought."
---

[Guide contents](/homepage/portfolio/tsmt/) · [Part II](/homepage/portfolio/tsmt/part-ii/)

## Start here

Suppose you want to prove $x^2-6x+9\ge0$. A square is always nonnegative. Can you find a square that matches the expression? Expanding $(x-3)^2$ gives the expression exactly.

## Worked example

Prove $a^2+b^2\ge2ab$. Read backwards. What would guarantee the result? If $a^2+b^2-2ab$ were a square, it would be nonnegative. The missing object is $(a-b)^2$. Now write the proof forwards.

$$(a-b)^2\ge0\quad\Longrightarrow\quad a^2+b^2-2ab\ge0\quad\Longrightarrow\quad a^2+b^2\ge2ab.$$

An **auxiliary object** is something you introduce to make the argument possible, such as this square or a line in a diagram. When reasoning backwards, check that each condition you find is sufficient to get back to the goal.

## Try it

- **Practice.** Prove $x^2+4x+5\ge1$ for every real $x$.
- **Stretch.** Prove $ab\le25$ when $a+b=10$, and determine exactly when equality holds. Find an auxiliary square involving the difference.

## Check your work

**Practice.** $x^2+4x+5=(x+2)^2+1\ge1$.

**Stretch.** $(a+b)^2-4ab=(a-b)^2\ge0$, so $4ab\le100$. Equality requires $a=b$, and the sum then forces $a=b=5$.

---

Previous: [Chapter 16 — Build an Object or an Algorithm](/homepage/portfolio/tsmt/chapter-16/)

Next: [Part II checkpoint](/homepage/portfolio/tsmt/part-ii/#part-ii-checkpoint)
