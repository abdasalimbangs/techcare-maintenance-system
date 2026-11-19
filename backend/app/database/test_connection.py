from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings


# Construire l'URL de connexion vers la base réservée aux tests.
URL_BASE_TEST = URL.create(
    drivername="postgresql+psycopg",
    username=settings.DB_USER,
    password=settings.DB_PASSWORD,
    host=settings.DB_HOST,
    port=settings.DB_PORT,
    database=settings.TEST_DB_NAME,
)

# Créer un moteur SQLAlchemy indépendant de celui du développement.
engine_test = create_engine(URL_BASE_TEST)

# Préparer les sessions qui seront utilisées pendant les tests.
SessionTest = sessionmaker(
    bind=engine_test,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)
