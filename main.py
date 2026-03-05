import os
from ingestion.loader import load_source
from chunking.chunker import chunk_files
from embeddings.embedder import generate_embeddings
from retreival.vector_store import VectorStore
from query.engine import generate_answer

STORAGE_DIR = "storage"

def build_index():
    
    source_type = input("Enter source type (local/github/zip): ")
    source_value = input("Enter path or URL: ")

    files = load_source(source_type, source_value)

    chunks = chunk_files(files)

    print("Total chunks:", len(chunks))

    embeddings = generate_embeddings(chunks)

    dim = len(embeddings[0])

    vector_store = VectorStore(dim)

    vector_store.add_embeddings(embeddings, chunks)

    vector_store.save(STORAGE_DIR)

    print("Index built and saved!")

def load_index():

    vector_store = VectorStore(384)

    vector_store.load(STORAGE_DIR)

    print("Index loaded!")

    return vector_store

if __name__ == "__main__":

    if not os.path.exists("storage/faiss.index"):
        build_index()

    vector_store = load_index()

    while True:

        query = input("\nAsk RepoMind: ")

        query_embedding = generate_embeddings([{"content": query}])

        results = vector_store.search(query_embedding)

        answer = generate_answer(query, results)

        print("\nRepoMind:\n", answer)