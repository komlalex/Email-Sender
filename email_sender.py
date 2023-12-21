import os
from dotenv import load_dotenv
from email.message import EmailMessage 

import ssl
import smtplib

load_dotenv()

EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")
PASSWORD = os.getenv("PASSWORD")


subject = "Hey, guess what's fun!"
body = """
When you feel board, write some python code. It will
cheer you up. I love writing Python.
"""

em = EmailMessage()
em["From"] = EMAIL_SENDER
em["To"] = EMAIL_RECEIVER
em["Subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as smtp:
    smtp.login(EMAIL_SENDER, PASSWORD)
    smtp.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, em.as_string())