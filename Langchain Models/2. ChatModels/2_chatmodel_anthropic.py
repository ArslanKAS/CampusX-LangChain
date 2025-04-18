from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

llm = ChatAnthropic(model = "claude-3.5-sonnet-20241022")

response = llm.invoke("What is the capital of Pakistan?")

print(response.content)