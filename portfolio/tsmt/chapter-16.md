---
title: "Chapter 16 — Build an Object or an Algorithm"
description: "Chapter 16 of The Structure of Mathematical Thought."
---

[Guide contents](/homepage/portfolio/tsmt/) · [Part II](/homepage/portfolio/tsmt/part-ii/)

## Start here

To prove that an object exists, try giving explicit instructions to build it. If you claim a procedure always works, show both why its steps are correct and why it eventually finishes.

## Worked example

Find the greatest common divisor of 48 and 18. Divide 48 by 18 to get a remainder of 12. A number divides both 48 and 18 exactly when it divides both 18 and 12, because $48=2\cdot18+12$. Repeat with $(18,12)$ to get $(12,6)$, then $(6,0)$.

This is **Euclid's algorithm**. The shared divisors stay the same at each step. The nonnegative second entry decreases until it reaches 0. At that point the first entry is the greatest common divisor, since all its divisors also divide 0. Here the answer is 6.

## Try it

- **Practice.** Use Euclid's algorithm to find the greatest common divisor of 84 and 30. Explain why you can discard 84 after the first step.
- **Stretch.** Given any finite list of positive integers, construct a positive integer that has remainder 1 when divided by every list entry greater than 1.

## Check your work

**Practice.** The pairs are $(84,30)$, $(30,24)$, $(24,6)$, and $(6,0)$. The common divisors stay the same because $84=2\cdot30+24$.

**Stretch.** Multiply all entries, then add 1. Every entry divides the product, so each entry greater than 1 leaves remainder 1.

---

Previous: [Chapter 15 — Change the Representation](/homepage/portfolio/tsmt/chapter-15/)

Next: [Chapter 17 — Work Backwards From the Goal](/homepage/portfolio/tsmt/chapter-17/)
