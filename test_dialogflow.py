import os
from google.cloud import dialogflow_v2 as dialogflow

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./keys/chatbot-itau-j9mv-82b0ad025789.json"
project_id = "chatbot-itau-j9mv"
session_id = "teste-local"

session_client = dialogflow.SessionsClient()
session = session_client.session_path(project_id, session_id)

text_input = dialogflow.TextInput(text="Oi", language_code="pt-BR")
query_input = dialogflow.QueryInput(text=text_input)

response = session_client.detect_intent(request={"session": session, "query_input": query_input})
print("Resposta:", response.query_result.fulfillment_text)
