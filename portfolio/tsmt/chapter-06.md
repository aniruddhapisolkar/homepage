---
title: "Chapter 06 — Rebuild a Result From Scratch"
description: "Chapter 6 of The Structure of Mathematical Thought."
---

[Guide contents](/homepage/portfolio/tsmt/) · [Part I](/homepage/portfolio/tsmt/part-i/)

## Start here

Suppose you forget how to add the integers from 1 to 100. Can you rebuild the shortcut? First look for a fact you can explain about how the numbers are arranged.

## Worked example

Write the sum twice, once forwards and once backwards. Align the terms.

$$
\begin{aligned}
S&=1+2+\cdots+99+100,\\
S&=100+99+\cdots+2+1.
\end{aligned}
$$

Each column adds to 101. There are 100 columns, so $2S=100\cdot101$. Divide by 2 to get $S=5050$. This argument avoids having to pair terms within one list, where an odd number of terms leaves a middle term.

For the list from 1 to any positive integer $n$, there are $n$ columns, each summing to $n+1$. Therefore $S=n(n+1)/2$. This is first-principles reasoning. Start with facts you can defend, derive the result, and name the assumptions the derivation uses.

## Try it

- **Practice.** Derive the sum of $4,7,10,13,16$ by pairing forward and reverse lists.
- **Stretch.** Show that the average of any finite list with constant spacing equals the average of the first and last terms. Explain why constant spacing matters.

## Check your work

**Practice.** Every column totals 20. Two copies total $5\cdot20$, so one copy totals 50.

**Stretch.** Moving one place inward from each end adds the spacing on the left and subtracts the same spacing on the right. The paired sum stays equal to the sum of the endpoints. Divide the doubled sum by twice the number of terms. A list like $1,2,9$ shows what can happen when the spacing changes.

---

Previous: [Chapter 05 — Abstract the Rule](/homepage/portfolio/tsmt/chapter-05/)

Next: [Part I checkpoint](/homepage/portfolio/tsmt/part-i/#part-i-checkpoint)
