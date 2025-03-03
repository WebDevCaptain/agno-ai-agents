# Finance Agent using agno and Ollama

A simple finance agent using Yahoo Finance tool and Open source LLMs via Ollama.

- The first basic agent uses Deepseek R1 (8B parameter) model.

- The finance agent uses Qwen 2.5 (1.5B parameter) model.

---

## Requirements

- [uv](https://github.com/astral-sh/uv)
- [ollama](https://github.com/ollama)

---

## Commands

1. Initialize the project

```bash
uv init
```

2. Create a Python virtual environment using `uv`

```bash
uv venv --python=3.13.2
```

3. Install `agno` (previously phi data) and `ollama`

```bash
uv add agno
uv add ollama
```

4. Pull Deepseek R1 (8B) and Qwen 2.5 (1.5B) models from Ollama registry

```bash
ollama pull deepseek-r1:8b

ollama pull qwen2.5:1.5b
```

5. Run the simple ollama-agent app

```bash
uv run ollama-agent.py
```

![Simple Ollama Agent](./images/ollama-agent.png)

---

## Finance agent using Yahoo Finance tool

- Run the finance-agent app

```bash
uv run finance-agent.py
```

![Finance Agent](./images/finance-agent.png)
