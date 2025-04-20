from langchain_openai import ChatOpenAI
from typing import TypedDict, Annotated, Literal, Optional
from dotenv import load_dotenv

load_dotenv()

class Review(TypedDict):
    key_themes: Annotated[list[str], "key themes of the review"]
    summary: Annotated[str, "summary of the review"]
    sentiment: Annotated[Literal["pos", "neg"], "sentiment of the review in Negative or Postitive"]
    sentiments: Annotated[Optional[int], "sentiment of the review in digits from 1 to 10"]
    pros: Annotated[list[str], "pros of the review"]
    cons: Annotated[list[str], "cons of the review"]

model = ChatOpenAI(model="gpt-4o-mini")

review_1 = """
    I had a truly wonderful experience at the restaurant. From the moment I walked in, the ambiance was warm and inviting, setting the tone for a delightful evening. The food was absolutely delicious—every dish was bursting with flavor and beautifully presented. It was clear that a lot of care went into both the preparation and the ingredients used. The service was equally impressive; the staff was attentive, friendly, and made sure we felt well taken care of throughout the meal. Overall, it was a memorable dining experience, and I would wholeheartedly recommend this place to my friends and anyone looking for great food paired with exceptional service."""

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