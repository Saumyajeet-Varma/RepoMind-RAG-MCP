from ingestion.loader import load_source

if __name__ == "__main__":

    source_type = input("Enter source type (local/github/zip): ")
    source_value = input("Enter path or URL: ")

    files = load_source(source_type, source_value)

    print("Total files:", len(files))

    for f in files[:5]:
        print(f["path"])