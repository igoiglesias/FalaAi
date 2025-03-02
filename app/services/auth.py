import functools
import jwt
from datetime import datetime, timedelta
from fastapi.responses import JSONResponse, RedirectResponse

from ..config.settings import Settings


class Auth:

    def __init__(self) -> None:
        """Inicializa User."""
        pass
    
    async def login(self, usuario: str, senha: str) -> JSONResponse:
        if usuario=='aidmin' and senha=='aidmin':
            token = self.generate_token({"sub": usuario})
            response = JSONResponse(content={"message": "Login realizado com sucesso!"})
            response.set_cookie(
                key=Settings.TOKEN_KEY,
                value=token,
                httponly=Settings.TOKEN_HTTPONLY,
                max_age=Settings.ACCESS_TOKEN_EXPIRE_MINUTES,
                samesite="Strict"
            )
            
            return response
        return JSONResponse(status_code=401, content={"message": "Credenciais inválidas"})

    def generate_token(self, data: dict) -> str:
        expire = datetime.now() + timedelta(minutes=Settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        data = {
            **data,
            "exp": expire
        }
        return jwt.encode(data, Settings.SECRET_KEY, algorithm=Settings.ALGORITHM)

    def is_auth(self):
        def decorator(fn):
            @functools.wraps(fn)
            async def wrapper(request, *args, **kwargs):
                token = request.cookies.get(Settings.TOKEN_KEY)
                if not token:
                    return RedirectResponse('login', status_code=307)
                return await fn(request, *args, **kwargs)
            return wrapper
        return decorator