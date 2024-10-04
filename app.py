import requests
import streamlit as st


query = st.text_input("Enter your query:")

button = st.button("Submit")

if button:
    if query:
        response = requests.post('http://localhost:8000/search', json={"query": query})
        if response.status_code == 200:
            st.text(response.json()["queries"])
        else:
            st.text(response.json())


