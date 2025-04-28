from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

text_splitter = SemanticChunker(
    OpenAIEmbeddings(), breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=1
)

text = """
Farmers in India were working hard in the fields, preparing the soil and planting seeds for the next season. 
The sun was bright, and the air smelled of earth and fresh grass. 
Islamabad is the nation's capital, while Karachi is its largest city and financial centre. 
Pakistan is the 33rd-largest country by area.

Terrorism is a big danger to peace and safety. It causes harm to people and creates fear in cities and villages. 
When such attacks happen, they leave behind pain and sadness. To fight terrorism, we need strong laws, alert security forces, 
and support from people who care about peace and safety.
"""

docs = text_splitter.create_documents([text])
print(len(docs))
print(docs)

