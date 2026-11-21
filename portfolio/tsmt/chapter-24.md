---
title: "Chapter 24 — Combine Strategies and Know When to Switch"
description: "Chapter 24 of The Structure of Mathematical Thought."
---

[Guide contents](/homepage/portfolio/tsmt/) · [Part III](/homepage/portfolio/tsmt/part-iii/)

## Start here

One method often opens the door and another finishes. If a direct proof stalls, write down what would finish it. Then choose a method that can supply that missing step.

## Worked example

Show that the only integer solution of $x^2=2y^2$ is $(0,0)$. The parity argument from Chapter [4](/homepage/portfolio/tsmt/chapter-04/) forces $x$ and $y$ to be even. If a nonzero solution exists, choose one with the smallest positive $|y|$. Such a minimum exists because every nonempty set of positive integers has a least member. Also, $y=0$ would force $x=0$.

Now halve both coordinates. The equation still holds, and the new $|y|$ is positive and smaller. That contradiction rules out every nonzero solution. The chain uses parity to produce a legal move, an extremal choice to make the move decisive, and **descent** to name the smaller-solution argument.

## Try it

- **Practice.** Name one method that could help when legal moves seem to preserve something. Name a different method when you need to show a candidate is best.
- **Stretch.** Prove that $x^2+y^2=3z^2$ has no nonzero integer solution. Start by listing possible square remainders upon division by 3.

## Check your work

**Practice.** Look for an invariant for the first problem. For the second, look for a bound and an example that attains it.

**Stretch.** Squares have remainders 0 and 1 modulo 3. A sum of two such remainders is 0 modulo 3 only when both are 0, so 3 divides $x$ and $y$. Their squared sum is divisible by 9, so $3\mid z^2$ and hence $3\mid z$. Divide all three coordinates by 3. A solution with smallest positive $|z|$ would give a smaller one. If $z=0$, then $x=y=0$.

### Stretch further

Write a positive integer $n$ as the sum of an ordered list of 1s and 2s. Count these lists in two ways. First sort by the last entry and find a rule relating consecutive counts. Then sort by the number $k$ of 2s. In the second approach there are $n-k$ entries in total, so ask how many ways you can choose the $k$ positions for the 2s. Compare what the two descriptions help you compute.

---

Previous: [Chapter 23 — See the Same Fact in Two Ways](/homepage/portfolio/tsmt/chapter-23/)

Next: [Part III checkpoint](/homepage/portfolio/tsmt/part-iii/#part-iii-checkpoint)
