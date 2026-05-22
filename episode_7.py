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
    name="my_documents"
)

# Sample documents
documents = [
    "RAG stands for Retrieval Augmented Generation",
    "Embeddings convert text into vectors",
    "Vector databases store embeddings efficiently",
    "LLMs generate human-like text responses"
]

# Generate embeddings and store documents
for i, doc in enumerate(documents):

    # Generate embedding
    embedding_response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=doc
    )

    # Extract embedding vector
    embedding = embedding_response.embeddings[0].values

    # Store in ChromaDB
    collection.add(
        ids=[str(i)],
        documents=[doc],
        embeddings=[embedding]
    )

print("Documents stored successfully!\n")

# Take user query
query = input("Enter your query: ")

# Generate embedding for query
query_embedding_response = client.models.embed_content(
    model="gemini-embedding-001",
    contents=query
)

# Extract query embedding
query_embedding = query_embedding_response.embeddings[0].values

# Search similar documents
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=2
)

# Display results
print("\nMost Relevant Documents:\n")

for doc in results["documents"][0]:
    print(doc)