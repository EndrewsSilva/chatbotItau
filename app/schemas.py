from pydantic import BaseModel

class UserQuestion(BaseModel):
    question: str

class BotResponse(BaseModel):
    answer: str
