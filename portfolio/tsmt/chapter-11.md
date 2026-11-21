---
title: "Chapter 11 — Look at the Smallest or Largest Case"
description: "Chapter 11 of The Structure of Mathematical Thought."
---

[Guide contents](/homepage/portfolio/tsmt/) · [Part II](/homepage/portfolio/tsmt/part-ii/)

## Start here

In a finite group, choose a shortest person. Nobody in the group is shorter than that person. That sounds trivial, but in a hard problem an extreme choice often gives you an inequality or rules out a move before you do any calculation.

## Worked example

Suppose several people sit in a row and each person claims someone immediately beside them is taller. Choose a tallest person in the row. Neither neighbor can be taller, so the claims cannot all be true. Ties are fine because the claim requires someone strictly taller.

This is the **extremal principle**. Decide what to maximize or minimize, establish that an extreme case exists, then ask what would violate its defining property. Finite nonempty collections of numbers have a largest and a smallest element. Infinite collections need care. The positive fractions $1,1/2,1/3,\dots$ have no smallest member.

## Try it

- **Practice.** At a tournament each player played a different positive number of matches, and each pair played at most once. Show this is impossible with at least two players.
- **Stretch.** A finite set of distinct integer points on a line has at least two points. Prove that some pair of consecutive points realizes the smallest distance among all pairs.

## Check your work

**Practice.** With $n$ players the largest match count is $n-1$. There are only $n-1$ possible positive counts. Equivalently, a player with the smallest count needs at least $n-1$ larger, distinct counts above theirs, which would force the largest to be at least $n$.

**Stretch.** Choose a pair with minimum distance. If another point lies between them, one of the smaller distances to that point contradicts minimality.

---

Previous: [Chapter 10 — Prove a Pattern by Induction](/homepage/portfolio/tsmt/chapter-10/)

Next: [Chapter 12 — Count the Same Objects Two Ways](/homepage/portfolio/tsmt/chapter-12/)
