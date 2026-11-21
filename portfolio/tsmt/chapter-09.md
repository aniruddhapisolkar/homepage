---
title: "Chapter 09 — Use Symmetry Without Losing Cases"
description: "Chapter 9 of The Structure of Mathematical Thought."
---

[Guide contents](/homepage/portfolio/tsmt/) · [Part II](/homepage/portfolio/tsmt/part-ii/)

## Start here

For two numbers $a$ and $b$, can you assume $a\le b$? You can when swapping the names leaves both the problem and its conclusion unchanged. Check what the labels mean before choosing an order.

## Worked example

To show $a+b\le 2\max(a,b)$, suppose $a\le b$. Then $a+b\le b+b$. The other ordering follows by swapping the names. This is what **without loss of generality** means.

Now suppose you are given $a+b=10$ and $a$ is a multiple of 3. Swapping $a$ and $b$ can break the condition about $a$. The pair $(6,4)$ is allowed, but $(4,6)$ is excluded. An apparent symmetry can disappear as soon as one label has a special role.

## Try it

- **Practice.** Two fair coins are flipped. Use symmetry to explain why “first heads, second tails” and “first tails, second heads” have equal probabilities. Assume independent flips.
- **Stretch.** Show that among any six people, some three are either all mutual acquaintances or all mutual strangers. Assume acquaintance is symmetric. Pick one person and look at their five relationships.

## Check your work

**Practice.** Swapping the flips exchanges the two outcomes and preserves their probabilities. Each has probability $1/4$.

**Stretch.** The chosen person has at least three relationships of one kind. Suppose they know three people. If any two of those three know each other, those two and the chosen person form an acquaintance triple. Otherwise the three form a stranger triple. If the chosen person has three stranger relationships, swap the words “acquaintance” and “stranger” throughout.

---

Previous: [Chapter 08 — Track What Stays the Same or Moves One Way](/homepage/portfolio/tsmt/chapter-08/)

Next: [Chapter 10 — Prove a Pattern by Induction](/homepage/portfolio/tsmt/chapter-10/)
