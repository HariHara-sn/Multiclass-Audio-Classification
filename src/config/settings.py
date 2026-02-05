# All environment- and model-specific configuration lives here.

import torch
import os

MODEL_ID = os.getenv(
    "MODEL_ID",
    "sanchit-gandhi/whisper-medium-fleurs-lang-id" #fall back
)

DEVICE = 0 if torch.cuda.is_available() else -1

DEFAULT_SAMPLE_RATE = 16000