import os
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from app.cv.models import CvModel, SkillModel

from dotenv import load_dotenv
load_dotenv()

from app.db.base import Base  # <-- importuj swoje Base

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Wersja sync connection string
DATABASE_URL = os.getenv("DATABASE_URL").replace("+asyncpg", "+psycopg2")
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# Interpret the config file for Python logging.
fileConfig(config.config_file_name)

# metadata do autogeneracji
target_metadata = Base.metadata  # <-- TU

def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
