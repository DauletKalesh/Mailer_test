from app.database import SessionLocal
from app.email.models import EmailDB

class EmailRepository:
    def __init__(self):
        self.db = SessionLocal()

    def save_email(self, email):
        email_db = EmailDB(to=email.to, subject=email.subject, message=email.message)
        self.db.add(email_db)
        self.db.commit()
        self.db.refresh(email_db)
        return email_db