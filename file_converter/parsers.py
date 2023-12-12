from abc import ABC, abstractmethod
import json
from lxml import etree


class ParserManager:
    """Parser factory class to manage parsers classes."""

    def __init__(self):
        self._parsers = {}


    def register_parser(self, format, parser):
        self._parsers[format] = parser

    
    def get_parser(self, format):
        parser = self._parsers[format]
        if not parser:
            raise ValueError(f"{format} format parser isn't registered.")
        return parser()
        

class Parser(ABC):
    """Abstract parser's interface."""

    def __init__(self):
        pass

    @abstractmethod
    def parse(self):
        raise NotImplementedError
        

class JsonParser(Parser):
    """Json parser class realization."""

    def parse(self, inputed_data):
       return json.loads(inputed_data)    


class XmlParser(Parser):
    """Xml parser class realization."""

    def tranform_to_object(self, elements=[], data={}):

        while len(elements):
            element = elements[0]
            tag = element.tag.split('}')[-1]
            if not element.getchildren() and element.text:
                data[tag] = element.text
                elements.remove(element)
            elif not element.getchildren() and not element.text:
                if tag in data.keys():
                    prev_value = data[tag]
                    data[tag] = [prev_value]
                    data[tag].append(element.attrib)
                else:
                    data[tag] = element.attrib
                elements.remove(element)
            else:
                if tag in data:
                    value = data[tag]
                    data[tag] = [value]
                    data[tag].append(self.tranform_to_object(element.getchildren(), {}))
                else:
                    data[tag] = {}
                    self.tranform_to_object(element.getchildren(), data[tag])
                grand_children = []
                for child in element.getchildren():
                    if child.getchildren():
                        for grand in child.getchildren():
                            grand_children.append(grand)
                elements = [e for e in elements if e not in element.getchildren() and e not in grand_children]
                elements.remove(element)
            
        return data

    
    def parse(self, inputed_data):

        root = etree.XML(bytes(inputed_data, encoding='utf-8'), etree.XMLParser(remove_blank_text=True))
        elements = list(root.iter("*"))[1:].copy()

        return self.tranform_to_object(elements, {})



parsers_manager = ParserManager()
parsers_manager.register_parser('json', JsonParser)
parsers_manager.register_parser('atom', XmlParser)
parsers_manager.register_parser('rss', XmlParser)