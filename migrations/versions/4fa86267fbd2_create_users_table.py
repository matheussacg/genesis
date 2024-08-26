from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "4fa86267fbd2"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Criação da tabela users
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("username", sa.String, unique=True, index=True),
        sa.Column(
            "hashed_password", sa.String, unique=False, index=True
        ),  # Adicionado o campo hashed_password
        sa.Column("email", sa.String, unique=True, index=True),
    )

    # Inserção de dados de teste
    users_table = sa.Table(
        "users",
        sa.MetaData(),
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("username", sa.String, unique=True, index=True),
        sa.Column(
            "hashed_password", sa.String, unique=False, index=True
        ),  # Adicionado o campo hashed_password
        sa.Column("email", sa.String, unique=True, index=True),
    )

    op.bulk_insert(
        users_table,
        [
            {
                "username": "alice",
                "hashed_password": "senha_hasheada_alice",
                "email": "alice@example.com",
            },
            {
                "username": "bob",
                "hashed_password": "senha_hasheada_bob",
                "email": "bob@example.com",
            },
            {
                "username": "jack",
                "hashed_password": "senha_hasheada_jack",
                "email": "jack@example.com",
            },
            {
                "username": "mat",
                "hashed_password": "senha_hasheada_mat",
                "email": "mat@exemple.com",
            },
        ],
    )


def downgrade() -> None:
    # Remoção da tabela users
    op.drop_table("users")
