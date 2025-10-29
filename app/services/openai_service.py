import openai
from app.utils.logger import logger

logger.info("Mensagem recebida do usuário")


async def ask_openai(prompt: str):
    """Envia o prompt para o modelo OpenAI e retorna a resposta."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        logger.error(f"Erro ao chamar OpenAI: {e}")
        return "Desculpe, ocorreu um erro ao processar sua solicitação."
