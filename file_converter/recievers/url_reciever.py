import re
import requests
from file_converter.recievers.base_reciever import Reciever
from file_converter.exceptions import ConnectionIsFailedException

class UrlReciever(Reciever):
    def __init__(self, url, client=requests):
        self.url = url
        self.client = client

    
    @staticmethod
    def get_format():
        return "url"


    @staticmethod
    def can_recieve(data):
        return re.match(r"(https|http):\/\/[\S+\/]*\.\w+[\w+]*", data)
    
    
    def recieve(self):
        try:
            response = self.client.get(self.url)
            data = response.text
            return data
        except Exception as e:
            raise ConnectionIsFailedException(
                f"The error occured while getting data from {self.url} address. See the original exception: {e}."
            )