from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct

from app.config import settings


class VectorStore:

    def __init__(self):

        self.client = QdrantClient(
            host=settings.QDRANT_HOST,
            port=settings.QDRANT_PORT
        )

        self.collection = settings.QDRANT_COLLECTION

        self._create_collection()

    def _create_collection(self):

        collections = [c.name for c in self.client.get_collections().collections]

        if self.collection not in collections:

            self.client.create_collection(
                collection_name=self.collection,
                vectors_config=VectorParams(size=384, distance=Distance.COSINE)
            )

    def upsert(self, vectors, payloads):

     points = []

     for i, vector in enumerate(vectors):

        payload = payloads[i]

        points.append(
            PointStruct(
                id=payload["id"],
                vector=vector,
                payload=payload
            )
        )

     self.client.upsert(
        collection_name=self.collection,
        points=points
     )

    def search(self, vector, limit):

        results=self.client.query_points(
            collection_name=self.collection,
            query=vector,
            limit=limit
        )
        return results.points


vector_store = VectorStore()