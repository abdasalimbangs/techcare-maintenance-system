
from datetime import datetime, timezone
from types import SimpleNamespace

import pytest
from pydantic import ValidationError

from app.schemas.administrateur import (
    AdministrateurInscription,
    AdministrateurReponse,
)


def test_inscription_accepte_des_donnees_valides():
    donnees = {
        "nom": "Bangoura",
        "prenom": "Salim",
        "email": "salim@example.com",
        "telephone": "+224 620 00 00 00",
        "mot_de_passe": "MotDePasseSecurise123!",
        "code_activation": "CODE-TEST-123",
    }

    administrateur = AdministrateurInscription(**donnees)

    assert administrateur.nom == "Bangoura"
    assert administrateur.prenom == "Salim"
    assert administrateur.email == "salim@example.com"
    assert administrateur.telephone == "+224 620 00 00 00"


def test_inscription_nettoie_les_espaces_autour_des_textes():
    donnees = {
        "nom": "  Bangoura  ",
        "prenom": "  Salim  ",
        "email": "salim@example.com",
        "telephone": "  +224 620 00 00 00  ",
        "mot_de_passe": "MotDePasseSecurise123!",
        "code_activation": "CODE-TEST-123",
    }

    administrateur = AdministrateurInscription(**donnees)

    assert administrateur.nom == "Bangoura"
    assert administrateur.prenom == "Salim"
    assert administrateur.telephone == "+224 620 00 00 00"


def test_inscription_nettoie_email_et_code_activation():
    donnees = {
        "nom": "Bangoura",
        "prenom": "Salim",
        "email": "  salim@example.com  ",
        "telephone": "+224 620 00 00 00",
        "mot_de_passe": "MotDePasseSecurise123!",
        "code_activation": "  CODE-TEST-123  ",
    }

    administrateur = AdministrateurInscription(**donnees)

    assert administrateur.email == "salim@example.com"
    assert administrateur.code_activation == "CODE-TEST-123"


def test_inscription_refuse_un_email_invalide():
    donnees = {
        "nom": "Bangoura",
        "prenom": "Salim",
        "email": "adresse-invalide",
        "telephone": "+224 620 00 00 00",
        "mot_de_passe": "MotDePasseSecurise123!",
        "code_activation": "CODE-TEST-123",
    }

    with pytest.raises(ValidationError):
        AdministrateurInscription(**donnees)


def test_inscription_refuse_les_champs_texte_vides():
    donnees = {
        "nom": "   ",
        "prenom": "Salim",
        "email": "salim@example.com",
        "telephone": "+224 620 00 00 00",
        "mot_de_passe": "MotDePasseSecurise123!",
        "code_activation": "CODE-TEST-123",
    }

    with pytest.raises(ValidationError):
        AdministrateurInscription(**donnees)


def test_inscription_refuse_un_code_activation_vide():
    donnees = {
        "nom": "Bangoura",
        "prenom": "Salim",
        "email": "salim@example.com",
        "telephone": "+224 620 00 00 00",
        "mot_de_passe": "MotDePasseSecurise123!",
        "code_activation": "   ",
    }

    with pytest.raises(ValidationError):
        AdministrateurInscription(**donnees)


def test_inscription_refuse_un_mot_de_passe_trop_court():
    donnees = {
        "nom": "Bangoura",
        "prenom": "Salim",
        "email": "salim@example.com",
        "telephone": "+224 620 00 00 00",
        "mot_de_passe": "Court123!",
        "code_activation": "CODE-TEST-123",
    }

    with pytest.raises(ValidationError):
        AdministrateurInscription(**donnees)


def test_inscription_refuse_un_mot_de_passe_trop_long():
    donnees = {
        "nom": "Bangoura",
        "prenom": "Salim",
        "email": "salim@example.com",
        "telephone": "+224 620 00 00 00",
        "mot_de_passe": "A" * 129,
        "code_activation": "CODE-TEST-123",
    }

    with pytest.raises(ValidationError):
        AdministrateurInscription(**donnees)


def test_reponse_administrateur_ne_contient_aucune_donnee_secrete():
    donnees = {
        "administrateur_id": 1,
        "nom": "Bangoura",
        "prenom": "Salim",
        "email": "salim@example.com",
        "telephone": "+224 620 00 00 00",
        "est_actif": True,
        "date_creation": "2026-11-18T10:00:00+00:00",
        "date_modification": "2026-11-18T10:00:00+00:00",
    }

    reponse = AdministrateurReponse(**donnees)

    champs_reponse = reponse.model_dump().keys()

    assert "mot_de_passe" not in champs_reponse
    assert "mot_de_passe_hash" not in champs_reponse
    assert "code_activation" not in champs_reponse


def test_reponse_accepte_un_objet_avec_des_attributs():
    administrateur = SimpleNamespace(
        administrateur_id=1,
        nom="Bangoura",
        prenom="Salim",
        email="salim@example.com",
        telephone="+224 620 00 00 00",
        est_actif=True,
        date_creation=datetime.now(timezone.utc),
        date_modification=datetime.now(timezone.utc),
    )

    reponse = AdministrateurReponse.model_validate(administrateur)

    assert reponse.administrateur_id == 1
    assert reponse.nom == "Bangoura"
    assert reponse.email == "salim@example.com"
