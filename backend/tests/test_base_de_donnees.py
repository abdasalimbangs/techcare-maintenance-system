from uuid import uuid4
from sqlalchemy import func, inspect, select

# Importer le modèle Administrateur.
from app.models.administrateur import Administrateur

# Importer le moteur connecté à la base réservée aux tests.
from app.database.test_connection import engine_test


def test_les_tables_principales_existent():
    """Vérifier que les quatre tables métier sont présentes."""

    # Récupérer les noms des tables réellement présentes dans PostgreSQL.
    inspecteur = inspect(engine_test)
    tables = inspecteur.get_table_names()

    # Définir les tables que notre application doit posséder.
    tables_attendues = {
        "administrateur",
        "produit",
        "service",
        "demande",
    }

    # Vérifier que toutes les tables attendues existent.
    assert tables_attendues.issubset(set(tables))


def test_commit_ne_valide_pas_la_transaction_principale(db_session):
    """Vérifier qu'un commit reste isolé dans la transaction du test."""

    # Créer une adresse unique pour éviter les conflits entre les tests.
    email_test = f"test-{uuid4().hex}@techcare.local"

    # Préparer un administrateur avec les champs obligatoires.
    administrateur = Administrateur(
        nom="Test",
        prenom="Transaction",
        email=email_test,
        telephone="+224620000000",
        mot_de_passe_hash="empreinte-fictive-pour-test",
    )

    # Ajouter l'administrateur à la session de test.
    db_session.add(administrateur)

    # Envoyer l'INSERT à PostgreSQL sans valider la transaction principale.
    db_session.flush()

    # Vérifier que l'administrateur est déjà visible dans cette session.
    administrateur_apres_flush = db_session.execute(
        select(Administrateur).where(
            Administrateur.email == email_test
        )
    ).scalar_one_or_none()

    assert administrateur_apres_flush is not None

    # Simuler le commit effectué par un service métier.
    db_session.commit()

    # Vérifier que l'administrateur est visible dans la session du test.
    administrateur_enregistre = db_session.execute(
        select(Administrateur).where(
            Administrateur.email == email_test
        )
    ).scalar_one_or_none()

    assert administrateur_enregistre is not None

    # Vérifier depuis une autre connexion que la transaction principale
    # n'a pas encore rendu cet administrateur visible.
    with engine_test.connect() as autre_connexion:
        nombre_administrateurs = autre_connexion.execute(
            select(func.count())
            .select_from(Administrateur)
            .where(Administrateur.email == email_test)
        ).scalar_one()

    assert nombre_administrateurs == 0
