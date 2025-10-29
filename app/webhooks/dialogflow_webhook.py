# app/webhooks/dialogflow_webhook.py

from fastapi import APIRouter, Request
from app.chatbot import ask_openai  # ajuste se necessário

router = APIRouter()

@router.post("/webhook/dialogflow")
async def dialogflow_webhook(request: Request):
    data = await request.json()
    user_text = data.get("queryResult", {}).get("queryText", "")
    response = await ask_openai(user_text)
    return {"fulfillmentText": response}
