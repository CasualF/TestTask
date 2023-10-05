from fastapi import APIRouter, HTTPException, status
from app.mailer.schemas import EmailRequest, EmailSentSchema
from app.worker.tasks import send_mail_worker


router = APIRouter()


@router.post('/send_email', status_code=250, response_model=EmailSentSchema)
def send_requested_email(email_data: EmailRequest):
    try:
        send_mail_worker.delay(email_to=email_data.to,
                               subject=email_data.subject,
                               text=email_data.message)
        return {'msg': f"Email was sent to {email_data.to}"}
    except:
        return {'msg': f"Couldn't send email to {email_data.to}"}
