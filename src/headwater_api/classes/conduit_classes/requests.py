from pydantic import BaseModel, Field, model_validator
from typing import Any, Annotated, Literal


class ConduitRequest(BaseModel):
    """
    Parameters that are constructed by Model and are sent to Clients.
    This is the dumb version of Conduit's Request object, without any logic.
    """

    # Core parameters
    output_type: Literal["text", "image", "audio"] = Field(
        default="text", description="Desired output: 'text', 'image', 'audio'"
    )
    model: str = Field(..., description="The model identifier to use for inference.")
    messages: BaseModel | list[BaseModel] = Field(
        default_factory=list,
        description="List of messages to send to the model. Can include text, images, audio, etc.",
    )

    # Optional parameters
    temperature: float | None = Field(
        default=None,
        description="Temperature for sampling. If None, defaults to provider-specific value.",
    )
    stream: bool = False
    verbose: Annotated[int, Field(ge=0, le=5)] = Field(
        default=0,
        exclude=True,
        description="Verbosity level for logging and progress display.",
    )
    response_model: type[BaseModel] | dict | None = Field(
        default=None,
        description="Pydantic model to convert messages to a specific format. If dict, this is a schema for the model for serialization / caching purposes.",
    )
    max_tokens: int | None = Field(
        default=None,
        description="Maximum number of tokens to generate. If None, it is not passed to the client (except for Anthropic, which requires it and has a default).",
    )
    # Post model init parameters
    provider: str | None = Field(
        default=None,
        description="Provider of the model, populated post init. Not intended for direct use.",
    )
    # Client parameters (embedded in dict for now)
    client_params: dict | None = Field(
        default=None,
        description="Client-specific parameters. Validated against the provider-approved params, through our ClientParams.",
    )


class BatchRequest(ConduitRequest):
    """
    BatchRequest extends ConduitRequest to allow for multiple prompt strings or input variables.
    This is useful for processing multiple requests in a single API call.
    """

    prompt_strings: list[str] = Field(
        default_factory=list,
        description="List of prompt strings for each request. Prompt strings should be fully rendered.",
    )
    input_variables_list: list[dict[str, str]] = Field(
        default_factory=list,
        description="List of input variables for each request. Each dict should match the model's input schema.",
    )
    prompt_str: str | None = Field(
        default=None, description="Single prompt string for the request."
    )

    @model_validator(mode="after")
    def _exactly_one(
        self,
    ):
        has_prompts = bool(self.prompt_strings)
        has_vars = bool(self.input_variables_list)
        if has_prompts == has_vars:
            raise ValueError(
                "Provide exactly one of 'prompt_strings' or 'input_variables_list'."
            )
        # If input_variables_list is provided, prompt_str should have a value
        if has_vars and not self.prompt_str:
            raise ValueError(
                "If 'input_variables_list' is provided, 'prompt_str' must also be provided."
            )
        return self


class ChromaBatch(BaseModel):
    # Mandatory fields
    ids: list[str] = Field(
        ..., description="List of unique identifiers for each item in the batch."
    )
    documents: list[str] = Field(
        ..., description="List of documents or text associated with each item."
    )
    # Optional fields
    embeddings: list[list[float]] | None = Field(
        default=None, description="List of embeddings corresponding to each item."
    )
    metadatas: list[dict[str, Any]] | None = Field(
        default=None, description="List of metadata dictionaries for each item."
    )


class EmbeddingsRequest(BaseModel):
    model: str = Field(
        ...,
        description="The embedding model to use for generating embeddings.",
    )
    batch: ChromaBatch = Field(
        ...,
        description="Batch of documents to generate embeddings for.",
    )


__all__ = ["ConduitRequest", "BatchRequest", "ChromaBatch", "EmbeddingsRequest"]
