# Import required modules
import os
import asyncio
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from mcp_use import MCPAgent, MCPClient

# Define the main asynchronous function
async def main():
    # Step 1: Load environment variables from .env file
    load_dotenv()

    # Step 2: Initialize the MCP client using the config file
    client = MCPClient.from_config_file(
        os.path.join(os.path.dirname(__file__), "browser_mcp.json")
    )

    # Step 3: Initialize the OpenAI language model
    llm = ChatOpenAI(model="gpt-4o-mini")

    # Step 4: Create the MCP agent using the LLM and client
    agent = MCPAgent(llm=llm, client=client, max_steps=30)

    # Step 5: Run the agent with a travel-related query
    result = await agent.run(
        "Search for a cheap place to stay in Faisalabad, Pakistan using airbnb. Show prices in PKR."
    )

    # Step 6: Print the result
    print(f"\nResult: {result}")

# Entry point for the script
if __name__ == "__main__":
    asyncio.run(main())