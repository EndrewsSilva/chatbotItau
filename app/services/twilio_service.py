import os
from twilio.rest import Client
from app.utils.logger import logger

# 🔧 Configurações
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")
TEST_MODE = os.getenv("TEST_MODE", "false").lower() == "true"

def send_whatsapp_message(to_number: str, body: str):
    """
    Envia mensagem de texto via WhatsApp (Twilio) ou simula envio em modo teste.
    """
    try:
        if TEST_MODE:
            logger.info(f"💬 [MODO TESTE] Mensagem simulada para {to_number}: {body}")
            return

        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        message = client.messages.create(
            body=body,
            from_=TWILIO_WHATSAPP_NUMBER,
            to=to_number,
        )

        logger.info(f"📤 Mensagem enviada via Twilio SID: {message.sid}")
        return message

    except Exception as e:
        logger.error(f"❌ Erro ao enviar mensagem pelo Twilio: {e}")
        raise
