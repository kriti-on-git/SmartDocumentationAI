from fastapi import APIRouter

from api.schemas import QueryRequest, QueryResponse
from services.rag_service import rag_service


router = APIRouter()


@router.post("/ask", response_model=QueryResponse)
def ask_docs(request: QueryRequest):

    answer = rag_service.generate(request.question)

    return {"answer": answer}