---
title: "Technical Debt, A Systems Level Problem"
date: 2023-02-05T19:33:40-08:00
draft: false
thumbnail: "wolf_and_elk.jpg"
---

![wolf and elk](./wolf_and_elk.jpg)


I just finished reading ["Managing Technical Debt"](https://dl.acm.org/doi/book/10.5555/3364312), and while it provides some excellent ideas on the topic, I felt like it was missing something vital.  The book focuses primarily on the technical side of the problem.  The human factors however, are just as important.  Not including them in our assessments is a major reason why we have so much trouble assessing the true cost of our technical debt.  I think this omission is common in the industry, and I think it's time to change that.

<!--more-->

But before getting into what I think is missing, it's worth mentioning that the book does provide some excellent strategies.  Many of them are common sense.  I most appreciated the section which provides a decision making formula for calculating the cost of the debt to determine if the benefits are worth it.  This sort of decision making is very rare in the industry however, because we often have a poor idea of the true cost.  In many cases, we hardly even know what we are building before we build it.  For a start-up that's striving to find their product-market fit before running out of their Angel money, this is the difference between success and failure.  But overall it was a great overview of the technical sources of debt and how to address them.  The earlier the better.

However, technical debt is not purely a technical problem, it's also a systems problem.  The idea of a systems problem might be new to people, so I will describe what I mean. Systems are complex systems that involve multiple agents and factors and an associated web of interdependencies.  With modern software systems, and the large organizations that build them,  it's easy to get lost in that web.  Systems level thinking is very different from linear thinking.  Linear thinking is common in the scientific world, because it reduces the problem down to a single cause and effect, which can be easily tested.  The goal is to eliminate other factors to reduce the experiment down to test only one thing.  This is incredibly helpful, but it falls short when trying to understand a complex system, for example, a natural ecosystem.

Most of what we know about systems comes from the scientific study of ecological systems.  Plants, animals, bacteria, and humans form complex interrelationships which are hard to understand in isolation. A common example comes from Yellowstone park.  Years ago the wolves in the area were hunted to extinction.  But surprisingly, this had significant effects on the waterways in the area, causing serious problems.  [The recent reintroduction of wolves to the ecosystem brought back balance to the system in a dramatic comeback.](https://www.yellowstonepark.com/things-to-do/wildlife/wolf-reintroduction-changes-ecosystem/)

Here is a diagram of the positive interactions between elements in the ecosystem at Yellowstone.  See Baker 2016.  We will compare this later with an interaction diagram from a software company.

![Ecosystem in Yellowstone Park](./yellowstone.drawio.png)

Software systems are like ecosystems.  This might be hard to see, because we try very hard to keep those interactions as simple as possible.  Arguably, a well designed system has fewest interdependencies possible.  We like to think that our UI depends on the API.   The API depends on the Database, and the Database depends on some 3rd party.  Sounds simple, but there's much more to it.  Consider the following scenarios
There's a cloud provider on which you run your software, which just deprecated the version of PostgreSQL that your API depends on.
There's a build and deploy system that tries to remove the human element from deployment, but ends up creating its own maintenance burden when a bump in the Kubernetes version breaks everything bringing development to a standstill.
The CTO has declared the API deprecated and to halt all feature development, but the alternative was supposed to be ready last month and everyone is still waiting, forcing developers to find awkward workarounds.

In a complex system, if you change something, it often has unexpected consequences. The consequences are unexpected, because we often have a poor model of how things actually work.  In my experience, the few people in the company who do actually understand it all, are poorly paid and over worked.  The problems the organization faces find them, but because they aren't problems that are recognized by management, they aren't given the recognition they deserve.

The "Debt" metaphor is easy for people to initially grasp, but it's insufficient to describe the effects I'm talking about here.  In many cases, the metaphor of debt can be misleading.  Debt is a linear phenomenon, with a clear relationship between principle and interest.  Interest grows exponentially, and we sort of understand that.  But it's a single relationship.  To stretch the metaphor into a system, you have multiple principals and multiple interest rates and are each compounding each other in ways the accountants don't quite understand.  And worse, they don't even know what the balance is at the end of the day.  This more accurately represents the predicament the software industry finds itself in.  Left unchecked, we leave ourselves very vulnerable to small changes in the environment, such as market pressures.  How can we really say we are being responsible for this problem if we only consider its "easy" to quantify parts.  This measurement bias is very much as the source of our trouble.  Without an understanding of the full problem, our solutions are ineffective, or at worst, counter productive.

A clear idea of the problem of technical debt is vital before we can begin to entertain solutions. "Managing Technical Debt" offered numerous solutions to the technical challenges presented.  But as a practitioner in the field, those solutions felt weak and overly simplistic.  They fail to grasp the situation that many companies find themselves in.  This was my motivation in writing this article, to gain a clearer picture of the full problem.  From there we work towards an enduring solution.  As the saying goes, "A problem well stated is a problem half solved."

As part of my exploration, I tried to capture the elements of the web of interconnections in a software system as I have experience them.  I was expecting to find some sort of feedback loop, where one effect feeds another and so on.  But what I found was that there are multiple feedback loops, each feeding into the other, and not in a good way.  Here's what I'm talking about.

![Tech Debt Ecosystem](./maintenance_costs.drawio.png)

Software has always been complicated.  But in recent years, this issue gets more attention as almost every detail of our lives depends on the reliability of our software.  From medical devices, to gaming systems.  Our alarm clocks to get us out of bed. The algorithms that set us up for a Friday night date.  When everything works, everything is fine.  But when they don't work, life grinds to a halt, and we feel the desire to smash the proverbial keyboard against our heads. We ask these unanswerable questions like, why did my computer just shut off?  Why is my phone acting all strange?  A perfectly valid question if your job is in quality assurance.  But when my Grandma calls and asks me whats going on, that's really not OK!  From our human view, it's as if these machines have a mind of their own.  Clearly they don't.  But what they do have is a complex web of relationships that's entirely hidden from view.  My Grandma has no idea, nor should she.  For all effective purposes, this hidden world has a life of its own separate from our reality, and for most of us it's indistinguishable from magic.  Not the good kind of magic that makes your dreams come true.  It's the chaotic magic, of not knowing what will happen next, leaving us with a sense of frustration and anxiety.  And it's getting worse.  For my Grandmas sake, I want to change this.

It's not just our loyal customers who have this experience.  Software developers experience this daily in their own work.  As systems get more and more complex, the number of surprises increases.  And getting visibility into the problem can be hard.  The idea that we can patch buggy software in production has become commonplace in our society.  We have trained everyone to restart their computer, close their browser and open it up again.  It's this inconvenience that is the unfortunately price we pay for convenience.

There are some specific feedback loops in the world of Technical Debt that I would like to draw attention to.  If we consider the material in "Managing Technical Debt" from the perspective of a complex system, we will have a better chance of arriving at a realistic estimate on the true costs of technical debt.  Without that accurate estimate, we risk making serious errors in our decision making.  From my own analysis, I've identified a few feedback loops on technical debt.  There may be others to consider.  The ones I will consider here are:

- Developer morale and developer churn
- Decision making in the context of the entire system
- "Debt Normalization"
- Business reactions to zero marginal productivity

I will discuss these individually.

## Developer Morale and Developer Churn

I am often surprised by the disconnect between Developers and Executives on the issue of Developer Churn.  As a developer myself, I see a direct connection between my satisfaction on the job, and the experience I have with my tools, and my ability to do my job well.  Technical Debt is directly related.  Management seems to have another perspective.  Morale is something delegated to Human Resources, Total Rewards, or the employees direct report.  And Churn is something that is seen as inevitable, and there's nothing to do about it. I was surprised by this, I read almost exactly that in a manual for managers are company I once worked for.  The rate of developer churn across the industry is really bad, and everyone is doing terribly.  So for the 50% of companies who are above average, they think they are doing fine, while the bottom 50% feel resigned, and engage in predictable coping mechanisms.  Perhaps following some of the advice in "Managing Technical Debt", in the hope that they can increase productivity enough to afford to hire back the developers they lost to Google last year.  In my experience, the most common effect of following the advice in this book is that you double your workload, you increase developers cognitive load, and you are forced to pivot to other urgent matters when the CEO sees the writing on the wall, leaving the work unfinished, thus creating a higher maintenance load than when you started.  These are the sort of systems level effects that are happening in the real world.

When I first started exploring some of these ideas, I was looking at some of the research into Developer Experience as a possible solution to address the abysmal attrition rate in the industry.  When I first started talking about it with management and executives, I was surprised by the response.  What seemed to me like an interesting avenue to explore was met with a dismissive attitude.  Like Technical Debt,  the solutions for Developer Experience can be quite nebulous, and management prefers things that are a bit more concrete.  This makes it a challenge to make the case.  Having a concrete idea of the risks and benefits is essential to get buy-in to address the problem.  "Managing Technical Debt" has some great ideas in this area of how to actually find and identify the debt in concrete ways that management will understand.  Unfortunately, identifying deficiencies in the technical realm is much easier than explaining them in the systems realm.  The very idea that a company is a "system" is vague and hard to define.  As humans, we really aren't good at this systems level stuff.

Just because we don't have a good understanding yet, doesn't mean that we aren't making decisions in the meantime.  I have often observed that in the absence of a clear understanding of the problem, companies resort to imitating industry leaders hoping that it will lead them to equal success.  I suspect this is why there is a remarkable level of uniformity among large tech companies.  This strategy of imitation however is terrible, for the simple reason that the industry leaders are terrible examples, not just with Technical Debt, but also in terms of employee retention and morale.  We should think twice before imitating them.  As an industry we need to better understand this problem and its complex relationships before we can ever hope to come up with a lasting solution.

## Decision Making in a System

In my experience, it is true that well made software breeds confident and consistent decisions that improve things daily.  On the flip side, poorly made software breeds hacks, stop-gaps, short-cuts, confused planning, and deadlines that never get met.  Technical Debt is related to how our decisions are made.  Decisions are continuously being made by everyone, from the Executive Team to Junior Developers.  Decisions are not made in a vacuum.  They are informed by the information at hand, and especially by the patterns that are commonly in place.  We rarely hold people to a higher standard than the one we is already expressed in the existing documentation and code.  Decisions happen in the context of a system, and the effects of these decisions compound daily, and multiplied by the number of developers making decisions.  It's no surprise that debt gets out of hand.  If you read "Managing Technical Debt", this issue is not discussed. This is a significant omission.  Without this understanding, we underestimate our predicament, and do not fully grasp the full effect of our decision making process.

Broken Window Theory describes the effect that broken windows in a neighborhood tend to breed more crime and vandalism.  This theory has been applied to software development and can provide some insight into the problem.  By fixing our broken windows, we can prevent the deleterious second order effects.  It might seem like a waste of time, because the problem seems small, and our real problems seem so large.  But it's important to not underestimate how powerful these small decisions can make on larger problems throughout the system.  If you are unwilling to tolerate small problems, large problems are less likely to proliferate and hide.

## Debt Normalization

When you've been dealing with Tech Debt for so long, it's not surprising that it becomes the new normal.  This is the condition the entire industry is in.  Debt has been with us for so long, and it's so familiar, and it's solutions are so vague and nebulous, that the issue has receded into the background as part of a new normal.  The consequences of this are not good.  Think about the Junior and Intermediate developers who have never known anything else.  We are actually training our developers to ignore the problem and work around it with hacks and stop gaps.  This is considered normal.  If you have a good team lead, they will insist you put an item in the backlog.  It never sees the light of day.  Backlogs are places to forget things.

Agile in a way encourages this new normal.  Agile was created as part of the observation that it was hard to define the requirements for a new project up front, and that it was better to quickly iterate.  This is an incredible improvement over the waterfall method.  But it tends to encourage the behavior of pushing undefined requirements into the indefinite future.  In the case of Technical Debt, we end up with piecemeal solutions done at a local level. You might expect Architects to dream up a solution to the problem, but they are subject to the same environment as everyone else, and often come up with insufficient solutions, but with well defined budgets and scope, that please their managers.  You might also expect your Project Manager to push the agenda, but they are really only interested in features. It falls on developers to make the case, and it's quite frustrating because it's not something anyone wants to hear.  It's demoralizing, and a significant source of churn in my experience.

The cost of normalization is an invisible factor.  If you ask a developer in an exit interview why they leave, they often tell you what you want to hear.  They might have some complaints about this or that.  But the reason they are leaving is likely unknown to even them.  The sources of frustration that a developer experiences are numerous, and when they come from systemic sources, we have few tools to identify the problem, let alone solve it.  We are left to cope and adapt.  The common sentiment I've felt from developers is one of resignation.  It's the feeling of "I have believed too many empty promises. I just don't believe anything is going to change."  It's time to admit that we have failed at dealing with this problem and begin looking for new ways of thinking that can help us actually make a difference, and lead our organizations out of this downward spiral of resignation.

It's hard to believe that companies are able to function at all, once you've peeked behind the curtain and seen how the sausage is made.  Marginal productivity is approaching zero, and it makes people a bit desperate.  Large companies are able to manage quite well by hiring top talent and trying to grow their way out of the problem.  This works for a time, but actually increases the scale of the problem.  As long as the economic outlook is good, we may be able to do this indefinitely.  But that's not likely to happen.  When a adjustment comes, a lot of large companies will find their debt unserviceable, and have to make the hard decisions.  Hiring your way out of debt is not a valid strategy, it's a coping mechanism that will eventually fail.  We can do better than this.


## Business reactions to zero marginal productivity

The final point I want to make is about how the business responds to the condition of approaching
zero marginal productivity.  It's important to emphasize the "marginal" part.  Because if you ask
people in the business, overall productivity has never been higher.  But if you look at the increase
in productivity per extra dollar spent, or per new hire, large business are seeing diminishing
returns.  This corresponds with my observations. But it's also the premise of the book "The Mythical
Man-Month", which is that adding programmers to an already delayed project, delays the project even
further.  Not at all intuitive, but this makes sense in the context of the system of effects.

What's troubling about what I see is that not understanding the root cause leads companies to make
decisions that only make matters worse, or simply delay the inevitable.  Layoffs and restructuring
are common responses to help boost dwindling productivity numbers, but they exacerbate the problem
in the long term.

The other common strategy is to obsess on short term goals and KPIs.  There's nothing inherently
wrong with focusing on these.  The problem arises when we focus on them at the expense of a long
term vision and a deeper understanding of the systemic effects.  Agile encourages this behavior in
it's sprint based focus, that pushes unknowns into an indefinite future.  Short term goals hides the
fact that we don't have a strategy to deal with our predicament.  So we try not to think about it
too much.

## In summary

Informed by this new perspective I would like to draw some conclusions:

- We are underestimating the rate at which Technical Debt compounds because we do not understand (or discount) the human level feedback loops.
- We obsess over the easy solutions that technology offers, while ignoring the human factors.  This creates a bias in decision making which is detrimental to the health of the organization as we favor easy solutions, over the hard to quantify human ones.
- Technical Debt accumulates daily by small decisions being made by everyone in the org.  It's not just the architects who are responsible for the solutions, everyone is doing it.
- By not proactively addressing Technical Debt on a systems level, we expose the company to significant risk.

Technical Debt poses an existential threat to software companies.  I don't think this is an overstatement.  It sounds crazy because we look at companies that seem to have it under control, but it's not always the case.  Smaller companies are forced to deal with this, and the solutions are pretty.  If they can make the transition they survive. Otherwise they are out of business.  With larger companies, this will happen on a larger time scale.

Addressing the significant problems in the industry, such as developer churn, rising maintenance costs, rising expectations due to our deep reliance on software as a part of our daily lives, will be a defining feature of a successful company in the long term.  It is costly, and it's risky.  All the more reason for leadership to step up and address the problem we have been ignoring for too long.

## References

[Baker, Christopher & Gordon, Ascelin & Bode, Michael. (2016). Ensemble ecosystem modeling for predicting ecosystem response to predator reintroduction. Conservation biology : the journal of the Society for Conservation Biology. 31. 10.1111/cobi.12798.](https://www.researchgate.net/publication/305778940_Ensemble_ecosystem_modeling_for_predicting_ecosystem_response_to_predator_reintroduction)

[Brooks, Frederick P., Jr. (1982). The Mythical man-month : essays on software engineering. Reading, Mass. :Addison-Wesley Pub. Co.](https://www.amazon.com/Mythical-Man-Month-Software-Engineering-Anniversary/dp/0201835959)

[Krutchten, Philippe & Nord, Robert & Ozkaya, Ipek. (2019). Managing Technical Debt: Reducing Friction in Software Development (1st. ed.). Addison-Wesley Professional.](https://dl.acm.org/doi/book/10.5555/3364312)

