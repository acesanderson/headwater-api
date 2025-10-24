from headwater_api.clients.conduit_client import ConduitClient
from headwater_api.classes import ConduitRequest, ConduitResponse
from conduit.message.textmessage import TextMessage


def test_conduit_sync_client():
    message = TextMessage(role="user", content="name three birds")
    messages = [message]
    request = ConduitRequest(messages=messages, model="gpt-oss:latest")
    client = ConduitClient()
    response = client.query_sync(request=request)
    assert isinstance(response, ConduitResponse)
    assert len(str(response.content)) > 0
    print(str(response.content))
