import re
import sys
import requests
from abc import ABC, abstractmethod
from file_converter.exceptions import (
    OptionIsRequiredException,
    InputMethodNotAllowedException,
    ConnectionIsFailedException,
    FormatIsUnsupportedException,
    FileIsIncorrectException,
    StreamErrorException
    )
import file_converter.parsers as parsers


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
            

    @staticmethod
    def get_inputed_data_format(data):
        """Makes primary content type definition."""

        if data.count('{') == data.count('}') and data.count('{') and not '<?xml' in data:
            return 'json'
        elif '<?xml' in data:
            if '<rss' in data and '</rss>' in data:
                    return 'rss'
            elif '<feed' in data and '</feed>' in data:
                return 'atom'
        raise FormatIsUnsupportedException(f"Content can't be parsed.")
    

    def info(self):
        """Shows information about inputed options."""

        return f' input - {self.input}, output - {self.output}, sort - {self.sort}, author - {self.author}, limit - {self.limit}'
    
    
    def get_input_data(self, client=requests, stream=sys.stdin):
        """Analyse the input type and return inputed data."""
        
        data, format = '', ''

        if re.match(r'[A-Z]:\/[\S+\s?\/]*\.\w+', self.input) or re.match(r'\/?[\w+\/]*\.\w+', self.input):
            try:
                with open(self.input, 'r', encoding='utf8') as filename:
                    data = ' '.join([l.strip() for l in filename.readlines()])
            except Exception as e:
                raise FileIsIncorrectException(f'The error occured while opening file by {self.input} path. See the original exception: {e}')
            
        elif re.match(r'(https|http):\/\/[\S+\/]*\.\w+[\w+]*', self.input):
            try:
                data = client.get(self.input).text
            except Exception as e:
                raise ConnectionIsFailedException(f'The error occured while getting data from {self.input} address. See the original exception: {e}.')
            
        elif self.input == 'stdin':
            try:
                data = stream.read()
            except Exception:
                raise StreamErrorException(f'The error occured while getting data by stdin. See the original exception: {e}.')
            
        else:
            raise InputMethodNotAllowedException(f'Inputed method {self.input} is not allowed.')
        
        format = ConverterCommand.get_inputed_data_format(data)
        
        return str(data), format
    

    def get_output_data_format(self):
        """Defines output file format by its extension."""

        return self.output.split('.')[-1]


    def start(self):
        """Starting converter command."""

        if self.input is None or self.output is None:
            raise OptionIsRequiredException('Some of required options are missing!')
        
        inputed_data, inputed_format = self.get_input_data()

        output_data = self.get_output_data_format()        

        print(parsers.parsers_manager.get_parser(inputed_format).parse(inputed_data))
