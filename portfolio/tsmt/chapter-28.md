---
title: "Chapter 28 — Compute, Simulate, and Check"
description: "Chapter 28 of The Structure of Mathematical Thought."
---

[Guide contents](/homepage/portfolio/tsmt/) · [Part IV](/homepage/portfolio/tsmt/part-iv/)

## Start here

A simulation repeatedly applies a rule to see what happens. A computation can answer a question quickly and still mislead you through rounding, a faulty implementation, or a poor model. Test the simplest cases you can solve by hand.

## Worked example

Suppose a calculator rounds to four significant digits. Evaluate $\sqrt{10001}-100$. The square root is about 100.005, which rounds to 100.0. Subtracting gives zero. The rounding error was small relative to the square root and large relative to the difference you wanted. This is **cancellation**.

Multiply by the conjugate to rewrite the expression before evaluating it.

$$\sqrt{10001}-100=\frac{10001-10000}{\sqrt{10001}+100}=\frac{1}{\sqrt{10001}+100}.$$

With the same rounded square root, the result is about 0.005. An exact algebraic rewrite improved the rounded computation. To check a simulation, distinguish **verification** (did the computation follow your rules?) from **validation** (do those rules describe the thing you care about?).

## Try it

- **Practice.** Rewrite $\sqrt{n+1}-\sqrt n$ so it avoids subtracting nearly equal square roots for large positive $n$.
- **Stretch.** Estimate the chance that two fair six-sided dice sum to 7 by simulation. Give a way to verify the answer exactly, then say what evidence you would need to validate the fair, independent dice model for a real pair.

## Check your work

**Practice.** The equivalent expression is $1/(\sqrt{n+1}+\sqrt n)$.

**Stretch.** Simulate independent pairs of uniform integers from 1 to 6 and count the fraction whose sum is 7. Exactly six of the 36 equally likely ordered pairs work, giving $1/6$. For real dice, collect repeated pairs and compare observed face frequencies and joint frequencies with the model. A close match is evidence with sampling uncertainty.

---

Previous: [Chapter 27 — Check Units and Scaling](/homepage/portfolio/tsmt/chapter-27/)

Next: [Chapter 29 — Ask What the Data Can Tell You](/homepage/portfolio/tsmt/chapter-29/)
