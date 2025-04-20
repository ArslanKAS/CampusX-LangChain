from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

chat_prompttemplate = ChatPromptTemplate([
    ('system', "You are a helpful assistant who has expertize in {domain} domain."),
    ("human", "Explain what is meant be {topic}? Do it in a simple way and in 2 lines only.")
])

prompt = chat_prompttemplate.invoke({"domain": "AI", "topic": "Generative AI"})
print(prompt)