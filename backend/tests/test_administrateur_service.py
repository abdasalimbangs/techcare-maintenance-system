import pytest
from app.core.securite import verifier_mot_de_passe
from app.models.administrateur import Administrateur
from app.schemas.administrateur import AdministrateurInscription
from app.services.administrateur_service import (
    creer_premier_administrateur,
)


def test_cree_premier_administrateur_avec_succes(
    db_session,
    monkeypatch,
):
    """Vérifier la création du premier administrateur."""

    # Simuler un code d'activation valide sans utiliser le vrai secret.
    monkeypatch.setattr(
        "app.services.administrateur_service.verifier_code_activation",
        lambda code: code == "CODE-TEST-VALIDE",
    )

    # Préparer les données d'inscription.
    donnees = AdministrateurInscription(
        nom="Diallo",
        prenom="Mamadou",
        email="mamadou.test@techcare.com",
        telephone="+224620000000",
        mot_de_passe="MotDePasseTest123!",
        code_activation="CODE-TEST-VALIDE",
    )

    # Appeler le service métier pour créer le compte.
    administrateur = creer_premier_administrateur(
        db=db_session,
        donnees=donnees,
    )

    # Vérifier que le service retourne bien un administrateur.
    assert isinstance(administrateur, Administrateur)

    # Vérifier que les informations principales sont enregistrées.
    assert administrateur.nom == "Diallo"
    assert administrateur.prenom == "Mamadou"
    assert administrateur.email == "mamadou.test@techcare.com"
    assert administrateur.est_actif is True

    # Vérifier que le mot de passe n'est pas enregistré en clair.
    assert administrateur.mot_de_passe_hash != "MotDePasseTest123!"

    # Vérifier que l'empreinte permet de reconnaître le bon mot de passe.
    assert verifier_mot_de_passe(
        "MotDePasseTest123!",
        administrateur.mot_de_passe_hash,
    )


def test_refuse_creation_avec_code_activation_incorrect(
    db_session,
    monkeypatch,
):
    """Vérifier qu'un code d'activation incorrect bloque la création."""

    # Simuler un code d'activation toujours refusé.
    monkeypatch.setattr(
        "app.services.administrateur_service.verifier_code_activation",
        lambda code: False,
    )

    # Préparer une inscription avec des données valides.
    donnees = AdministrateurInscription(
        nom="Diallo",
        prenom="Mamadou",
        email="mamadou.refus@example.com",
        telephone="+224620000001",
        mot_de_passe="MotDePasseTest123!",
        code_activation="MAUVAIS-CODE",
    )

    # Vérifier que le service refuse la création du compte.
    with pytest.raises(
        ValueError,
        match="Le code d'activation est incorrect.",
    ):
        creer_premier_administrateur(
            db=db_session,
            donnees=donnees,
        )

    # Vérifier qu'aucun administrateur n'a été enregistré.
    administrateur = db_session.query(Administrateur).first()

    assert administrateur is None

def test_refuse_creation_si_administrateur_existe_deja(
    db_session,
    monkeypatch,
):
    """Vérifier qu'un deuxième administrateur ne peut pas être créé."""

    # Simuler un code d'activation valide pour les deux inscriptions.
    monkeypatch.setattr(
        "app.services.administrateur_service.verifier_code_activation",
        lambda code: True,
    )

    # Préparer les données du premier administrateur.
    premier_compte = AdministrateurInscription(
        nom="Diallo",
        prenom="Mamadou",
        email="premier.admin@example.com",
        telephone="+224620000002",
        mot_de_passe="MotDePasseTest123!",
        code_activation="CODE-VALIDE",
    )

    # Créer le premier administrateur.
    creer_premier_administrateur(
        db=db_session,
        donnees=premier_compte,
    )

    # Préparer les données d'un deuxième administrateur.
    deuxieme_compte = AdministrateurInscription(
        nom="Bah",
        prenom="Ibrahima",
        email="deuxieme.admin@example.com",
        telephone="+224620000003",
        mot_de_passe="MotDePasseTest456!",
        code_activation="CODE-VALIDE",
    )

    # Vérifier que la deuxième création est refusée.
    with pytest.raises(
        ValueError,
        match="Le compte administrateur a déjà été créé.",
    ):
        creer_premier_administrateur(
            db=db_session,
            donnees=deuxieme_compte,
        )

    # Vérifier que le premier administrateur est toujours le seul enregistré.
    administrateurs = db_session.query(Administrateur).all()

    assert len(administrateurs) == 1
    assert administrateurs[0].email == "premier.admin@example.com"
