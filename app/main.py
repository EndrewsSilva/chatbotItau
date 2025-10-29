from fastapi import FastAPI
from app.schemas import UserQuestion, BotResponse
from app.chatbot import ask_openai
from fastapi import File, UploadFile
from app.voice_chat import process_audio
from app.webhooks import dialogflow_webhook, whatsapp_webhook





app = FastAPI(title="Chatbot Itaú - ICT")



@app.get("/")
def root():
    return {"message": "Chatbot bancário com OpenAI. Use /docs para testar a API."}

@app.post("/chat", response_model=BotResponse)
async def chat(user_question: UserQuestion):
    answer = await ask_openai(user_question.question)
    return BotResponse(answer=answer)

@app.post("/voice-chat", response_model=BotResponse)
async def voice_chat(file: UploadFile = File(...)):
    answer = await process_audio(file)
    return BotResponse(answer=answer)



app.include_router(dialogflow_webhook.router)
app.include_router(whatsapp_webhook.router)