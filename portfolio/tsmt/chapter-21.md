---
title: "Chapter 21 — Reason With Probability"
description: "Chapter 21 of The Structure of Mathematical Thought."
---

[Guide contents](/homepage/portfolio/tsmt/) · [Part III](/homepage/portfolio/tsmt/part-iii/)

## Start here

Suppose 1 in 100 emails is spam. A filter flags nearly all spam, but it also flags some ordinary emails. To judge a flag, you need to compare the number of true flags with the total number of flags.

## Worked example

Imagine 2,000 emails in the given proportions. Suppose there are 20 spam emails and the filter flags 18 of them. Suppose it also flags 5% of the 1,980 ordinary emails, which is 99. Among 117 flags, only 18 are spam, or about 15%.

The spam rate before seeing the flag is the **base rate**. The chance of spam among flagged emails is a **conditional probability**, calculated within the flagged group. Writing down the group in the denominator prevents you from confusing “flagged among spam” with “spam among flagged.”

## Try it

- **Practice.** An audit finds 20 faulty parts in a lot of 200. A scanner flags 16 faulty parts and 18 good parts. What fraction of flagged parts are faulty?
- **Stretch.** You draw two cards without replacement from a deck of ten cards, three of them red. What is the expected number of red cards drawn? The expected number is the long-run average over repeated draws. Does the calculation need the draws to be independent?

## Check your work

**Practice.** There are 34 flags and 16 flagged faulty parts, so the fraction is $16/34=8/17$.

**Stretch.** Each draw position has a $3/10$ chance of being red. Count 1 for red and 0 otherwise in each position. The average of the sum is the sum of the averages, $3/10+3/10=3/5$. The draws are dependent, but adding these averages does not require independence.

## Use an average to prove existence

Can you color the vertices of any finite graph without loops red or blue so at least half its edges join different colors? Assign the colors independently by fair coin flips. For each edge, the two ends get different colors with probability $1/2$. Count 1 when an edge crosses between colors and 0 otherwise. Adding these averages gives an expected crossing count of half the edges, even though crossing events can depend on one another.

If every coloring had fewer crossings than the average, their average would be smaller too. So at least one coloring reaches half. This is the **probabilistic method**. Use a random construction to prove some choice works. The proof here tells you such a coloring exists.

---

Previous: [Chapter 20 — Prove an Answer Is Best](/homepage/portfolio/tsmt/chapter-20/)

Next: [Chapter 22 — Estimate Growth With Bounds](/homepage/portfolio/tsmt/chapter-22/)
