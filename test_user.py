
from tavily import TavilyClient

# Step 1. Instantiating your TavilyClient
tavily_client = TavilyClient(api_key="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")

# Step 2. Executing a simple search query
response = tavily_client.search("Who won the football world cup in 2014?")

# Step 3. That's it! You've done a Tavily Search!
print(response)