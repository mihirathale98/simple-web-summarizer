from fastapi import FastAPI
import uvicorn


from src.web_search_api import BingSearch




bing_search = BingSearch()



if __name__ == "__main__":
    print(bing_search.search(search_term="Python"))

