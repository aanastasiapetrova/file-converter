from abc import ABC, abstractmethod


class ParserManager:
    """Parser factory class to manage parsers classes."""

    def __init__(self):
        self._creators = {}


    def register_parser(self, format, creator):
        self._creators[format] = creator

    
    def get_parser(self, format):
        creator = self._creators[format]
        if not creator:
            raise ValueError(f"{format} format parser isn't registered.")
        

class Parser(ABC):
    """Abstract parser's interface."""

    def __init__(self):
        raise NotImplementedError


    @abstractmethod
    def start_object(self):
        raise NotImplementedError
    

    @abstractmethod
    def add_property(self):
        raise NotImplementedError
    

class JsonParser(Parser):
    """Json parser class realization."""

    pass


class AtomParser(Parser):
    """Atom parser class realization."""

    pass


class RssParser(Parser):
    """Rss parser class realization."""
    
    pass