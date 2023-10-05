from app.mailer.utils import send_email
from app.worker.celery_app import celery
from pydantic import EmailStr


@celery.task
def send_mail_worker(email_to: EmailStr, subject: str, text: str):
    send_email(email_to, subject, text)
