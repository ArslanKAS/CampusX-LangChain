from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

messages = [
    SystemMessage(content="You are a helpful assistant.")
]

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    messages.append(HumanMessage(content=user_input))
    # print(f"User: {user_input}")

    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print(f"Assistant: {response.content}")

print(messages)