from abc import ABC, abstractmethod


class Converter(ABC):
    """Abstract converter's interface."""

    def __init__(self):
        pass

    @abstractmethod
    def convert(self):
        raise NotImplementedError
