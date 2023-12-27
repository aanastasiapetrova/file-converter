from abc import ABC, abstractmethod


class Parser(ABC):
    """Abstract parser's interface."""

    def __init__(self):
        pass

    @abstractmethod
    def parse(self):
        raise NotImplementedError
    
    @staticmethod
    #@abstractmethod
    def is_valid():
        raise NotImplementedError
