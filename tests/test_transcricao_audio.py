import pytest
from pathlib import Path
from app.services.voice_service import transcrever_audio_twilio

@pytest.mark.parametrize("audio_url", [
    "https://file-examples.com/storage/fefbfc8e02f2f45a8b3f708/2017/11/file_example_OOG_1MG.ogg",
])
def test_transcricao_audio(monkeypatch, audio_url):
    """
    Testa se a função de transcrição retorna texto válido usando URL.
    Usa monkeypatch para simular download de áudio e chamada ao Whisper.
    """

    # 🧩 Mock da resposta da OpenAI
    class MockOpenAIResponse:
        text = "Teste de áudio transcrito com sucesso"

    def mock_transcribe(*args, **kwargs):
        return MockOpenAIResponse()

    # 🧩 Mock do requests.get para não depender da URL
    class MockResponse:
        def raise_for_status(self):
            pass
        @property
        def content(self):
            return b"fake audio content"

    def mock_requests_get(url, **kwargs):
        return MockResponse()

    import app.services.voice_service as vs

    # Monkeypatch OpenAI
    monkeypatch.setattr(vs.openai.audio.transcriptions, "create", mock_transcribe)
    # Monkeypatch requests.get
    monkeypatch.setattr(vs.requests, "get", mock_requests_get)

    # Executa o teste
    texto = transcrever_audio_twilio(audio_url)

    # Verifica resultado
    assert isinstance(texto, str)
    assert len(texto) > 0
    assert "transcrito" in texto.lower()
