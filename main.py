from ingestion.loader import load_source
from chunking.chunker import chunk_files

if __name__ == "__main__":

    source_type = input("Enter source type (local/github/zip): ")
    source_value = input("Enter path or URL: ")

    files = load_source(source_type, source_value)

    print("Total files:", len(files))

    chunks = chunk_files(files)

    print("Chunks:", len(chunks))

    for c in chunks[:3]:
        print("\n--- CHUNK ---")
        print(c["file_path"])
        print(c["content"][:200])