from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model = "gpt-3.5-turbo-instruct")

response = llm.invoke("What is the capital of Pakistan?")

print(response)