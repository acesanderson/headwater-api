"""
Client for interacting with the Conduit service.
ConduitAPI is defined, as a mixin.
We define ConduitClient at the bottom of the file, combining API with HeadwaterTransport.
"""

from headwater_api.classes import (
    ConduitRequest,
    ConduitResponse,
    BatchRequest,
    BatchResponse,
    ConduitError,
)
from headwater_api.transport.headwater_transport import HeadwaterTransport


class ConduitAPI:
    def query_sync(self, request: ConduitRequest) -> ConduitResponse | ConduitError:
        """Send a synchronous query to the server"""
        method = "POST"
        endpoint = "/conduit/sync"
        json_payload = request.model_dump_json()
        response = self._request(method, endpoint, json_payload=json_payload)
        try:
            return ConduitResponse.model_validate_json(response)
        except Exception as e:
            try:
                return ConduitError.model_validate_json(response)
            except Exception as e:
                raise ValueError(
                    "Response could not be validated as ConduitResponse or ConduitError"
                ) from e

    def query_async(self, batch: BatchRequest) -> BatchResponse:
        """Send an asynchronous batch query to the server"""
        method = "POST"
        endpoint = "/conduit/async"
        json_payload = batch.model_dump_json()
        response = self._request(method, endpoint, json_payload=json_payload)
        return BatchResponse.model_validate_json(response)


class ConduitClient(HeadwaterTransport, ConduitAPI):
    pass
