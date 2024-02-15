from abc import ABC, abstractmethod


class Adapter(ABC):
    """Abstract adapter's interface."""

    def __init__(self):
        pass


    @staticmethod
    def get_format():
        raise NotImplementedError


    @abstractmethod
    def adapt(self):
        raise NotImplementedError
