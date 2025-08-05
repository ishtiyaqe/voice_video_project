from faster_whisper import WhisperModel

def transcribe_local(audio_bytes: bytes, language: str | None = None) -> dict:
    with open("temp.wav", "wb") as f:
        f.write(audio_bytes)

    model = WhisperModel("tiny", compute_type="int8")
    segments, _ = model.transcribe("temp.wav", language=language, word_timestamps=True)

    openai_format = {"text": "", "segments": []}
    for idx, seg in enumerate(segments):
        words = [{"start": w.start, "end": w.end, "word": w.word} for w in seg.words]
        openai_format["segments"].append({
            "id": idx,
            "start": seg.start,
            "end": seg.end,
            "text": seg.text,
            "words": words
        })
        openai_format["text"] += seg.text + " "
    return openai_format
