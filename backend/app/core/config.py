from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Paramètres de connexion à PostgreSQL pour le développement.
    DB_HOST: str
    DB_PORT: int = 5432
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str

    # Nom de la base réservée aux tests automatisés.
    # Elle utilise le même serveur et le même utilisateur PostgreSQL.
    TEST_DB_NAME: str = "bd_techcare_test"

    # Paramètre secret utilisé pour créer le premier administrateur.
    CODE_ACTIVATION: str

    # Charge les variables depuis le fichier .env.
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )


settings = Settings()
