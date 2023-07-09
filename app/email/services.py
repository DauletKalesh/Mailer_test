from app.email.models import Email
from app.email.repositories import EmailRepository
from app.email.email_sender import EmailSender


class EmailService:
    def __init__(self):
        self.email_repository = EmailRepository()
        self.email_sender = EmailSender()

    async def send_email(self, email: Email):
        await self.email_sender.send(email)
        await self.email_repository.save_email(email)
