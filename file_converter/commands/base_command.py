from abc import ABC, abstractmethod

class Command(ABC):
    """Abstract command's interface."""

    def __init__(self):
        raise NotImplementedError

    @abstractmethod
    def info(self):
        raise NotImplementedError

    @abstractmethod
    def start(self):
        raise NotImplementedError
