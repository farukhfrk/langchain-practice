"""
Document Similarity Search Using Embeddings

This module demonstrates how to:
1. Generate embeddings for multiple documents
2. Generate embedding for a query
3. Calculate cosine similarity between query and documents
4. Find the most similar document to a query

Uses OpenAI's embedding model to convert text to dense vectors,
then applies cosine similarity to find semantic matches.

This is useful for:
- Semantic search
- Document recommendation
- Retrieval-Augmented Generation (RAG)
- Clustering similar documents

Example:
    python 1_document_similarity.py
"""

from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load environment variables
load_dotenv()

# Initialize embedding model from OpenAI
# Using text-embedding-3-large with 300 dimensions
# Higher dimensions capture more semantic information
embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)

# Sample documents covering various domains (AI, Finance, Cloud, DevOps, Fitness, Health)
documents = [
    "Artificial intelligence enables machines to learn patterns from data and make decisions.",
    "Supervised learning uses labeled datasets to train predictive models.",
    "The stock market allows investors to buy and sell shares of public companies.",
    "Bonds are fixed-income instruments used by governments and corporations to raise capital.",
    "Cloud computing provides on-demand access to servers, storage, and networking resources.",
    "Microservices architecture breaks applications into independently deployable services.",
    "Kafka is a distributed streaming platform used for real-time data pipelines.",
    "Redis is an in-memory data store commonly used for caching and fast lookups.",
    "Strength training increases muscle mass through progressive overload.",
    "A balanced diet supports overall health with proper nutrients and hydration.",
    "Machine learning models improve performance as they are exposed to more data.",
    "Containerization with Docker ensures consistent application deployment across environments.",
    "REST APIs enable communication between client and server using HTTP protocols.",
    "Indexing in databases improves query performance by reducing search time.",
    "Auto-scaling automatically adjusts compute resources based on traffic demand."
]

# Query: What protocol do applications use to communicate?
# This should match with the REST API document
query = 'which protocol does applications use to communicate'

# Generate embeddings for all documents
# Returns a list of vectors, one for each document
doc_embeddings = embedding.embed_documents(documents)

# Generate embedding for the query
query_embedding = embedding.embed_query(query)

# Calculate cosine similarity between query embedding and all document embeddings
# Returns similarity scores in range [-1, 1] where 1 is most similar
scores = cosine_similarity([query_embedding], doc_embeddings)[0]

# Find the document with highest similarity score
# sorted() returns [(index, score), ...] sorted by score
# [-1] gets the last item (highest score)
index, score = sorted(list(enumerate(scores)), key=lambda x: x[1])[-1]

# Display results
print(f"Query: '{query}'")
print(f"\nMost similar document: '{documents[index]}'")
print(f"Similarity score: {score:.4f}")