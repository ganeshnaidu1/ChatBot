from langchain.tools import tool
from langchain_tavily import TavilyExtract

@tool
def Tavily(query: str, apiKey: str) -> dict:
    """
    Search the web for the query using Tavily.
    """
    tool = TavilyExtract(
        extract_depth="basic",
        include_images=False,
        tavily_api_key=apiKey,
    )
    print("inTool")
    return tool.invoke(query)