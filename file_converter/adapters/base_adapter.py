from abc import ABC, abstractmethod


class Adapter(ABC):
    """Abstract adapter's interface."""

    def __init__(self):
        pass

    @abstractmethod
    def adapt(self):
        raise NotImplementedError
