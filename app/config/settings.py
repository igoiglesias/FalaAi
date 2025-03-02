import logging
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "FalaAi"
    APP_VERSION: str = "0.0.1"
    DEBUG: bool = True
    LOGGING_LEVEL: int = logging.INFO
    
    DATABASE_URL: str = "sqlite://app/database/db.sqlite3"
    
    TEMPLATE_FOLDER: str = "app/templates"
    STATIC_FOLDER: str = "app/static"
    
    SECRET_KEY: str = "mysecretkey"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 3600
    TOKEN_KEY: str = "access_token"
    TOKEN_SAMESITE: str = "samesite"
    TOKEN_HTTPONLY: bool = True
        
    SLOGANS: list = [
    "FalaAi – Porque nem o HAL 9000 fala sozinho! 🤖",
    "FalaAi – Transformando texto em áudio mais rápido que o C-3PO traduzindo! 🚀",
    "FalaAi – Dando voz ao seu texto, sem precisar de um Jarvis! 🎤",
    "FalaAi – Porque até o Groot gostaria de variar o vocabulário! 🌱",
    "FalaAi – Seu texto em áudio, sem precisar de um encantamento do D&D! ⚡",
    "FalaAi – Porque até o R2-D2 precisa de voz! 🔊",
    "FalaAi – O Text-to-Speech que o Sheldon aprovaria! 🧠",
    "FalaAi – Como se o BB-8 falasse de verdade! ⚙️",
    "FalaAi – Porque ler é muito século passado! 📚",
    "FalaAi – O TTS que o Mario diria ‘It’s-a me!’ 🍄",
    "FalaAi – Agora seu texto tem voz, sem precisar de um Dalek! 👽",
    "FalaAi – Porque até o Spock quer ouvir seu texto em áudio! 🖖",
    "FalaAi – Como um feitiço de sonorus para o seu texto! ✨",
    "FalaAi – Porque até o Darth Vader precisa de um dublador! 🎙️",
    "FalaAi – Agora até o Coringa pode ouvir sua piada! 🤡",
    "FalaAi – Seu texto falando mais rápido que o Flash! ⚡",
    "FalaAi – Porque até o KITT do Super Máquina fala! 🚗",
    "FalaAi – O jeito geek de dar voz à sua URA! 📞",
    "FalaAi – Como se o Neo do Matrix tivesse um assistente virtual! 💻",
    "FalaAi – Como um T-800 lendo seu texto para você! 🤖",
    "FalaAi – O TTS que vai te fazer ouvir até o futuro! ⏳",
    "FalaAi – Seu texto tem mais personalidade que o Tony Stark! 🦸‍♂️",
    "FalaAi – Falando como um Jedi, sem esforço! 🌠",
    "FalaAi – O TTS que dá voz até para o Baby Yoda! 👶",
    "FalaAi – Porque até o Capitão Kirk precisa de uma assistente! 🛸",
    "FalaAi – Como um assistente da Alexa, mas com mais estilo! 🎧",
    "FalaAi – Como se você tivesse um microfone do Dr. Who! 🎙️",
    "FalaAi – Seu texto falado mais rápido que o DeLorean! 🚗",
    "FalaAi – Dando voz ao seu conteúdo como um super-herói! 🦸‍♀️",
    "FalaAi – Transformando palavras em áudio com o poder do Thor! ⚡",
    "FalaAi – Porque até o Batman tem voz para falar com você! 🦇",
    "FalaAi – Seu texto, falado como um filme de Hollywood! 🎬",
    "FalaAi – Sem precisar de uma varinha mágica, só a tecnologia! ✨",
    "FalaAi – O futuro da leitura é ouvido! 🎧",
    "FalaAi – O que você digita, nós damos vida! 💬",
    "FalaAi – Transformando texto em música para os seus ouvidos! 🎶",
    "FalaAi – Porque até o R2-D2 fala mais do que você pensa! 🎙️",
    "FalaAi – Como se você tivesse um microfone de rádio, mas sem o estúdio! 🎤",
    "FalaAi – Transforme qualquer texto em um filme com voz! 🎥",
    "FalaAi – Porque até o Aladdin teria um “FalaAi” em seu tapete! 🧞‍♂️",
    "FalaAi – Falando mais do que o Pikachu, literalmente! ⚡",
    "FalaAi – Dando voz ao que você escreveu, como um supercomputador! 🖥️",
    "FalaAi – Seu texto vira som mais rápido que uma rede neural! 🤖",
    "FalaAi – O TTS mais geek que o Bat-Sinal! 🦇",
    "FalaAi – Porque até o Buzz Lightyear falaria seu texto! 🚀",
    "FalaAi – Como se você tivesse o poder de um supercomputador! 🖥️",
    "FalaAi – A magia do TTS para transformar tudo em voz! ✨",
    "FalaAi – Seu texto tem mais voz do que qualquer holograma! 📡",
    "FalaAi – Falando como o Hulk, mas sem gritar! 💪",
    "FalaAi – O TTS que até o Professor Xavier aprovaria! 🧠",
    "FalaAi – Colocando voz nos seus textos mais rápido que a velocidade da luz! 💨",
    "FalaAi – Porque até o Gandalf falaria seu texto em voz alta! 🧙‍♂️",
    "FalaAi – Seu texto em áudio mais rápido que uma fórmula química! 🧪",
    "FalaAi – Porque até o Ultron não pode calar sua voz! 🤖",
    "FalaAi – O TTS mais rápido do que uma corrida de F1! 🏎️",
    "FalaAi – O texto com a voz do futuro! 🔮"
]


    class Config:
        env_file = ".env"

settings = Settings()