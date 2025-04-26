# RunnableLambda converts a python function into a Runnable

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda, RunnableBranch

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

parser = StrOutputParser()

prompt_1 = PromptTemplate(
    template='Write a detailed report on the topic: {topic}',
    input_variables=['topic']
)

prompt_2 = PromptTemplate(
    template='Summarize the text in 500 words: "{text}"',
    input_variables=['text']
)

report_gen_chain = RunnableSequence(prompt_1, model, parser)

conditional_chain = RunnableBranch(
    (lambda x: len(x.split()) > 500, RunnableSequence(prompt_2, model, parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain,  conditional_chain)

print(final_chain.invoke({'topic':'AI'}))