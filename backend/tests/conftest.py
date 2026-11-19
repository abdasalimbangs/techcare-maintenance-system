import pytest
from sqlalchemy import text
from sqlalchemy.orm import Session

# Importer Base et tous les modèles pour enregistrer les tables.
from app.database.base import Base
from app.models import Administrateur, Produit, Service, Demande

# Importer le moteur réservé à la base de test.
from app.database.test_connection import engine_test


@pytest.fixture(scope="session", autouse=True)
def preparer_base_de_test():
    """
    Créer les tables une seule fois pour toute la session Pytest.
    """

    # Vérifier que nous utilisons bien la base de test.
    with engine_test.connect() as connexion:
        nom_base = connexion.execute(
            text("SELECT current_database()")
        ).scalar()

        assert nom_base == "bd_techcare_test", (
            "Les tests doivent utiliser uniquement bd_techcare_test."
        )

    # Créer les tables si elles n'existent pas déjà.
    Base.metadata.create_all(bind=engine_test)

    # Conserver les tables pendant et après les tests.
    yield


@pytest.fixture
def db_session(preparer_base_de_test):
    """
    Fournir une session isolée à chaque test utilisant la base.
    """

    # Ouvrir une connexion dédiée au test.
    connexion = engine_test.connect()

    # Démarrer une transaction principale contrôlée par Pytest.
    transaction = connexion.begin()

    # Créer une session liée à cette connexion.
    # Les commit() du code testé utilisent des transactions imbriquées
    # sans valider définitivement la transaction principale.
    session = Session(
        bind=connexion,
        join_transaction_mode="create_savepoint",
        autoflush=False,
        expire_on_commit=False,
    )

    try:
        # Mettre la session à disposition du test.
        yield session

    finally:
        # Fermer la session et libérer ses ressources.
        session.close()

        # Annuler toutes les modifications du test.
        if transaction.is_active:
            transaction.rollback()

        # Fermer la connexion.
        connexion.close()
