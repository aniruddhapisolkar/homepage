---
title: "Chapter 04 — Write a Proof Someone Can Check"
description: "Chapter 4 of The Structure of Mathematical Thought."
---

[Guide contents](/homepage/portfolio/tsmt/) · [Part I](/homepage/portfolio/tsmt/part-i/)

## Start here

The sum of 7 and 9 is even. So is the sum of 11 and 13. Examples suggest a rule. A **proof** explains why the rule holds for every allowed pair.

## Worked example

To prove that any two odd integers add to an even integer, take arbitrary odd integers $a$ and $b$. By definition, $a=2j+1$ and $b=2k+1$ for some integers $j$ and $k$. Then

$$a+b=2(j+k+1).$$

The quantity inside the parentheses is an integer, so the sum is even. The proof works because the letters can stand for any two odd integers. Writing the sum in the form required by the definition closes the argument.

| What the claim asks for | A first approach |
|---|---|
| Show that a rule always holds | Start with an arbitrary allowed example and reason from the assumptions. |
| Show that something exists | Build one and check every requirement. |
| Show that something is impossible | Assume you have it and look for a contradiction. |
| Disprove a rule | Give one allowed case where the conclusion fails. |

## Try it

- **Practice.** Prove that the product of two odd integers is odd. Explain what justifies the final step.
- **Stretch.** Prove that $\sqrt{2}$ is irrational. Use Chapter [3](/homepage/portfolio/tsmt/chapter-03/) and begin by assuming $\sqrt{2}=a/b$ with the fraction in lowest terms.

## Check your work

**Practice.** $(2j+1)(2k+1)=2(2jk+j+k)+1$. The term $2jk+j+k$ is an integer.

**Stretch.** Squaring gives $a^2=2b^2$, so $a$ is even. Writing $a=2k$ yields $b^2=2k^2$, so $b$ is also even. Both share a factor of 2, contradicting lowest terms.

---

Previous: [Chapter 03 — Follow the Logic](/homepage/portfolio/tsmt/chapter-03/)

Next: [Chapter 05 — Abstract the Rule](/homepage/portfolio/tsmt/chapter-05/)
