from sqlalchemy import inspect
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
