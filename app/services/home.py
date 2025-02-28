import re
from bs4 import BeautifulSoup
from fastapi import Request

from ..modules.tts import sintetizar_audio
from ..models.conversoes import Convesoes


class Home:

    def __init__(self) -> None:
        """Inicializa User."""
        pass

    async def text_to_audio(self, text: str, request: Request) -> str:
        """Lista todos os usuários."""
        client_ip = await self.get_client_ip(request)
        file_name = sintetizar_audio(self._clear_text(text))
        await self.save_convesao(text, file_name, client_ip)
        return file_name

    def _clear_text(self, text: str) -> str:
        text = BeautifulSoup(text, "html.parser").get_text()
        text = re.sub(r'[^\w\s@.-]', '', text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    async def get_client_ip(self, request: Request):
        client_ip = request.headers.get("CF-Connecting-IP")  # IP real via Cloudflare

        if not client_ip:  # Se não estiver disponível, tenta X-Forwarded-For
            forwarded = request.headers.get("X-Forwarded-For")
            if forwarded:
                client_ip = forwarded.split(",")[0]  # Primeiro IP da lista
            else:
                client_ip = request.client.host  # Último recurso: IP direto

        return client_ip

    async def save_convesao(self, texto: str, audio: str, ip: str) -> None:
        conversao = Convesoes(
            texto=texto,
            audio=audio,
            ip=ip
        )
        await conversao.save()