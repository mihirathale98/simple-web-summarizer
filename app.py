import requests
import streamlit as st
import time


query = st.text_input("Enter your query:")

button = st.button("Submit")

if button:
    if query:
        response = requests.post('http://localhost:8000/search', json={"query": query})
        if response.status_code == 200:
            queries = response.json()["queries"]
            reasoning = response.json()["reasoning"]
        else:
            st.text(response.json())
        web_search_results = {}
        for query in queries:
            with st.spinner(f'Searching for "{query}"'):
                response = requests.post('http://localhost:8000/web_search', json={"query": query, "k": 5})
                if response.status_code == 200:
                    results = response.json()["results"]
                else:
                    st.text(response.json())
                web_search_results[query] = results
                time.sleep(2)


        content = ""
        for query, results in web_search_results.items():
            with st.spinner(f'Retrieving Data for "{query}"'):
                urls = [result["url"] for result in results]
                scraped_text = requests.post('http://localhost:8000/scrape', json={"urls": urls}).json()["texts"]

                content += f"## {query}\n"
                content += scraped_text
                content += "\n\n"
        if content != "":
            with st.spinner('Getting your answer'):
                final_summary = requests.post('http://localhost:8000/summarize', json={"query": query, "intent_reasoning": reasoning, "sub_queries": queries, "web_results": content}).json()["summary"]

            st.write(final_summary)

        


            


