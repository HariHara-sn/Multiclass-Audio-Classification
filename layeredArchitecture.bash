src/
├── config/
│   └── settings.py
├── models/
│   └── language_classifier.py
├── audio/
│   └── audio_loader.py
├── services/
│   └── inference.py
├── main.py
└── requirements.txt

# This is a layered architecture (config → infrastructure → service → application).
# This line create the above folders
mkdir config, models, audio, services

New-Item config/settings.py -ItemType File
New-Item models/language_classifier.py -ItemType File
New-Item audio/audio_loader.py -ItemType File
New-Item services/inference.py -ItemType File
New-Item requirements.txt -ItemType File