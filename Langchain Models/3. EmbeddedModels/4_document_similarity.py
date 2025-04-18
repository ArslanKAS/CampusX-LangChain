from langchain_openai import OpenAIEmbeddings
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model = "text-embedding-3-large", dimensions=300)

documents = [
    "The capital of Afghanistan is Kabul.", 
    "The capital of France is Paris.",
    "The capital of Italy is Rome."
    ]

query = "Tell me something about Rome"

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

similarity_scores = cosine_similarity([query_embedding], doc_embeddings)[0]

index, score = sorted(list(enumerate(similarity_scores)), key=lambda x: x[1])[-1]

print(f"Most similar document: {documents[index]}")
print(f"Similarity score: {score}")

