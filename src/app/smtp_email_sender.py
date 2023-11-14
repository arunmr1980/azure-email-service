import os

from app.email_sender_interface import EmailSenderInterface

class SMTPEmailSender(EmailSenderInterface):

    ''' 
        TODO
        - Implement email sending
    '''
    def send_email(self, request_dict):
        pass


    # TODO: Implement as per SMTP request format. Refer /events/request.json for request format
    def get_smtp_request(self, request_dict):
        channels = request_dict["channels"]
        req = {}
        
        '''
        for channel in channels:
            channel_type = channel["type"]
            if channel_type == "email":
                az_req["senderAddress"] = channel["from_address"]
                az_req["content"] = self.get_content(channel)
                az_req["recipients"] = self.get_recipients(channel)
        '''

        return az_req

'''
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
 '''               





