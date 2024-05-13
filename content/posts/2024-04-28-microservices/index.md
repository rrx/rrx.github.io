---
title: "Microservices and Monoliths: More than you think"
date: 2024-04-28T09:31:12-08:00
draft: false
tags: 
- architecture
---

When evaluating a complex software system, we must consider the architectural choice between microservices and monoliths. Many articles have been written on the difference between these two, but they mostly focus on the obvious. I'd like to dig a little deeper in this article. If you’re not quite clear on the distinction, [here is a great article.](https://aws.amazon.com/compare/the-difference-between-monolithic-and-microservices-architecture/)

<!--more-->

<figure>
    <img src="microservices.jpg" alt="battleship and container ship (sd)" loading="lazy">
    <figcaption>battleship and container ship (sd)</figcaption>
</figure>

When we talk about the choice between microservices and monoliths, it’s commonly presented as an either/or decision. However, most organizations have some combination of both monolith and microservices.  For example, a legacy monolith, with more recent work happening in microservices. Most articles tend to disparage monoliths and evangelize microservices. This bias isn’t helpful to a decision maker faced with a messy history of prior work spanning years or decades.

Consider the following situations.  How would you make these decisions?

- The microservice is no longer so micro, and it’s starting to encounter some issues. Is it time to break it up into smaller services? 
- You want to add a new feature, do you add it to one of the existing services, or do you create a new service?
- A microservice seems to be the source of a number of bugs or outages . Are there some architectural choices we can consider to improving the situation?
- A monolith is working fine, but your manager insists that microservices are the future.  How do you convince them it is not?

Let’s dig into some reasons why you might want to consider one or the other, or even both!  Even if you work in an organization that’s all in on microservices, these principles still apply. Not only does a growing and evolving code base, force you to make these decisions, but the constant change in the industry can also force you to reevaluate.

The automatic reflex to build a new service every time you can’t find a place for something will multiply your problems. Alternatively, how can you make the case to your manager that you need to split your service?

Let’s dive into some principles that have helped me make these decisions.
## When to consider a monolith

Monoliths aren’t all bad. In fact, there are some compelling advantages. Most of the dreaded complexity in monoliths can be handled through modularization (the modular monolith) and enforced with tooling or language features.

For example, a monolith can include all the features you expect from microservices. When your service spans multiple domains, or handles a variety of requests, it might look like a caterpillar wanting to become a butterfly. While it's tempting to split these pieces out, keeping them together isn’t always a bad idea.  A tight coupling between components and provide simplicity and performance.  The right choice depends on your circumstances.

Here are some reasons to consider a monolith:

- **Longer Release Cycles**: If your team works with extended release cycles, say every two weeks or more, and there’s no imminent shift towards continuous delivery, a monolith might serve you better. Consider the QA process: testing a single, cohesive artifact or appliance can be simpler and more straightforward than wrestling with multiple microservices. The integrated nature of a monolith ensures that all components interact within the same environment, significantly simplifying integration testing.  

- **Standardized Tech Stack**: Monoliths shine in environments with a uniform tech stack. Leveraging the full feature set of a single programming language to manage different components of your application can offer a robust composition layer, avoiding the overhead of remote procedure calls typical in microservice architectures. Moreover, if your development team isn't huge or highly skilled, having a single stack reduces the learning curve and fosters better understanding and collaboration among team members. Languages that have strong support for modular programming can help create API boundaries within the monolith, making interfaces explicit, and implementations subject to change.  All of this without the operational complexity of microservices.

- **Performance Critical Software**: For applications where performance is paramount, like the demand for low-latency requests in financial transactions, the potential performance gains of a monolith can be significant. When an entire application runs on a single system, the network overhead of microservices can be minimized.  Having fewer networked dependencies means fewer things can break, giving a potential boost to reliability in failure sensitive situations.

- **Simplicity in Development**: Often a company starts with a monolith and only migrates to microservices when the complexity of their operations requires it. For startups focused on rapidly iterating until they find their market fit, the monolith offers fewer moving parts and a lower barrier to initial development. Debugging is more straightforward when you don’t need to trace issues across network boundaries, and the overall system architecture is easier to grasp for new developers.  This simplicity can yield significant productivity gains in situations where margins are low, or capital is limited.

- **When High Availability Is Not a Requirement**: Not every application needs to be available 24/7. For desktop software or applications used solely during business hours, the promise of high availability that microservices offer may not justify the burden. In such cases, if a monolithic architecture can meet your availability needs effectively, why make it more complicated?

