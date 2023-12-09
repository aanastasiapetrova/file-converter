from abc import ABC, abstractmethod
from file_converter.exceptions import OptionIsRequiredException


class Command(ABC):
    def __init__(self):
        raise NotImplementedError

    @abstractmethod
    def info(self):
        raise NotImplementedError
    
    @abstractmethod
    def start(self):
        raise NotImplementedError


class ConverterCommand(Command):
    def __init__(self, input, output, sort=None, author=None, limit=None):
        self._input = input
        self._output = output
        self._sort = sort
        self._author = author
        self._limit = limit

    def info(self):
        """Shows information abouted inputed options."""

        return f' input - {self._input}, output - {self._output}, sort - {self._sort}, author - {self._author}, limit - {self._limit}'
    
    def start(self):
        """Starting converter command."""

        if self._input is None or self._output is None:
            raise OptionIsRequiredException('Some of required options are missing!')