from typing import Dict
from fastapi import APIRouter
from models.ingest import RequestPayload
from service.embedding import EmbeddingService

router = APIRouter()


@router.post("/ingest")
async def ingest(payload: RequestPayload) -> Dict:
    embedding_service = EmbeddingService(
        files=payload.files,
        index_name=payload.index_name,
        vector_credentials=payload.vector_database,
    )
    documents = await embedding_service.generate_documents()
    chunks = await embedding_service.generate_chunks(documents=documents)
    await embedding_service.generate_embeddings(nodes=chunks)
    return {"success": True}