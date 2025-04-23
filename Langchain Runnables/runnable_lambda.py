# RunnableLambda converts a python function into a Runnable

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda

load_dotenv()

prompt1 = PromptTemplate(
    template='Write a short joke about {topic}',
    input_variables=['topic']
)

model = ChatOpenAI(model="gpt-4o-mini")

parser = StrOutputParser()

def word_count(text):
    return len(text.split())

joke_generator_chain = RunnableSequence(prompt1, model, parser)

parrallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word count': RunnableLambda(word_count)
})

final_chain = RunnableSequence(joke_generator_chain, parrallel_chain)

print(final_chain.invoke({'topic':'AI'}))