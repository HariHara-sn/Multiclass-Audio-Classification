# Responsible only for model construction.
from transformers import pipeline

def load_language_classifier(model_id: str, device: int):
    return pipeline(
        task="audio-classification",
        model=model_id,
        device=device
    )
