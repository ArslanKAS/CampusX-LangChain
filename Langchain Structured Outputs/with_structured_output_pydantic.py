from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

# schema
class Review(BaseModel):

    key_themes: list[str] = Field(description="Write down all the key themes discussed in the review in a list")
    summary: str = Field(description="A brief summary of the review")
    sentiment: Literal["pos", "neg"] = Field(description="Return sentiment of the review either negative, positive or neutral")
    pros: Optional[list[str]] = Field(default=None, description="Write down all the pros inside a list")
    cons: Optional[list[str]] = Field(default=None, description="Write down all the cons inside a list")
    name: Optional[str] = Field(default=None, description="Write the name of the reviewer")
    rating: Optional[float] = Field(default=None, description="Write the rating of the product out of 10")
    

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""I had a truly wonderful experience at the restaurant. From the moment I walked in, the ambiance was warm and inviting, setting the tone for a delightful evening. The food was absolutely delicious—every dish was bursting with flavor and beautifully presented. It was clear that a lot of care went into both the preparation and the ingredients used. The service was equally impressive; the staff was attentive, friendly, and made sure we felt well taken care of throughout the meal. Overall, it was a memorable dining experience, and I would wholeheartedly recommend this place to my friends and anyone looking for great food paired with exceptional service.
                                 
Review by KAS
""")

print(result)