
from app.database.base import Base
from app.database.connection import engine
from app import models


def initialiser_tables():
    """Crée les tables qui n'existent pas encore dans PostgreSQL."""
    Base.metadata.create_all(bind=engine)
