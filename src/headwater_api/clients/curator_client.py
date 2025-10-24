"""
Client for interacting with the Curator service.
CuratorAPI is defined, as a mixin.
We define CuratorClient at the bottom of the file, combining CuratorAPI with HeadwaterTransport.
"""

from headwater_api.classes import (
    CuratorRequest,
    CuratorResponse,
)
from headwater_api.transport.headwater_transport import HeadwaterTransport


class CuratorAPI:
    def curate(self, request: CuratorRequest) -> CuratorResponse:
        """
        Curate items using the server.
        """
        method = "POST"
        endpoint = "/curator/curate"
        response_json = request.model_dump_json()
        response = self._request(method, endpoint, json_payload=response_json)
        return CuratorResponse.model_validate_json(response)


class CuratorClient(CuratorAPI, HeadwaterTransport):
    pass
