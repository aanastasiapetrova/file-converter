from abc import ABC, abstractmethod
import json
from lxml import etree


class ParserManager:
    """Parser factory class to manage parsers classes."""

    def __init__(self):
        self._parsers = {}


    def register_parser(self, format, parser):
        self._parsers[format] = parser

    
    def get_parser(self, format, inputed_data):
        parser = self._parsers[format]
        if not parser:
            raise ValueError(f"{format} format parser isn't registered.")
        return parser(inputed_data)
        

class Parser(ABC):
    """Abstract parser's interface."""

    def __init__(self, inputed_data):
        self.inputed_data = inputed_data


    @abstractmethod
    def parse(self):
        raise NotImplementedError
        

class JsonParser(Parser):
    """Json parser class realization."""

    def parse(self):
       return json.loads(self.inputed_data)    


class AtomParser(Parser):
    """Atom parser class realization."""

    def parse(self, elements=[], data={}):
        root = etree.XML(bytes(self.inputed_data, encoding='utf-8'), etree.XMLParser(remove_blank_text=True))

        elements = list(root.iter("*"))[1:].copy()

        while len(elements):
            element = elements[0]
            tag = element.tag.split('}')[-1]
            if not element.getchildren() and element.text:
                data[tag] = element.text
                elements.remove(element)
            elif not element.getchildren() and not element.text:
                data[tag] = element.attrib
                elements.remove(element)
            else:
                data[tag] = {}
                for child in element.getchildren():
                    child_tag = child.tag.split('}')[-1]
                    data[tag][child_tag] = child.text
                    elements.remove(child)
                elements.remove(element)
        print(data)




class RssParser(Parser):
    """Rss parser class realization."""
    
    def parse(self):
        pass


parsers_manager = ParserManager()
parsers_manager.register_parser('json', JsonParser)
parsers_manager.register_parser('atom', AtomParser)
parsers_manager.register_parser('rss', RssParser)