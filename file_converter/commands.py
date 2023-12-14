import re
import sys
from abc import ABC, abstractmethod

import requests

import file_converter.adapters as adapters
import file_converter.converters as converters
import file_converter.parsers as parsers
import file_converter.queries as queries
import file_converter.savers as savers
from file_converter.exceptions import (
    ConnectionIsFailedException,
    FileIsIncorrectException,
    FormatIsUnsupportedException,
    InputMethodNotAllowedException,
    OptionIsRequiredException,
    OutputFormatIsIncorrectException,
    StreamErrorException,
)


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
        if (
            data.count("{") == data.count("}")
            and data.count("{")
            and not "<?xml" in data
        ):
            return "json"
        elif "<?xml" in data:
            if "<rss" in data and "</rss>" in data:
                return "rss"
            elif "<feed" in data and "</feed>" in data:
                return "atom"
        raise FormatIsUnsupportedException(f"Content can't be parsed.")

    def info(self):
        """Shows information about inputed options."""

        return f" input - {self.input}, output - {self.output}, sort - {self.sort}, author - {self.author}, limit - {self.limit}"

    def get_input_data(self, client=requests, stream=sys.stdin):
        """Analyse the input type and return inputed data."""

        data, format = "", ""

        if re.match(r"[A-Z]:\\[\S+\s?\/]*\.\w+", self.input) or re.match(
            r"\/?[\w+\/]*\.\w+", self.input
        ):
            try:
                with open(self.input, "r", encoding="utf8") as filename:
                    data = " ".join([l.strip() for l in filename.readlines()])
            except Exception as e:
                raise FileIsIncorrectException(
                    f"The error occured while opening file by {self.input} path. See the original exception: {e}"
                )

        elif re.match(r"(https|http):\/\/[\S+\/]*\.\w+[\w+]*", self.input):
            try:
                response = client.get(self.input)
                data = response.text
            except Exception as e:
                raise ConnectionIsFailedException(
                    f"The error occured while getting data from {self.input} address. See the original exception: {e}."
                )

        elif self.input == "stdin":
            try:
                data = stream.read()
            except Exception:
                raise StreamErrorException(
                    f"The error occured while getting data by stdin. See the original exception: {e}."
                )

        else:
            raise InputMethodNotAllowedException(
                f"Inputed method {self.input} is not allowed."
            )

        format = ConverterCommand.get_inputed_data_format(data)

        return str(data), format

    def get_output_data_type(self):
        """Define output type by inputed option."""

        if re.match(r"[A-Z]:\\[\S+\s?\/]*\.\w+", self.output) or re.match(
            r"\/?[\S+\/]*\.\S+", self.output
        ):
            return "file"
        raise OutputFormatIsIncorrectException(
            f"The iputed output format {self.output} is incorrect."
        )

    def get_output_data_format(self):
        """Defines output file format by its extension."""

        return self.output.split(".")[-1]

    def start(self):
        """Executing converter command."""

        if self.input is None or self.output is None:
            raise OptionIsRequiredException("Some of required options are missing!")

        inputed_data, inputed_format = self.get_input_data()
        output_format = self.get_output_data_format()

        parser = parsers.parsers_manager.get_parser(inputed_format)
        parsed_data = parser.parse(inputed_data)

        query = queries.query_manager.get_query(inputed_format)

        if self.sort:
            parsed_data = query.sort(self.sort, parsed_data)
        if self.author:
            parsed_data = query.filter(self.author, parsed_data)
        if self.limit:
            parsed_data = query.limit(self.limit, parsed_data)

        adapter = adapters.adapter_manager.get_adapter(inputed_format)
        adapted_data = adapter.adapt(parsed_data)

        converter = converters.converter_manager.get_converter(output_format)
        converted_data = converter.convert(adapted_data)

        saver = savers.saver_manager.get_saver(self.get_output_data_type())
        saver.save(self.output, converted_data)
