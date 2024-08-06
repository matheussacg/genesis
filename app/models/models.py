from core.configs import settings
from sqlalchemy import Column, Date, String


# Tabela de funcionários
class Usuario(settings.DBBaseModel):
    __tablename__ = "usuario"

    cpf = Column(String(11), primary_key=True, unique=True, nullable=False)
    nome = Column(String(250))
    endereco = Column(String(250))
    estado = Column(String(250))
    data_nasc = Column(Date)
    rg = Column(String(12))
    telefone = Column(String(13))
    cod_banco = Column(String(4))
    nome_banco = Column(String(150), nullable=True)
    agencia = Column(String(6))
    conta_corrente = Column(String(14))
    matricula = Column(String(20))
    posto_trabalho = Column(String(250))
    cargo = Column(String(150))
    cidade = Column(String(250))
    centro_custo = Column(String(150))
