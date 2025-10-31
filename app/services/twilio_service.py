# app/services/twilio_service.py

import os
from twilio.rest import Client
from app.utils.logger import logger
import logging

# Desativa logs do Twilio
logging.getLogger("twilio").setLevel(logging.WARNING)
logging.getLogger("twilio.http_client").setLevel(logging.WARNING)


# 🔧 Configurações
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")
TEST_MODE = os.getenv("TEST_MODE", "false").lower() == "true"

def send_whatsapp_message(to_number: str, body: str):
    """
    Envia mensagem de texto via WhatsApp (Twilio) ou simula envio em modo teste.
    Somente loga mensagens enviadas, sem headers ou status detalhado.
    """
    try:
        # 🔹 Modo teste: apenas loga mensagem
        if TEST_MODE:
            logger.info(f"[TESTE] Para {to_number}: {body}")
            return None

        # 🔹 Cria cliente Twilio
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        # 🔹 Envia a mensagem
        message = client.messages.create(
            body=body,
            from_=TWILIO_WHATSAPP_NUMBER,
            to=to_number,
        )

        # 🔹 Log apenas da mensagem enviada
        logger.info(f"💬 Para {to_number}: {body}")

        return message

    except Exception as e:
        logger.error(f"❌ Erro ao enviar mensagem pelo Twilio: {e}")
        raise
