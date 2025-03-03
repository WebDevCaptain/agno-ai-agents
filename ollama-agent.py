from agno.agent import Agent
from agno.models.ollama import Ollama

agent = Agent(model=Ollama(id="deepseek-r1:8b"))

agent.print_response(
    "Write a paragraph in 100 words about the future of finance", stream=True
)
