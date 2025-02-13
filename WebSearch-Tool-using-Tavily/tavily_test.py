import os
from dotenv import load_dotenv  # Import the dotenv package
from langchain_community.tools.tavily_search import TavilySearchResults
from tavily import TavilyClient

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
api_key = os.getenv('TAVILY_API_KEY')

# Check if the key is loaded correctly
if not api_key:
    raise ValueError("API_KEY environment variable is not set. Check your .env file.")

# Initialize TavilyClient
try:
    tavily_client = TavilyClient(api_key=api_key)
except Exception as e:
    print(f"Error initializing TavilyClient: {e}")
    exit(1)

# Initialize TavilySearchResults without passing the key explicitly
tavily_search = TavilySearchResults(max_results=3)

# Search with error handling
try:
    search_docs = tavily_search.invoke("What is LangGraph?")
    print(search_docs)
except Exception as e:
    print(f"An error occurred during the search: {e}")
