# import logging
from emails import Message

from app.config import settings


def send_email(
        email_to: str,
        subject: str = '',
        text: str = '',
) -> None:
    assert settings.EMAILS_ENABLED, "emails are disabled"
    message = Message(
        subject=subject,
        text=text,
        mail_from=(settings.EMAILS_FROM_NAME, settings.EMAILS_FROM_EMAIL)
    )
    smtp_options = {"host": settings.SMTP_HOST, "port": settings.SMTP_PORT}
    if settings.SMTP_TLS:
        smtp_options["tls"] = True
    if settings.SMTP_USER:
        smtp_options["user"] = settings.SMTP_USER
    if settings.SMTP_PASSWORD:
        smtp_options["password"] = settings.SMTP_PASSWORD
    response = message.send(to=email_to, smtp=smtp_options)
    # logging.info(f"send email result: {response}")
    return response
