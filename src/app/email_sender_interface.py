from abc import ABC, abstractmethod

class EmailSenderInterface(ABC):

    @abstractmethod
    def send_email(self, request_dict):
        pass


