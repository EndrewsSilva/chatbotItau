import pytest
import unicodedata
from app.services.voice_service import transcrever_audio_twilio


def remover_acentos(texto):
    """
    Remove acentos para facilitar comparações em testes de transcrição.
    """
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )


@pytest.mark.parametrize("audio_file", [
    "tests/audios/sul.ogg",
    "tests/audios/sudeste.ogg",
    "tests/audios/nordeste.ogg",
    "tests/audios/norte.ogg",
])
def test_transcricao_real(audio_file):
    """
    Testa a transcrição real (sem mock) de diferentes sotaques regionais.
    """
    texto = transcrever_audio_twilio(f"file://{audio_file}")

    print(f"\n🎧 Transcrição do áudio {audio_file}:")
    print(texto)

    assert isinstance(texto, str)
    assert len(texto) > 0

    # Normaliza (remove acentos e coloca tudo em minúsculo)
    texto_normalizado = remover_acentos(texto.lower())

    assert "itau" in texto_normalizado
