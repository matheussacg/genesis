import os

from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema

from core.auth import criar_token_acesso_formulario
from core.configs import config
from schema.usuario_schema import EmailSchema

load_dotenv()
link_acesso_base = os.getenv("LINK_ACESSO")

router = APIRouter()


@router.post("/enviar-link-acesso", status_code=status.HTTP_202_ACCEPTED)
async def enviar_link_acesso(email_schema: EmailSchema):
    email = email_schema.email

    if not email.endswith("@fesfsus.ba.gov.br"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=(
                "Apenas emails com o domínio @fesfsus.ba.gov.br"
                "são autorizados"
                "a receber o link de acesso."
            ),
        )

    # Simulando a criação do token sem armazenar o email no banco
    token = criar_token_acesso_formulario(sub=email)

    # Construir o link de acesso com o token JWT
    link_acesso = f"http://{link_acesso_base}?token={token}"

    # Preparar o corpo do email
    body = (
        "Olá,<br><br>"
        "Você solicitou um link de acesso ao Sistema de Registro de "
        "Documentos. "
        "Clique no link abaixo para acessar:<br>"
        f"<a href='{link_acesso}'>Clique aqui para acessar o sistema</a>"
    )

    message = MessageSchema(
        subject="Link de Acesso ao Sistema de Registro de Documentos",
        recipients=[email],
        body=body,
        subtype="html",
    )

    # Enviar o email
    fm = FastMail(config)
    await fm.send_message(message)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "Email enviado com sucesso."},
    )
