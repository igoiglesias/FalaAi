import os
import hashlib
from datetime import datetime
from gtts import gTTS


def sintetizar_audio(texto: str) -> str:
    """Gera áudio a partir de texto (Text-to-Speech) usando Google TTS"""
    file_name = f"{_generate_file_name(texto)}.mp3"
    tts = gTTS(text=texto, lang="pt", tld="com.br")
    caminho_audio = os.path.abspath(f"app/static/audios/{file_name}")
    tts.save(caminho_audio)
    return file_name

def _generate_file_name(texto: str) -> str:
    return hashlib.sha1(texto.encode('utf-8')).hexdigest()