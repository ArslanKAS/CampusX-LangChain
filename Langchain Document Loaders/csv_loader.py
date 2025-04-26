# Creating a text loader for Langchain Document Loaders

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import CSVLoader
load_dotenv()

loader = CSVLoader("Langchain Document Loaders/Pakistan_GDP.csv")

docs = loader.load()

print(f"Number of documents: {len(docs)}")  # Print the number of documents loaded
print(f"Document type: {type(docs)}")  # Print the type of the documents loaded
print(f"Document type: {type(docs[0])}")  # Print the type of the first document
print(docs[0].page_content[:5])  # Print the content of the first document
print(docs[0].metadata)  # Print the metadata of the first document

full_text = [doc.page_content for doc in docs]

model = ChatOpenAI(model="gpt-4o-mini")
prompt = PromptTemplate(
    template='Compare the GDP of Pakistan with the World and summarize in 2-lines for me: {text}',
    input_variables=['text']
)
parser = StrOutputParser()

chain = prompt | model | parser
result = chain.invoke({'text': full_text})
print(result)

