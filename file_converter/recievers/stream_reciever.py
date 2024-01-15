import sys
from file_converter.recievers.base_reciever import Reciever
from file_converter.exceptions import StreamErrorException


class StreamReciever(Reciever):
    def __init__(self, stream=sys.stdin):
        self.stream = stream

    
    @staticmethod
    def get_format():
        return "stream"

    
    @staticmethod
    def can_recieve(data):
        return data == "stdin"
    

    def recieve(self):
        try:
            data = self.stream.read()
            return data
        except Exception as e:
            raise StreamErrorException(
                f"The error occured while getting data by stdin. See the original exception: {e}."
            )