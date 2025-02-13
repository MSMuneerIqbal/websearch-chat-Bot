import os
from dotenv import load_dotenv
import streamlit as st
from langchain_community.tools.tavily_search import TavilySearchResults
from tavily import TavilyClient

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv('TAVILY_API_KEY')

# Streamlit UI
st.set_page_config(page_title="Tavily Web Search", layout="centered")
st.title("🔎 Tavily Web Search")

# Input field for search query
query = st.text_input("Enter your search query:", placeholder="e.g., What is LangGraph?")

# Button to trigger the search
if st.button("Search"):
    # Check if API key is loaded
    if not api_key:
        st.error("API_KEY environment variable is not set. Check your .env file.")
    else:
        # Initialize TavilyClient and TavilySearchResults
        try:
            tavily_client = TavilyClient(api_key=api_key)
            tavily_search = TavilySearchResults(max_results=3)
            
            # Perform search
            with st.spinner("Searching..."):
                search_docs = tavily_search.invoke(query)

            # Display results if available
            if search_docs:
                st.success("Search Results:")
                for i, doc in enumerate(search_docs, 1):
                    # Safely display each component if available
                    url = doc.get('url', '#')  # Use URL for the link
                    content = doc.get('content', 'No Content Available')  # Use content for the snippet

                    st.markdown(f"### Result {i}")
                    st.markdown(f"**Link:** [Read More]({url})")
                    st.markdown(f"**Snippet:** {content}")
                    st.markdown("---")
            else:
                st.info("No results found.")
        except Exception as e:
            st.error(f"An error occurred during the search: {e}")
