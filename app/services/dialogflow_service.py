from google.cloud import dialogflow_v2 as dialogflow
from app.config import DIALOGFLOW_PROJECT_ID, DIALOGFLOW_LANGUAGE_CODE

def detect_intent_text(text: str, session_id="whatsapp-session"):
    """Envia texto para o Dialogflow e retorna o resultado."""
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, session_id)
    text_input = dialogflow.TextInput(text=text, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(request={"session": session, "query_input": query_input})
    return response.query_result
