---
title: "Chapter 31 — Turn a Pattern Into a Conjecture"
description: "Chapter 31 of The Structure of Mathematical Thought."
---

[Guide contents](/homepage/portfolio/tsmt/) · [Part V](/homepage/portfolio/tsmt/part-v/)

## Start here

The rule $n^2+n+41$ gives 41, 43, 47, 53, and 61 at $n=0,1,2,3,4$. Each is prime. Does the rule always give primes? At $n=41$, the value is $41\cdot43$, which is composite.

## Worked example

A **conjecture** is a precise mathematical claim you suspect is true and have yet to prove. “This looks prime often” leaves too much unspecified. “For every nonnegative integer $n$, $n^2+n+41$ is prime” has a clear domain and a clear way to fail.

The failed guess suggests a new question. When is the expression divisible by 41? Since it is $n(n+1)+41$, divisibility by 41 is equivalent to 41 dividing $n(n+1)$. A prime dividing a product divides at least one factor, so this occurs exactly when $n$ or $n+1$ is a multiple of 41. A guess about all primes became a precise, provable statement about one factor.

## Try it

- **Practice.** State a precise conjecture about $n^2+n$ for all integers and prove it.
- **Stretch.** For a prime $p$, characterize all integers $n$ for which $p$ divides $n^2+n+p$. Then find a composite $p$ for which the corresponding statement fails.

## Check your work

**Practice.** $n^2+n=n(n+1)$ is even because one of two consecutive integers is even.

**Stretch.** For prime $p$, $p$ divides the expression exactly when $p$ divides $n$ or $n+1$. With $p=6$ and $n=2$, the product $2\cdot3$ is divisible by 6, while neither factor is.

---

Previous: [Chapter 30 — Follow Feedback Through a System](/homepage/portfolio/tsmt/chapter-30/)

Next: [Chapter 32 — Find Counterexamples and Test the Boundaries](/homepage/portfolio/tsmt/chapter-32/)
