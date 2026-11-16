from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Paramètres de connexion à PostgreSQL.
    DB_HOST: str
    DB_PORT: int = 5432
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str

    # Charge les variables depuis le fichier .env.
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )


settings = Settings()
