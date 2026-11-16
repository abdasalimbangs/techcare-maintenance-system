
from datetime import datetime

from sqlalchemy import (
    BigInteger,
    CheckConstraint,
    DateTime,
    ForeignKey,
    String,
    Text,
    func
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Demande(Base):
    __tablename__ = "demande"

    # Une demande doit concerner exactement un produit ou un service.
    __table_args__ = (
        CheckConstraint(
            """
            (
                produit_id IS NOT NULL
                AND service_id IS NULL
            )
            OR
            (
                produit_id IS NULL
                AND service_id IS NOT NULL
            )
            """,
            name="ck_demande_produit_ou_service"
        ),
        CheckConstraint(
            "statut IN ('NOUVELLE', 'EN_COURS', 'TRAITEE')",
            name="ck_demande_statut"
        ),
    )

    # Identifiant unique de la demande.
    demande_id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )

    # Coordonnées du client.
    nom_client: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    telephone_client: Mapped[str] = mapped_column(
        String(30),
        nullable=False
    )

    email_client: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    message: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    # Une seule des deux références doit être renseignée.
    produit_id: Mapped[int | None] = mapped_column(
        BigInteger,
        ForeignKey("produit.produit_id"),
        nullable=True
    )

    service_id: Mapped[int | None] = mapped_column(
        BigInteger,
        ForeignKey("service.service_id"),
        nullable=True
    )

    # Statut de traitement de la demande.
    statut: Mapped[str] = mapped_column(
        String(20),
        default="NOUVELLE",
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

    # Relations ORM avec le produit et le service concernés.
    produit: Mapped["Produit | None"] = relationship(
        back_populates="demandes"
    )

    service: Mapped["Service | None"] = relationship(
        back_populates="demandes"
    )
