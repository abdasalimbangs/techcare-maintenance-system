
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


class Service(Base):
    __tablename__ = "service"

    # Le prix doit respecter le mode de tarification choisi.
    __table_args__ = (
        CheckConstraint(
            """
            (
                type_tarification = 'PRIX_FIXE'
                AND prix IS NOT NULL
                AND prix > 0
            )
            OR
            (
                type_tarification = 'PRIX_SUR_DEMANDE'
                AND prix IS NULL
            )
            """,
            name="ck_service_tarification_prix"
        ),
        CheckConstraint(
            "type_tarification IN ('PRIX_FIXE', 'PRIX_SUR_DEMANDE')",
            name="ck_service_type_tarification"
        ),
        CheckConstraint(
            "etat_disponibilite IN ('DISPONIBLE', 'INDISPONIBLE')",
            name="ck_service_etat_disponibilite"
        ),
    )

    # Identifiant unique du service.
    service_id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )

    # Administrateur propriétaire du service.
    administrateur_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("administrateur.administrateur_id"),
        nullable=False
    )

    # Informations principales du service.
    nom: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    # Mode de tarification et prix en GNF.
    type_tarification: Mapped[str] = mapped_column(
        String(30),
        nullable=False
    )

    prix: Mapped[int | None] = mapped_column(
        BigInteger,
        nullable=True
    )

    # Référence de la photo stockée hors de la base.
    photo: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    # Disponibilité commerciale du service.
    etat_disponibilite: Mapped[str] = mapped_column(
        String(30),
        default="DISPONIBLE",
        nullable=False
    )

    # Permet de masquer un service sans le supprimer.
    est_actif: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
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

    # Relation ORM avec l'administrateur propriétaire.
    administrateur: Mapped["Administrateur"] = relationship(
        back_populates="services"
    )

    # Relation ORM avec une demande.
    demandes: Mapped[list["Demande"]] = relationship(
        back_populates="service"
    )
