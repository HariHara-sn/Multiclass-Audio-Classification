# Thin application layer / entry point.
from IPython.display import Audio, display
from src.config.settings import MODEL_ID, DEVICE
from src.models.language_classifier import load_language_classifier
from src.audio.audio_loader import load_audio_from_file
from src.services.inference import classify_language


def main():
    print("Loading model...")
    classifier = load_language_classifier(MODEL_ID, DEVICE)
    print("Model loaded successfully")

    # url = "https://huggingface.co/datasets/Narsil/asr_dummy/resolve/main/mlk.flac"
    path = "Testing/audio/harvard.wav"

    # audio, sr = load_audio_from_url(url) 
    audio, sr = load_audio_from_file(path)

    display(Audio(audio, rate=sr))

    results = classify_language(classifier, audio, sr)

    for r in results:
        print(f"{r['label']:15s} {r['score']:.4f}")

if __name__ == "__main__":
    main()