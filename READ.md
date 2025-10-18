# Chatbot Bancário com Texto e Voz – Desafio ITAÚ

Este projeto implementa um chatbot inteligente com suporte a entrada por **texto e voz**, voltado para o atendimento bancário. A solução utiliza a **API da OpenAI** com os modelos **GPT (chat)** e **Whisper (áudio)**, integrados via **FastAPI** para criação de uma API moderna, simples e escalável.

---

##  Objetivo

Atender ao desafio do Itaú para desenvolvimento de uma prova de conceito (PoC) de um assistente virtual capaz de responder dúvidas bancárias com linguagem natural, tanto em **mensagens de texto** quanto por **áudio gravado** pelo usuário.

---

## Tecnologias Utilizadas

- Python 3.10+
- FastAPI
- OpenAI API (`gpt-3.5-turbo`  e `whisper-1`)
- Uvicorn (servidor ASGI)
- python-multipart (upload de arquivos)

---

##  Como Rodar Localmente

### 1. Clone o repositório

```bash
git clone https://github.com/seuusuario/chatbot-itau.git
cd chatbot-itau

2. Crie um ambiente virtual

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

3. Instale as dependências

pip install -r requirements.txt

4. Configure a chave da API OpenAI

OPENAI_API_KEY=sk-...

5. Inicie a API

uvicorn app.main:app --reload

A API estará disponível em: http://127.0.0.1:8000

6 Exemplos de Uso, chat por textp

{
  "question": "Qual o limite do meu cartão?"
}

7 Chat por Voz

Endpoint: POST /audio

Input: Arquivo de áudio (formato .mp3, .wav, etc.)

Resposta será uma mensagem baseada na transcrição da fala enviada.
