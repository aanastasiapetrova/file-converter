import re
import sys
import requests
from abc import ABC, abstractmethod
from file_converter.exceptions import OptionIsRequiredException, InputMethodNotAllowed


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
    def __init__(self, input, output, sort, author, limit):
        self._input = input
        self._output = output
        self._sort = sort
        self._author = author
        self._limit = limit


    def info(self):
        """Shows information abouted inputed options."""

        return f' input - {self._input}, output - {self._output}, sort - {self._sort}, author - {self._author}, limit - {self._limit}'
    
    
    def get_input_data(self, input):
        """Analyse the input type and return inputed data."""

        data = []

        if re.match(r'[A-Z]:/[\w+/]*\.\w+', input) or re.match(r'\/?[\w+\/]*\.\w+', input):
            with open(input, 'r') as filename:
                data = filename.readlines()
        elif re.match(r'(https|http)://[\w+\/]*\.\w+[\w+]*', input):
            data = requests.get(input).text
        elif input == 'stdin':
            data = sys.stdin.read()
        else:
            raise InputMethodNotAllowed(f'Inputed method {input} is not allowed.')
        
        return data


    def start(self):
        """Starting converter command."""

        if self._input is None or self._output is None:
            raise OptionIsRequiredException('Some of required options are missing!')
        inputed_data = self.get_input_data(self._input)
