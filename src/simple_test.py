
import json

from app.azure_email_sender import AzureEmailSender

JSON_REQUEST_FILE_PATH = '../events/request.json'

def test_email(email_sender):
    email_sender.send_email(get_request_json())


def get_request_json():
    with open(JSON_REQUEST_FILE_PATH, 'r') as file:
        json_req = json.load(file)
    return json_req


azure_email_sender = AzureEmailSender()
test_email(azure_email_sender)

