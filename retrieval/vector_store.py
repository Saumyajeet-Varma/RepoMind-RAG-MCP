import faiss
import numpy as np

class VectorStore:

    def __init__(self, dim):
        self.index = faiss.IndexFlatL2(dim)
        self.metadata = []

    def add_embeddings(self, embeddings, chunks):
        self.index.add(np.array(embeddings))
        self.metadata.extend(chunks)

    def search(self, query_embedding, k=5):
        distances, indices = self.index.serach(query_embedding, k)
        results = []
        for i in indices[0]:
            results.append(self.metadata[i])
        return results