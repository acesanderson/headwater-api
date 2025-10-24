"""
Main client for interacting with Headwater APIs.
Usage:
```python
from headwater_api.headwater_client import HeadwaterClient
client = HeadwaterClient()
response = client.conduit.query_sync(request)
embeddings = client.embeddings.generate_embeddings(request)
curated_courses = client.curator.curate(request)
```
"""

from headwater_api.api.conduit_api import ConduitAPI
from headwater_api.api.curator_api import CuratorAPI
from headwater_api.api.embeddings_api import EmbeddingsAPI
from headwater_api.transport.headwater_transport import HeadwaterTransport


class HeadwaterClient:
    def __init__(self):
        self._transport = HeadwaterTransport()
        self.conduit = ConduitAPI(self._transport)
        self.curator = CuratorAPI(self._transport)
        self.embeddings = EmbeddingsAPI(self._transport)
