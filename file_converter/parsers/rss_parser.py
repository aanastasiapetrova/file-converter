from file_converter.parsers.xml_parser import XmlParser


class RssParser(XmlParser):
    
    @staticmethod
    def get_format():
        return "rss"
    

    @staticmethod
    def can_parse(data):
        return bool("<?xml" in data and "<rss" in data and "</rss>" in data)