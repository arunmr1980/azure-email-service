
import os

from azure.communication.email import EmailClient
from app.email_sender_interface import EmailSenderInterface

class AzureEmailSender(EmailSenderInterface):

    #CONNECTION_STRING = "endpoint=https://hi-communication-service-1.unitedstates.communication.azure.com/;accesskey=mCkx5HCDawpyzB+f/OKn0YRWyKDxWp6xnnaKlVmjbeqR8yPVhaKxnl4rxE0qQK2X3b8dpHhsk7MSDaUL1T1czg==i"
    CONNECTION_STRING = os.environ.get("AZR_EMAIL_CONNECTION_STRING")


    def send_email(self, request_dict):

        if self.CONNECTION_STRING is None:
            raise ValueError("Required environment variable AZR_EMAIL_CONNECTION_STRING is not present")

        client = EmailClient.from_connection_string(self.CONNECTION_STRING)

        print('<--> Email client created ')
        message = self.get_azure_request(request_dict)
        print('Request in azure format')
        print(message)
        poller = client.begin_send(message)
        print('<--> Email sending initiated')
        result = poller.result()
        print('<--> Result ')
        print(result)


    def send_email_raw(self, request_dict):
        client = EmailClient.from_connection_string(self.CONNECTION_STRING)

        print('<--> Email client created ')
        message = {
                    "content": {
                        "subject": "This is the subject",
                        "plainText": "This is the body",
                        "html": "<html><h1>This is the body</h1></html>"
                    },
                    "recipients": {
                        "to": [
                            {
                                "address": "merry.arun@gmail.com",
                                "displayName": "Email from Azure"
                            }
                        ]
                    },
                    "senderAddress": "DoNotReply@81bc4d3f-8729-4379-884b-64c08d452238.azurecomm.net"
                }
        poller = client.begin_send(message)
        print('<--> Email sent')
        result = poller.result()
        print('<--> Result ')
        print(result)


    def get_azure_request(self, request_dict):
        channels = request_dict["channels"]
        az_req = {}

        for channel in channels:
            channel_type = channel["type"]
            if channel_type == "email":
                az_req["senderAddress"] = channel["from_address"]
                az_req["content"] = self.get_content(channel)
                az_req["recipients"] = self.get_recipients(channel)

        return az_req


    def get_content(self, channel):
        content = {
                    "subject": channel["subject"],
                    "plainText": channel["message_text"],
                    "html": channel["message_html"]
                }
        return content


    def get_recipients(self, channel):
        recipients_list = []
        recipients_dict = {
                            "to": recipients_list
                        }
        for to_address in channel["to_addresses"]:
            recipient_address = {
                        "address": to_address["identifier"],
                        "displayName": to_address["name"]
                    }
            recipients_list.append(recipient_address)
                    
        return recipients_dict
                





