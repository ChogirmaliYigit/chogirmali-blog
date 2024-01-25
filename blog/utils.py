import os
import subprocess

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


def restart_server_service(pull_command, restart_command, project_directory=None):
    script_directory = os.path.dirname(os.path.abspath(__file__))
    script_directory = os.path.dirname(script_directory)
    subprocess.run(
        f"cd {project_directory if project_directory else script_directory} && {pull_command}",
        shell=True,
    )
    subprocess.run(restart_command, shell=True)
