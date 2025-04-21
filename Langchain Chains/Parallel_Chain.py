from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

load_dotenv()

model_1 = ChatOpenAI(model="gpt-4o-mini")
model_2 = ChatOpenAI(model="gpt-3.5-turbo")
model_3 = ChatOpenAI(model="gpt-4.1-mini")

parser = StrOutputParser()

prompt_1 = PromptTemplate(
    template="Generate 5 bullet point notes from the following text: \n  '{text}'",
    input_variables=["text"],
)

prompt_2 = PromptTemplate(
    template="Generate 5 questions and answers (FAQ) from the following text: \n  '{text}'",
    input_variables=["text"],
)

prompt_3 = PromptTemplate(
    template="Combine the notes and FAQ into a single document. \n  '{notes}' \n  '{faq}'",
    input_variables=["notes", "faq"],
)

parallel_chain = RunnableParallel({
    'notes': prompt_1 | model_1 | parser,
    'faq': prompt_2 | model_2 | parser,
})

merge_chain = prompt_3 | model_3 | parser

chain = parallel_chain | merge_chain

print("Visualize Chain:")
print(chain.get_graph().print_ascii())

text = """
Muhammad Ali (/ɑːˈliː/;[2] born Cassius Marcellus Clay Jr.; January 17, 1942 – June 3, 2016) was an American professional boxer and social activist.[a] A global cultural icon, widely known by the epithet "The Greatest", he is frequently cited as the greatest heavyweight boxer of all time. He held the Ring magazine heavyweight title from 1964 to 1970, was the undisputed champion from 1974 to 1978, and was the WBA and Ring heavyweight champion from 1978 to 1979. In 1999, he was named Sportsman of the Century by Sports Illustrated and the Sports Personality of the Century by the BBC.

Born in Louisville, Kentucky, he began training as an amateur boxer at age 12. At 18, he won a gold medal in the light heavyweight division at the 1960 Summer Olympics and turned professional later that year. He joined the Nation of Islam in the early 1960s, but later disavowed it in the mid-1970s. He won the world heavyweight championship, defeating Sonny Liston in a major upset on February 25, 1964, at age 22. During that year, he denounced his birth name as a "slave name" and formally changed his name to Muhammad Ali. In 1967, Ali refused to be drafted into the military, owing to his religious beliefs and ethical opposition to the Vietnam War, and was found guilty of draft evasion and stripped of his boxing titles. He stayed out of prison while appealing the decision to the Supreme Court, where his conviction was overturned in 1971. He did not fight for nearly four years and lost a period of peak performance as an athlete. Ali's actions as a conscientious objector to the Vietnam War made him an icon for the larger counterculture of the 1960s generation, and became a prominent, high-profile figure of racial pride for African Americans during the civil rights movement and throughout his career.
"""
result = chain.invoke({"text": text})

print(result)