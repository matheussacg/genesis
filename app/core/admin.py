from fastapi.requests import Request
from fastapi.security import HTTPAuthorizationCredentials
from sqladmin import Admin, ModelView
from sqladmin.authentication import AuthenticationBackend
from sqlalchemy.future import select

from app.core.auth import criar_token_acesso_formulario
from app.core.configs import settings
from app.core.database import Session, engine
from app.core.deps import validate_form_token
from app.core.security import verificar_senha
from app.models.models import User
from app.schemas.user_schema import UserLoginSchema


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        login_data = UserLoginSchema(**form)

        async with Session() as session:
            user = await session.execute(
                select(User).where(User.username == login_data.username)
            )
            user = user.scalar_one_or_none()

            if user is None or not verificar_senha(
                login_data.password, user.hashed_password
            ):
                return False

            token = criar_token_acesso_formulario(sub=user.id)
            request.session.update({"token": token})
            return True

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")

        if not token:
            return False

        # Cria um objeto HTTPAuthorizationCredentials a partir da string do token
        try:
            auth_credentials = HTTPAuthorizationCredentials(
                scheme="Bearer", credentials=token
            )

            # Passa o objeto para validate_form_token
            await validate_form_token(auth_credentials)
            return True
        except Exception:
            return False


# Configuração do SQLAdmin com autenticação
def init_admin(app):
    authentication_backend = AdminAuth(secret_key=settings.JWT_SECRET)
    admin = Admin(
        app=app, engine=engine, authentication_backend=authentication_backend
    )

    class UserAdmin(ModelView, model=User):
        column_list = [
            User.id,
            User.username,
            User.email,
        ]

        def is_visible(self, request: Request) -> bool:
            return True

        def is_accessible(self, request: Request) -> bool:
            return True

    admin.add_view(UserAdmin)
