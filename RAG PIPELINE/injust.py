from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

# Load environment variables
load_dotenv()

# -----------------------------
# Step 1: Load PDF
# -----------------------------
print("Loading PDF...")

loader = PyPDFLoader("Docs/Gen AI.pdf")
documents = loader.load()

print(f"Total Pages Loaded: {len(documents)}")

# -----------------------------
# Step 2: Split into Chunks
# -----------------------------
print("Splitting into chunks...")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = text_splitter.split_documents(documents)

print(f"Total Chunks Created: {len(chunks)}")

# -----------------------------
# Step 3: Create Embedding Model
# -----------------------------
print("Loading Embedding Model...")

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    
)

# -----------------------------
# Step 4: Store in ChromaDB
# -----------------------------
print("Creating Vector Database...")

db = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="chroma_db"
)

print("Vector Database Created Successfully!")

print(f"Stored {len(chunks)} chunks inside ChromaDB.")

print("\nIngestion Completed Successfully!")