# Tavily Web Search Tool

This is a **Tavily Web Search** tool built with **Streamlit** and the **Tavily API**, designed to search the web for relevant information based on user queries. The tool provides a user-friendly interface to search and display results related to a specific query.

## Feature

- **Web Search**: Utilizes the Tavily API to search the web for relevant results.
- **Streamlit Interface**: Simple, interactive web interface for entering search queries and viewing results.
- **Customizable Results**: Limit the number of search results (up to 3 by default).
- **API Integration**: The tool is integrated with the Tavily API to fetch real-time data.
- **Error Handling**: Displays errors if there are issues with the search or API key.

## Prerequisite

- Python 3.8 or higher.
- The following Python packages are required:
  - `streamlit`
  - `dotenv`
  - `langchain`
  - `tavily`

To install the required packages, run:

```bash
pip install -r requirements.txt
