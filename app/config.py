from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ORACLE_DRIVER: str = ""
    ORACLE_USERNAME: str = ""
    ORACLE_PASSWORD: str = ""
    ORACLE_HOST: str = ""
    ORACLE_PORT: str = ""
    ORACLE_SERVICE_NAME: str = ""
    APP_PASSWORD: str = ""
    SENDER_EMAIL: str = ""
    RECEIVER_EMAIL: str = ""
    ORACLE_CLIENT_PATH: str = ""
    DRIVER: str = ""

    class Config:
        env_file = ".env"

settings = Settings()