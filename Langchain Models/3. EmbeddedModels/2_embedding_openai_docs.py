from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model = "text-embedding-3-large", dimensions=32)

documents = [
    "The capital of Afghanistan is Kabul.", 
    "The capital of France is Paris.",
    "The capital of Italy is Rome."
    ]

result = embedding.embed_documents(documents)

print(str(result))

