# Headwater API Python Client

A Python client for interacting with the Headwater API, providing methods for model inference, data synthesis, embeddings generation, and content curation.

## Quick Start

This guide assumes you have access to a running Headwater API server instance.

**1. Install Dependencies**

This client requires the `requests` and `pydantic` libraries.

```bash
pip install requests pydantic
```

**2. Run a Query**

The following example connects to the client and uses the `curate` endpoint to retrieve relevant items for a given query. Save this as `example.py`.

```python
from headwater_api.client import HeadwaterClient
from headwater_api.classes import CuratorRequest

# Replace with the actual URL of your Headwater API server
HEADWATER_API_URL = "http://localhost:8080"

def get_top_search_results():
    """
    Initializes the client and retrieves curated search results.
    """
    try:
        # 1. Initialize the client
        client = HeadwaterClient(base_url=HEADWATER_API_URL)

        # 2. Create a request object
        request = CuratorRequest(
            query_string="What are the latest developments in machine learning?",
            k=3  # Request the top 3 results
        )

        # 3. Call the API method
        response = client.curate(request)

        # 4. Process the response
        print("Curation successful. Top results:")
        for result in response.results:
            print(f"- ID: {result.id}, Score: {result.score:.4f}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    get_top_search_results()
```

Run the script from your terminal:

```bash
python example.py
```

Expected output:

```
Curation successful. Top results:
- ID: doc_789, Score: 0.9123
- ID: doc_123, Score: 0.8876
- ID: doc_456, Score: 0.8543
```

## Core Features Example

This example demonstrates a more complex workflow:
1.  **Check Server Status**: Ensure the API is healthy.
2.  **Generate Embeddings**: Create vector embeddings for a batch of documents.
3.  **Run Batch Inference**: Use the `conduit` service to process multiple prompts asynchronously.

```python
import os
from headwater_api.client import HeadwaterClient
from headwater_api.classes import EmbeddingsRequest, BatchRequest

# Assumes ChromaBatch is available from a shared library
# For demonstration, we'll use a mock class.
class MockChromaBatch:
    def __init__(self, documents, ids):
        self.documents = documents
        self.ids = ids
    def model_dump(self):
        return {"documents": self.documents, "ids": self.ids}

# Replace with the actual URL of your Headwater API server
HEADWATER_API_URL = os.getenv("HEADWATER_API_URL", "http://localhost:8080")

def run_full_workflow():
    """
    Demonstrates checking status, generating embeddings, and batch processing.
    """
    client = HeadwaterClient(base_url=HEADWATER_API_URL)

    try:
        # 1. Check server status
        status = client.get_status()
        print(f"Server status: {status['status']}")
        if status['status'] != 'healthy':
            print("Server is not healthy. Aborting.")
            return

        # 2. Generate embeddings for a batch of text
        print("\n--- Generating Embeddings ---")
        docs_to_embed = ["The first document.", "The second document."]
        embedding_req = EmbeddingsRequest(
            model="bge",
            batch=MockChromaBatch(documents=docs_to_embed, ids=["doc1", "doc2"])
        )
        embedding_res = client.generate_embeddings(embedding_req)
        print(f"Generated {len(embedding_res.embeddings)} embeddings.")
        print(f"Dimension of first embedding: {len(embedding_res.embeddings[0])}")

        # 3. Process multiple prompts in a single async call
        print("\n--- Running Batch Inference ---")
        batch_req = BatchRequest(
            model="claude-3-haiku",
            prompt_str="Summarize the following text: {text}",
            input_variables_list=[
                {"text": "Photosynthesis is a process used by plants."},
                {"text": "The mitochondria is the powerhouse of the cell."}
            ]
        )
        batch_res = client.query_async(batch_req)
        print("Received responses for batch request:")
        for i, res in enumerate(batch_res):
            # Assuming ConduitResponse has a 'text' attribute
            # The actual attribute may vary based on the 'conduit' library
            print(f"  Response {i+1}: {res.text[:50]}...")

    except Exception as e:
        print(f"An error occurred during the workflow: {e}")

if __name__ == "__main__":
    run_full_workflow()
```

## Installation and Setup

### Prerequisites
*   Python 3.8+
*   Access to a running Headwater API server.

### Installation
The client depends on external packages that can be installed via pip:
```bash
pip install requests pydantic
```
Internal dependencies such as `conduit`, `siphon`, and `dbclients` must be available in your Python environment.

### Client Initialization
To use the client, import and instantiate `HeadwaterClient`. The constructor requires the base URL of the Headwater API server.

```python
from headwater_api.client import HeadwaterClient

# Recommended: Use an environment variable for the URL
api_url = os.getenv("HEADWATER_API_URL", "http://localhost:8080")

client = HeadwaterClient(base_url=api_url)
```

## API Overview

The client provides methods to interact with the three core services of the Headwater API.

| Service   | Client Methods                         | Purpose                                      |
|-----------|----------------------------------------|----------------------------------------------|
| **Curator** | `curate()`                             | Information retrieval and result curation.   |
| **Conduit** | `query_sync()`, `query_async()`, `generate_embeddings()` | Synchronous and asynchronous model inference. |
| **Siphon**  | `generate_synthetic_data()`            | Generation of complex synthetic datasets.    |

### Basic Usage

#### Curator: Information Retrieval
Use `curate` to perform a search or retrieval task.

```python
from headwater_api.classes import CuratorRequest

request = CuratorRequest(query_string="Benefits of unit testing")
response = client.curate(request)
# response is a CuratorResponse object with a list of results
```

#### Conduit: Batch Inference
Use `query_async` for efficient, parallel processing of multiple prompts.

```python
from headwater_api.classes import BatchRequest

request = BatchRequest(
    model="gpt-4-turbo",
    prompt_strings=[
        "What is the capital of France?",
        "Translate 'hello' to Spanish."
    ]
)
responses = client.query_async(request)
# responses is a list of ConduitResponse or ConduitError objects
```

#### Error Handling
API errors are raised as a `HeadwaterServerException`. This exception contains a `server_error` attribute, which is a `HeadwaterServerError` Pydantic model providing detailed information about the failure, including `error_type`, `message`, and `status_code`.

```python
from headwater_api.classes import HeadwaterServerException

try:
    # Make a request that might fail
    client.curate(CuratorRequest(query_string=""))
except HeadwaterServerException as e:
    print(f"API Error: {e.server_error.error_type}")
    print(f"Message: {e.server_error.message}")
    if e.server_error.validation_errors:
        print("Details:", e.server_error.validation_errors)
```
