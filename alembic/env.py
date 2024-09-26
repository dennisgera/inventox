from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
import os
from logging.config import fileConfig
from app.database import Base

# Load the dotenv file, if needed
from dotenv import load_dotenv

load_dotenv()  # This will load environment variables from a .env file if you use one

# this is the Alembic Config object, which provides access to the .ini file values.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# Get the DATABASE_URL from environment variables
database_url = os.getenv("DATABASE_URL")

# If it's not set, raise an error to alert the developer
if not database_url:
    raise ValueError("DATABASE_URL is not set in the environment.")

# Set the sqlalchemy.url dynamically
config.set_main_option("sqlalchemy.url", database_url)

# Add your model's MetaData object here for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata

# other stuff...


def run_migrations_offline():
    """Run migrations in 'offline' mode."""
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
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
