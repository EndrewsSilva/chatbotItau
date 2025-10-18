from fastapi import UploadFile
from openai import OpenAI
from app.config import OPENAI_API_KEY
import io

client = OpenAI(api_key=OPENAI_API_KEY)

async def process_audio(file: UploadFile) -> str:
    try:
        # Lê o conteúdo do arquivo enviado
        audio_bytes = await file.read()

        # Cria um buffer com nome e tipo
        audio_file = io.BytesIO(audio_bytes)
        audio_file.name = file.filename  # <- ESSENCIAL para Whisper saber o formato

        # Transcreve o áudio
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )

        text = transcription.text
        print(f"Texto transcrito: {text}")

        # Envia a pergunta para o chatbot
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um atendente bancário simpático e direto."},
                {"role": "user", "content": text}
            ]
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Erro ao processar áudio: {e}"
