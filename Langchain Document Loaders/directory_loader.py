# Creating a text loader for Langchain Document Loaders

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path="Langchain Document Loaders/pdfs",
    glob="**/*.pdf",
    loader_cls=PyPDFLoader)

docs = loader.load()

print(f"Number of documents: {len(docs)}")  # Print the number of documents loaded
print(f"Document type: {type(docs)}")  # Print the type of the documents loaded
print(f"Document type: {type(docs[0])}")  # Print the type of the first document
print(docs[0].page_content)  # Print the content of the first document
print(docs[0].metadata)  # Print the metadata of the first document

