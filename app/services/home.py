from ..modules.tts import sintetizar_audio


class Home:

    def __init__(self) -> None:
        """Inicializa User."""
        pass

    async def text_to_audio(self, text: str) -> str:
        """Lista todos os usuários."""
        file_name = sintetizar_audio(text)
        return file_name
