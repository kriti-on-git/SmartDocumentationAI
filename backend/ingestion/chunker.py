import re
from typing import List, Dict
from app.config import settings


def chunk_document(doc: Dict) -> List[Dict]:

    text = doc["content"]

    sections = re.split(r"(#{1,6} .+)", text)

    chunks = []
    current_heading = "root"

    for part in sections:

        if part.startswith("#"):
            current_heading = part.strip()
            continue

        words = part.split()

        for i in range(0, len(words), settings.CHUNK_SIZE):

            chunk_text = " ".join(
                words[i:i + settings.CHUNK_SIZE]
            )

            chunks.append({
                "text": chunk_text,
                "heading": current_heading,
                "source": doc["filename"],
                "path": doc["path"],
                "type": doc["type"]
            })

    return chunks