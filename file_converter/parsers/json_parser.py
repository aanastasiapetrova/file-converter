import json

from file_converter.parsers.base_parser import Parser


class JsonParser(Parser):
    """Json parser class realization."""

    def parse(self, inputed_data):
        """Parse inputed data to python object."""

        return json.loads(inputed_data)
    
    @staticmethod
    def is_valid(data):
        if (
            data.count("{") == data.count("}")
            and data.count("{")
            and "<?xml" not in data
        ):
            return 'json'
        return False
