from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")

documents = [
    "The capital of Afghanistan is Kabul.", 
    "The capital of France is Paris.",
    "The capital of Italy is Rome."
    ]

result = embedding.embed_documents(documents)

print(str(result))

