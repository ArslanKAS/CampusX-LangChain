# RunnableParallel connects two or more runnables in parallel and returns the results as a dictionary.

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel

load_dotenv()

prompt1 = PromptTemplate(
    template='Write a tweet on the topic "{topic}"',
    input_variables=['topic']
)

model = ChatOpenAI(model="gpt-4o-mini")

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template='Write a Linkedin post on the topic "{topic}"',
    input_variables=['topic']
)

chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1, model, parser),
    'linkedin': RunnableSequence(prompt2, model, parser)
})

print(chain.invoke({'topic':'CXEX'}))