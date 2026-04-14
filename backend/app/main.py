from fastapi import FastAPI

from api.routes import router
from app.config import settings


app = FastAPI(title=settings.APP_NAME)

app.include_router(router, prefix=settings.API_V1_PREFIX)
@router.get("/docs/{path:path}")
def get_doc(path: str):

    with open(f"./docs/{path}.md", "r") as f:
        return f.read()