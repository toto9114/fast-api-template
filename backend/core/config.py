from typing import Optional, Dict, Any
from os.path import join, dirname
from pydantic import BaseSettings, validator
from dotenv import load_dotenv
from backend.utils.env_loader import load_env

dotenv_path = join(dirname(__file__), "../", ".env")
load_dotenv(dotenv_path)


class AppSetting(BaseSettings):
    # PROJECT
    PROJECT_NAME: str = load_env("PROJECT_NAME", required=True)

    # MYSQL
    MYSQL_USER: str = load_env("MYSQL_USER", required=True)
    MYSQL_PASSWORD: str = load_env("MYSQL_PASSWORD", required=True)
    MYSQL_DB_NAME: str = load_env("MYSQL_DB_NAME", required=True)
    MYSQL_HOST: str = load_env("MYSQL_HOST", required=True)
    MYSQL_PORT: int = load_env("MYSQL_PORT", required=True, as_type=int)

    SQLALCHEMY_DATABASE_URL: Optional[str] = None

    @validator("SQLALCHEMY_DATABASE_URL", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> str:
        if isinstance(v, str):
            return v
        return f"mysql+pymysql://{values['MYSQL_USER']}:{values['MYSQL_PASSWORD']}@{values['MYSQL_HOST']}:{values['MYSQL_PORT']}/{values['MYSQL_DB_NAME']}"


settings = AppSetting()
