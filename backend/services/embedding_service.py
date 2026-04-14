from sentence_transformers import SentenceTransformer
from app.config import settings


class EmbeddingService:

    def __init__(self):

        self.model = SentenceTransformer(settings.EMBEDDING_MODEL)

    def embed(self, texts):

        return self.model.encode(texts).tolist()


embedding_service = EmbeddingService()