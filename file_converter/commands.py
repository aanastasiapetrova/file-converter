import re
import sys
import requests
from abc import ABC, abstractmethod
from file_converter.exceptions import OptionIsRequiredException, InputMethodNotAllowedException, ConnectionFailureException


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


class ConverterCommand(Command):
    """Converter command class realization."""
    
    def __init__(self, input, output, sort=None, author=None, limit=None):
        self.input = input
        self.output = output
        self.sort = sort
        self.author = author
        self.limit = limit


    def info(self):
        """Shows information abouted inputed options."""

        return f' input - {self.input}, output - {self.output}, sort - {self.sort}, author - {self.author}, limit - {self.limit}'
    
    
    def get_input_data(self, client=requests):
        """Analyse the input type and return inputed data."""

        data = ''

        if re.match(r'[A-Z]:\/[\S+\s?\/]*\.\w+', self.input) or re.match(r'\/?[\w+\/]*\.\w+', self.input):
            with open(self.input, 'r') as filename:
                data = filename.readlines()
        elif re.match(r'(https|http):\/\/[\S+\/]*\.\w+[\w+]*', self.input):
            try:
                data = client.get(self.input).text
            except Exception:
                raise ConnectionFailureException(f'Getting data from {self.input} address is failed. Try again or choose another address.')
        elif self.input == 'stdin':
            data = sys.stdin.read()
        else:
            raise InputMethodNotAllowedException(f'Inputed method {self.input} is not allowed.')
        
        return data


    def start(self):
        """Starting converter command."""

        if self.input is None or self.output is None:
            raise OptionIsRequiredException('Some of required options are missing!')
        inputed_data = self.get_input_data()
