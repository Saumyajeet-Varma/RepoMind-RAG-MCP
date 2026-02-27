from sentence_transformers import SentenceTransformer
from config.settings import EMBEDDING_MODEL

model = SentenceTransformer(EMBEDDING_MODEL)

def generate_embeddings(chunks):

    text = [chunk["content"] for chunk in chunks]

    embeddings = model.encode(text)

    return embeddings