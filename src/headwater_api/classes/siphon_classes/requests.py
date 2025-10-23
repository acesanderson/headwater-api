from pydantic import BaseModel, model_validator
from siphon.context.context_classes import ContextUnion


class SyntheticDataRequest(BaseModel):
    context: ContextUnion
    model: str = "gemini2.5"

    @model_validator(mode="before")
    @classmethod
    def deserialize_context(cls, data):
        if isinstance(data, dict) and "context" in data:
            context_data = data["context"]
            if isinstance(context_data, dict):
                # Reconstruct the right context class
                from siphon.context.context_classes import ContextClasses

                sourcetype_value = context_data.get("sourcetype")

                for context_class in ContextClasses:
                    if (
                        context_class.__name__.replace("Context", "")
                        == sourcetype_value
                    ):
                        data["context"] = context_class.model_validate(context_data)
                        break
        return data
