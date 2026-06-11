# News MCP Server

An MCP server that provides news tools powered by NewsAPI.org.

## Live Backend
https://news-mcp-server-acx6.onrender.com

## Tools

| Tool | Parameters | Description |
|---|---|---|
| `get_company_news` | `company: str` | Top headlines for a company or keyword |
| `search_recent_news` | `query: str, days_back: int` | Search news for past N days (default 7) |
| `get_category_news` | `category: str` | Headlines by category |

Valid categories: `business`, `technology`, `science`, `health`, `sports`, `entertainment`

## API Endpoints

| Endpoint | Parameters | Description |
|---|---|---|
| `GET /headlines` | `query` | Top headlines |
| `GET /search` | `query`, `days_back` | Search articles |
| `GET /category` | `category` | Category headlines |

## Setup

```bash
python3.11 -m venv venv
source venv/bin/activate
pip install "mcp[cli]" requests
```

Add to `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "news-mcp-server": {
      "command": "/path/to/venv/bin/python",
      "args": ["/path/to/server.py"]
    }
  }
}
```