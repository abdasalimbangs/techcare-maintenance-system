from datetime import datetime

from sqlalchemy import (
    BigInteger,
    Boolean,
    CheckConstraint,
    DateTime,
    ForeignKey,
    String,
    Text,
    func
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base

class Produit(Base):
    __tablename__ = "produit"

    # Identifiant unique du produit.
    produit_id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )

    # Administrateur propriétaire du produit.
    administrateur_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("administrateur.administrateur_id"),
        nullable=False
    )

        # Informations principales du produit.
    nom: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    # Prix exprimé en francs guinéens, sans décimales.
    prix_actuel: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False
    )

    # Chemin ou référence de la photo stockée hors de la base.
    photo: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    # État commercial du produit.
    etat_disponibilite: Mapped[str] = mapped_column(
        String(30),
        default="DISPONIBLE",
        nullable=False
    )

    # Permet de masquer un produit sans supprimer son historique.
    est_actif: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )
    # Relation ORM avec l'administrateur propriétaire.
    administrateur: Mapped["Administrateur"] = relationship(
        back_populates="produits"
    )
    # Relation ORM avec une Demande.
    demandes: Mapped[list["Demande"]] = relationship(
        back_populates="produit"
    )
    # Dates de suivi.
    date_creation: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    date_modification: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

    __table_args__ = (
        CheckConstraint(
            "prix_actuel > 0",
            name="ck_produit_prix_positif"
        ),
    )