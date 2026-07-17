import streamlit as st

from dotenv import load_dotenv

from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings,
    ChatGoogleGenerativeAI,
)

from langchain_chroma import Chroma

load_dotenv()

st.title("📚 PDF RAG Chatbot")

# Embeddings
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    
)

# Load Chroma
db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings,
)

retriever = db.as_retriever(search_kwargs={"k":3})

# Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

question = st.text_input("Ask a question")

if st.button("Generate Answer"):

    docs = retriever.invoke(question)

    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""
Answer only from the context.

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    st.subheader("Answer")

    st.write(response.content)

    with st.expander("Retrieved Chunks"):

        for doc in docs:

            st.write(doc.page_content)
            st.write("------------")