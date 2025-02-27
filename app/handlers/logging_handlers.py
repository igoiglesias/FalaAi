import logging
from logging.handlers import RotatingFileHandler
from ..config.settings import settings

LOG_FILE = "error.log"
def setup_logging():
    # Criar o formatter
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    # Criar handlers
    file_handler = RotatingFileHandler(LOG_FILE, maxBytes=10**6, backupCount=3)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(settings.LOGGING_LEVEL)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(settings.LOGGING_LEVEL)

    # Configurar o logger raiz
    root_logger = logging.getLogger()
    root_logger.setLevel(settings.LOGGING_LEVEL)
    root_logger.addHandler(file_handler)
    root_logger.addHandler(stream_handler)

    # Configurar o logger do Uvicorn e FastAPI
    for logger_name in ("uvicorn", "uvicorn.error", "uvicorn.access", "fastapi"):
        logger = logging.getLogger(logger_name)
        logger.setLevel(settings.LOGGING_LEVEL)
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)