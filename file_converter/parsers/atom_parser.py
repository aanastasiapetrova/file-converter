from file_converter.parsers.xml_parser import XmlParser
from file_converter.constants import ATOM_NECESSARY_TAGS


class AtomParser(XmlParser):
    
    @staticmethod
    def get_format():
        return "atom"
    
    @staticmethod
    def can_parse(data):
        can_parse = False

        if "<?xml" in data:
            for tag in ATOM_NECESSARY_TAGS:
                can_parse = True
                open_tag, close_tag = tag[0], tag[1]
                if open_tag not in data or close_tag not in data or data.count(open_tag) != data.count(close_tag):
                    can_parse = False
                    return can_parse
            return can_parse

