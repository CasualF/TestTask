from pydantic import BaseModel, EmailStr


class EmailRequest(BaseModel):
    to: EmailStr
    subject: str
    message: str


class EmailSentSchema(BaseModel):
    msg: str
