import os
import requests
import sys

from file_converter.managers.adapters_manager import adapters_manager
from file_converter.managers.parsers_manager import parsers_manager, parsers
from file_converter.managers.queries_manager import queries_manager
from file_converter.managers.converters_manager import converters_manager
from file_converter.managers.savers_manager import savers_manager

from file_converter.exceptions import (
    FormatIsUnsupportedException,
    OptionIsRequiredException,
    OutputFormatIsIncorrectException,
)

from file_converter.commands.base_command import Command
from file_converter.helpers.registrator import Registrator
from file_converter.constants import FILES_TO_IGNORE
from file_converter.helpers.data_getter import DataGetter

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
        print(parsers)
        for parser in list(parsers.values()):
            can_parse = parser.can_parse(data)
            if can_parse:
                return parser.get_format()
        raise FormatIsUnsupportedException("Content can't be parsed.")
        

    def info(self):
        """Shows information about inputed options."""

        return f" input - {self.input}, output - {self.output}, sort - {self.sort}, author - {self.author}, limit - {self.limit}"
    


    def get_input_data(self, client=requests, stream=sys.stdin):
        """Analyse the input type and return inputed data."""

        data, format = "", ""

        data_getter = DataGetter(self.input, client, stream)
        data = data_getter.get_data()

        format = self.get_inputed_data_format(data)

        return str(data), format


    def get_output_data_type(self):
        """Define output type by inputed option."""

        data_getter = DataGetter(self.output)

        if data_getter.is_file():
            return "file"
        raise OutputFormatIsIncorrectException(
            f"The iputed output format {self.output} is incorrect."
        )


    def get_output_data_format(self):
        """Defines output file format by its extension."""

        return self.output.split(".")[-1]
    

    def parse_data(self, data, format):
        parser = parsers_manager.get(format)
        parsed_data = parser.parse(data)

        return parsed_data
    

    def filter_data(self, data, format):
        query = queries_manager.get(format)

        if self.sort:
            data = query.sort(self.sort, data)
        if self.author:
            data = query.filter(self.author, data)
        if self.limit:
            data = query.limit(self.limit, data)
        
        return data
    

    def adapt_data(self, format, data):
        adapter = adapters_manager.get(format)
        data = adapter.adapt(data)

        return data
    

    def convert_data(self, format, data):
        converter = converters_manager.get(format)
        data = converter.convert(data)

        return data
    

    def save_data(self, data):
        saver = savers_manager.get(self.get_output_data_type())
        saver.save(self.output, data)


    def register_modules(self, cwd):
        converter_dir = os.path.join(cwd, "file_converter")
        managers_dir = os.path.join(converter_dir, "managers")

        dirs_list = os.listdir(converter_dir)
        managers_list = os.listdir(managers_dir)
        dirs_to_register = []

        for path in managers_list:
            if os.path.isfile(os.path.join(managers_dir, path)) and path not in FILES_TO_IGNORE:
                dirs_to_register.append(path.split("_")[0])

        for path in dirs_list:
            if os.path.isdir(os.path.join(converter_dir, path)) and path in dirs_to_register:
                registrator = Registrator(os.path.join(converter_dir, path))
                registrator.register()
    

    def start(self):
        """Executing converter command."""

        if self.input is None or self.output is None:
            raise OptionIsRequiredException("Some of required options are missing!")
        
        self.register_modules(os.path.abspath(os.getcwd()))

        inputed_data, inputed_format = self.get_input_data()
        output_format = self.get_output_data_format()

        parsed_data = self.parse_data(inputed_data, inputed_format)

        filtered_data = self.filter_data(parsed_data, inputed_format)

        adapted_data = self.adapt_data(inputed_format, filtered_data)

        converted_data = self.convert_data(output_format, adapted_data)

        self.save_data(converted_data)
        