from __future__ import with_statement
import sys
import os
from alembic import context
from sqlalchemy import engine_from_config, pool
from src.utils.database import Base
from src.models import *  # Import all models to ensure they are registered

config = context.config
config.set_main_option('sqlalchemy.url', os.getenv('DATABASE_URL', 'sqlite:///./my_payment_service.db'))

def run_migrations_offline():
    context.configure(url=config.get_main_option('sqlalchemy.url'), target_metadata=Base.metadata, literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(config.get_section(config.config_ini_section), prefix='sqlalchemy.', poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=Base.metadata)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
