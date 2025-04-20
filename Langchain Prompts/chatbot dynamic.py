from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

chat_template = ChatPromptTemplate([
    ("system", "You are a helpful assistant that translates English to Roman Urdu, not Hindi."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "{input}"),
])

chat_history = []

with open("langchain prompts/chat_history.txt", "r") as file:
    chat_history.extend(file.readlines())

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    chat_history.append('human' + ": " + user_input + "\n")
    # print(f"User: {user_input}")

    chain = chat_template | model
    result = chain.invoke({
        "chat_history": chat_history,
        "input": user_input
    })
    chat_history.append('AI: ' + result.content + "\n")
    print('AI: ' + result.content)

print(chat_history)