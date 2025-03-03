from agno.agent import Agent
from agno.models.ollama import Ollama

agent = Agent(model=Ollama(id="deepseek-r1:8b"))  # can also use qwen2.5:1.5b model

agent.print_response(
    "Write a paragraph in 100 words about the future of finance", stream=True
)
