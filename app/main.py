from fastapi import FastAPI

from app.config import app_configs
from app.mailer.router import router as mail_router

app = FastAPI(**app_configs)
app.include_router(mail_router)
