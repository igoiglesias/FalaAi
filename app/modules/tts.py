import os
from datetime import datetime
from gtts import gTTS


def sintetizar_audio(texto):
    """Gera áudio a partir de texto (Text-to-Speech) usando Google TTS"""
    file_name = f"{_generate_file_name()}.mp3"
    tts = gTTS(text=texto, lang="pt", tld="com.br")
    caminho_audio = os.path.abspath(f"app/static/audios/{file_name}")
    tts.save(caminho_audio)
    return file_name

def _generate_file_name() -> str:
    now = datetime.now()
    return str(round(now.timestamp()))