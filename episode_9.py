import os
from dotenv import load_dotenv
from google import genai
import chromadb
import PyPDF2

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Create ChromaDB client
chroma_client = chromadb.Client()

# Create collection
collection = chroma_client.create_collection(
    name="pdf_chatbot"
)

# Read PDF
pdf_path = "./data/IPL_Strategy_PDF_Chatbot_Demo.pdf"

pdf_reader = PyPDF2.PdfReader(pdf_path)

text = ""

for page in pdf_reader.pages:
    text += page.extract_text()

print("PDF Loaded Successfully!\n")

# Split text into chunks
chunk_size = 500

chunks = [
    text[i:i + chunk_size]
    for i in range(0, len(text), chunk_size)
]

print(f"Created {len(chunks)} chunks\n")

# Generate embeddings and store chunks
for i, chunk in enumerate(chunks):

    embedding_response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=chunk
    )

    embedding = embedding_response.embeddings[0].values

    collection.add(
        ids=[str(i)],
        documents=[chunk],
        embeddings=[embedding]
    )

print("Embeddings stored in Vector DB!\n")

# User Question
query = input("Ask a question from the PDF: ")

# Generate query embedding
query_embedding_response = client.models.embed_content(
    model="gemini-embedding-001",
    contents=query
)

query_embedding = query_embedding_response.embeddings[0].values

# Retrieve relevant chunks
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=2
)

retrieved_chunks = results["documents"][0]

print("\nRetrieved Chunks:\n")

for chunk in retrieved_chunks:
    print(chunk)
    print("\n-------------------\n")

# Combine retrieved context
context = "\n".join(retrieved_chunks)

# Final prompt
final_prompt = f"""
Answer the question using the PDF context below.

Context:
{context}

Question:
{query}
"""

# Generate final response
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=final_prompt
)

# Print final answer
print("\nFinal AI Response:\n")
print(response.text)