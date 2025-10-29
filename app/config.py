# app/config.py
from dotenv import load_dotenv
import os

# 1️⃣ Carrega variáveis do .env
load_dotenv()

# =========================================================
# 🔑 CONFIGURAÇÕES DO OPENAI
# =========================================================
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# =========================================================
# 🎯 CONFIGURAÇÕES DO DIALOGFLOW
# =========================================================
DIALOGFLOW_PROJECT_ID = os.getenv("DIALOGFLOW_PROJECT_ID")
DIALOGFLOW_LANGUAGE_CODE = os.getenv("DIALOGFLOW_LANGUAGE_CODE", "pt-BR")
DIALOGFLOW_SESSION_ID = os.getenv("DIALOGFLOW_SESSION_ID", "whatsapp-session")

# Caminho para o arquivo de credenciais do Dialogflow
GOOGLE_APPLICATION_CREDENTIALS = os.getenv(
    "GOOGLE_APPLICATION_CREDENTIALS",
    "./keys/chatbot-itau-j9mv-d3b59a94289a.json"  # fallback seguro
)
# Define para a SDK do Google Cloud usar automaticamente
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_APPLICATION_CREDENTIALS

# =========================================================
# 📞 CONFIGURAÇÕES DO TWILIO
# =========================================================
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

# =========================================================
# ☁️ CONFIGURAÇÕES DE CLOUD E GENAI (futuro)
# =========================================================
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
BEDROCK_MODEL_ID = os.getenv("BEDROCK_MODEL_ID", "anthropic.claude-v2")

# =========================================================
# ⚙️ OUTRAS CONFIGURAÇÕES GERAIS
# =========================================================
TEST_MODE = os.getenv("TEST_MODE", "false").lower() == "true"

# =========================================================
# 🧾 LOG VISUAL DE CONFIRMAÇÃO
# =========================================================
print("✅ Configurações carregadas:")
print(f"   - Dialogflow Project ID: {DIALOGFLOW_PROJECT_ID}")
print(f"   - Twilio WhatsApp Number: {TWILIO_WHATSAPP_NUMBER}")
print(f"   - Test Mode: {TEST_MODE}")
print(f"   - Google Credentials: {GOOGLE_APPLICATION_CREDENTIALS}")
