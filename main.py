from fastapi import FastAPI
import uvicorn

from src.models import TogetherModel
from src.web_search_api import brave_search
from src.query_gen import generate_queries
from src.page_scraper import Scraper

model = TogetherModel()
scraper = Scraper()


app = FastAPI()

@app.post('/search')
def search(request: dict):
    query = request["query"]
    queries, reasoning = generate_queries(query)
    return {"queries": queries, "reasoning": reasoning}

@app.post('/web_search')
def web_search(request: dict):
    query = request["query"]
    k = request["k"]
    results = brave_search(query, k)
    return {"results": results}

@app.post('/scrape')
def scrape(request: dict):
    urls = request["urls"]
    texts = [f'URL: {url}\nContent: \n{scraper.get_text_from_url(url)}' for url in urls]
    return {"texts": '\n\n'.join(texts)}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)  


