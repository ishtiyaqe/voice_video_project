# Voice Video Project
## Overview

This project adds a **local ASR (Automatic Speech Recognition) fallback** to the existing transcription pipeline. It reduces cost and API dependency by enabling local transcription using the faster-whisper model when OpenAI's API is unavailable or rate-limited.

The backend keeps the **same JSON output format** as the OpenAI transcription, ensuring all downstream consumers remain compatible.

---

## Why?

- Reduce reliance on OpenAI API and lower costs
- Provide a seamless fallback transcription option locally
- Keep downstream code unchanged by adapting local ASR output to OpenAI-compatible JSON format

---

## Features & Scope

1. **Configurable ASR provider**

   - Use environment variable `WHISPER_PROVIDER` with values:  
     `openai` | `faster-whisper` | `auto`  
   - Set in `dev.env` and `test.env`
   - Loaded in `src/app.py` and exposed via `os.getenv`
   - Allows switching providers without code changes

2. **Local ASR implementation**

   - New module: `src/utils/asr_local.py`
   - Function: `transcribe_local(audio_bytes: bytes, language: str | None) -> dict`
   - Uses `faster-whisper` (tiny/base model recommended for CPU)
   - Converts `faster-whisper` output to OpenAI verbose JSON format:

   ```json
   {
     "text": "...",
     "segments": [
       {
         "id": 0,
         "start": 0.12,
         "end": 1.87,
         "text": "...",
         "words": [
           {"start": 0.12, "end": 0.32, "word": "Hi"},
           ...
         ]
       }
     ]
   }
