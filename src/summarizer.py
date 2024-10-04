from src.models import TogetherModel
from src.utils import parse_markdown

together = TogetherModel()

def summarize(query, intent_reasoning, sub_queries, web_results):

    prompt = """
You are an intelligent assistant who answers the user's query in a detailed and explainatory manner.
You will be provided the user's original query followed by some sub queries that are related to the original query.
For each sub query you will be provided with the web search results(the url and the content of the web page).

You will also be provided with a intent reasoning that was used to generate the sub queries.

Based on the reasoning, and understanding of the user's query, answer the user's query in the most appropriate way possible.

Only use the relevant search results and discard the urls and content which are not aligned to the user's query(take the majority).

Analyse the user's query properly and think step by step to answer the query.

Provide references in the href format.

user query: {query}

intent reasoning: {intent_reasoning}

sub queries: {sub_queries}

web search results: {web_results}

Think step by step in the following thinking tags:
<thinking></thinking>

Only output the final answer in a markdown format like this.
```markdown
<your answer here>
```

Final answer:
"""

    summary = together.generate(prompt.format(query=query, intent_reasoning=intent_reasoning, sub_queries=sub_queries, web_results=web_results))

    return summary