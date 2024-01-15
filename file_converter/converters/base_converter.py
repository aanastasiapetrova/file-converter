from abc import ABC, abstractmethod


class Converter(ABC):
    """Abstract converter's interface."""

    def __init__(self):
        pass


    @staticmethod
    def get_format():
        raise NotImplementedError


    @abstractmethod
    def convert(self):
        raise NotImplementedError
