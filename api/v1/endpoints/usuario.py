from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema
from sqlalchemy.ext.asyncio import AsyncSession
from dotenv import load_dotenv
import os
from core.deps import get_session, validate_form_token
from core.auth import criar_token_acesso_formulario
from core.configs import config
from schema.usuario_schema import EmailSchema


load_dotenv()
link_acesso_base = os.getenv("LINK_ACESSO")

router = APIRouter()


@router.post("/enviar-link-acesso", status_code=status.HTTP_202_ACCEPTED)
async def enviar_link_acesso(
    email_schema: EmailSchema, db: AsyncSession = Depends(get_session)
):
    email = email_schema.email

    if not email.endswith("@fesfsus.ba.gov.br"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Apenas emails com o domínio @fesfsus.ba.gov.br são autorizados a receber o link de acesso.",
        )

    # Simulando a criação do token sem armazenar o email no banco
    token = criar_token_acesso_formulario(sub=email)

    # Construir o link de acesso com o token JWT
    link_acesso = f"http://{link_acesso_base}?token={token}"

    # Preparar o corpo do email
    message = MessageSchema(
        subject="Link de Acesso ao Sistema de Registro de Documentos",
        recipients=[email],
        body=f"Olá,<br><br>"
        f"Você solicitou um link de acesso ao Sistema de Registro de Documentos. Clique no link abaixo para acessar:<br>"
        f"<a href='{link_acesso}'>Clique aqui para acessar o sistema</a>",
        subtype="html",
    )

    # Enviar o email
    fm = FastMail(config)
    await fm.send_message(message)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "Email enviado com sucesso."},
    )
