from headwater_api.client.headwater_client import HeadwaterClient
from headwater_api.classes import CuratorRequest, CuratorResponse


def test_headwater_client_initialization():
    hc = HeadwaterClient()
    assert hc is not None
    assert isinstance(hc, HeadwaterClient)
    status = hc.get_status()
    print(status)


def test_curator():
    curator_request = CuratorRequest(
        query_string="sexual harassment in the workplace",
    )
    hc = HeadwaterClient()
    curator_response: CuratorResponse = hc.curate(curator_request)
    assert curator_response is not None
    assert isinstance(curator_response, CuratorResponse)
    print(curator_response)


if __name__ == "__main__":
    test_headwater_client_initialization()
    test_curator()
