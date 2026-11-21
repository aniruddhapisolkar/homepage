---
title: "Chapter 30 — Follow Feedback Through a System"
description: "Chapter 30 of The Structure of Mathematical Thought."
---

[Guide contents](/homepage/portfolio/tsmt/) · [Part IV](/homepage/portfolio/tsmt/part-iv/)

## Start here

A queue grows whenever more people arrive than can be served. Even if the server works at full speed, the queue can keep growing. The result depends on how arrivals, service, and the current backlog interact.

## Worked example

At the start of each round there are $q$ waiting customers. Four arrive, and the team serves up to five. The next queue is $\max(0,q-1)$. Starting with six people, the queues after each round are $5,4,3,2,1,0$. Once the queue is zero, arrivals are handled in the same round.

Now suppose a long queue attracts walk-up customers who assume the service is popular. When $q\ge5$, six arrive instead of four. Above the threshold the queue grows by one per round, which keeps it above the threshold. The output affects the next input. That is **feedback**. In this model, queues starting at 4 and 5 move in opposite directions.

## Try it

- **Practice.** With the feedback rule, write the next three queue sizes starting from 4 and from 5.
- **Stretch.** If a second worker raises total service capacity to six, what happens above the threshold? Find the smallest whole-number capacity that reduces every positive queue under this model.

## Check your work

**Practice.** From 4, the sizes are 3, 2, 1. From 5, they are 6, 7, 8.

**Stretch.** With capacity six, a queue at or above five stays the same because arrivals equal service. Capacity seven makes every positive queue decrease, regardless of which arrival rate applies.

## When the parts hide the whole

Three voters rank options A, B, and C. Their orders are A–B–C, B–C–A, and C–A–B, with the best option first. A beats B by two votes to one. B beats C by the same margin. C also beats A by that margin. The majority preference cycles even though each person's ranking has a fixed order.

This is an example of **emergence**. A rule for combining individual choices produces a property you cannot see by inspecting any one person. To check a claim about a group, write down how the group result is made and test a tiny case.

---

Previous: [Chapter 29 — Ask What the Data Can Tell You](/homepage/portfolio/tsmt/chapter-29/)

Next: [Part IV checkpoint](/homepage/portfolio/tsmt/part-iv/#part-iv-checkpoint)
