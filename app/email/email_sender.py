import aiosmtplib
from email.message import EmailMessage
import logging
# import aioredis
import pika
from app.utils.validation import validate_email

class EmailSender:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        # self.redis = aioredis.from_url("redis://redis")
        # self.rabbitmq_connection = pika.BlockingConnection(
        #     pika.ConnectionParameters(host="rabbitmq")
        # )

    async def send(self, email):
        if not self.validate_email(email.to):
            raise Exception("Invalid email address")

        message = EmailMessage()
        message["Subject"] = email.subject
        message["From"] = "your_email@example.com"
        message["To"] = email.to
        message.set_content(email.message)

        try:
            await aiosmtplib.send(
                message,
                hostname="smtp.gmail.com",
                port=587,
                username="sebab63808@meogl.com",
                password="your_password"
            )

            self.logger.info("Email sent to: %s, Subject: %s", email.to, email.subject)

            # await self.save_email_to_redis(email.to, email.subject, email.message)

            # self.send_email_to_queue(email.to, email.subject, email.message)

        except Exception as e:
            self.logger.error("Failed to send email: %s", str(e))
            raise

    def validate_email(self, email):
        return validate_email(email)

    # async def save_email_to_redis(self, to, subject, message):
    #     key = f"email:{to}"
    #     email_data = {"to": to, "subject": subject, "message": message}
    #     await self.redis.hmset_dict(key, email_data)

    # def send_email_to_queue(self, to, subject, message):
    #     channel = self.rabbitmq_connection.channel()
    #     channel.queue_declare(queue="emails")
    #     channel.basic_publish(
    #         exchange="",
    #         routing_key="emails",
    #         body=f"{to},{subject},{message}"
    #     )
