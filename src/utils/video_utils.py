import os
from src.utils.openai_whisper import transcribe_openai
from src.utils.asr_local import transcribe_local

def get_whisper_srt(f_name, audio_bytes):
    provider = os.getenv("WHISPER_PROVIDER", "auto")

    if provider == "openai":
        return transcribe_openai(audio_bytes)

    elif provider == "faster-whisper":
        return transcribe_local(audio_bytes)

    elif provider == "auto":
        try:
            return transcribe_openai(audio_bytes)
        except Exception as e:
            print(f"[Fallback] OpenAI failed: {e}")
            return transcribe_local(audio_bytes)

    raise ValueError("Unsupported WHISPER_PROVIDER")
