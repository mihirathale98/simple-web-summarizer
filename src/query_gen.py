from src.models import TogetherModel
from src.utils import parse_json

together = TogetherModel()

def generate_queries(query):
    prompt ="""
    You are an intelligent assistant who helps search internet to retrieve the most recent and most relevant content for a given query.

    Given the user query you have to think step by step and figure out the intent of the user. Determine what he is actually looking for and then generate 3 queries which would satisfy the query and user's intent. 

    user query: {query}

    Think step by step in the following thinking tags:
    <thinking></thinking>

    Based on the reasoning, generate the 3 queries in the following format:
    ```json["query_1", "query_2", "query_3"]```

    Output:
""" 
    
    queries = parse_json(together.generate(prompt.format(query=query)))
    return queries