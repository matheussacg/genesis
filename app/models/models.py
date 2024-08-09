from sqlalchemy import Column, Integer, String

from app.core.configs import settings


# Tabela de funcionários
class User(settings.DBBaseModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
