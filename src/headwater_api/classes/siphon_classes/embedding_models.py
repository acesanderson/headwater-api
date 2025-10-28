import json
from pathlib import Path

embedding_models_file = Path(__file__).parent / "embedding_models.json"


def load_embedding_models() -> list[str]:
    with open(embedding_models_file, "r") as f:
        json_data = json.load(f)
    model_list: list[str] = json_data["embedding_models"]
    return model_list
