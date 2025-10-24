from headwater_api.clients.curator_client import CuratorClient
from headwater_api.classes import CuratorRequest, CuratorResponse


def test_curator():
    curator_request = CuratorRequest(
        query_string="sexual harassment in the workplace",
    )
    cc = CuratorClient()
    curator_response: CuratorResponse = cc.curate(curator_request)
    assert curator_response is not None
    assert isinstance(curator_response, CuratorResponse)
    print(curator_response)