## When to consider microservices

Considering microservices goes beyond the decision at the start of a new project.  It's something to consider as your services grow and evolve.  When a service has become too difficult to extend or maintain, we must challenge our initial architectural assumptions.  Using microservices isn't the only answer, here are some reasons you might want to consider splitting up your monolith into microservices.  Or if you have an unwieldy microservice, splitting it up into smaller units.

- **Managing Stack or Language Incompatibilities**: Microservices are great for integrating across diverse technologies. Is your stack is getting a bit wild? A little python here, some Golang there, all wrapped up with multiple targets in a Dockerfile, then duck taped with bash scripts?  You might want to consider splitting that beast up, and avoid the temptation to continually feed more hacks to your Frankenstein monster. Splitting it up can provide more clear API boundaries, and provide independent units of deployment.  This may be a good time to reconsider your original stack or language choices to see if they still apply.

- **Isolating Critical Components**: Separating services according to their criticality ensures that less critical components can fail without cascading effects. In particular, service separation can isolate resource utilization.  For example, you have a queue consumer that has large variations in memory usage, and a web service that has fixed resource usage.  By splitting these two up, you can prevent the consumer from causing out of memory errors on unrelated parts of the code.

- **Life cycle Differences**: Does your service change frequently? Sometimes many times a day? Microservices can provide isolation for parts of the system that change at different rates. Services that require frequent updates or have many volatile dependencies can be updated separately, reducing the risk to more stable parts.  An example might be a service that has a stable set of APIs, but there's active development on new features.  Splitting the service can provide greater stability to the existing system, while reducing the pressure on current development to not break anything.

- **Stable and Compatible APIs**: Microservices can be used to define and enforce API compatibility, preventing breaking changes to existing API clients. You can use this trick with monoliths as well, but it's more commonly seen in microservices. Tools like gRPC, Thrift, and GraphQL not only facilitate building and consuming APIs, but with some additional tooling you can check at build time that your API is compatible across all versions of your product.  This is especially helpful with mobile clients that have longer release cycles.

- **API Usage Patterns**: Microservices enable tailored scaling and optimization strategies based on specific usage patterns.  For example, long-lived requests, and low latency requests can be better optimized with separate services, through the choice of language, scaling, or resource limits.  Requests that are core to your application and affect the majority of your user base might be best kept separate from more experimental or risky changes.

- **Data Requirements and Regulatory Compliance**: In scenarios with stringent data handling or compliance regulations like GDPR or FedRAMP, microservices can allow for clear segregation of data, aligning architecture with compliance needs. 

- **Reduce Complexity**: While microservices are often associated with increased complexity, they better used to manage complexity. Decomposing your system into self-contained services can actually help encapsulate difficult parts of the system. This can reduce cognitive load when reasoning about the system as a whole.

- **Deploy Contention**: In highly active development environments where deployment pipelines become congested, microservices offer a way out, by allowing teams to deploy their work independently. In my experience, this is often the final straw that forces a decision to split a service up.

- **Blast Radius**: The concept of 'blast radius' refers to the extent of impact a failure can have on the wider system. Microservices help limit blast radius by isolating failures to individual services. But beware, microservices are also well known for causing cascading failures, and rather than limiting blast radius, your entire system can be at risk. A well planned system can avoid these problems.

- **Cleanly Separated Domains**: Microservices encourage the separation of business capabilities into distinct domains, each with its own database and service environment. This is closely related to [Domain Driven Design (DDD)](https://en.wikipedia.org/wiki/Domain-driven_design), which benefits from microservices by aligning service boundaries with domain boundaries.

## Conclusion

I hope this article gave you a some ideas you can apply to your specific circumstances. These are just the considerations I have thought about, and I'm sure there's more. Remember, it's not black and white, and it's worth considering both options. What will work for you depends entirely on your situation. The fun part of software is having the power and flexibility to build things just right.

Here are some thoughts to end with:

- Not every situation requires Google level architecture. If you find yourself working on a monolith, consider the advantages to doing so.   
- Has your microservice has grown beyond your comfort zone?  Think things though.  It might be fine as is, though you might want to modularize things nonetheless.
- If everyone is complaining about how long it takes to get code deployed, splitting up the code could help you.  Or it might just bankrupt your company.  As always, think it through.

No easy answers, just lots to think about. Thanks for reading.

