import openai
import os

def transcribe_openai(audio_bytes: bytes) -> dict:
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    with open("temp.wav", "wb") as f:
        f.write(audio_bytes)

    with open("temp.wav", "rb") as audio_file:
        transcript = openai.Audio.transcribe(
            "whisper-1", audio_file, response_format="verbose_json"
        )
    return transcript
