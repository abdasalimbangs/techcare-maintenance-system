
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker

from app.core.config import settings


# Construit l'URL sans exposer le mot de passe dans le code.
DATABASE_URL = URL.create(
    drivername="postgresql+psycopg",
    username=settings.DB_USER,
    password=settings.DB_PASSWORD,
    host=settings.DB_HOST,
    port=settings.DB_PORT,
    database=settings.DB_NAME
)

# Gère les connexions à PostgreSQL.
engine = create_engine(DATABASE_URL)

# Crée les sessions utilisées pour accéder aux données.
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


def get_db():
    """Fournit une session et garantit sa fermeture."""
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
