from gtts import gTTS
import os

# Frases personalizadas por sotaque
frases = {
    "sul.ogg": "Bah, tudo certo? Eu sou do Sul e estou participando do teste de voz do Itaú.",
    "sudeste.ogg": "Oi, tudo bem? Eu sou do Sudeste e estou participando do teste de voz do Itaú.",
    "nordeste.ogg": "E aí, visse? Eu sou do Nordeste e tô participando do teste de voz do Itaú.",
    "norte.ogg": "Oi, tudo bom? Eu sou do Norte e estou participando do teste de voz do Itaú.",
}

# Cria a pasta de destino se não existir
os.makedirs("tests/audios", exist_ok=True)

# Gera os arquivos de áudio
for arquivo, texto in frases.items():
    tts = gTTS(text=texto, lang="pt-br")  # Português do Brasil
    caminho = os.path.join("tests/audios", arquivo)
    tts.save(caminho)
    print(f"🎙️ Áudio gerado: {caminho}")

print("\n✅ Todos os áudios foram criados com sucesso!")
