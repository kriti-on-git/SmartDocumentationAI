import hashlib

from ingestion.markdown_loader import load_documents
from ingestion.chunker import chunk_document

from services.embedding_service import embedding_service
from db.vector_store import vector_store


def hash_text(text: str):

    return hashlib.md5(text.encode()).hexdigest()


def ingest():

    docs = load_documents()

    all_chunks = []
    seen_hashes = set()

    for doc in docs:

        chunks = chunk_document(doc)

        for c in chunks:

            h = hash_text(c["text"])

            if h in seen_hashes:
                continue

            seen_hashes.add(h)
            c["id"] = h
            all_chunks.append(c)

    texts = [c["text"] for c in all_chunks]

    embeddings = embedding_service.embed(texts)

    vector_store.upsert(embeddings, all_chunks)

    print(f"Ingested {len(all_chunks)} chunks")