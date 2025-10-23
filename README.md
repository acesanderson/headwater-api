✓ gemini-2.5-pro-preview-05-06 | [0/0]  | (39.8s)

╭─ ✓ FULL CONVERSATION 39.8s ──────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ User: You are an expert technical writer tasked with creating an exceptional README.md file for a GitHub project. Your goal is to    │
│ create documentation that serves as an effective front door to the codebase, answering key visitor questions within seconds while    │
│ maintaining conciseness and clarity.                                                                                                 │
│                                                                                                                                      │
│ ## Step 1: Codebase Analysis                                                                                                         │
│                                                                                                                                      │
│ First, systematically analyze the project structure:                                                                                 │
│                                                                                                                                      │
│ - **Identify entry points**: Main files, package.json, setup.py, Cargo.toml, etc.                                                    │
│ - **Map project architecture**: Understand how major components interact                                                             │
│ - **Detect project type**: CLI tool, library, web service, framework, or application                                                 │
│ - **Analyze dependencies**: Key technologies and frameworks used                                                                     │
│ - **Review existing documentation**: Build upon or replace existing README content                                                   │
│ - **Examine test structure**: Understand testing approach and examples                                                               │
│ - **Check configuration files**: Docker, CI/CD, environment setup requirements                                                       │
│                                                                                                                                      │
│ Then create a README that includes these essential elements, prioritized by importance:                                              │
│                                                                                                                                      │
│ ### Must-Have (Top Priority)                                                                                                         │
│ 1. **Project Identity** (30-second test)                                                                                             │
│    - Clear, descriptive title                                                                                                        │
│    - One-sentence value proposition                                                                                                  │
│                                                                                                                                      │
│ 2. **Quick Start** (One-click rule)                                                                                                  │
│    - Single command installation                                                                                                     │
│    - Minimal working example that demonstrates core functionality                                                                    │
│    - Copy-pasteable code that runs successfully                                                                                      │
│                                                                                                                                      │
│ 3. **Core Value Demonstration**                                                                                                      │
│    - One powerful example showing 3-4 key features                                                                                   │
│    - Real-world use case, not "Hello World"                                                                                          │
│                                                                                                                                      │
│ ### Should-Have (Secondary Priority)                                                                                                 │
│ 4. **Architecture Overview** (for complex projects)                                                                                  │
│    - High-level component interaction                                                                                                │
│    - Visual diagram if helpful                                                                                                       │
│    - Key concepts/terminology                                                                                                        │
│                                                                                                                                      │
│ 5. **Installation & Setup**                                                                                                          │
│    - Prerequisites clearly stated                                                                                                    │
│    - Multiple installation methods if relevant                                                                                       │
│    - Environment setup requirements                                                                                                  │
│                                                                                                                                      │
│ 6. **Basic Usage**                                                                                                                   │
│    - Essential commands/API calls                                                                                                    │
│    - Common configuration options                                                                                                    │
│    - Expected outputs                                                                                                                │
│                                                                                                                                      │
│ ## Step 4: Apply Conciseness Strategies                                                                                              │
│                                                                                                                                      │
│ - **Progressive disclosure**: Keep main README to 2-3 screens, link to detailed docs                                                 │
│ - **Visual shortcuts**: Use diagrams, tables, and screenshots over prose                                                             │
│ - **Smart linking**: Reference external documentation instead of explaining everything                                               │
│ - **Ruthless editing**: Remove anything not essential for first successful use                                                       │
│ - **Consolidate examples**: One comprehensive example vs. multiple small ones                                                        │
│                                                                                                                                      │
│ ## Step 5: Technology-Specific Considerations                                                                                        │
│                                                                                                                                      │
│ Adapt your approach based on the technology stack:                                                                                   │
│                                                                                                                                      │
│ - **Node.js**: Emphasize npm installation, package.json scripts                                                                      │
│ - **Python**: Highlight pip installation, virtual environments, requirements                                                         │
│ - **Go**: Focus on go get, module structure                                                                                          │
│ - **Rust**: Cargo installation, feature flags                                                                                        │
│ - **Docker**: Container usage, compose files                                                                                         │
│ - **Web frameworks**: Local development, deployment options                                                                          │
│                                                                                                                                      │
│ ## Step 6: Voice & Tone Guidelines                                                                                                   │
│                                                                                                                                      │
│ Match your writing style to the project:                                                                                             │
│                                                                                                                                      │
│ - **Technical depth**: Match the complexity of your audience                                                                         │
│ - **Formality level**: Open source casual vs. enterprise professional                                                                │
│ - **Assumed knowledge**: Don't over-explain basics for expert tools                                                                  │
│                                                                                                                                      │
│ ## Step 7: Quality Validation                                                                                                        │
│                                                                                                                                      │
│ Before finalizing, ensure:                                                                                                           │
│                                                                                                                                      │
│ - [ ] Installation steps are complete and accurate                                                                                   │
│ - [ ] Examples actually run as written                                                                                               │
│ - [ ] Links are functional                                                                                                           │
│ - [ ] Quick start is genuinely quick (under 5 minutes)                                                                               │
│ - [ ] README answers "what, why, how" for the target audience                                                                        │
│ - [ ] No outdated information or broken references                                                                                   │
│ - [ ] Appropriate section headings for easy scanning                                                                                 │
│                                                                                                                                      │
│ ## Anti-Patterns to Avoid                                                                                                            │
│                                                                                                                                      │
│ - Generic boilerplate that could apply to any project                                                                                │
│ - Overwhelming newcomers with advanced configuration upfront                                                                         │
│ - Multiple competing examples that confuse rather than clarify                                                                       │
│ - Outdated installation instructions or dependencies                                                                                 │
│ - Assuming too much or too little prior knowledge                                                                                    │
│ - Making users read documentation to understand what the project does                                                                │
│                                                                                                                                      │
│ ## Output Format                                                                                                                     │
│                                                                                                                                      │
│ Structure your README using standard markdown with:                                                                                  │
│ - Clear hierarchical headings (##, ###)                                                                                              │
│ - Code blocks with appropriate syntax highlighting                                                                                   │
│ - Tables for configuration options                                                                                                   │
│ - Badges at the top for key metrics                                                                                                  │
│ - Table of contents for longer documents                                                                                             │
│                                                                                                                                      │
│ Remember: A great README gets someone from discovery to first success with minimal friction while making deeper information easily   │
│ accessible. Focus on the user's journey, not comprehensive documentation.                                                            │
│                                                                                                                                      │
│ ## Don't be annoying!                                                                                                                │
│                                                                                                                                      │
│ DO NOT:                                                                                                                              │
│ - do not write in the first person ("I", "we")                                                                                       │
│ - do not use icons or emojis -- they're trash                                                                                        │
│ - do not use lofty or breathless or overly promotional language                                                                      │
│ - do not add a license section, or anything for contributors. This is for users only.                                                │
│ - do not add "PyPI version", "Build Status", or "Python Versions" or any kind of badges.                                             │
│                                                                                                                                      │
│ Here's the code project:                                                                                                             │
│ <code>                                                                                                                               │
│ <?xml version="1.0" ?>                                                                                                               │
│ <project name="headwater-api-project">                                                                                               │
│   <directory_tree>                                                                                                                   │
│     <directory name="headwater-api-project">                                                                                         │
│       <directory name="tests">                                                                                                       │
│         <file name="test_basic.py" path="tests/test_basic.py"/>                                                                      │
│       </directory>                                                                                                                   │
│       <directory name="src">                                                                                                         │
│         <directory name="headwater_api">                                                                                             │
│           <file name="__main__.py" path="src/headwater_api/__main__.py"/>                                                            │
│           <file name="__init__.py" path="src/headwater_api/__init__.py"/>                                                            │
│           <directory name="classes">                                                                                                 │
│             <file name="__init__.py" path="src/headwater_api/classes/__init__.py"/>                                                  │
│             <directory name="server_classes">                                                                                        │
│               <file name="status.py" path="src/headwater_api/classes/server_classes/status.py"/>                                     │
│               <file name="exceptions.py" path="src/headwater_api/classes/server_classes/exceptions.py"/>                             │
│             </directory>                                                                                                             │
│             <directory name="conduit_classes">                                                                                       │
│               <file name="requests.py" path="src/headwater_api/classes/conduit_classes/requests.py"/>                                │
│               <file name="responses.py" path="src/headwater_api/classes/conduit_classes/responses.py"/>                              │
│             </directory>                                                                                                             │
│             <directory name="siphon_classes">                                                                                        │
│               <file name="requests.py" path="src/headwater_api/classes/siphon_classes/requests.py"/>                                 │
│               <file name="responses.py" path="src/headwater_api/classes/siphon_classes/responses.py"/>                               │
│             </directory>                                                                                                             │
│             <directory name="curator_classes">                                                                                       │
│               <file name="requests.py" path="src/headwater_api/classes/curator_classes/requests.py"/>                                │
│               <file name="responses.py" path="src/headwater_api/classes/curator_classes/responses.py"/>                              │
│             </directory>                                                                                                             │
│           </directory>                                                                                                               │
│           <directory name="client">                                                                                                  │
│             <file name="headwater_client.py" path="src/headwater_api/client/headwater_client.py"/>                                   │
│           </directory>                                                                                                               │
│         </directory>                                                                                                                 │
│       </directory>                                                                                                                   │
│     </directory>                                                                                                                     │
│   </directory_tree>                                                                                                                  │
│   <file_contents>                                                                                                                    │
│     <file path="tests/test_basic.py">def test_sanity():                                                                              │
│     assert True                                                                                                                      │
│ </file>                                                                                                                              │
│     <file path="src/headwater_api/__main__.py">def main() -&gt; None:                                                                │
│     print("hello from headwater-api")                                                                                                │
│ if __name__ == "__main__":                                                                                                           │
│     main()                                                                                                                           │
│ </file>                                                                                                                              │
│     <file path="src/headwater_api/__init__.py">__all__ = []                                                                          │
│ </file>                                                                                                                              │
│     <file path="src/headwater_api/classes/__init__.py"># Requests                                                                    │
│ from headwater_api.classes.conduit_classes.requests import (                                                                         │
│     ConduitRequest,                                                                                                                  │
│     BatchRequest,                                                                                                                    │
│     EmbeddingsRequest,                                                                                                               │
│ )                                                                                                                                    │
│ from headwater_api.classes.siphon_classes.requests import (                                                                          │
│     SyntheticDataRequest,                                                                                                            │
│ )                                                                                                                                    │
│ from headwater_api.classes.curator_classes.requests import (                                                                         │
│     CuratorRequest,                                                                                                                  │
│ )                                                                                                                                    │
│                                                                                                                                      │
│ # Responses                                                                                                                          │
│ from headwater_api.classes.conduit_classes.responses import (                                                                        │
│     ConduitResponse,                                                                                                                 │
│     ConduitError,                                                                                                                    │
│     EmbeddingsResponse,                                                                                                              │
│ )                                                                                                                                    │
│ from headwater_api.classes.curator_classes.responses import (                                                                        │
│     CuratorResponse,                                                                                                                 │
│ )                                                                                                                                    │
│ from headwater_api.classes.siphon_classes.responses import (                                                                         │
│     SyntheticData,                                                                                                                   │
│ )                                                                                                                                    │
│                                                                                                                                      │
│ # Server                                                                                                                             │
│ from headwater_api.classes.server_classes.exceptions import (                                                                        │
│     HeadwaterServerError,                                                                                                            │
│     HeadwaterServerException,                                                                                                        │
│ )                                                                                                                                    │
│ from headwater_api.classes.server_classes.status import StatusResponse                                                               │
│                                                                                                                                      │
│ __all__ = [                                                                                                                          │
│     # Requests                                                                                                                       │
│     "ConduitRequest",                                                                                                                │
│     "BatchRequest",                                                                                                                  │
│     "EmbeddingsRequest",                                                                                                             │
│     "SyntheticDataRequest",                                                                                                          │
│     "CuratorRequest",                                                                                                                │
│     # Responses                                                                                                                      │
│     "ConduitResponse",                                                                                                               │
│     "ConduitError",                                                                                                                  │
│     "EmbeddingsResponse",                                                                                                            │
│     "SyntheticData",                                                                                                                 │
│     "CuratorResponse",                                                                                                               │
│     # Server                                                                                                                         │
│     "HeadwaterServerError",                                                                                                          │
│     "HeadwaterServerException",                                                                                                      │
│     "StatusResponse",                                                                                                                │
│ ]                                                                                                                                    │
│ </file>                                                                                                                              │
│     <file path="src/headwater_api/classes/server_classes/status.py">from pydantic import BaseModel, Field                            │
│                                                                                                                                      │
│                                                                                                                                      │
│ # Status                                                                                                                             │
│ class StatusResponse(BaseModel):                                                                                                     │
│     """Server status response"""                                                                                                     │
│                                                                                                                                      │
│     status: str = Field(                                                                                                             │
│         ..., description="Server status: 'healthy', 'degraded', 'error'"                                                             │
│     )                                                                                                                                │
│     message: str = Field(..., description="Status message")                                                                          │
│     models_available: list[str] = Field(..., description="Available models by provider")                                             │
│     gpu_enabled: bool = Field(..., description="Whether GPU acceleration is available")                                              │
│     uptime: float | None = Field(None, description="Server uptime in seconds")                                                       │
│ </file>                                                                                                                              │
│     <file path="src/headwater_api/classes/server_classes/exceptions.py">from pydantic import BaseModel, Field                        │
│ from typing import Any                                                                                                               │
│ from enum import Enum                                                                                                                │
│ import traceback                                                                                                                     │
│ import time                                                                                                                          │
│                                                                                                                                      │
│                                                                                                                                      │
│ class ErrorType(str, Enum):                                                                                                          │
│     VALIDATION_ERROR = "validation_error"                                                                                            │
│     PYDANTIC_VALIDATION = "pydantic_validation"                                                                                      │
│     DATA_VALIDATION = "data_validation"                                                                                              │
│     MODEL_NOT_FOUND = "model_not_found"                                                                                              │
│     BATCH_SIZE_EXCEEDED = "batch_size_exceeded"                                                                                      │
│     INVALID_REQUEST = "invalid_request"                                                                                              │
│     INTERNAL_ERROR = "internal_error"                                                                                                │
│     TIMEOUT_ERROR = "timeout_error"                                                                                                  │
│     DEPENDENCY_ERROR = "dependency_error"                                                                                            │
│                                                                                                                                      │
│                                                                                                                                      │
│ class HeadwaterServerError(BaseModel):                                                                                               │
│     """Centralized error response format for HeadwaterServer"""                                                                      │
│                                                                                                                                      │
│     # Core error info                                                                                                                │
│     error_type: ErrorType                                                                                                            │
│     message: str                                                                                                                     │
│     status_code: int = Field(ge=100, le=599)                                                                                         │
│                                                                                                                                      │
│     # Request context                                                                                                                │
│     path: str | None = None                                                                                                          │
│     method: str | None = None                                                                                                        │
│     request_id: str | None = None                                                                                                    │
│     timestamp: float = Field(default_factory=time.time)                                                                              │
│                                                                                                                                      │
│     # Detailed error information                                                                                                     │
│     validation_errors: list[dict[str, Any]] | None = None                                                                            │
│     original_exception: str | None = None                                                                                            │
│     traceback: str | None = None                                                                                                     │
│                                                                                                                                      │
│     # Additional context                                                                                                             │
│     context: dict[str, Any] | None = Field(default_factory=dict)                                                                     │
│                                                                                                                                      │
│     @classmethod                                                                                                                     │
│     def from_validation_error(                                                                                                       │
│         cls, exc, request=None, include_traceback: bool = False                                                                      │
│     ) -&gt; "HeadwaterServerError":                                                                                                  │
│         """Create error from Pydantic ValidationError"""                                                                             │
│         return cls(                                                                                                                  │
│             error_type=ErrorType.PYDANTIC_VALIDATION,                                                                                │
│             message="Request validation failed",                                                                                     │
│             status_code=422,                                                                                                         │
│             path=str(request.url.path) if request else None,                                                                         │
│             method=request.method if request else None,                                                                              │
│             request_id=getattr(request.state, "request_id", None) if request else None,                                              │
│             validation_errors=exc.errors() if hasattr(exc, "errors") else None,                                                      │
│             original_exception=str(exc),                                                                                             │
│             traceback=traceback.format_exc() if include_traceback else None,                                                         │
│         )                                                                                                                            │
│                                                                                                                                      │
│     @classmethod                                                                                                                     │
│     def from_http_exception(                                                                                                         │
│         cls, exc, request=None, error_type: ErrorType = ErrorType.INTERNAL_ERROR                                                     │
│     ) -&gt; "HeadwaterServerError":                                                                                                  │
│         """Create error from HTTPException"""                                                                                        │
│         return cls(                                                                                                                  │
│             error_type=error_type,                                                                                                   │
│             message=str(exc.detail) if hasattr(exc, "detail") else str(exc),                                                         │
│             status_code=getattr(exc, "status_code", 500),                                                                            │
│             path=str(request.url.path) if request else None,                                                                         │
│             method=request.method if request else None,                                                                              │
│             request_id=getattr(request.state, "request_id", None) if request else None,                                              │
│             original_exception=str(exc),                                                                                             │
│         )                                                                                                                            │
│                                                                                                                                      │
│     @classmethod                                                                                                                     │
│     def from_general_exception(                                                                                                      │
│         cls,                                                                                                                         │
│         exc: Exception,                                                                                                              │
│         request=None,                                                                                                                │
│         status_code: int = 500,                                                                                                      │
│         include_traceback: bool = True,                                                                                              │
│     ) -&gt; "HeadwaterServerError":                                                                                                  │
│         """Create error from any exception"""                                                                                        │
│         return cls(                                                                                                                  │
│             error_type=ErrorType.INTERNAL_ERROR,                                                                                     │
│             message=f"Internal server error: {str(exc)}",                                                                            │
│             status_code=status_code,                                                                                                 │
│             path=str(request.url.path) if request else None,                                                                         │
│             method=request.method if request else None,                                                                              │
│             request_id=getattr(request.state, "request_id", None) if request else None,                                              │
│             original_exception=str(exc),                                                                                             │
│             traceback=traceback.format_exc() if include_traceback else None,                                                         │
│             context={"exception_type": type(exc).__name__},                                                                          │
│         )                                                                                                                            │
│                                                                                                                                      │
│     def add_context(self, key: str, value: Any) -&gt; "HeadwaterServerError":                                                        │
│         """Add additional context information"""                                                                                     │
│         if self.context is None:                                                                                                     │
│             self.context = {}                                                                                                        │
│         self.context[key] = value                                                                                                    │
│         return self                                                                                                                  │
│                                                                                                                                      │
│                                                                                                                                      │
│ class HeadwaterServerException(Exception):                                                                                           │
│     """Client-side exception wrapping SiphonServerError"""                                                                           │
│                                                                                                                                      │
│     def __init__(self, server_error: HeadwaterServerError):                                                                          │
│         self.server_error: HeadwaterServerError = server_error                                                                       │
│         super().__init__(server_error.message)                                                                                       │
│                                                                                                                                      │
│     def __str__(self):                                                                                                               │
│         return (                                                                                                                     │
│             f"SiphonServer {self.server_error.error_type}: {self.server_error.message}"                                              │
│         )                                                                                                                            │
│ </file>                                                                                                                              │
│     <file path="src/headwater_api/classes/conduit_classes/requests.py">from conduit.request.request import Request as ConduitRequest │
│ from conduit.embeddings.chroma_batch import ChromaBatch                                                                              │
│ from pydantic import BaseModel, Field, model_validator                                                                               │
│                                                                                                                                      │
│                                                                                                                                      │
│ class BatchRequest(ConduitRequest):                                                                                                  │
│     """                                                                                                                              │
│     BatchRequest extends ConduitRequest to allow for multiple prompt strings or input variables.                                     │
│     This is useful for processing multiple requests in a single API call.                                                            │
│     """                                                                                                                              │
│                                                                                                                                      │
│     prompt_strings: list[str] = Field(                                                                                               │
│         default_factory=list,                                                                                                        │
│         description="List of prompt strings for each request. Prompt strings should be fully rendered.",                             │
│     )                                                                                                                                │
│     input_variables_list: list[dict[str, str]] = Field(                                                                              │
│         default_factory=list,                                                                                                        │
│         description="List of input variables for each request. Each dict should match the model's input schema.",                    │
│     )                                                                                                                                │
│     prompt_str: str | None = Field(                                                                                                  │
│         default=None, description="Single prompt string for the request."                                                            │
│     )                                                                                                                                │
│                                                                                                                                      │
│     @model_validator(mode="after")                                                                                                   │
│     def _exactly_one(                                                                                                                │
│         self,                                                                                                                        │
│     ):                                                                                                                               │
│         has_prompts = bool(self.prompt_strings)                                                                                      │
│         has_vars = bool(self.input_variables_list)                                                                                   │
│         if has_prompts == has_vars:                                                                                                  │
│             raise ValueError(                                                                                                        │
│                 "Provide exactly one of 'prompt_strings' or 'input_variables_list'."                                                 │
│             )                                                                                                                        │
│         # If input_variables_list is provided, prompt_str should have a value                                                        │
│         if has_vars and not self.prompt_str:                                                                                         │
│             raise ValueError(                                                                                                        │
│                 "If 'input_variables_list' is provided, 'prompt_str' must also be provided."                                         │
│             )                                                                                                                        │
│         return self                                                                                                                  │
│                                                                                                                                      │
│                                                                                                                                      │
│ class EmbeddingsRequest(BaseModel):                                                                                                  │
│     model: str = Field(                                                                                                              │
│         ...,                                                                                                                         │
│         description="The embedding model to use for generating embeddings.",                                                         │
│     )                                                                                                                                │
│     batch: ChromaBatch = Field(                                                                                                      │
│         ...,                                                                                                                         │
│         description="Batch of documents to generate embeddings for.",                                                                │
│     )                                                                                                                                │
│                                                                                                                                      │
│                                                                                                                                      │
│ __all__ = ["ConduitRequest", "BatchRequest", "ChromaBatch", "EmbeddingsRequest"]                                                     │
│ </file>                                                                                                                              │
│     <file path="src/headwater_api/classes/conduit_classes/responses.py">from pydantic import BaseModel, Field                        │
│ from conduit.result.response import Response as ConduitResponse                                                                      │
│ from conduit.result.error import ConduitError                                                                                        │
│                                                                                                                                      │
│                                                                                                                                      │
│ # Embeddings                                                                                                                         │
│ class EmbeddingsResponse(BaseModel):                                                                                                 │
│     """Response model for embeddings generation"""                                                                                   │
│                                                                                                                                      │
│     embeddings: list[list[float]] = Field(                                                                                           │
│         ..., description="List of generated embeddings"                                                                              │
│     )                                                                                                                                │
│                                                                                                                                      │
│                                                                                                                                      │
│ __all__ = ["EmbeddingsResponse", "ConduitResponse", "ConduitError"]                                                                  │
│ </file>                                                                                                                              │
│     <file path="src/headwater_api/classes/siphon_classes/requests.py">from pydantic import BaseModel, model_validator                │
│ from siphon.context.context_classes import ContextUnion                                                                              │
│                                                                                                                                      │
│                                                                                                                                      │
│ class SyntheticDataRequest(BaseModel):                                                                                               │
│     context: ContextUnion                                                                                                            │
│     model: str = "gemini2.5"                                                                                                         │
│                                                                                                                                      │
│     @model_validator(mode="before")                                                                                                  │
│     @classmethod                                                                                                                     │
│     def deserialize_context(cls, data):                                                                                              │
│         if isinstance(data, dict) and "context" in data:                                                                             │
│             context_data = data["context"]                                                                                           │
│             if isinstance(context_data, dict):                                                                                       │
│                 # Reconstruct the right context class                                                                                │
│                 from siphon.context.context_classes import ContextClasses                                                            │
│                                                                                                                                      │
│                 sourcetype_value = context_data.get("sourcetype")                                                                    │
│                                                                                                                                      │
│                 for context_class in ContextClasses:                                                                                 │
│                     if (                                                                                                             │
│                         context_class.__name__.replace("Context", "")                                                                │
│                         == sourcetype_value                                                                                          │
│                     ):                                                                                                               │
│                         data["context"] = context_class.model_validate(context_data)                                                 │
│                         break                                                                                                        │
│         return data                                                                                                                  │
│ </file>                                                                                                                              │
│     <file path="src/headwater_api/classes/siphon_classes/responses.py">from siphon.data.synthetic_data import SyntheticData          │
│                                                                                                                                      │
│ __all__ = ["SyntheticData"]                                                                                                          │
│ </file>                                                                                                                              │
│     <file path="src/headwater_api/classes/curator_classes/requests.py">from pydantic import BaseModel, Field                         │
│                                                                                                                                      │
│                                                                                                                                      │
│ class CuratorRequest(BaseModel):                                                                                                     │
│     # Mandatory fields                                                                                                               │
│     query_string: str = Field(..., description="The query string for retrieval.")                                                    │
│     # Optional fields with defaults                                                                                                  │
│     k: int = Field(default=5, description="Number of top documents to retrieve.")                                                    │
│     n_results: int = Field(                                                                                                          │
│         default=30, description="Total number of results to consider."                                                               │
│     )                                                                                                                                │
│     model_name: str = Field(                                                                                                         │
│         default="bge", description="The embedding model to use for retrieval."                                                       │
│     )                                                                                                                                │
│     cached: bool = Field(default=True, description="Whether to use cached results.")                                                 │
│ </file>                                                                                                                              │
│     <file path="src/headwater_api/classes/curator_classes/responses.py">from pydantic import BaseModel, Field                        │
│                                                                                                                                      │
│                                                                                                                                      │
│ # Curator                                                                                                                            │
│ class CuratorResult(BaseModel):                                                                                                      │
│     id: str = Field(..., description="Unique identifier for the curated item")                                                       │
│     score: float = Field(..., description="Curation score for the item")                                                             │
│                                                                                                                                      │
│                                                                                                                                      │
│ class CuratorResponse(BaseModel):                                                                                                    │
│     results: list[CuratorResult] = Field(                                                                                            │
│         ..., description="List of curation results with IDs and scores"                                                              │
│     )                                                                                                                                │
│ </file>                                                                                                                              │
│     <file path="src/headwater_api/client/headwater_client.py">from headwater_api.classes import (                                    │
│     ConduitRequest,                                                                                                                  │
│     BatchRequest,                                                                                                                    │
│     EmbeddingsRequest,                                                                                                               │
│     SyntheticDataRequest,                                                                                                            │
│     CuratorRequest,                                                                                                                  │
│     ConduitResponse,                                                                                                                 │
│     ConduitError,                                                                                                                    │
│     EmbeddingsResponse,                                                                                                              │
│     SyntheticData,                                                                                                                   │
│     CuratorResponse,                                                                                                                 │
│     HeadwaterServerError,                                                                                                            │
│     HeadwaterServerException,                                                                                                        │
│     StatusResponse,                                                                                                                  │
│ )                                                                                                                                    │
│                                                                                                                                      │
│ # Other imports                                                                                                                      │
│ from dbclients import get_network_context                                                                                            │
│ import requests                                                                                                                      │
│ import logging                                                                                                                       │
│ import json                                                                                                                          │
│ import os                                                                                                                            │
│                                                                                                                                      │
│ # Set up logging                                                                                                                     │
│ log_level = int(os.getenv("PYTHON_LOG_LEVEL", "2"))  # Default to INFO                                                               │
│ levels = {1: logging.WARNING, 2: logging.INFO, 3: logging.DEBUG}                                                                     │
│ logging.basicConfig(                                                                                                                 │
│     level=levels.get(log_level, logging.INFO), format="%(levelname)s: %(message)s"                                                   │
│ )                                                                                                                                    │
│ logger = logging.getLogger(__name__)                                                                                                 │
│                                                                                                                                      │
│ # Constants                                                                                                                          │
│ HEADWATER_SERVER_DEFAULT_PORT = 8080                                                                                                 │
│ HEADWATER_SERVER_IP = get_network_context().siphon_server                                                                            │
│                                                                                                                                      │
│                                                                                                                                      │
│ class HeadwaterClient:                                                                                                               │
│     def __init__(self, base_url: str = ""):                                                                                          │
│         if base_url == "":                                                                                                           │
│             self.base_url: str = self._get_url()                                                                                     │
│         else:                                                                                                                        │
│             self.base_url = base_url.rstrip("/")                                                                                     │
│                                                                                                                                      │
│     def _get_url(self) -&gt; str:                                                                                                    │
│         """Get HeadwaterServer URL with same host detection logic as PostgreSQL"""                                                   │
│         return f"http://{HEADWATER_SERVER_IP}:{HEADWATER_SERVER_DEFAULT_PORT}"                                                       │
│                                                                                                                                      │
│     def _handle_error_response(self, response: requests.Response) -&gt; None:                                                        │
│         """Parse HeadwaterServerError from response and raise appropriate exception"""                                               │
│         try:                                                                                                                         │
│             error_data = response.json()                                                                                             │
│                                                                                                                                      │
│             # Check if it's our structured error format                                                                              │
│             if isinstance(error_data, dict) and "error_type" in error_data:                                                          │
│                 server_error = HeadwaterServerError.model_validate(error_data)                                                       │
│                                                                                                                                      │
│                 logger.error(                                                                                                        │
│                     f"Server error [{server_error.request_id}]: {server_error.error_type}"                                           │
│                 )                                                                                                                    │
│                 logger.error(f"Message: {server_error.message}")                                                                     │
│                                                                                                                                      │
│                 if server_error.validation_errors:                                                                                   │
│                     logger.error(                                                                                                    │
│                         f"Validation errors: {json.dumps(server_error.validation_errors, indent=2)}"                                 │
│                     )                                                                                                                │
│                                                                                                                                      │
│                 if server_error.context:                                                                                             │
│                     logger.error(                                                                                                    │
│                         f"Context: {json.dumps(server_error.context, indent=2)}"                                                     │
│                     )                                                                                                                │
│                                                                                                                                      │
│                 raise HeadwaterServerException(server_error)                                                                         │
│                                                                                                                                      │
│             # Fallback for non-structured errors                                                                                     │
│             logger.error(                                                                                                            │
│                 f"Non-structured error response: {json.dumps(error_data, indent=2)}"                                                 │
│             )                                                                                                                        │
│                                                                                                                                      │
│         except (json.JSONDecodeError, ValueError):                                                                                   │
│             # Raw text response                                                                                                      │
│             logger.error(f"Raw error response: {response.text}")                                                                     │
│                                                                                                                                      │
│         # Still raise the original HTTP error                                                                                        │
│         response.raise_for_status()                                                                                                  │
│                                                                                                                                      │
│     def get_status(self) -&gt; StatusResponse:                                                                                       │
│         """Get server status"""                                                                                                      │
│         response = requests.get(f"{self.base_url}/status")                                                                           │
│         response.raise_for_status()                                                                                                  │
│         return response.json()                                                                                                       │
│                                                                                                                                      │
│     def query_sync(self, request: ConduitRequest) -&gt; ConduitResponse | ConduitError:                                              │
│         """Send a synchronous query to the server"""                                                                                 │
│         response = requests.post(                                                                                                    │
│             f"{self.base_url}/conduit/sync", json=request.model_dump()                                                               │
│         )                                                                                                                            │
│         response.raise_for_status()                                                                                                  │
│         try:                                                                                                                         │
│             return ConduitResponse.model_validate_json(response.text)                                                                │
│         except Exception as e:                                                                                                       │
│             return ConduitError.model_validate_json(response.text)                                                                   │
│                                                                                                                                      │
│     def query_async(self, batch: BatchRequest) -&gt; list[ConduitResponse | ConduitError]:                                           │
│         """Send an asynchronous batch query to the server"""                                                                         │
│         response = requests.post(                                                                                                    │
│             f"{self.base_url}/conduit/async", json=batch.model_dump()                                                                │
│         )                                                                                                                            │
│         response.raise_for_status()                                                                                                  │
│         try:                                                                                                                         │
│             return [                                                                                                                 │
│                 ConduitResponse.model_validate_json(item) for item in response.json()                                                │
│             ]                                                                                                                        │
│         except Exception as e:                                                                                                       │
│             return [ConduitError.model_validate_json(item) for item in response.json()]                                              │
│                                                                                                                                      │
│     def generate_synthetic_data(                                                                                                     │
│         self, request: SyntheticDataRequest                                                                                          │
│     ) -&gt; SyntheticDataUnion | ConduitError:                                                                                       │
│         """Generate synthetic data using the server with structured error handling"""                                                │
│         endpoint = f"{self.base_url}/siphon/synthetic_data"                                                                          │
│                                                                                                                                      │
│         # Log the request details                                                                                                    │
│         request_data = request.model_dump()                                                                                          │
│         logger.info(f"Sending request to {endpoint}")                                                                                │
│         logger.debug(f"Request payload keys: {list(request_data.keys())}")                                                           │
│         logger.debug(f"Context type: {type(request.context).__name__}")                                                              │
│         logger.debug(f"Model: {request.model}")                                                                                      │
│                                                                                                                                      │
│         # Log a hash of the request for duplicate detection                                                                          │
│         import hashlib                                                                                                               │
│                                                                                                                                      │
│         request_hash = hashlib.md5(                                                                                                  │
│             json.dumps(request_data, sort_keys=True).encode()                                                                        │
│         ).hexdigest()[:8]                                                                                                            │
│         logger.info(f"Request hash: {request_hash}")                                                                                 │
│                                                                                                                                      │
│         try:                                                                                                                         │
│             response = requests.post(endpoint, json=request_data)                                                                    │
│                                                                                                                                      │
│             # Log response details before checking status                                                                            │
│             logger.info(f"Response status: {response.status_code}")                                                                  │
│             logger.debug(f"Response headers: {dict(response.headers)}")                                                              │
│                                                                                                                                      │
│             # Extract request ID from response headers if available                                                                  │
│             request_id = response.headers.get("X-Request-ID", "unknown")                                                             │
│             logger.info(f"Server request ID: {request_id}")                                                                          │
│                                                                                                                                      │
│             if response.status_code != 200:                                                                                          │
│                 logger.error(f"HTTP {response.status_code} error from {endpoint}")                                                   │
│                 self._handle_error_response(response)                                                                                │
│                                                                                                                                      │
│             # 3. Reconstruct SyntheticData                                                                                           │
│             from siphon.data.type_definitions.source_type import SourceType                                                          │
│                                                                                                                                      │
│             json_dict = response.json()                                                                                              │
│             synthetic_data = None                                                                                                    │
│             sourcetype = SourceType(json_dict["sourcetype"])                                                                         │
│             from siphon.synthetic_data.synthetic_data_classes import (                                                               │
│                 SyntheticDataClasses,                                                                                                │
│             )                                                                                                                        │
│                                                                                                                                      │
│             # Find the right SyntheticData subclass                                                                                  │
│             synthetic_data_class = None                                                                                              │
│             for cls_candidate in SyntheticDataClasses:                                                                               │
│                 if (                                                                                                                 │
│                     cls_candidate.__name__.replace("SyntheticData", "")                                                              │
│                     == sourcetype.value                                                                                              │
│                 ):                                                                                                                   │
│                     synthetic_data_class = cls_candidate                                                                             │
│                     break                                                                                                            │
│                                                                                                                                      │
│             if not synthetic_data_class:                                                                                             │
│                 # Fallback to base SyntheticData class                                                                               │
│                 synthetic_data_class = SyntheticData                                                                                 │
│                                                                                                                                      │
│             synthetic_data = synthetic_data_class.model_validate(json_dict)                                                          │
│             logger.info(f"Successfully received synthetic data [hash: {request_hash}]")                                              │
│             return synthetic_data                                                                                                    │
│         except HeadwaterServerException:                                                                                             │
│             # Re-raise our structured exceptions                                                                                     │
│             raise                                                                                                                    │
│         except requests.exceptions.HTTPError as e:                                                                                   │
│             logger.error(f"HTTPError: {e}")                                                                                          │
│             raise                                                                                                                    │
│         except requests.exceptions.RequestException as e:                                                                            │
│             logger.error(f"RequestException: {e}")                                                                                   │
│             raise                                                                                                                    │
│         except Exception as e:                                                                                                       │
│             logger.error(f"Unexpected error: {e}")                                                                                   │
│             logger.error(f"Error type: {type(e).__name__}")                                                                          │
│             raise                                                                                                                    │
│                                                                                                                                      │
│     def generate_embeddings(                                                                                                         │
│         self,                                                                                                                        │
│         request: EmbeddingsRequest,                                                                                                  │
│     ) -&gt; EmbeddingsResponse | ConduitError:                                                                                       │
│         """                                                                                                                          │
│         Generate embeddings using the server.                                                                                        │
│         """                                                                                                                          │
│         response = requests.post(                                                                                                    │
│             f"{self.base_url}/conduit/embeddings",                                                                                   │
│             json=request.model_dump(),                                                                                               │
│         )                                                                                                                            │
│         response.raise_for_status()                                                                                                  │
│         try:                                                                                                                         │
│             return EmbeddingsResponse.model_validate_json(response.text)                                                             │
│                                                                                                                                      │
│         except Exception as e:                                                                                                       │
│             return ConduitError.model_validate_json(response.text)                                                                   │
│                                                                                                                                      │
│     def curate(self, request: CuratorRequest) -&gt; CuratorResponse:                                                                 │
│         """                                                                                                                          │
│         Curate items using the server.                                                                                               │
│         """                                                                                                                          │
│         response = requests.post(                                                                                                    │
│             f"{self.base_url}/curator/curate",                                                                                       │
│             json=request.model_dump(),                                                                                               │
│         )                                                                                                                            │
│         response.raise_for_status()                                                                                                  │
│         return CuratorResponse.model_validate_json(response.text)                                                                    │
│ </file>                                                                                                                              │
│   </file_contents>                                                                                                                   │
│ </project>                                                                                                                           │
│                                                                                                                                      │
│ </code>                                                                                                                              │
│                                                                                                                                      │
│ Assistant: # Headwater API Python Client                                                                                             │
│                                                                                                                                      │
│ A Python client for interacting with the Headwater API, providing methods for model inference, data synthesis, embeddings            │
│ generation, and content curation.                                                                                                    │
│                                                                                                                                      │
│ ## Quick Start                                                                                                                       │
│                                                                                                                                      │
│ This guide assumes you have access to a running Headwater API server instance.                                                       │
│                                                                                                                                      │
│ **1. Install Dependencies**                                                                                                          │
│                                                                                                                                      │
│ This client requires the `requests` and `pydantic` libraries.                                                                        │
│                                                                                                                                      │
│ ```bash                                                                                                                              │
│ pip install requests pydantic                                                                                                        │
│ ```                                                                                                                                  │
│                                                                                                                                      │
│ **2. Run a Query**                                                                                                                   │
│                                                                                                                                      │
│ The following example connects to the client and uses the `curate` endpoint to retrieve relevant items for a given query. Save this  │
│ as `example.py`.                                                                                                                     │
│                                                                                                                                      │
│ ```python                                                                                                                            │
│ from headwater_api.client import HeadwaterClient                                                                                     │
│ from headwater_api.classes import CuratorRequest                                                                                     │
│                                                                                                                                      │
│ # Replace with the actual URL of your Headwater API server                                                                           │
│ HEADWATER_API_URL = "http://localhost:8080"                                                                                          │
│                                                                                                                                      │
│ def get_top_search_results():                                                                                                        │
│     """                                                                                                                              │
│     Initializes the client and retrieves curated search results.                                                                     │
│     """                                                                                                                              │
│     try:                                                                                                                             │
│         # 1. Initialize the client                                                                                                   │
│         client = HeadwaterClient(base_url=HEADWATER_API_URL)                                                                         │
│                                                                                                                                      │
│         # 2. Create a request object                                                                                                 │
│         request = CuratorRequest(                                                                                                    │
│             query_string="What are the latest developments in machine learning?",                                                    │
│             k=3  # Request the top 3 results                                                                                         │
│         )                                                                                                                            │
│                                                                                                                                      │
│         # 3. Call the API method                                                                                                     │
│         response = client.curate(request)                                                                                            │
│                                                                                                                                      │
│         # 4. Process the response                                                                                                    │
│         print("Curation successful. Top results:")                                                                                   │
│         for result in response.results:                                                                                              │
│             print(f"- ID: {result.id}, Score: {result.score:.4f}")                                                                   │
│                                                                                                                                      │
│     except Exception as e:                                                                                                           │
│         print(f"An error occurred: {e}")                                                                                             │
│                                                                                                                                      │
│ if __name__ == "__main__":                                                                                                           │
│     get_top_search_results()                                                                                                         │
│ ```                                                                                                                                  │
│                                                                                                                                      │
│ Run the script from your terminal:                                                                                                   │
│                                                                                                                                      │
│ ```bash                                                                                                                              │
│ python example.py                                                                                                                    │
│ ```                                                                                                                                  │
│                                                                                                                                      │
│ Expected output:                                                                                                                     │
│                                                                                                                                      │
│ ```                                                                                                                                  │
│ Curation successful. Top results:                                                                                                    │
│ - ID: doc_789, Score: 0.9123                                                                                                         │
│ - ID: doc_123, Score: 0.8876                                                                                                         │
│ - ID: doc_456, Score: 0.8543                                                                                                         │
│ ```                                                                                                                                  │
│                                                                                                                                      │
│ ## Core Features Example                                                                                                             │
│                                                                                                                                      │
│ This example demonstrates a more complex workflow:                                                                                   │
│ 1.  **Check Server Status**: Ensure the API is healthy.                                                                              │
│ 2.  **Generate Embeddings**: Create vector embeddings for a batch of documents.                                                      │
│ 3.  **Run Batch Inference**: Use the `conduit` service to process multiple prompts asynchronously.                                   │
│                                                                                                                                      │
│ ```python                                                                                                                            │
│ import os                                                                                                                            │
│ from headwater_api.client import HeadwaterClient                                                                                     │
│ from headwater_api.classes import EmbeddingsRequest, BatchRequest                                                                    │
│                                                                                                                                      │
│ # Assumes ChromaBatch is available from a shared library                                                                             │
│ # For demonstration, we'll use a mock class.                                                                                         │
│ class MockChromaBatch:                                                                                                               │
│     def __init__(self, documents, ids):                                                                                              │
│         self.documents = documents                                                                                                   │
│         self.ids = ids                                                                                                               │
│     def model_dump(self):                                                                                                            │
│         return {"documents": self.documents, "ids": self.ids}                                                                        │
│                                                                                                                                      │
│ # Replace with the actual URL of your Headwater API server                                                                           │
│ HEADWATER_API_URL = os.getenv("HEADWATER_API_URL", "http://localhost:8080")                                                          │
│                                                                                                                                      │
│ def run_full_workflow():                                                                                                             │
│     """                                                                                                                              │
│     Demonstrates checking status, generating embeddings, and batch processing.                                                       │
│     """                                                                                                                              │
│     client = HeadwaterClient(base_url=HEADWATER_API_URL)                                                                             │
│                                                                                                                                      │
│     try:                                                                                                                             │
│         # 1. Check server status                                                                                                     │
│         status = client.get_status()                                                                                                 │
│         print(f"Server status: {status['status']}")                                                                                  │
│         if status['status'] != 'healthy':                                                                                            │
│             print("Server is not healthy. Aborting.")                                                                                │
│             return                                                                                                                   │
│                                                                                                                                      │
│         # 2. Generate embeddings for a batch of text                                                                                 │
│         print("\n--- Generating Embeddings ---")                                                                                     │
│         docs_to_embed = ["The first document.", "The second document."]                                                              │
│         embedding_req = EmbeddingsRequest(                                                                                           │
│             model="bge",                                                                                                             │
│             batch=MockChromaBatch(documents=docs_to_embed, ids=["doc1", "doc2"])                                                     │
│         )                                                                                                                            │
│         embedding_res = client.generate_embeddings(embedding_req)                                                                    │
│         print(f"Generated {len(embedding_res.embeddings)} embeddings.")                                                              │
│         print(f"Dimension of first embedding: {len(embedding_res.embeddings[0])}")                                                   │
│                                                                                                                                      │
│         # 3. Process multiple prompts in a single async call                                                                         │
│         print("\n--- Running Batch Inference ---")                                                                                   │
│         batch_req = BatchRequest(                                                                                                    │
│             model="claude-3-haiku",                                                                                                  │
│             prompt_str="Summarize the following text: {text}",                                                                       │
│             input_variables_list=[                                                                                                   │
│                 {"text": "Photosynthesis is a process used by plants."},                                                             │
│                 {"text": "The mitochondria is the powerhouse of the cell."}                                                          │
│             ]                                                                                                                        │
│         )                                                                                                                            │
│         batch_res = client.query_async(batch_req)                                                                                    │
│         print("Received responses for batch request:")                                                                               │
│         for i, res in enumerate(batch_res):                                                                                          │
│             # Assuming ConduitResponse has a 'text' attribute                                                                        │
│             # The actual attribute may vary based on the 'conduit' library                                                           │
│             print(f"  Response {i+1}: {res.text[:50]}...")                                                                           │
│                                                                                                                                      │
│     except Exception as e:                                                                                                           │
│         print(f"An error occurred during the workflow: {e}")                                                                         │
│                                                                                                                                      │
│ if __name__ == "__main__":                                                                                                           │
│     run_full_workflow()                                                                                                              │
│ ```                                                                                                                                  │
│                                                                                                                                      │
│ ## Installation and Setup                                                                                                            │
│                                                                                                                                      │
│ ### Prerequisites                                                                                                                    │
│ *   Python 3.8+                                                                                                                      │
│ *   Access to a running Headwater API server.                                                                                        │
│                                                                                                                                      │
│ ### Installation                                                                                                                     │
│ The client depends on external packages that can be installed via pip:                                                               │
│ ```bash                                                                                                                              │
│ pip install requests pydantic                                                                                                        │
│ ```                                                                                                                                  │
│ Internal dependencies such as `conduit`, `siphon`, and `dbclients` must be available in your Python environment.                     │
│                                                                                                                                      │
│ ### Client Initialization                                                                                                            │
│ To use the client, import and instantiate `HeadwaterClient`. The constructor requires the base URL of the Headwater API server.      │
│                                                                                                                                      │
│ ```python                                                                                                                            │
│ from headwater_api.client import HeadwaterClient                                                                                     │
│                                                                                                                                      │
│ # Recommended: Use an environment variable for the URL                                                                               │
│ api_url = os.getenv("HEADWATER_API_URL", "http://localhost:8080")                                                                    │
│                                                                                                                                      │
│ client = HeadwaterClient(base_url=api_url)                                                                                           │
│ ```                                                                                                                                  │
│                                                                                                                                      │
│ ## API Overview                                                                                                                      │
│                                                                                                                                      │
│ The client provides methods to interact with the three core services of the Headwater API.                                           │
│                                                                                                                                      │
│ | Service   | Client Methods                         | Purpose                                      |                                │
│ |-----------|----------------------------------------|----------------------------------------------|                                │
│ | **Curator** | `curate()`                             | Information retrieval and result curation.   |                              │
│ | **Conduit** | `query_sync()`, `query_async()`, `generate_embeddings()` | Synchronous and asynchronous model inference. |           │
│ | **Siphon**  | `generate_synthetic_data()`            | Generation of complex synthetic datasets.    |                              │
│                                                                                                                                      │
│ ### Basic Usage                                                                                                                      │
│                                                                                                                                      │
│ #### Curator: Information Retrieval                                                                                                  │
│ Use `curate` to perform a search or retrieval task.                                                                                  │
│                                                                                                                                      │
│ ```python                                                                                                                            │
│ from headwater_api.classes import CuratorRequest                                                                                     │
│                                                                                                                                      │
│ request = CuratorRequest(query_string="Benefits of unit testing")                                                                    │
│ response = client.curate(request)                                                                                                    │
│ # response is a CuratorResponse object with a list of results                                                                        │
│ ```                                                                                                                                  │
│                                                                                                                                      │
│ #### Conduit: Batch Inference                                                                                                        │
│ Use `query_async` for efficient, parallel processing of multiple prompts.                                                            │
│                                                                                                                                      │
│ ```python                                                                                                                            │
│ from headwater_api.classes import BatchRequest                                                                                       │
│                                                                                                                                      │
│ request = BatchRequest(                                                                                                              │
│     model="gpt-4-turbo",                                                                                                             │
│     prompt_strings=[                                                                                                                 │
│         "What is the capital of France?",                                                                                            │
│         "Translate 'hello' to Spanish."                                                                                              │
│     ]                                                                                                                                │
│ )                                                                                                                                    │
│ responses = client.query_async(request)                                                                                              │
│ # responses is a list of ConduitResponse or ConduitError objects                                                                     │
│ ```                                                                                                                                  │
│                                                                                                                                      │
│ #### Error Handling                                                                                                                  │
│ API errors are raised as a `HeadwaterServerException`. This exception contains a `server_error` attribute, which is a                │
│ `HeadwaterServerError` Pydantic model providing detailed information about the failure, including `error_type`, `message`, and       │
│ `status_code`.                                                                                                                       │
│                                                                                                                                      │
│ ```python                                                                                                                            │
│ from headwater_api.classes import HeadwaterServerException                                                                           │
│                                                                                                                                      │
│ try:                                                                                                                                 │
│     # Make a request that might fail                                                                                                 │
│     client.curate(CuratorRequest(query_string=""))                                                                                   │
│ except HeadwaterServerException as e:                                                                                                │
│     print(f"API Error: {e.server_error.error_type}")                                                                                 │
│     print(f"Message: {e.server_error.message}")                                                                                      │
│     if e.server_error.validation_errors:                                                                                             │
│         print("Details:", e.server_error.validation_errors)                                                                          │
│ ```                                                                                                                                  │
│                                                                                                                                      │
│ Model: gemini-2.5-pro-preview-05-06 • Timestamp: 2025-10-22T21:33:38.825852                                                          │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── 21:33:38 ─╯
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
