from abc import ABC, abstractmethod


class Saver(ABC):
    """Abstract saver's interface."""

    def __init__(self):
        pass

    @abstractmethod
    def save(self):
        raise NotImplementedError
