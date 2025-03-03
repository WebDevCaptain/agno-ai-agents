# Finance Agent using agno and Ollama 

A simple agent using Deepseek R1 (8B) model via Ollama (hosted locally)

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

4. Pull Deepseek R1 (8B) model from Ollama registry

```bash
ollama pull deepseek-r1:8b
```

5. Run the app

```bash
uv run ollama-agent.py
```

![Simple Ollama Agent](./images/ollama-agent.png)