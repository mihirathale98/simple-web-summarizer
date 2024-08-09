from fastapi import FastAPI
import uvicorn

from src.models import TogetherModel
from src.web_search_api import BingSearch


bing_search = BingSearch()
model = TogetherModel()


if __name__ == "__main__":
    #print(bing_search.search(search_term="Python"))
    print(model.generate("Hi"))
