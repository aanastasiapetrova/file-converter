import re
import sys

import requests

from file_converter.managers.adapter_manager import adapter_manager
from file_converter.managers.parser_manager import parsers_manager, parsers
from file_converter.managers.query_manager import query_manager
from file_converter.managers.converter_manager import converter_manager
from file_converter.managers.saver_manager import saver_manager

from file_converter.exceptions import (
    ConnectionIsFailedException,
    FileIsIncorrectException,
    FormatIsUnsupportedException,
    InputMethodNotAllowedException,
    OptionIsRequiredException,
    OutputFormatIsIncorrectException,
    StreamErrorException,
)

from file_converter.commands.base_command import Command

class ConverterCommand(Command):
    """Converter command class realization."""

    def __init__(self, input, output, sort=None, author=None, limit=None):
        self.input = input
        self.output = output
        self.sort = sort
        self.author = author
        self.limit = limit
        ConverterCommand.absolute_path_regexp = r"[A-Z]:\\[\S+\s?\/]*\.\w+"
        ConverterCommand.relative_path_regexp = r"\/?[\w+\/]*\.\w+"
        ConverterCommand.remote_url_regexp = r"(https|http):\/\/[\S+\/]*\.\w+[\w+]*"


    @staticmethod
    def get_inputed_data_format(data):
        """Makes primary content type definition."""
        for parser in list(parsers.values()):
            format = parser.is_valid(data)
            if format:
                return format
        raise FormatIsUnsupportedException("Content can't be parsed.")
    

    @staticmethod
    def is_file(data):
        return re.match(ConverterCommand.absolute_path_regexp, data) or re.match(
            ConverterCommand.relative_path_regexp, data
        )


    @staticmethod
    def is_url(data):
        return re.match(ConverterCommand.remote_url_regexp, data)


    @staticmethod
    def is_stream(data):
        return data == "stdin"
    

    def info(self):
        """Shows information about inputed options."""

        return f" input - {self.input}, output - {self.output}, sort - {self.sort}, author - {self.author}, limit - {self.limit}"
    

    def get_data_from_file(self):
        try:
            with open(self.input, "r", encoding="utf8") as filename:
                data = " ".join([line.strip() for line in filename.readlines()])
                return data
        except Exception as e:
            raise FileIsIncorrectException(
                f"The error occured while opening file by {self.input} path. See the original exception: {e}"
                )
        
    
    def get_data_from_url(self, client):
        try:
            response = client.get(self.input)
            data = response.text
            return data
        except Exception as e:
            raise ConnectionIsFailedException(
                f"The error occured while getting data from {self.input} address. See the original exception: {e}."
            )
        
    
    def get_data_from_stream(self, stream):
        try:
            data = stream.read()
            return data
        except Exception as e:
            raise StreamErrorException(
                f"The error occured while getting data by stdin. See the original exception: {e}."
            )
    

    def get_input_data(self, client=requests, stream=sys.stdin):
        """Analyse the input type and return inputed data."""

        data, format = "", ""

        if ConverterCommand.is_file(self.input):
            data = self.get_data_from_file()
        elif ConverterCommand.is_url(self.input):
            data = self.get_data_from_url(client)
        elif ConverterCommand.is_stream(self.input):
            data = self.get_data_from_stream(stream)
        else:
            raise InputMethodNotAllowedException(
                f"Inputed method {self.input} is not allowed."
            )

        format = self.get_inputed_data_format(data)

        return str(data), format


    def get_output_data_type(self):
        """Define output type by inputed option."""

        if ConverterCommand.is_file(self.output):
            return "file"
        raise OutputFormatIsIncorrectException(
            f"The iputed output format {self.output} is incorrect."
        )


    def get_output_data_format(self):
        """Defines output file format by its extension."""

        return self.output.split(".")[-1]
    

    def parse_data(self, data, format):
        parser = parsers_manager.get_parser(format)
        parsed_data = parser.parse(data)

        return parsed_data
    

    def filter_data(self, data, format):
        query = query_manager.get_query(format)

        if self.sort:
            data = query.sort(self.sort, data)
        if self.author:
            data = query.filter(self.author, data)
        if self.limit:
            data = query.limit(self.limit, data)
        
        return data
    

    def adapt_data(self, format, data):
        adapter = adapter_manager.get_adapter(format)
        data = adapter.adapt(data)

        return data
    

    def convert_data(self, format, data):
        converter = converter_manager.get_converter(format)
        data = converter.convert(data)

        return data
    

    def save_data(self, data):
        saver = saver_manager.get_saver(self.get_output_data_type())
        saver.save(self.output, data)



    def start(self):
        """Executing converter command."""

        if self.input is None or self.output is None:
            raise OptionIsRequiredException("Some of required options are missing!")

        inputed_data, inputed_format = self.get_input_data()
        output_format = self.get_output_data_format()

        parsed_data = self.parse_data(inputed_data, inputed_format)

        filtered_data = self.filter_data(parsed_data, inputed_format)

        adapted_data = self.adapt_data(inputed_format, filtered_data)

        converted_data = self.convert_data(output_format, adapted_data)

        self.save_data(converted_data)
        