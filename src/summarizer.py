from src.models import TogetherModel
from src.utils import parse_markdown

together = TogetherModel()

def summarize(query, intent_reasoning, sub_queries, web_results):

    prompt = """
You are an intelligent assistant tasked with answering the user's query in a detailed, comprehensive, and explanatory manner. You will be provided with the following information:

1. The user's original query
2. Sub-queries related to the original query
3. Web search results for each sub-query (including URLs and content of web pages)
4. Intent reasoning used to generate the sub-queries

Your task is to:

1. Carefully analyze the user's query and the provided information.
2. Think through the problem step-by-step, considering all relevant aspects.
3. Use the intent reasoning to understand the context and purpose of the sub-queries.
4. Evaluate the web search results, focusing on those most relevant to the user's query.
5. Discard any URLs and content that are not aligned with the user's query (consider the majority of relevant results).
6. Synthesize the information to create a comprehensive and detailed answer.
7. Provide references to support your answer using the following format: <a href="URL">relevant text</a>.

When formulating your response:

1. Begin with a clear and concise summary of the main points.
2. Elaborate on each point, providing detailed explanations and examples where appropriate.
3. Address any potential sub-topics or related issues that may be relevant to the user's query.
4. If applicable, discuss different perspectives or approaches to the topic.
5. Conclude with a brief recap of the key takeaways.

Use the following structure for your response:

<thinking>
[Your step-by-step thought process here]
</thinking>

Give a well-structured, informative answer that directly addresses the user's needs in the following format enclosed in triple backticks
```markdown
[Your comprehensive and detailed answer here, including references in the specified format]
```

user query: {query}
intent reasoning: {intent_reasoning}
sub queries: {sub_queries}
web search results: {web_results}
Remember to analyze the query thoroughly, think step-by-step, and provide a well-structured, informative answer that directly addresses the user's needs.

Output:
"""
    response = together.generate(prompt.format(query=query, intent_reasoning=intent_reasoning, sub_queries=sub_queries, web_results=web_results))

    summary = parse_markdown(response)
    if summary is None:
        print(response)

    return summary