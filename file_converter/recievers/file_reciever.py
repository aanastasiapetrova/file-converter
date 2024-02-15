import re
from file_converter.recievers.base_reciever import Reciever
from file_converter.exceptions import FileIsIncorrectException


class FileReciever(Reciever):
    def __init__(self, path):
        self.path = path

    
    @staticmethod
    def get_format():
        return "file"

    
    @staticmethod
    def can_recieve(data):
        return re.match(r"[A-Z]:\\[\S+\s?\/]*\.\w+", data) or re.match(
            r"\/?[\w+\/]*\.\w+", data
        )


    def recieve(self):
        try:
            with open(self.path, "r", encoding="utf8") as filename:
                data = " ".join([line.strip() for line in filename.readlines()])
                return data
        except Exception as e:
            raise FileIsIncorrectException(
                f"The error occured while opening file by {self.path} path. See the original exception: {e}"
                )