import os
import dotenv
from fastapi_mail import ConnectionConfig
from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

dotenv.load_dotenv()

env = os.getenv("ENV", "development")


# Classe para armazenar configurações da api
class Settings(BaseSettings):
    # Rota base da API
    API_V1_STR: str = os.getenv("API_V1_STR", "/api/v1")

    # Configurações de banco de dados
    if env == "development":
        DB_URL: str = "sqlite+aiosqlite:///./dev.db"
    else:
        DB_NOME = os.getenv("PROD_DB_NOME")
        DB_USER = os.getenv("PROD_DB_USER")
        DB_SENHA = os.getenv("PROD_DB_SENHA")
        DB_HOST = os.getenv("PROD_DB_HOST")
        DB_PORT = os.getenv("PROD_DB_PORT")
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


# Instância das configurações da api
settings: Settings = Settings()

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
