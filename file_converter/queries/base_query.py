from abc import ABC, abstractmethod


class Query(ABC):
    def __init__(self):
        pass


    @staticmethod
    def get_format():
        raise NotImplementedError


    @abstractmethod
    def sort(self):
        raise NotImplementedError
    

    @abstractmethod
    def filter(self):
        raise NotImplementedError
    

    @abstractmethod
    def limit(self):
        raise NotImplementedError
