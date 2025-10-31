import os
import requests
import tempfile
import openai
from app.config import OPENAI_API_KEY, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN

openai.api_key = OPENAI_API_KEY


def transcrever_audio_twilio(media_url: str) -> str:
    """
    Faz download do áudio via Twilio (se for URL http/https)
    ou lê localmente (se for arquivo no sistema).
    Transcreve com Whisper.
    """
    try:
        # Caso 1: URL do Twilio (começa com http ou https)
        if media_url.startswith("http"):
            print(f"🎧 Baixando áudio remoto: {media_url}")
            auth = (TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
            response = requests.get(media_url, auth=auth)
            response.raise_for_status()

            with tempfile.NamedTemporaryFile(suffix=".ogg", delete=True) as temp_audio:
                temp_audio.write(response.content)
                temp_audio.flush()

                with open(temp_audio.name, "rb") as audio_file:
                    transcript = openai.audio.transcriptions.create(
                        model="whisper-1",
                        file=audio_file
                    )

        # Caso 2: Caminho local (com ou sem prefixo file://)
        else:
            if media_url.startswith("file://"):
                media_url = media_url.replace("file://", "")

            print(f"🎤 Lendo áudio local: {media_url}")
            if not os.path.exists(media_url):
                raise FileNotFoundError(f"Arquivo não encontrado: {media_url}")

            with open(media_url, "rb") as audio_file:
                transcript = openai.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file
                )

        texto = transcript.text.strip()
        print(f"✅ Transcrição concluída: {texto[:60]}...")
        return texto

    except Exception as e:
        print(f"❌ Erro ao transcrever áudio: {e}")
        return ""
