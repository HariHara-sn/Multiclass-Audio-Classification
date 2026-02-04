# Contains business logic (what you do with the model).
from typing import List, Dict


def classify_language(
    classifier,
    audio,
    sampling_rate: int,
    top_k: int = 5
) -> List[Dict]:
    results = classifier(
        {"array": audio, "sampling_rate": sampling_rate}
    )

    return results[:top_k]
