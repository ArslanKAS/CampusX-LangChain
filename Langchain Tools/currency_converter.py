from dotenv import load_dotenv
import os
import requests
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage

# Step 1: Load environment variables from .env file
load_dotenv()
# Step 2: Retrieve API key for exchange rate service
EXCHANGE_RATE_API_KEY = os.getenv("EXCHANGE_RATE_API_KEY")

@tool  # Step 3: Define a tool to fetch the conversion factor between two currencies
def get_conversion_factor(base_currency: str, target_currency: str) -> float:
    """Fetches the conversion factor between two currencies using an external API."""
    # Step 4: Build the API request URL
    url = f"https://v6.exchangerate-api.com/v6/{EXCHANGE_RATE_API_KEY}/pair/{base_currency}/{target_currency}"
    # Step 5: Make HTTP GET request to the API
    response = requests.get(url)
    # Step 6: Raise an error if the API call failed
    response.raise_for_status()
    # Step 7: Parse and return the JSON conversion rate
    return response.json()["conversion_rate"]

@tool  # Step 8: Define a tool to convert an amount using a given conversion factor
def convert_currency(base_currency_value: float, conversion_factor: float) -> float:
    """Converts the base currency amount using the given conversion factor."""
    # Step 9: Perform multiplication and rounding for the final value
    return round(base_currency_value * conversion_factor, 2)

# Step 10: Initialize the chat model with tool support
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
# Step 11: Bind both tools to the LLM instance
llm_with_tools = llm.bind_tools([get_conversion_factor, convert_currency])

def run_currency_conversion(query: str) -> str:
    """
    Step 12: Add the user's query to the message history, invoke tools as needed,
    and return the final answer once no more tool calls are required.
    """
    # Step 13: Initialize a fresh message history list
    messages = []
    # Step 14: Add the human message (user query)
    messages.append(HumanMessage(query))
    
    while True:
        # Step 15: Invoke the LLM with the current conversation history
        result = llm_with_tools.invoke(messages)
        # Step 16: Append the model's response message
        messages.append(result)

        # Step 17: If the LLM requested any tool calls, execute them
        if result.tool_calls:
            # Step 18: Map tool names to actual functions
            tool_mapping = {
                "get_conversion_factor": get_conversion_factor,
                "convert_currency": convert_currency
            }
            for tool_call in result.tool_calls:
                # Step 19: Identify the tool and invoke it with provided args
                tool_name = tool_call["name"].lower()
                selected_tool = tool_mapping[tool_name]
                tool_msg = selected_tool.invoke(tool_call)
                # Step 20: Append the tool's output to history
                messages.append(tool_msg)
            # Step 21: Continue the loop to let the LLM process tool outputs
            continue

        # Step 22: No tool calls remain, return the final generated content
        return result.content

if __name__ == "__main__":
    # Step 23: Example user query for currency conversion
    user_query = (
        "What is the conversion factor between USD and PKR,"
        " and based on that can you convert 10 USD to PKR"
    )
    # Step 24: Run the conversion logic
    answer = run_currency_conversion(user_query)
    # Step 25: Print out the final answer
    print(answer)
