# 🎧 Multiclass Audio Classification (Language Identification)

A **PyTorch-based multilingual audio classification system** built using **Hugging Face Transformers (Wav2Vec2)** to identify the language spoken in an audio file.
The system supports **both public audio URLs and local audio files** and outputs **confidence scores per language**.

---
## Overview
The system is developed incrementally across clearly versioned milestones:

* **Version 1.0.0** – [Basic Language Classification](https://github.com/HariHara-sn/Text-Detection-and-Extraction-using-OpenCV-OCR-and-LLM/tree/Sample-Extraction)
* **Version 2.0.0** – [Extended Audio Input Support](https://github.com/HariHara-sn/Text-Detection-and-Extraction-using-OpenCV-OCR-and-LLM/tree/medical-prescription-extraction)
* **Version 3.0.0** – [under construction]()
* **Version 4.0.0** – [not yet released]()


## Tech Stack

* **Goal:** Language Identification (LID)
* **Model:** Wav2Vec2 (fine-tuned on FLEURS)
* **Framework:** PyTorch + Hugging Face Transformers
* **Input:** Any spoken audio (local file or public URL)
* **Output:** Language probabilities (softmax scores)
* **Languages Supported:** **102 languages**

---

## Model Details

* **Model Type:** Multiclass Audio Classification
* **Architecture:** Transformer-based Wav2Vec2
* **Dataset:** Google **FLEURS**
* **Sampling Rate:** 16 kHz (mandatory)
* **Output Head:** Softmax over 102 language labels

> The FLEURS dataset is designed for multilingual speech tasks and provides balanced speech samples across languages, enabling robust language identification.


---
## 📌 How many languages it supports

The model is fine-tuned on the FLEURS dataset, which contains speech in 102 languages

This model was trained on Google’s FLEURS dataset, which was designed for multilingual speech tasks and includes:

✔ **102 languages** across:

* Asia (Tamil, Hindi, Chinese, Japanese, etc.)
* Europe (English, French, German, etc.)
* Africa
* Middle East
* Low-resource languages

---

## 🗂 Project Structure

```
src/
└── app/
    ├── main.py
    ├── config/
    │   └── settings.py
    ├── models/
    │   └── language_classifier.py
    ├── audio/
    │   └── audio_loader.py
    └── services/
        └── inference.py
```

## ⚙️ Core Functions

### `load_audio(path | url)`

* Loads audio using `librosa` / `soundfile`
* Converts stereo → mono
* Resamples to **16 kHz**
* Normalizes amplitude

---

### `classify_language(audio, sample_rate)`

* Extracts features using `Wav2Vec2Processor`
* Runs inference via transformer
* Applies softmax
* Returns ranked language probabilities

---

## ▶️ Installation

```bash
pip install -r requirements.txt
```
## Environment Variables

Create a `.env` file and set:

```
MODEL_NAME=<your_pretrained_model_name>
```

## ▶️ Running the Application

From the project root:

```bash
python -m app.main
```

This will:

1. Load the pretrained model
2. Load audio input (URL or local)
3. Perform language classification
4. Print confidence scores

---




## Usage

```python
path = "Testing/audio/harvard.wav"
url = "https://huggingface.co/datasets/Narsil/asr_dummy/resolve/main/mlk.flac"

audio, sr = load_audio_from_url(url) #public url 
audio, sr = load_audio_from_file(path) # local audio

display(Audio(audio, rate=sr))

results = classify_language(classifier, audio, sr)

print(results)
```
### Sample Output

```json
{
  "English": 0.95,
  "Welsh": 0.02,
  "Kabyle": 0.01,
  "Chinese_China": 0.01,
  "Russian": 0.01
}
```

### Online Audio Classification (~100%)

![Online Audio Output](https://github.com/HariHara-sn/Multiclass-Audio-Classification/blob/audio-local-v2/POC_IMAGES/online_audio_100%25_3.png?raw=true)

### Tamil Audio Classification (~99%)

![Tamil Audio Output](https://github.com/HariHara-sn/Multiclass-Audio-Classification/blob/main/POC_IMAGES/Tamil_audio_99%25_4.png?raw=true)

---

## 🔊 Audio Samples for Testing

### Tamil

🔗 [https://commons.wikimedia.org/wiki/Category:Audio_files_in_Tamil](https://commons.wikimedia.org/wiki/Category:Audio_files_in_Tamil)

### English

🔗 [https://www.kaggle.com/datasets/pavanelisetty/sample-audio-files-for-speech-recognition](https://www.kaggle.com/datasets/pavanelisetty/sample-audio-files-for-speech-recognition)

