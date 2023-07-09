from fastapi import FastAPI
from app.email.services import EmailService
from app.email.models import Email

app = FastAPI()
email_service = EmailService()


@app.post("/send_email")
async def send_email(email: Email):
    await email_service.send_email(email)
    return {"message": "Email sent"}
