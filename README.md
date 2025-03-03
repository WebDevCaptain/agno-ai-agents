# Finance Agent using agno and Ollama (Deepseek R1 - 8B model)


## Requirements

- uv
- ollama


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

4. Run the app

```bash
uv run ollama-agent.py
```