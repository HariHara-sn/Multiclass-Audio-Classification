# All environment- and model-specific configuration lives here.

import torch
import os

MODEL_ID = os.getenv(
    "LANG_ID_MODEL",
    "sanchit-gandhi/whisper-medium-fleurs-lang-id"
)

DEVICE = 0 if torch.cuda.is_available() else -1

DEFAULT_SAMPLE_RATE = 16000