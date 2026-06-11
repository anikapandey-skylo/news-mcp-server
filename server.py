from mcp.server.fastmcp import FastMCP
from tools import get_top_headlines, search_news, get_news_by_category

mcp = FastMCP("news-mcp-server")

@mcp.tool()
def get_company_news(company: str) -> str:
    """Get the latest news headlines for a company or topic."""
    return get_top_headlines(company)

@mcp.tool()
def search_recent_news(query: str, days_back: int = 7) -> str:
    """Search news articles about any topic for the past N days."""
    return search_news(query, days_back)

@mcp.tool()
def get_category_news(category: str) -> str:
    """Get top headlines by category. Categories: business, technology, science, health, sports, entertainment."""
    return get_news_by_category(category)

if __name__ == "__main__":
    mcp.run()