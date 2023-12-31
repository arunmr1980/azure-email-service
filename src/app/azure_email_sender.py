import os

from azure.communication.email import EmailClient
from app.email_sender_interface import EmailSenderInterface

class AzureEmailSender(EmailSenderInterface):

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
                





