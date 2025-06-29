# LLM Stacks

> Structured repository to document patterns, experiments, and learnings about Large Language Models (LLMs)


> ***What you will find here***

* **Prompting templates** – reusable prompt skeletons designed for chats, code generation, and evaluation.
* **Techniques** – step-by-step guides that explain how to combine LLMs and humans effectively (TDD, Multi-Agent, Live-RAG …).
* **Stacks** – opinionated selections of libraries and tools for tasks such as data analysis, RAG, or UI prototyping.



## Getting started

1. Clone the repo and create a Python virtual environment (optional, but usefull in general if you haven’t try it already).
2. Explore the folders above to find ready-to-use templates, stacks, or techniques relevant to your project.

```bash
.
├── prompting/              # Prompt templates and experiments
│   └── templates/          # Parameterised prompt templates
├── stacks/                 # Technology stacks for different problem domains
├── techniques/             # Methodologies for working with LLMs (TDD, Multi-Agent, Live-RAG, …)
│   ├── Live-RAG/
│   ├── MultiAgent/
│   └── TestDrivenDevelopment/
└── LICENSE                 # MIT license
```

3. Contribute back! Feel free to open pull-requests with new templates, methodologies, or improvements.



## Roadmap

- Add unit & integration test examples for each technique.
- Expand the `stacks` section with containerised starter projects.
- Provide reference implementations for automated evaluation pipelines.
- Feel free to propse ideas, techniques, or tools. Do you miss something? Let us know!

## Other Tools & Related Repos
- [Local-RAG-Prototype](https://github.com/IntrinsicalAI/Local-RAG-Prototype): Local RAG prototype with a ports & adapted architecure, ready to plug in / apply custom changes!
- [RepoGPT](https://github.com/MrCabss69/RepoGPT): code repository analysis tool. Creates summaries for largue repos, in different formats / structures. Usefull as code-structure compressor for LLMs. Support jq syntax + filters / abstraction levels for advance queries.
- [Ðata Analysis and OSINT](https://github.com/MrCabss69/Sandworm-Spain-04-2025): an example on how to use efficiently LLMs on a research project - OSINT, data analysis, data scraping.
- [MCP-local-agent](https://github.com/Intrinsical-AI/MCP-local-agent): a local example for an MCP based agent - added custom tools to a Gemini3:4b model used via Ollama local API. 


## License

This project is licensed under the MIT License – see the `LICENSE` file for details.

---

Feel free to raise issues if you spot inconsistencies or have suggestions. Happy hacking! 🚀
