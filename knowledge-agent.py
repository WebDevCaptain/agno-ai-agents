from agno.agent import Agent
from agno.embedder.ollama import OllamaEmbedder
from agno.knowledge.pdf import PDFKnowledgeBase
from agno.models.ollama import Ollama
from agno.vectordb.chroma.chromadb import ChromaDb


chroma_db = ChromaDb(
    collection="llm-tips",
    path="chroma.sqlite",
    persistent_client=True,
    embedder=OllamaEmbedder(id="llama3.2", dimensions=3072),
)


knowledge_base = PDFKnowledgeBase(path="pdfs/How_I_Use_LLMs.pdf", vector_db=chroma_db)

knowledge_base.load(recreate=False)  # Comment out after first run

agent = Agent(
    model=Ollama(id="llama3.2"),
    knowledge=knowledge_base,
    show_tool_calls=True,
)
agent.print_response(
    "Give me a practical tip from Fundamentals of LLM Operations section.",
    markdown=False,
)
