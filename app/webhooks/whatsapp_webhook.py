from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from app.services.dialogflow_service import detect_intent_text
from app.services.twilio_service import send_whatsapp_message
from app.utils.logger import logger
from app.chatbot import ask_openai

router = APIRouter(prefix="/webhook", tags=["WhatsApp Webhook"])

@router.post("/whatsapp")
async def whatsapp_webhook(request: Request):
    try:
        form = await request.form()
        user_message = form.get("Body")
        user_number = form.get("From")

        if not user_message:
            logger.warning("Mensagem vazia recebida.")
            return JSONResponse(status_code=400, content={"error": "Mensagem vazia"})

        logger.info(f"📩 Mensagem recebida do {user_number}: {user_message}")

        # 🔹 Detecta intent com Dialogflow
        dialogflow_result = detect_intent_text(user_message)
        intent_name = dialogflow_result.intent.display_name
        fulfillment_text = dialogflow_result.fulfillment_text
        parameters = dialogflow_result.parameters

        # 🔹 Lógica personalizada simplificada
        if intent_name.lower() == "saldo conta":
            tipo_conta = parameters.get("tipo_conta") or "corrente"
            reply = f"Seu saldo da conta {tipo_conta} é R$ 1.234,56"

        elif intent_name.lower() == "transferência":
            valor = parameters.get("valor")
            tipo_conta_destino = parameters.get("tipo_conta_destino")
            if valor and tipo_conta_destino:
                reply = f"Transferindo R$ {valor} para conta {tipo_conta_destino}... ✅"
            else:
                reply = "Por favor, informe o valor e a conta de destino."

        elif intent_name.lower() in ["perguntar_ia", "resposta_generativa", "default fallback intent"]:
            reply = await ask_openai(user_message)

        else:
            reply = fulfillment_text or "Desculpe, não compreendi."

        # 🔹 Envia resposta
        send_whatsapp_message(user_number, reply)
        logger.info(f"📤 Resposta enviada para {user_number}")

        return JSONResponse(status_code=200, content={"status": "ok", "reply": reply})

    except Exception as e:
        logger.error(f"🔥 Erro inesperado no webhook: {e}")
        return JSONResponse(status_code=500, content={"error": str(e)})
