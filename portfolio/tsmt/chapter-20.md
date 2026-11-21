---
title: "Chapter 20 — Prove an Answer Is Best"
description: "Chapter 20 of The Structure of Mathematical Thought."
---

[Guide contents](/homepage/portfolio/tsmt/) · [Part III](/homepage/portfolio/tsmt/part-iii/)

## Start here

Which rectangle with perimeter 20 has the largest area? Finding a rectangle with area 25 gives you a candidate. To prove it is best, you also need a reason every allowed rectangle has area at most 25.

## Worked example

Let the positive side lengths be $a$ and $b$. The perimeter condition gives $a+b=10$. Then

$$4ab=(a+b)^2-(a-b)^2\le100.$$

Every area is at most 25. The $5\times5$ rectangle attains 25, so the upper bound and the example meet. The identity and the example are a **certificate**, a short way for someone else to verify the optimum.

One way to get a bound is a **relaxation**. Allow more choices than the original rules permit and solve that easier problem. For a maximum, this can only raise the best value, so it gives an upper bound. Check whether an original choice actually reaches it.

## Try it

- **Practice.** With perimeter 22 and positive integer sides, find the maximum area and prove it. What does allowing fractional sides change?
- **Stretch.** You have positive integer sides summing to $n\ge2$. Show why moving 1 unit from the longer side to the shorter side improves the area whenever the sides differ by at least 2.

## Check your work

**Practice.** The same identity gives $ab\le121/4=30.25$. Integer areas are therefore at most 30, and sides 5 and 6 attain 30. Fractional sides can reach 30.25 with sides 5.5 and 5.5.

**Stretch.** If $b\ge a+2$, then $(a+1)(b-1)-ab=b-a-1>0$. Repeat until the sides differ by at most 1. This is an **exchange argument** because it rules out any unbalanced optimum by improving it.

---

Previous: [Chapter 19 — Recognize the Same Structure in Disguise](/homepage/portfolio/tsmt/chapter-19/)

Next: [Chapter 21 — Reason With Probability](/homepage/portfolio/tsmt/chapter-21/)
