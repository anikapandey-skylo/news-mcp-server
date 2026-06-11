from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime, timedelta
import requests
import os

app = FastAPI()

NEWS_API_KEY = os.getenv("NEWS_API_KEY", "9513a136bb4a470dba009b0f58682c65")

class NewsRequest(BaseModel):
    query: str
    days_back: int = 7

@app.get("/headlines")
def get_headlines(query: str):
    url = f"https://newsapi.org/v2/top-headlines?q={query}&language=en&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    return response.json()

@app.get("/search")
def search_news(query: str, days_back: int = 7):
    from_date = (datetime.now() - timedelta(days=days_back)).strftime("%Y-%m-%d")
    url = f"https://newsapi.org/v2/everything?q={query}&from={from_date}&language=en&sortBy=publishedAt&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    return response.json()

@app.get("/category")
def get_category(category: str):
    valid = ["business", "technology", "science", "health", "sports", "entertainment"]
    if category.lower() not in valid:
        return {"error": f"Invalid category. Choose from: {', '.join(valid)}"}
    url = f"https://newsapi.org/v2/top-headlines?category={category}&language=en&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    return response.json()

@app.post("/search-post")
def search_news_post(request: NewsRequest):
    from_date = (datetime.now() - timedelta(days=request.days_back)).strftime("%Y-%m-%d")
    url = f"https://newsapi.org/v2/everything?q={request.query}&from={from_date}&language=en&sortBy=publishedAt&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    return response.json()