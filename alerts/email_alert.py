# alerts/email_alert.py

import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = "123abc@gmail.com"
EMAIL_PASSWORD = "App Password that you set on Gmail app"
TO_EMAIL = "123abc@gmail.com"


def send_email_alert(subject, body):
    try:
        msg = EmailMessage()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = TO_EMAIL
        msg["Subject"] = subject
        msg.set_content(body)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=10) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

        print("[EMAIL] Alert sent!")
    except Exception as e:
        print(f"[EMAIL] Failed to send alert: {e}")
