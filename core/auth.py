from datetime import datetime, timedelta

from fastapi.security import HTTPBearer
from jose import jwt
from pytz import timezone

from core.configs import settings

oauth2_schema = HTTPBearer(bearerFormat="JWT", auto_error=False)


def criar_token(
    tipo_token: str, tempo_vida: timedelta, sub: str, scopes: list[str] = []
) -> str:

    payload = {}

    ba = timezone("America/Bahia")
    expira = datetime.now(tz=ba) + tempo_vida

    payload["type"] = tipo_token

    payload["exp"] = expira

    payload["iat"] = datetime.now(tz=ba)

    payload["sub"] = str(sub)

    payload["scopes"] = scopes

    return jwt.encode(
        payload, settings.JWT_SECRET, algorithm=settings.ALGORITHM
    )


def criar_token_acesso(sub: str, scopes: list[str] = []) -> str:

    return criar_token(
        tipo_token="access_token",
        tempo_vida=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        sub=sub,
        scopes=scopes,
    )


def criar_token_acesso_formulario(sub: str) -> str:
    return criar_token_acesso(sub=sub, scopes=["form_access"])
