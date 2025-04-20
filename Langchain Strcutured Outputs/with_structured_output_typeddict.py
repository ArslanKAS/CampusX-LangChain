from langchain_openai import ChatOpenAI
from typing import TypedDict
from dotenv import load_dotenv

load_dotenv()

class Review(TypedDict):
    summary: str
    sentiment: str

model = ChatOpenAI(model="gpt-4o-mini")

review_1 = """
    I had a great experience at the restaurant. The food was delicious and the service was excellent.
    I would definitely recommend it to my friends."""

review_2 = """
    The food was cold and the service was slow. I was very disappointed with my experience.
    I would not recommend it to anyone."""

structured_model = model.with_structured_output(Review)

response_1 = structured_model.invoke(review_1)

print("Response 1:")
print(response_1)   

response_2 = structured_model.invoke(review_2)

print("Response 2:")
print(response_2)