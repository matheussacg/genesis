import os
from typing import ClassVar

import dotenv
from fastapi_mail import ConnectionConfig
from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

dotenv.load_dotenv()

env: ClassVar[str] = os.getenv("ENV", "dev")


class Settings(BaseSettings):
    # Rota base da API
    TITLE: str = os.getenv("TITLE")
    API_V1_STR: str = os.getenv("API_V1_STR")

    # Configurações de banco de dados
    if env == "dev":
        DB_URL: ClassVar[str] = "sqlite+aiosqlite:///./dev.db"
    else:
        DB_NOME: ClassVar[str] = os.getenv("PROD_DB_NAME")
        DB_USER: ClassVar[str] = os.getenv("PROD_DB_USER")
        DB_SENHA: ClassVar[str] = os.getenv("PROD_DB_PASSWORD")
        DB_HOST: ClassVar[str] = os.getenv("PROD_DB_HOST")
        DB_PORT: ClassVar[str] = os.getenv("PROD_DB_PORT")

        # Verifica se todas as variáveis de ambiente foram carregadas corretamente
        if not all([DB_NOME, DB_USER, DB_SENHA, DB_HOST, DB_PORT]):
            raise ValueError(
                "Missing one or more environment variables for production database connection."
            )

        DB_URL: str = (
            f"postgresql+asyncpg://{DB_USER}:{DB_SENHA}@{DB_HOST}:{DB_PORT}/{DB_NOME}"
        )

    # Base de modelo do SQLAlchemy
    DBBaseModel: DeclarativeMeta = declarative_base()

    # Configurações para geração de tokens JWT
    JWT_SECRET: str = os.getenv("JWT_SECRET")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 8

    # Configurações de log e reload
    LOG_LEVEL: str = (
        os.getenv("DEV_LOG_LEVEL")
        if env == "development"
        else os.getenv("PROD_LOG_LEVEL")
    )
    RELOAD: bool = (
        os.getenv("DEV_RELOAD", "false").lower() == "true"
        if env == "development"
        else os.getenv("PROD_RELOAD").lower() == "true"
    )

    class Config:
        case_sensitive = True


# Instância das configurações da API
settings: Settings = Settings()

# print(f"Database URL: {settings.DB_URL}")
# print(f"TITLE: {settings.TITLE}")
# print(f"API_V1_STR: {settings.API_V1_STR}")

# Configurações de conexão com o servidor de e-mail
config = ConnectionConfig(
    MAIL_USERNAME=os.getenv("MAIL_USERNAME"),
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD"),
    MAIL_FROM=os.getenv("MAIL_FROM"),
    MAIL_PORT=587,
    MAIL_SERVER="smtp.office365.com",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
)
