import re

from pydantic import BaseModel, Field, validator
from validate_docbr import CPF


class UsuarioCPF(BaseModel):
    cpf: str = Field(..., min_length=11, max_length=11)

    @validator("cpf")
    def validar_cpf(cls, cpf: str) -> str:
        cpf_numerico = re.sub(r"\D", "", cpf)

        # Verificar o tamanho do CPF
        if len(cpf_numerico) != 11:
            raise ValueError("O CPF deve conter 11 dígitos numéricos")

        # Verificar se o CPF é válido
        cpf_validator = CPF()
        if not cpf_validator.validate(cpf_numerico):
            raise ValueError("CPF inválido")

        return cpf_numerico
