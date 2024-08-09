from typing import AsyncGenerator

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials
from jose import JWTError, jwt
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.auth import oauth2_schema
from app.core.configs import settings
from app.core.database import Session


async def get_session() -> AsyncGenerator:
    session: AsyncSession = Session()
    try:
        yield session
    finally:
        await session.close()


async def validate_form_token(
    token: HTTPAuthorizationCredentials = Depends(oauth2_schema),
) -> str:
    if token is None or not token.credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token de acesso não fornecido",
            headers={"WWW-Authenticate": "Bearer"},
        )

    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token de acesso inválido ou expirado",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token.credentials,
            settings.JWT_SECRET,
            algorithms=[settings.ALGORITHM],
            options={"verify_aud": False},
        )
        if "form_access" not in payload.get("scopes", []):
            raise credential_exception
    except JWTError:
        raise credential_exception

    return payload["sub"]
