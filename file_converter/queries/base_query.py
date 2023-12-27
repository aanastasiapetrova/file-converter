from abc import ABC, abstractmethod


class Query(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def sort(self):
        raise NotImplementedError

    @abstractmethod
    def filter(self):
        raise NotImplementedError

    @abstractmethod
    def limit(self):
        raise NotImplementedError
