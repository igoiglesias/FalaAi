from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.exceptions import HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .config.settings import settings
from .database.connection import init_db, close_db
from .handlers.error_handlers import api_error_handler
from .handlers.html_error_handlers import html_error_handler
from .handlers.logging_handlers import setup_logging


setup_logging()

async def lifespan(app: FastAPI):
    """
    Gerencia o ciclo de vida da aplicação.
    Executa ações durante startup e shutdown.
    """
    print("Starting application...")
    await init_db()  # Conexão com o banco de dados
    yield  # Pausa aqui enquanto a aplicação está rodando
    print("Shutting down application...")
    await close_db()

app= FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan
)

templates = Jinja2Templates(directory=settings.TEMPLATE_FOLDER)

app.mount(
    '/static',
    StaticFiles(directory=settings.STATIC_FOLDER),
    name="static"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(404)
async def not_found_handler(request: Request, exc):
    return templates.TemplateResponse(
        "pages/404.html",
        {
            "request": request,
        }
    )

@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    """
    Define qual manipulador de erro será usado, dependendo do tipo de requisição.
    """
    breakpoint()
    accept_header = request.headers.get("accept", "")
    if "application/json" in accept_header or request.url.path.startswith("/api"):
        return await api_error_handler(request, exc)
    else:
        return await html_error_handler(request, exc, templates)
