# Arquivo de configurações da api
import os

import dotenv
from fastapi_mail import ConnectionConfig
from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

dotenv.load_dotenv()


# Carregar variáveis de ambiente
db_nome = os.getenv("DB_NOME")
db_user = os.getenv("DB_USER")
db_senha = os.getenv("DB_SENHA")
db_host = os.getenv("DB_HOST")
jwt_token = os.getenv("JWT_SECRET")


# Classe para armazenar configurações da api
class Settings(BaseSettings):
    # Rota base da API
    API_V1_STR: str = "/api/v1"
    # URL do banco de dados
    DB_URL: str = f"postgresql+asyncpg://{db_user}:{db_senha}@{db_host}:5432/{db_nome}"
    # Base de modelo do SQLAlchemy
    DBBaseModel: DeclarativeMeta = declarative_base()
    # Configurações para geração de tokens JWT
    JWT_SECRET: str = jwt_token
    ALGORITHM: str = "HS256"
    # 60 minutos * 8 horas * 8 horas
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 8

    class Config:
        case_sensitive = True


# Instância das configurações da api
settings: Settings = Settings()


# Configurações de conexão com o servidor de e-mail
config = ConnectionConfig(
    MAIL_USERNAME=os.environ["MAIL_USERNAME"],
    MAIL_PASSWORD=os.environ["MAIL_PASSWORD"],
    MAIL_FROM=os.environ["MAIL_FROM"],
    MAIL_PORT=587,
    MAIL_SERVER="smtp.office365.com",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
)
