from file_converter.parsers.xml_parser import XmlParser


class AtomParser(XmlParser):
    
    @staticmethod
    def get_format():
        return "atom"
    
    @staticmethod
    def can_parse(data):
        return bool("<?xml" in data and "<feed" in data and "</feed>" in data)
