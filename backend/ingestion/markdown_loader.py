from pathlib import Path
from typing import List, Dict
from app.config import settings


def load_documents() -> List[Dict]:

    docs = []
    base_path = Path(settings.DOCS_PATH)

    for file in base_path.rglob("*"):

        if file.suffix not in [".md", ".typ"]:
            continue

        with open(file, "r", encoding="utf-8") as f:
            content = f.read()

        docs.append({
            "content": content,
            "path": str(file),
            "filename": file.name,
            "type": file.suffix
        })

    return docs