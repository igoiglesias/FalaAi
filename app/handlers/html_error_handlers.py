from fastapi.exceptions import HTTPException
from fastapi.templating import Jinja2Templates
from starlette.requests import Request


async def html_error_handler(request: Request, exc: HTTPException, templates: Jinja2Templates):
    """
    Manipulador de erros para páginas HTML.
    Renderiza um template com detalhes do erro.
    """
    context = {
        "request": request,
        "status_code": exc.status_code,
        "detail": exc.detail or "An error occurred.",
    }
    return templates.TemplateResponse("error.html", context, status_code=exc.status_code)