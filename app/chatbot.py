from openai import OpenAI
from app.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

async def ask_openai(question: str) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # ou "gpt-4o" se preferir
            messages=[
                {"role": "system", "content": "Você é um assistente bancário educado e objetivo."},
                {"role": "user", "content": question}
            ],
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Erro ao consultar OpenAI: {e}"
