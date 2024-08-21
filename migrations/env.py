import asyncio
from logging.config import fileConfig

from alembic import context
from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import async_engine_from_config

from app.core.configs import settings

config = context.config

database = settings.DB_BANCO
print(f"Usando banco de dados: {database}")

config.set_main_option("sqlalchemy.url", settings.DB_URL)

# Interpret the config file for Python logging.
if context.config.config_file_name is not None:
    fileConfig(context.config.config_file_name)

# Add your model's MetaData object here
target_metadata = settings.DBBaseModel.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = settings.DB_URL
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    """Run migrations in 'online' mode."""
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


async def run_async_migrations() -> None:
    url = settings.DB_URL
    print(f"Conectando ao banco de dados: {database}")
    connectable = async_engine_from_config(
        {
            "sqlalchemy.url": url,
        },
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    asyncio.run(run_async_migrations())


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
