def chunk_files(files, chunk_size=500):

    chunks = []
    
    for file in files:

        path = file["path"]
        content = file["content"]

        start = 0
        chunk_id = 0

        while start < len(content):

            chunk = content[start:start+chunk_size]

            chunks.append({
                "file_path": path,
                "chunk_id": chunk_id,
                "content": chunk
            })

            start += chunk_size
            chunk_id += 1
    
    return chunks