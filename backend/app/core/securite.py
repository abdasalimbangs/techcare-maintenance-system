
import secrets
from pwdlib import PasswordHash
from app.core.config import settings


# Préparer le système de hachage avec Argon2.
hachage_mot_de_passe = PasswordHash.recommended()


def verifier_code_activation(code_fourni: str) -> bool:
    """Vérifier le code d'activation fourni."""

    return secrets.compare_digest(
        code_fourni,
        settings.CODE_ACTIVATION
    )


def hacher_mot_de_passe(mot_de_passe: str) -> str:
    """Transformer un mot de passe en empreinte sécurisée."""

    return hachage_mot_de_passe.hash(mot_de_passe)


def verifier_mot_de_passe(
    mot_de_passe_fourni: str,
    mot_de_passe_hash: str
) -> bool:
    """Vérifier un mot de passe à partir de son empreinte."""

    return hachage_mot_de_passe.verify(
        mot_de_passe_fourni,
        mot_de_passe_hash
    )
