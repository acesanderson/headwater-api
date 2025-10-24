from pydantic import BaseModel, Field
from conduit.result.response import Response as ConduitResponse
from conduit.result.error import ConduitError


# Async
class BatchResponse(BaseModel):
    """Response model for batch processing"""

    results: list[ConduitResponse | ConduitError] = Field(
        ..., description="List of results for each input"
    )


# Embeddings
class EmbeddingsResponse(BaseModel):
    """Response model for embeddings generation"""

    embeddings: list[list[float]] = Field(
        ..., description="List of generated embeddings"
    )


__all__ = ["EmbeddingsResponse", "ConduitResponse", "ConduitError"]
