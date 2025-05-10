import asyncio
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from mcp_use import MCPAgent, MCPClient

async def main():
    # Load environment variables
    load_dotenv()

    client = MCPClient.from_config_file(
            os.path.join("Langchain MCP/browser_mcp.json")
        )

    # Create LLM
    llm = ChatOpenAI(model="gpt-4o-mini")

    # Create agent with the client
    agent = MCPAgent(llm=llm, client=client, max_steps=30)

    # Run the query
    result = await agent.run(
        "Find the best restaurant in San Francisco",
    )
    print(f"\nResult: {result}")

if __name__ == "__main__":
    asyncio.run(main())