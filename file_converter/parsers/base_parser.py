from abc import ABC, abstractmethod


class Parser(ABC):
    """Abstract parser's interface."""

    def __init__(self):
        pass
    

    @abstractmethod
    def parse(self):
        raise NotImplementedError
    

    @staticmethod
    def get_format():
        raise NotImplementedError
    
    
    @staticmethod
    def can_parse():
        raise NotImplementedError
