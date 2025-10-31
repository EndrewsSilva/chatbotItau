import pytest
from app.services.voice_service import transcrever_audio_twilio
import os

@pytest.mark.parametrize("audio_file", [
    "tests/audios/sul.ogg",
    "tests/audios/sudeste.ogg",
    "tests/audios/nordeste.ogg",
    "tests/audios/norte.ogg",
])
def test_transcricao_sotaques(monkeypatch, audio_file):
    """Testa a transcrição de diferentes sotaques usando mock."""

    class MockTranscriptionResponse:
        @property
        def text(self):
            return "Áudio transcrito com sucesso"

    def mock_create(*args, **kwargs):
        return MockTranscriptionResponse()

    import app.services.voice_service as vs
    monkeypatch.setattr(vs.openai.audio.transcriptions, "create", mock_create)

    # Caminho absoluto para garantir que o arquivo existe
    audio_path = os.path.abspath(audio_file)
    texto = transcrever_audio_twilio(audio_path)

    assert isinstance(texto, str)
    assert len(texto) > 0
    assert "transcrito" in texto.lower()
