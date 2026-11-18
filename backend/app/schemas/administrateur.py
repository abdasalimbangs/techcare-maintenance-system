
from datetime import datetime

from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
    Field,
    field_validator,
)


class AdministrateurInscription(BaseModel):
    """
    Schéma utilisé pour recevoir et valider
    les informations du formulaire d'inscription.
    """

    # Informations personnelles.
    nom: str = Field(min_length=1, max_length=100)
    prenom: str = Field(min_length=1, max_length=100)

    # Informations de contact.
    email: EmailStr
    telephone: str = Field(min_length=1, max_length=30)

    # Informations de sécurité.
    mot_de_passe: str = Field(min_length=12, max_length=128)
    code_activation: str = Field(min_length=1)

    @field_validator("email", mode="before")
    @classmethod
    def nettoyer_email(cls, valeur: str) -> str:
        """Supprimer les espaces autour de l'adresse e-mail."""
        if isinstance(valeur, str):
            return valeur.strip()

        return valeur

    @field_validator("nom", "prenom", "telephone")
    @classmethod
    def nettoyer_champs_texte(cls, valeur: str) -> str:
        """Nettoyer et vérifier les champs texte obligatoires."""
        valeur = valeur.strip()

        if not valeur:
            raise ValueError("Ce champ ne peut pas être vide.")

        return valeur

    @field_validator("code_activation")
    @classmethod
    def nettoyer_code_activation(cls, valeur: str) -> str:
        """Nettoyer et vérifier le code d'activation."""
        valeur = valeur.strip()

        if not valeur:
            raise ValueError("Le code d'activation ne peut pas être vide.")

        return valeur


class AdministrateurReponse(BaseModel):
    """
    Schéma utilisé pour renvoyer les informations
    publiques de l'administrateur après sa création.
    """

    administrateur_id: int
    nom: str
    prenom: str
    email: EmailStr
    telephone: str
    est_actif: bool
    date_creation: datetime
    date_modification: datetime

    # Autoriser la création du schéma à partir d'un objet SQLAlchemy.
    model_config = ConfigDict(from_attributes=True)
