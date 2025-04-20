from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

chat_template = ChatPromptTemplate([
    ("system", "You are a helpful assistant that translates English to Urdu, not Hindi."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "{input}"),
])

chat_history = []

with open("langchain prompts/chat_history.txt", "r") as file:
    chat_history.extend(file.readlines())

prompt = chat_template.invoke({
    'chat_history' : chat_history,
    'input' : "Translate 'Hello, how are you?' to Urdu."
    })

print(prompt)