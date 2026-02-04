# Thin application layer / entry point.
from IPython.display import Audio, display
from src.config.settings import MODEL_ID, DEVICE
from src.models.language_classifier import load_language_classifier
from src.audio.audio_loader import load_audio_from_url
from src.services.inference import classify_language


def main():
    print("Loading model...")
    classifier = load_language_classifier(MODEL_ID, DEVICE)
    print("Model loaded successfully")

    url = "https://huggingface.co/datasets/Narsil/asr_dummy/resolve/main/mlk.flac"

    audio, sr = load_audio_from_url(url)

    display(Audio(audio, rate=sr))

    results = classify_language(classifier, audio, sr)

    for r in results:
        print(f"{r['label']:15s} {r['score']:.4f}")


if __name__ == "__main__":
    main()


# from io import BytesIO
# import requests
# import torch
# import numpy as np
# import soundfile as sf

# from transformers import pipeline
# from IPython.display import Audio, display

# MODEL_ID = "sanchit-gandhi/whisper-medium-fleurs-lang-id"

# # Load pipeline
# lang_classifier = pipeline(
#     task="audio-classification",
#     model=MODEL_ID,
#     device=0 if torch.cuda.is_available() else -1
# )

# print("Model loaded successfully")

# # -----------------------------
# # Download public English speech sample
# url = "https://huggingface.co/datasets/Narsil/asr_dummy/resolve/main/mlk.flac"
# response = requests.get(url)
# response.raise_for_status()

# audio, sr = sf.read(BytesIO(response.content))

# if audio.ndim == 2:
#     audio = np.mean(audio, axis=1)

# audio = audio.astype(np.float32)

# display(Audio(audio, rate=sr))

# # invoke language classification
# results = lang_classifier(
#     {"array": audio, "sampling_rate": sr}
# )

# for r in results[:5]:
#     print(f"{r['label']:15s} {r['score']:.4f}")