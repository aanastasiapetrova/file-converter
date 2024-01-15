import re
import sys
import requests
from file_converter.exceptions import (
    InputMethodNotAllowedException,
    FileIsIncorrectException,
    ConnectionIsFailedException,
    StreamErrorException
    )


class DataGetter:
    def __init__(self, input_typa_data, client, stream):
        self.input_type_data = input_typa_data
        self.client = client
        self.stream = stream

        DataGetter.absolute_path_regexp = r"[A-Z]:\\[\S+\s?\/]*\.\w+"
        DataGetter.relative_path_regexp = r"\/?[\w+\/]*\.\w+"
        DataGetter.remote_url_regexp = r"(https|http):\/\/[\S+\/]*\.\w+[\w+]*"

        DataGetter.input_type_config = {
            "file": self.is_file,
            "url": self.is_url,
            "stream": self.is_stream
        }
        DataGetter.get_data_config = {
            "file": self.get_data_from_file,
            "url": self.get_data_from_url,
            "stream": self.get_data_from_stream
        }


    def is_file(self):
        return re.match(DataGetter.absolute_path_regexp, self.input_type_data) or re.match(
            DataGetter.relative_path_regexp, self.input_type_data
        )


    def is_url(self):
        return re.match(DataGetter.remote_url_regexp, self.input_type_data)


    def is_stream(self):
        return self.input_type_data == "stdin"
    
    
    def get_data_from_file(self):
        try:
            with open(self.input_type_data, "r", encoding="utf8") as filename:
                data = " ".join([line.strip() for line in filename.readlines()])
                return data
        except Exception as e:
            raise FileIsIncorrectException(
                f"The error occured while opening file by {self.input_type_data} path. See the original exception: {e}"
                )
        
    
    def get_data_from_url(self):
        try:
            response = self.client.get(self.input_type_data)
            data = response.text
            return data
        except Exception as e:
            raise ConnectionIsFailedException(
                f"The error occured while getting data from {self.input_type_data} address. See the original exception: {e}."
            )
        
    
    def get_data_from_stream(self):
        try:
            data = self.stream.read()
            return data
        except Exception as e:
            raise StreamErrorException(
                f"The error occured while getting data by stdin. See the original exception: {e}."
            )
        
    
    def define_input_type(self):
        for type, condition in DataGetter.input_type_config.items():
            if condition():
                return type
        raise InputMethodNotAllowedException(
                f"Inputed method {self.input_type_data} is not allowed."
            )
    
    def get_data(self):
        input_type = self.define_input_type()
        return self.get_data_config[input_type]()
        