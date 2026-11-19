
from app.core.securite import (
    hacher_mot_de_passe,
    verifier_mot_de_passe,
    verifier_code_activation,
)
from unittest.mock import patch


def test_accepte_un_code_activation_correct():
    with patch(
        "app.core.securite.settings.CODE_ACTIVATION",
        "CODE-SECRET-TEST"
    ):
        assert verifier_code_activation("CODE-SECRET-TEST") is True


def test_refuse_un_code_activation_incorrect():
    with patch(
        "app.core.securite.settings.CODE_ACTIVATION",
        "CODE-SECRET-TEST"
    ):
        assert verifier_code_activation("MAUVAIS-CODE") is False


def test_hache_un_mot_de_passe():
    mot_de_passe = "MotDePasseSecurise123!"

    resultat = hacher_mot_de_passe(mot_de_passe)

    assert resultat != mot_de_passe
    assert resultat != ""


def test_verifie_un_mot_de_passe_correct():
    mot_de_passe = "MotDePasseSecurise123!"
    mot_de_passe_hash = hacher_mot_de_passe(mot_de_passe)

    assert verifier_mot_de_passe(
        mot_de_passe,
        mot_de_passe_hash
    ) is True


def test_refuse_un_mot_de_passe_incorrect():
    mot_de_passe_hash = hacher_mot_de_passe(
        "MotDePasseSecurise123!"
    )

    assert verifier_mot_de_passe(
        "MauvaisMotDePasse123!",
        mot_de_passe_hash
    ) is False
