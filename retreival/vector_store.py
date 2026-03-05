import os
import faiss
import pickle
import numpy as np

class VectorStore:

    def __init__(self, dim):
        self.index = faiss.IndexFlatL2(dim)
        self.metadata = []

    def add_embeddings(self, embeddings, chunks):
        self.index.add(np.array(embeddings))
        self.metadata.extend(chunks)

    def search(self, query_embedding, k=5):
        distances, indices = self.index.search(query_embedding, k)
        results = []
        for i in indices[0]:
            results.append(self.metadata[i])
        return results
    
    def save(self, path="storage"):
        os.makedirs(path, exist_ok=True)
        faiss.write_index(self.index, f"{path}/faiss.index")
        with open(f"{path}/metadata.pkl", "wb") as f:
            pickle.dump(self.metadata, f)

    def load(self, path="storage"):
        self.index = faiss.read_index(f"{path}/faiss.index")
        with open(f"{path}/matadata.pkl", "rb") as f:
            self.metadata = pickle.load(f)