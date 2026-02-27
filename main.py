from ingestion.loader import load_source
from chunking.chunker import chunk_files
from embeddings.embedder import generate_embeddings
from retreival.vector_store import VectorStore

if __name__ == "__main__":

    source_type = input("Enter source type (local/github/zip): ")
    source_value = input("Enter path or URL: ")

    files = load_source(source_type, source_value)

    chunks = chunk_files(files)

    print("Total chunks:", len(chunks))

    embeddings = generate_embeddings(chunks)

    dim = len(embeddings[0])

    vector_store = VectorStore(dim)

    vector_store.add_embeddings(embeddings, chunks)

    print("Vector DB created!")

    query = input("\nAsk about the repo: ")

    query_embedding = generate_embeddings(
        [{"content": query}]
    )

    results = vector_store.search(query_embedding)

    print("\nTop results:\n")

    for r in results:
        print(r["file_path"])
        print(r["content"][:200])
        print("-----")