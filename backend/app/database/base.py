from sqlalchemy.orm import DeclarativeBase


# Classe commune dont hériteront tous les modèles SQLAlchemy.
class Base(DeclarativeBase):
    pass
