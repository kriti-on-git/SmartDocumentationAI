import requests
from services.retrieval_service import retrieval_service
from app.config import settings


class RAGService:

    def build_prompt(self, query, contexts):

        context_block = "\n\n".join([
            f"[{c['source']} - {c['heading']}]\n{c['text']}"
            for c in contexts
        ])

        return f"""
You are a senior developer documentation assistant.

Rules:
- Answer ONLY from provided context
- If unsure, say "Not found in docs"
- Be precise and technical

Context:
{context_block}

Question:
{query}

Answer:
"""

    def generate(self, query):

        contexts = retrieval_service.retrieve(query)

        prompt = self.build_prompt(query, contexts)

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": settings.LLM_MODEL,
                "prompt": prompt,
                "stream": False
            }
        )

        return response.json()["response"]


rag_service = RAGService()


def store_interaction(self, query, answer):
    # later: store in DB / fine-tune dataset
    with open("learning_log.txt", "a") as f:
        f.write(f"Q: {query}\nA: {answer}\n\n")
