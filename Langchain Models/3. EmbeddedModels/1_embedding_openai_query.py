from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model = "text-embedding-3-large", dimensions=32)

result = embedding.embed_query("The capital of Afghanistan is Kabul.")

print(str(result))

