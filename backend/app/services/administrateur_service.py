
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.core.securite import (
    hacher_mot_de_passe,
    verifier_code_activation,
)
from app.models.administrateur import Administrateur
from app.schemas.administrateur import AdministrateurInscription


def creer_premier_administrateur(
    db: Session,
    donnees: AdministrateurInscription,
) -> Administrateur:
    """
    Créer le premier administrateur de TechCare Mini.

    Cette fonction applique les règles métier de l'inscription :
    - empêcher la création de plusieurs premiers administrateurs ;
    - vérifier le code d'activation ;
    - protéger le mot de passe avec Argon2 ;
    - enregistrer le compte dans PostgreSQL.
    """

    try:
        # Verrouiller la création du premier administrateur.
        # Le verrou reste actif jusqu'à la fin de cette transaction.
        db.execute(
            select(func.pg_advisory_xact_lock(224007))
        )

        # Vérifier si un administrateur existe déjà.
        administrateur_existant = db.execute(
            select(Administrateur.administrateur_id).limit(1)
        ).first()

        if administrateur_existant is not None:
            raise ValueError(
                "Le compte administrateur a déjà été créé."
            )

        # Vérifier le code d'activation fourni.
        if not verifier_code_activation(donnees.code_activation):
            raise ValueError("Le code d'activation est incorrect.")

        # Transformer le mot de passe avant son enregistrement.
        mot_de_passe_hash = hacher_mot_de_passe(
            donnees.mot_de_passe
        )

        # Préparer le nouvel administrateur sans enregistrer le code secret.
        nouvel_administrateur = Administrateur(
            nom=donnees.nom,
            prenom=donnees.prenom,
            email=str(donnees.email),
            telephone=donnees.telephone,
            mot_de_passe_hash=mot_de_passe_hash,
        )

        # Ajouter le compte à la transaction en cours.
        db.add(nouvel_administrateur)

        # Envoyer les changements à PostgreSQL.
        db.flush()

        # Valider définitivement la création du compte.
        db.commit()

        # Actualiser les données de l'objet après validation.
        db.refresh(nouvel_administrateur)

        return nouvel_administrateur

    except Exception:
        # Annuler toutes les modifications si une erreur survient.
        db.rollback()
        raise
