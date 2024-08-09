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
        sa.Column("email", sa.String, unique=True, index=True),
    )

    # Inserção de dados de teste
    op.bulk_insert(
        sa.Table(
            "users",
            sa.MetaData(),
            autoload_with=op.get_bind(),  # Use a conexão ativa para carregar a tabela
        ),
        [
            {"username": "alice", "email": "alice@example.com"},
            {"username": "bob", "email": "bob@example.com"},
            {"username": "jack", "email": "jack@example.com"},
        ],
    )


def downgrade() -> None:
    # Remoção da tabela users
    op.drop_table("users")
