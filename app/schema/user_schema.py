from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class UserSchemaBase(BaseModel):
    cpf: str
    nome: Optional[str]
    endereco: Optional[str]
    estado: Optional[str]
    data_nasc: Optional[str]
    rg: Optional[str]
    telefone: Optional[str]
    cod_banco: Optional[str]
    nome_banco: Optional[str]
    agencia: Optional[str]
    conta_corrente: Optional[str]
    matricula: Optional[str]
    posto_trabalho: Optional[str]
    cargo: Optional[str]
    cidade: Optional[str]
    centro_custo: Optional[str]

    class Config:
        from_attributes = True


class UserSchemaUp(BaseModel):
    cpf: str = Field(..., min_length=11, max_length=11)
    cod_banco: Optional[str] = None
    nome_banco: Optional[str] = None
    agencia: Optional[str] = None
    conta_corrente: Optional[str] = None


class EmailSchema(BaseModel):
    email: EmailStr
