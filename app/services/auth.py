import functools
import jwt
import bcrypt
from datetime import datetime, timedelta
from fastapi.responses import JSONResponse, RedirectResponse

from ..config.settings import settings

HASH_SENHA = "$2b$12$Yc6QqjH6gyKZ6sa6Bd63XeegoDPOf2VELg8uJmDccNG1Qqay3dWpe"


class Auth:
    def __init__(self) -> None:
        """Inicializa User."""
        pass

    async def login(self, usuario: str, senha: str) -> JSONResponse:
        if self.check_password(senha, HASH_SENHA):
            token = self.generate_token({"sub": usuario})
            response = JSONResponse(content={"message": "Login realizado com sucesso!"})
            response.set_cookie(
                key=settings.TOKEN_KEY,
                value=token,
                httponly=settings.TOKEN_HTTPONLY,
                max_age=settings.ACCESS_TOKEN_EXPIRE_MINUTES,
                samesite="strict",
            )

            return response
        return JSONResponse(
            status_code=401, content={"message": "Credenciais inválidas"}
        )

    def generate_token(self, data: dict) -> str:
        expire = datetime.now() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
        data = {**data, "exp": expire}
        return jwt.encode(data, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    def validate_token(self, token) -> bool:
        try:
            if jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]):
                return True
            return False
        except:
            return False

    def is_auth(self):
        def decorator(fn):
            @functools.wraps(fn)
            async def wrapper(request, *args, **kwargs):
                token = request.cookies.get(settings.TOKEN_KEY)
                if not token or not self.validate_token(token):
                    return RedirectResponse("login", status_code=307)
                return await fn(request, *args, **kwargs)

            return wrapper

        return decorator

    @staticmethod
    def hash_password(password: str) -> str:
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    @staticmethod
    def check_password(password: str, hashed_password: str) -> bool:
        if not bcrypt.checkpw(password.encode(), hashed_password.encode()):
            return False
        return True
