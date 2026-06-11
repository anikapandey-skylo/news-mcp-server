import requests
from datetime import datetime, timedelta

BASE_URL = "https://news-mcp-server-acx6.onrender.com"

def get_top_headlines(query: str) -> str:
    response = requests.get(f"{BASE_URL}/headlines", params={"query": query})
    data = response.json()

    if data.get("status") != "ok":
        return "Failed to fetch news."

    articles = data["articles"]
    if not articles:
        return f"No headlines found for '{query}'."

    result = f"Top headlines for '{query}':\n\n"
    for i, article in enumerate(articles[:5], 1):
        result += f"{i}. {article['title']}\n"
        result += f"   {article['description']}\n"
        result += f"   {article['url']}\n\n"

    return result


def search_news(query: str, days_back: int = 7) -> str:
    response = requests.get(f"{BASE_URL}/search", params={"query": query, "days_back": days_back})
    data = response.json()

    if data.get("status") != "ok":
        return "Failed to fetch news."

    articles = data["articles"]
    if not articles:
        return f"No articles found for '{query}' in the last {days_back} days."

    result = f"News about '{query}' from the last {days_back} days:\n\n"
    for i, article in enumerate(articles[:5], 1):
        result += f"{i}. {article['title']}\n"
        result += f"   {article['description']}\n"
        result += f"   {article['url']}\n\n"

    return result


def get_news_by_category(category: str) -> str:
    response = requests.get(f"{BASE_URL}/category", params={"category": category})
    data = response.json()

    if "error" in data:
        return data["error"]

    articles = data["articles"]
    if not articles:
        return f"No headlines found for category '{category}'."

    result = f"Top {category} headlines:\n\n"
    for i, article in enumerate(articles[:5], 1):
        result += f"{i}. {article['title']}\n"
        result += f"   {article['description']}\n"
        result += f"   {article['url']}\n\n"

    return result