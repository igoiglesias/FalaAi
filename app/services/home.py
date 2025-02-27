import re
from bs4 import BeautifulSoup
from ..modules.tts import sintetizar_audio


class Home:

    def __init__(self) -> None:
        """Inicializa User."""
        pass

    async def text_to_audio(self, text: str) -> str:
        """Lista todos os usuários."""
        file_name = sintetizar_audio(self._clear_text(text))
        return file_name

    def _clear_text(self, text: str) -> str:
        text = BeautifulSoup(text, "html.parser").get_text()
        text = re.sub(r'[^\w\s@.-]', '', text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text