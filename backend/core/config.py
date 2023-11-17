import secrets
from os.path import join, dirname
from typing import Optional

from dotenv import load_dotenv
from pydantic import PostgresDsn
from pydantic import field_validator, ValidationInfo
from pydantic_settings import BaseSettings

from backend.utils.env_loader import load_env

dotenv_path = join(dirname(__file__), "../", ".env")
load_dotenv(dotenv_path)


class AppSetting(BaseSettings):
    # PROJECT
    PROJECT_NAME: str = load_env("PROJECT_NAME", required=True)

    # POSTGRES
    POSTGRES_USER: str = load_env("POSTGRES_USER", required=True)
    POSTGRES_PASSWORD: str = load_env("POSTGRES_PASSWORD", required=True)
    POSTGRES_DB: str = load_env("POSTGRES_DB", required=True)
    POSTGRES_HOST: str = load_env("POSTGRES_HOST", required=True)

    # REDIS
    REDIS_HOST: str = load_env("REDIS_HOST", required=True)
    REDIS_PORT: int = load_env("REDIS_PORT", "6379", as_type=int)

    # # MYSQL
    # MYSQL_USER: str = load_env("MYSQL_USER", required=True)
    # MYSQL_PASSWORD: str = load_env("MYSQL_PASSWORD", required=True)
    # MYSQL_DB_NAME: str = load_env("MYSQL_DB_NAME", required=True)
    # MYSQL_HOST: str = load_env("MYSQL_HOST", required=True)
    # MYSQL_PORT: int = load_env("MYSQL_PORT", required=True, as_type=int)

    # JWT
    JWT_SECRET: str = load_env("JWT_SECRET", secrets.token_urlsafe(32))
    JWT_EXPIRE_MINUTE: int = load_env(
        "JWT_EXPIRE_MINUTE", str(60 * 24 * 8), as_type=int
    )

    SQLALCHEMY_DATABASE_URL: Optional[str] = None

    @field_validator("SQLALCHEMY_DATABASE_URL", mode="after")
    def assemble_db_connection(cls, v: Optional[str], info: ValidationInfo) -> str:
        if isinstance(v, str):
            return v

        return f"postgresql+asyncpg://${info.data.get('POSTGRES_USER')}:${info.data.get('POSTGRES_PASSWORD')}@${info.data.get('POSTGRES_HOST')}/${info.data.get('POSTGRES_DB')}"

    # @field_validator("SQLALCHEMY_DATABASE_URL")
    # def assemble_db_connection(cls, v: Optional[str], values: ValidationInfo) -> str:
    #     if isinstance(v, str):
    #         return v
    #
    #     return f"mysql+pymysql://{values.data.get('MYSQL_USER')}:{values.data.get('MYSQL_PASSWORD')}@{values.data.get('MYSQL_HOST')}:{values.data.get('MYSQL_PORT')}/{values.data.get('MYSQL_DB_NAME')}"


settings = AppSetting()
