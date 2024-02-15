from abc import ABC, abstractmethod


class Saver(ABC):
    """Abstract saver's interface."""

    def __init__(self):
        pass


    @staticmethod
    def get_format():
        raise NotImplementedError


    @abstractmethod
    def save(self):
        raise NotImplementedError
