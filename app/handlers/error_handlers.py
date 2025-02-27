from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from starlette.requests import Request

async def api_error_handler(request: Request, exc: HTTPException):
    """
    Manipulador de erros para requisições de API.
    Retorna uma resposta JSON com detalhes do erro.
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "type": "HTTPException",
                "detail": exc.detail,
                "status_code": exc.status_code,
                "path": request.url.path,
            }
        },
    )