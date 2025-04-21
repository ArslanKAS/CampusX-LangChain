from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

parser = StrOutputParser()

prompt_1 = PromptTemplate(
    template="Geneate a report on the topic '{topic}'",
    input_variables=["topic"],
)

prompt_2 = PromptTemplate(
    template="Summarize the report in 3 bullet points. The report is: {text}",
    input_variables=["text"],
)

chain = prompt_1 | model | parser | prompt_2 | model | parser

print("Visualize Chain:")
print(chain.get_graph().print_ascii())

result = chain.invoke({"topic": "Muhammad Ali"})

print(result)