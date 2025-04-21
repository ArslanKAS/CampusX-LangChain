from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

class Person(BaseModel):
    name: str = Field(description = "Name of the person")
    age: int = Field(description = "Age of the person")
    city: str = Field(description = "City where the person lives")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="Generate the name, age and city of a fictional {place} person. \n {format_instructions}",
    input_variables=["place"],
    partial_variables={'format_instructions': parser.get_format_instructions}
)

chain = template | model | parser

response = chain.invoke({"place": "Pakistani"})

print(response.model_dump_json())