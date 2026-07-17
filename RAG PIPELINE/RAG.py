from dotenv import load_dotenv

from langchain_chroma import Chroma

from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings,
    ChatGoogleGenerativeAI,
)

load_dotenv()

# Embedding model
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    
)

# Load existing ChromaDB
db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings,
)

# Retriever
retriever = db.as_retriever(search_kwargs={"k":3})

# Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

while True:

    question = input("\nAsk Question: ")

    if question.lower() == "exit":
        break

    docs = retriever.invoke(question)

    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""
Use ONLY the context below.

Context:
{context}

Question:
{question}
"""

    answer = llm.invoke(prompt)

    print("\nAnswer:\n")

    print(answer.content)