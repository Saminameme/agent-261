# Agent-261

## Overview
Agent-261 is a **personal agent framework** designed to grow with the user.  
It doesn’t force predefined tasks, remains transparent and editable, and uses your computer as a tool to execute requested missions.  
Each agent is defined by a **prompt profile** (e.g., `agents/agent0/prompts/…`) that specifies its role, specialization, and behavioral rules.

---

## Project Structure

| Folder / File | Purpose |
|---------------|---------|
| `agent.py` | **Core engine** – manages the main communication loop, agent contexts, and the invocation of tools or extensions. |
| `python/` | Python code – APIs, helpers, tools, and extension points. |
| `prompts/` | Message templates (system, interactions, tools) used to build prompts sent to LLMs. |
| `agents/` | Agent profiles (custom prompts, dedicated tools). |
| `knowledge/`, `memory/` | Persistent knowledge base and memory storage. |
| `webui/` | Web interface (HTML/JS). |
| `conf/` | Configuration files, including LLM provider settings. |

---

## Key Concepts

### Tools
- An agent’s abilities are powered by **Python tools**.
- Each tool inherits from the `Tool` class and implements an `execute` method.
- Example: a web search tool that queries an external API.

### Extensions
- Behavior can be enhanced via **extension points**.
- Example: `agent_init/_10_initial_message.py` adds a welcome message at the first interaction.

### API
- HTTP endpoints are located in `python/api`.
- The `message.py` handler shows how a user request becomes an agent message and returns the generated response.

### LLM Models
- `models.py` wraps access to models via LiteLLM and defines their configuration (chat or embeddings).
- Available providers (OpenAI, Anthropic, Ollama, etc.) are listed in `conf/model_providers.yaml`.

---

## Getting Started

1. **Understand the agent loop**  
   Review `agent.py` to see how messages are processed, tools are called, and extensions are triggered.

2. **Experiment with prompts**  
   Edit or create templates in `prompts/` and `agents/<profile>/prompts/` to customize behavior.

3. **Create new tools**  
   Use examples in `python/tools/` to build new features (e.g., API integrations, file processing).

4. **Use extensions**  
   Add scripts under `python/extensions/<extension_point>/` to respond to different lifecycle events (initialization, end of loop, etc.).

5. **Configure models**  
   Adjust `conf/model_providers.yaml` and environment variables to work with various LLM providers and models.

6. **Read the docs**  
   The `docs/` folder and README contain installation guides, extension tips, and advanced usage.

---

With these steps, new contributors can quickly understand how Agent-261 works, extend its capabilities, and integrate it into their own projects.
