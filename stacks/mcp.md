## What is Model Context Protocol?

**MCP** is an open, cross-platform standard designed to connect language models (LLMs) with external tools, data, and systems in a **standardized and secure** way.

Launched by **Anthropic on November 25, 2024**, MCP addresses the classic M×N integration problem between models and tools by replacing it with a **M+N** model—far more scalable and modular.

It is built on top of **JSON-RPC 2.0**, enabling a clear and well-defined semantics for remote procedure calls.

---

## Architecture

MCP follows a **Client/Server** architecture with three key roles:

* **Host:** The LLM-enabled application (such as Claude Desktop, an IDE, or a custom agent) that initiates the conversation.
* **MCP Client:** A module within the host that manages the connection, discovers capabilities, and forwards requests.
* **MCP Server:** The external entity that exposes tools, resources, and prompt templates to the model.

```plaintext
[Host] → [MCP Client] ⇆ [MCP Server]
```

---

## Interaction Flow

1. **Initial connection** and exchange of versions and capabilities.
2. **Discovery** of available tools, resources, and prompts.
3. **Exposure of JSON schemas** for tools and prompt templates.
4. **Invocation by the model** (e.g., `fetch_github_issues`).
5. **External execution** of the tool and return of the result to the client.
6. **Context enrichment** of the LLM and generation of the final output.

---

## Transport

* **Local:** via `stdio` (`stdin` / `stdout`)
* **Remote:** over `HTTP` and `SSE` (Server-Sent Events)

---

## Functional Components

### 🛠️ Tools

Functions that can be invoked by models to perform external actions or computations—APIs, commands, scripts, etc.

### 📁 Resources

Read-only data, similar to `GET` in REST—logs, files, database entries, etc.

### 🧠 Prompts

Predefined templates that guide the model in specific tasks, such as code review, content drafting, etc.

---

## MCP Client Examples

* **Claude Desktop**
* **Claude Code**

These operate as local MCP clients, enabling real-time interaction between models and their environments.

---

## Resources and Useful Links

* [Model Context Protocol – Official site](https://modelcontextprotocol.io)
* [Technical deep dive by Phil Schmid](https://philschmid.de)
* [Security analysis by Stytch](https://stytch.com)
* [Press release on The Verge](https://theverge.com)
* [Anthropic – Product page](https://anthropic.com)