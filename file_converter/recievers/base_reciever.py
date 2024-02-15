from abc import ABC, abstractmethod


class Reciever(ABC):

    def __init__(self):
        pass


    @staticmethod
    def get_format():
        pass
    

    @staticmethod
    def can_recieve():
        pass
    

    @abstractmethod
    def recieve(self):
        pass