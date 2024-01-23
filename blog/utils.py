import requests
from django.conf import settings


def send_contact_info_to_telegram_chat(data):
    name = data.get("name")
    email_or_username = data.get("email_or_username")
    subject = data.get("subject")
    message = data.get("message")

    text = (
        f"New message: {subject}\n\n"
        f"From: {name}\n"
        f"Email or telegram: {email_or_username}\n"
        f"Message: {message}"
    )

    requests.post(
        f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage",
        data={
            "chat_id": settings.TELEGRAM_CHAT_ID,
            "text": text,
            "disable_web_page_preview": True,
        },
    )
