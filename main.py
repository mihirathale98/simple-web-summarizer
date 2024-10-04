from fastapi import FastAPI
import uvicorn

from src.models import TogetherModel
from src.web_search_api import brave_search
from src.query_gen import generate_queries

model = TogetherModel()


app = FastAPI()

@app.post('/search')
def search(request: dict):
    query = request["query"]
    queries = generate_queries(query)

    # results = {query: brave_search(query) for query in queries}
    return {"queries": queries}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)  


