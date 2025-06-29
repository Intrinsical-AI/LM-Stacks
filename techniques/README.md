# @How To Work With LLMs - Different Techniques

**The core idea** that runs through all these methodologies is to establish a symbiotic collaboration between humans and LLMs: the model brings accuracy, speed, diversity of perspectives, and automation, while the human provides strategic direction, critical judgment, and high-level validation. Instead of “using LLMs as oracles” or as closed-box code generators, the goal is to **work WITH** them—defining structured conversational workflows, clear roles, and iterative verification processes.

---

## Assumptions

* Different LLMs have distinct training data and architectures, which leads to different technical and cultural assumptions—that is, “different viewpoints.”
  Models include `DeepSeek`, `Qwen`, `ChatGPT`, `Claude`, `Gemini`, and `LLaMa`.
  Even within the same company, different models exhibit some variance (though less than between different vendors).

* LLMs with sufficient—and precise—context can solve problems more efficiently and **much** faster than the average programmer.

* Through **conversational flows** (semantic trajectories) and, to a lesser extent, **prompts**, you can mitigate biases and make the model aware of its own mistakes. This presumes a certain capacity for adaptation on the model’s part: there are no absolute errors, only mistaken viewpoints.

* Many failures stem from lack of context—either about the problem/approach/implementation in the current project, or because the model doesn’t have access to the latest library documentation (e.g., it was trained on an earlier version of that library).

* It is possible to automate the vast majority of tasks—even in large codebases—using LLMs, by delegating to humans only the roles of direction, critical decision-making, step-by-step validation, and verification.

---

## How to do it?

Before proceeding, think about it: tt’s **not** about making an LLM work **for** you. The idea is to work **WITH** LLMs, collaboratively.

---

## Which methodologies?

### [Test Driven Development](TestDrivenDevelopment/README.md)

* Generate tests and code with different models for implicit validation.

---

### [Multiagent](MultiAgent/README.md)

* Methodology for working with multiple agents that share context and reach consensus on decisions
* Multiple agents share explicit context
* Distributed consensus for critical decisions
* Task specialization, promoting diversity and complementary approaches
* The human makes the final decisions


---


### [Live-RAG](Live-RAG/README.md)

* Dynamic (on-demand?) indexing + “on-the-fly” retrieval
* Index and retrieve knowledge as needed
* Dynamically adapt context as the conversational flows progress
* Use specialized agents for search, validation, and updating
