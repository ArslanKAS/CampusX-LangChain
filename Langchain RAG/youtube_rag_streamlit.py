import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

st.title("📺 YouTube Video Q&A (RAG-based)")

video_id = st.text_input("Enter YouTube Video ID (e.g. Wm3VzPu0UK8)")
question = st.text_input("Ask a question based on the video transcript")

if st.button("Get Answer") and video_id and question:
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])
        transcript = " ".join(chunk["text"] for chunk in transcript_list)

        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = splitter.create_documents([transcript])

        embeddings = OpenAIEmbeddings()
        vectorstore = FAISS.from_documents(chunks, embeddings)
        retriever = vectorstore.as_retriever()

        template = """
        You are an assistant that answers questions based on YouTube video transcripts.

        Context:
        {context}

        Question:
        {question}

        Answer:
        """
        prompt = PromptTemplate.from_template(template)

        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

        from langchain_core.runnables import RunnableMap, RunnablePassthrough
        chain = (
            RunnableMap({"context": retriever, "question": RunnablePassthrough()})
            | prompt
            | llm
        )

        response = chain.invoke(question)
        st.success("Answer:")
        st.write(response.content)

    except TranscriptsDisabled:
        st.error("No captions available for this video.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
