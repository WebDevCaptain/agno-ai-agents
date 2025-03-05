from pathlib import Path

from agno.agent import Agent
from agno.media import Image
from agno.models.ollama import Ollama

agent = Agent(
    model=Ollama(id="llama3.2-vision"),
    markdown=True,
)

image_path = Path(__file__).parent.joinpath("./images/ai-agents-architecture.png")

agent.print_response(
    "Describe the concept explained in the image.",
    images=[Image(filepath=image_path)],
)
