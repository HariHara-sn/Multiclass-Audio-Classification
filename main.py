# 1. Load Model & Processor

import torch
import librosa
from dotenv import load_dotenv
import os
from transformers import Wav2Vec2Processor, Wav2Vec2ForSequenceClassification

load_dotenv()
MODEL_NAME = os.getenv("MODEL_NAME")
processor = Wav2Vec2Processor.from_pretrained(MODEL_NAME)
model = Wav2Vec2ForSequenceClassification.from_pretrained(
    MODEL_NAME,
    num_labels=5  # change based on your classes
)

model.eval()

# 🔹 Load & Preprocess Audio
def load_audio(path):
    audio, sr = librosa.load(path, sr=16000)  # force 16kHz
    return audio

# 🔹 Run Classification
import torch.nn.functional as F

LABELS = ["English", "Welsh", "Kabyle", "Chinese_China", "Russian"]

def classify_audio(audio_path):
    audio = load_audio(audio_path)

    inputs = processor(
        audio,
        sampling_rate=16000,
        return_tensors="pt",
        padding=True
    )

    with torch.no_grad():
        logits = model(**inputs).logits

    probs = F.softmax(logits, dim=-1).squeeze()

    results = {
        LABELS[i]: round(probs[i].item(), 3)
        for i in range(len(LABELS))
    }

    return results


# OUTPUT
if __name__ == "__main__":
    test_audio_path = "path_to_your_test_audio.wav"  # replace with your test audio path
    results = classify_audio(test_audio_path)
    print("Classification Results:", results)
    