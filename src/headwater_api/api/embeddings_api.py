"""
Client for interacting with the Curator service.
"""

from headwater_api.api.base_api import BaseAPI
from headwater_api.classes import (
    EmbeddingsRequest,
    EmbeddingsResponse,
)


class EmbeddingsAPI(BaseAPI):
    def generate_embeddings(
        self,
        request: EmbeddingsRequest,
    ) -> EmbeddingsResponse:
        """
        Generate embeddings using the server.
        """
        method = "POST"
        endpoint = "/conduit/embeddings"
        json_payload = request.model_dump_json()
        response = self._request(method, endpoint, json_payload=json_payload)
        return EmbeddingsResponse.model_validate_json(response)
