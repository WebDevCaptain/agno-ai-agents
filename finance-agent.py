"""Run `pip install yfinance` to install dependencies."""

from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.tools.yfinance import YFinanceTools


def get_stock_ticker_symbol(company_name: str) -> str:
    """Retrieve the stock ticker symbol for a given company listed on the Stock exchange.

    Args:
        company_name (str): The full name of the company.

    Returns:
        str: The stock ticker symbol of the company if found; otherwise, 'Unknown'.
    """
    symbols = {
        "Apple": "AAPL",
        "Microsoft": "MSFT",
        "Amazon": "AMZN",
        "Meta": "META",
        "Google": "GOOGL",
        "Nvidia": "NVDA",
        "Advanced Micro Devices": "AMD",
    }
    return symbols.get(company_name, "Unknown")


agent = Agent(
    model=Ollama(id="qwen2.5:1.5b"),  # deepseek-r1:8b is not supported
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True,
            historical_prices=True,
            company_info=True,
            company_news=True,
        ),
        get_stock_ticker_symbol,
    ],
    instructions=[
        "Use concise tables to display data.",
        "If you need to find the symbol for a company, use the get_stock_ticker_symbol tool.",
    ],
    add_datetime_to_instructions=True,
    show_tool_calls=True,
    markdown=True,
    # debug_mode=True,
)

agent.print_response(
    "Summarize and compare analyst recommendations and fundamentals for Microsoft and Google. Which one is the favorite among traders ? Keep the entire answer in under 200 words.",
    stream=True,
)
