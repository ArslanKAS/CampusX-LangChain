from langchain.vectorstores import Chroma
from langchain.schema import Document
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

doc1 = Document(
    page_content="Karachi is the largest city in Pakistan, known for its vibrant culture, bustling markets, and beautiful beaches like Clifton. It serves as the country's economic hub and is famous for its diverse cuisine.",
    metadata={"food": "Biryani"}
)

doc2 = Document(
    page_content="Lahore, the heart of Pakistan, is known for its rich history, Mughal architecture, and lively atmosphere. The city is a cultural capital and offers iconic landmarks like the Badshahi Mosque and Lahore Fort.",
    metadata={"food": "Nihari"}
)

doc3 = Document(
    page_content="Islamabad, the capital city of Pakistan, is renowned for its scenic beauty, organized structure, and landmarks like Faisal Mosque and Daman-e-Koh. It offers a serene contrast to the hustle of major cities.",
    metadata={"food": "Chapli Kebab"}
)

doc4 = Document(
    page_content="Faisalabad is a major industrial center in Pakistan, often referred to as the 'Manchester of Pakistan' for its textile production. It has a strong entrepreneurial spirit and growing urban life.",
    metadata={"food": "Samosa"}
)

doc5 = Document(
    page_content="Peshawar, one of the oldest cities in South Asia, reflects a rich blend of culture and history. Its historic Qissa Khawani Bazaar and traditional hospitality are famous.",
    metadata={"food": "Chappal Kebab"}
)

docs = [doc1, doc2, doc3, doc4, doc5]
