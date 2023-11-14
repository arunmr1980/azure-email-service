
import json
import os

from app.azure_email_sender import AzureEmailSender
from app.smtp_email_sender import SMTPEmailSender

JSON_REQUEST_FILE_PATH = '../events/request.json'

EMAIL_SERVICE_PROVIDER = "AZURE"

def test_email(email_sender):
    email_sender.send_email(get_request_json())


def get_request_json():
    with open(JSON_REQUEST_FILE_PATH, 'r') as file:
        json_req = json.load(file)
    return json_req


email_sender = None
if EMAIL_SERVICE_PROVIDER == "AZURE":
    email_sender = AzureEmailSender()
elif EMAIL_SERVICE_PROVIDER == "SMTP":
    email_sender = SMTPEmailSender()


test_email(email_sender)

