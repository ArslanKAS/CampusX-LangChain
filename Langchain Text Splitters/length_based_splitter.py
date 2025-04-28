from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("Langchain Document Loaders/Arsalan_Ali_Resume_2025.pdf")

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=10,
    separator="."
)

chunks = splitter.split_documents(docs)

print(f"Number of chunks: {len(chunks)}")  # Print the number of chunks created
print(chunks[0])  # Print the content of the first chunk