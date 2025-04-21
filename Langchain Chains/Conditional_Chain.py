from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableBranch, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

class Sentiments(BaseModel):
    sentiment: Literal['positive', 'negative', 'neutral'] = Field(description="Generate sentiments out of the feedback")


parser = StrOutputParser()
pydantic_parser = PydanticOutputParser(pydantic_object=Sentiments)

prompt_1 = PromptTemplate(
    template="We've a customer feedback. Please review it and classify sentiment as either Positive, Negative or Neutral : \n  '{feedback}' {format_instructions}",
    input_variables=["feedback"],
    partial_variables = {"format_instructions": pydantic_parser.get_format_instructions()}
)

classification_chain = prompt_1 | model | pydantic_parser

prompt_2 = PromptTemplate(
    template="Write an appropriate 2-liner response to the positive customer feedback. \n  '{feedback}'",
    input_variables=["feedback"],
)

prompt_3 = PromptTemplate(
    template="Write an appropriate 2-liner response to the negative customer feedback. \n  '{feedback}'",
    input_variables=["feedback"],
)

conditional_chain = RunnableBranch(
    (lambda x:x.sentiment == "positive", prompt_2 | model | parser),
    (lambda x:x.sentiment == "negative", prompt_3 | model | parser),
    RunnableLambda(lambda x:"Sentiments are Neutral. No response is required."),
)

chain = classification_chain | conditional_chain

negative_feedback = """
Arsalan: This ice cream suck. It does not have any taste and also there was an insect on top of it. It was melting a lot faster too. I would never recommend this place to anyone. I am very disappointed and I will never come back again.
"""

positive_feedback = """
Arsalan: The ice cream was great and everything on the menu was superd. I loved the chocolate flavor and the way it was presented. The staff was also very friendly and helpful.
I would love to come back again and again. I would recommend this place to everyone.
"""

neutral_feedback = """
Arsalan: Everything was alright as it should be. It wasn't good nor it was bad. I would say it was average. I would not recommend this place to anyone but I would not stop anyone from going there either.
"""

print("Visualize Chain:")
print(chain.get_graph().print_ascii())

result = chain.invoke({"feedback": positive_feedback})

print(result)