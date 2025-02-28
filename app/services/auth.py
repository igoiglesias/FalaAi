import functools
import jwt
from datetime import datetime, timedelta
from fastapi.responses import JSONResponse, RedirectResponse

SECRET_KEY = "mysecretkey"  # Troque isso por uma chave mais segura
ALGORITHM = "HS256"         # Algoritmo de assinatura
ACCESS_TOKEN_EXPIRE_MINUTES = 3600


class Auth:

    def __init__(self) -> None:
        """Inicializa User."""
        pass
    
    async def login(self, usuario: str, senha: str) -> JSONResponse:
        if usuario=='aidmin' and senha=='aidmin':
            expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            data = {
                "sub": usuario,
                "exp": expire
            }
            token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
            response = JSONResponse(content={"message": "Login realizado com sucesso!"})
            response.set_cookie(
                key="access_token",
                value=token,
                httponly=True,
                max_age=3600,
                samesite="Strict"
            )
            
            return response
        return JSONResponse(status_code=401, content={"message": "Credenciais inválidas"})
    
    def is_auth(self):
        def decorator(fn):
            @functools.wraps(fn)
            async def wrapper(request, *args, **kwargs):
                token = request.cookies.get(f"access_token")
                if not token:
                    return RedirectResponse('login', status_code=307)
                return await fn(request, *args, **kwargs)
            return wrapper
        return decorator