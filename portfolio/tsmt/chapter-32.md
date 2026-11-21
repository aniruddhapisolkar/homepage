---
title: "Chapter 32 — Find Counterexamples and Test the Boundaries"
description: "Chapter 32 of The Structure of Mathematical Thought."
---

[Guide contents](/homepage/portfolio/tsmt/) · [Part V](/homepage/portfolio/tsmt/part-v/)

## Start here

“Every odd integer is prime” sounds plausible if you look only at 3, 5, and 7. The integer 9 meets the condition and fails the conclusion. One **counterexample** settles a claim about every member of a group.

## Worked example

Take the statement “If positive integers $a$ and $b$ have no common factor greater than 1, and $a$ divides $bc$, then $a$ divides $c$.” Test the role of the first assumption by dropping it and keeping everything else. Choose $a=6$, $b=4$, and $c=3$. Then 6 divides 12 and 6 does not divide 3. The shared factor 2 in $a$ and $b$ supplies a factor that $c$ lacks.

This is **boundary hunting**. Choose one assumption to remove, keep the others, and search for a case that breaks the conclusion. If a candidate also violates a condition you meant to keep, discard it and try again.

## Try it

- **Practice.** Find a counterexample to “If $a^2>b^2$, then $a>b$” for integers. Find a restriction on both variables that repairs the implication.
- **Stretch.** For positive integers $a$ and $b$, prove that whenever they share a factor greater than 1, there is a positive $c$ with $a$ dividing $bc$ and $a$ failing to divide $c$.

## Check your work

**Practice.** $a=-3$ and $b=2$ give $9>4$ but $-3<2$. For nonnegative $a,b$, if $a\le b$ then $a^2\le b^2$, so the implication holds.

**Stretch.** Let $d>1$ divide both $a$ and $b$. Choose $c=a/d$. Then $bc=a(b/d)$ is a multiple of $a$, while $0<c<a$ rules out divisibility of $c$ by $a$.

---

Previous: [Chapter 31 — Turn a Pattern Into a Conjecture](/homepage/portfolio/tsmt/chapter-31/)

Next: [Chapter 33 — Run an Experiment That Can Surprise You](/homepage/portfolio/tsmt/chapter-33/)
