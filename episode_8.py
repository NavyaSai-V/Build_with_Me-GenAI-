import os
from dotenv import load_dotenv
from google import genai
import chromadb

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
    name="rag_collection"
)

# Sample documents
documents = [
    "RAG improves LLM responses using external knowledge.",
    "Vector databases store embeddings efficiently.",
    "Embeddings help AI understand semantic meaning.",
    "LLMs generate responses based on context."
]

# Store documents in Vector DB
for i, doc in enumerate(documents):

    # Generate embedding
    embedding_response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=doc
    )

    embedding = embedding_response.embeddings[0].values

    # Store in ChromaDB
    collection.add(
        ids=[str(i)],
        documents=[doc],
        embeddings=[embedding]
    )

print("Documents stored in Vector DB!\n")

# User question
query = input("Ask a question: ")

# Generate query embedding
query_embedding_response = client.models.embed_content(
    model="gemini-embedding-001",
    contents=query
)

query_embedding = query_embedding_response.embeddings[0].values

# Retrieve relevant documents
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=2
)

retrieved_docs = results["documents"][0]

print("\nRetrieved Context:\n")

for doc in retrieved_docs:
    print("-", doc)

# Combine retrieved context
context = "\n".join(retrieved_docs)

# Final prompt for LLM
final_prompt = f"""
Answer the question using the context below.

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