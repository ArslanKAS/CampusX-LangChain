# Creating a text loader for Langchain Document Loaders

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import WebBaseLoader
load_dotenv()

url = "https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/"
loader = WebBaseLoader(url)

docs = loader.load()

print(f"Number of documents: {len(docs)}")  # Print the number of documents loaded
print(f"Document type: {type(docs)}")  # Print the type of the documents loaded
print(f"Document type: {type(docs[0])}")  # Print the type of the first document
print(docs[0].page_content[:5])  # Print the content of the first document
print(docs[0].metadata)  # Print the metadata of the first document

model = ChatOpenAI(model="gpt-4o-mini")
prompt = PromptTemplate(
    template='Write a 2-line summary of the following text: {text}',
    input_variables=['text']
)
parser = StrOutputParser()

chain = prompt | model | parser
result = chain.invoke({'text': docs[0].page_content})
print(result)

