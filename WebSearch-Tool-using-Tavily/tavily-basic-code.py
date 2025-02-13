import os
from dotenv import load_dotenv  # Import the dotenv package
from langchain_community.tools.tavily_search import TavilySearchResults
from tavily import TavilyClient
# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
api_key = os.getenv('TAVILY_API_KEY')

# Initialize TavilyClient
tavily_client = TavilyClient(api_key=api_key)

# Initialize TavilySearchResults without passing the key explicitly
tavily_search = TavilySearchResults(max_results=3)

search_docs = tavily_search.invoke("What is LangGraph?")
print(search_docs)