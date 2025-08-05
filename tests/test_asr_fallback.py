import pytest
import io
from src.app import create_app

app = create_app()

def mock_transcribe_local(audio_bytes, language=None, word_timestamps=True):
    # Return a list of segments to mimic real output
    return [
        {
            "id": 0,
            "start": 0.0,
            "end": 1.0,
            "text": "Hello world",
            "words": [
                {"start": 0.0, "end": 0.5, "word": "Hello"},
                {"start": 0.5, "end": 1.0, "word": "world"}
            ]
        }
    ]


def test_fallback(monkeypatch):
    monkeypatch.setenv("WHISPER_PROVIDER", "faster-whisper")
    monkeypatch.setattr("src.utils.video_utils.transcribe_local", mock_transcribe_local)

    client = app.test_client()
    
    data = {
        'file': (io.BytesIO(b"fake-audio-bytes"), 'How often do you..._  A1 English Listening Test.mp3')
    }

    res = client.post("/build_srt_file/xyz", content_type='multipart/form-data', data=data)
    
    assert res.status_code == 200
    json_data = res.get_json()
    assert json_data["status"] == "MEDIA_SRT_CREATED"
    assert isinstance(json_data["transcript"], list)
    assert "text" in json_data["transcript"][0]


