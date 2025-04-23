from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

prompt1 = PromptTemplate(
    template='Write a short joke about {topic}',
    input_variables=['topic']
)

model = ChatOpenAI(model="gpt-4o-mini")

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template='Explain the following joke in 2 lines - {text}',
    input_variables=['text']
)

joke_generator_chain = RunnableSequence(prompt1, model, parser)

parrallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': RunnableSequence(prompt2, model, parser)
})

final_chain = RunnableSequence(joke_generator_chain, parrallel_chain)

print(final_chain.invoke({'topic':'AI'}))