
from datetime import datetime

from sqlalchemy import BigInteger, Boolean, DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Administrateur(Base):
    __tablename__ = "administrateur"

    # Identifiant unique généré automatiquement.
    administrateur_id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, autoincrement=True
    )

    # Informations personnelles et de connexion.
    nom: Mapped[str] = mapped_column(String(100), nullable=False)
    prenom: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    telephone: Mapped[str] = mapped_column(String(30), nullable=False)
    mot_de_passe_hash: Mapped[str] = mapped_column(String(255), nullable=False)

    # Informations facultatives.
    adresse: Mapped[str | None] = mapped_column(String(255), nullable=True)
    photo_profil: Mapped[str | None] = mapped_column(String(255), nullable=True)

    # État du compte et dates de suivi.
    est_actif: Mapped[bool] = mapped_column(
        Boolean, default=True, nullable=False
    )

    # Relation ORM avec produit.
    produits: Mapped[list["Produit"]] = relationship(
        back_populates="administrateur"
    )

    # Relation ORM avec service.
    services: Mapped[list["Service"]] = relationship(
        back_populates="administrateur"
    )

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
