import os
import smtplib
from email.message import EmailMessage

def require_env(key: str) -> str:
    val = os.environ.get(key)
    if not val:
        raise RuntimeError(f"Missing env var: {key}")
    return val

def send_email(subject: str, body: str) -> None:
    email = require_env("GMAIL")
    app_password = require_env("GMAIL_APP_PASSWORD")

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = email
    msg["To"] = email
    msg.set_content(body)

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(email, app_password)
        server.send_message(msg)
