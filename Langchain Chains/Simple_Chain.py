from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

parser = StrOutputParser()

template = PromptTemplate(
    template="Write 5 bullet points about {topic}",
    input_variables=["topic"],
)

chain = template | model | parser

print("Visualize Chain:")
print(chain.get_graph().print_ascii())

# result = chain.invoke({"topic": "Python programming"})

# print(result)