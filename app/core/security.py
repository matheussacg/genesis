import random
import secrets
import string

from passlib.context import CryptContext

CRIPTO = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verificar_senha(senha: str, hash_senha: str) -> bool:
    return CRIPTO.verify(senha, hash_senha)


def gerar_hash_senha(senha: str) -> str:
    return CRIPTO.hash(senha)


# GERADOR DE SENHA AUTO
def gerar_senha():
    letras_maiusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numero = string.digits

    senha = [
        secrets.choice(letras_maiusculas),
        secrets.choice(letras_minusculas),
    ]

    for _ in range(6):
        senha.append(
            secrets.choice(letras_maiusculas + letras_minusculas + numero)
        )

    random.shuffle(senha)
    senha = "".join(senha)

    return senha
