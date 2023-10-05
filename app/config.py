from pydantic import EmailStr
from pydantic_settings import BaseSettings
from typing import Optional, Literal
import os


class Settings(BaseSettings):
    title: str = 'Mailer'
    PROJECT_NAME: str
    ENVIRONMENT: str
    MODE: Literal['DEV', 'TEST', 'PROD']

    BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))

    REDIS_HOST: str
    REDIS_PORT: str

    SMTP_TLS: bool = True
    SMTP_PORT: Optional[int] = None
    SMTP_HOST: Optional[str] = None
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    EMAILS_FROM_EMAIL: Optional[EmailStr] = None
    EMAILS_FROM_NAME: Optional[str] = None

    EMAILS_ENABLED: bool = True

    class Config:
        env_file = '.env'


settings = Settings()

SHOW_DOCS_ENVIRONMENT = ('local', 'staging')

app_configs = {'title': 'Mailer'}


if settings.ENVIRONMENT not in SHOW_DOCS_ENVIRONMENT:
    app_configs['openapi_url'] = None
