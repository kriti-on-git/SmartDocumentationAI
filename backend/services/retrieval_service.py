from services.embedding_service import embedding_service
from db.vector_store import vector_store
from app.config import settings


class RetrievalService:

    def retrieve(self, query):

        query_vector = embedding_service.embed([query])[0]

        results = vector_store.search(
            query_vector,
            settings.TOP_K
        )

        contexts = []

        for r in results:

            payload = r.payload

            contexts.append({
                "text": payload["text"],
                "source": payload["source"],
                "heading": payload.get("heading", "")
            })

        return contexts


retrieval_service = RetrievalService()