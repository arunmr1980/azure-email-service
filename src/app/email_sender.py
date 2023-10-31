from azure.communication.email import EmailClient

connection_string = "endpoint=https://hi-communication-service-1.unitedstates.communication.azure.com/;accesskey=mCkx5HCDawpyzB+f/OKn0YRWyKDxWp6xnnaKlVmjbeqR8yPVhaKxnl4rxE0qQK2X3b8dpHhsk7MSDaUL1T1czg==i"
client = EmailClient.from_connection_string(connection_string)

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
