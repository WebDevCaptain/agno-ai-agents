from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools


search_agent = Agent(
    name="Search Agent",
    role="Search the web",
    instructions=[
        "Given a stock ticker symbol, retrieve news and company information from the web by using the DuckDuckGo search engine. Always include sources.",
    ],
    model=Ollama(id="qwen2.5:1.5b"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    instructions=[
        "Given a stock ticker symbol, retrieve stock price, analyst recommendations, stock fundamentals, historical prices, and company information from Yahoo Finance."
    ],
    model=Ollama(id="qwen2.5:1.5b"),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True,
            historical_prices=True,
            company_info=True,
        )
    ],
    show_tool_calls=True,
    markdown=True,
)

agent_team = Agent(
    model=Ollama(id="qwen2.5:1.5b"),
    team=[search_agent, finance_agent],
    description=[
        "You are a team of agents, with the ability to search the web using DuckDuckGo and extract financial data from yahoo finance."
    ],
    instructions=[
        "First, use the Search Agent to retrieve news and company information for the given stock ticker symbol. Then, use the Finance Agent to retrieve stock price, analyst recommendations, stock fundamentals, historical prices, and company information.",
    ],
    show_tool_calls=True,
    add_datetime_to_instructions=True,
    markdown=True,
    debug_mode=True,
)

agent_team.print_response(
    "Summarize analyst recommendations and share the latest news for Apple with stock ticker symbol of AAPL.",
    stream=True,
)
