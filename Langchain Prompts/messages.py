from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

messsages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Who is the most popular person in Pakistan in 2007? Just give me a 1-liner.")
]

result = model.invoke(messsages)

messsages.append(AIMessage(content=result.content))
print(messsages)