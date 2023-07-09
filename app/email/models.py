from pydantic import BaseModel
from sqlalchemy import Column, String, Integer
from app.database import Base

class Email(BaseModel):
    to: str
    subject: str
    message: str


class EmailDB(Base):
    __tablename__ = "emails"

    id = Column(Integer, primary_key=True, index=True)
    to = Column(String, index=True)
    subject = Column(String)
    message = Column(String)