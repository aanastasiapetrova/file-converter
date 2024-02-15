class ParserManager:
    """Parser factory class to manage parsers classes."""

    def __init__(self):
        self._parsers = {}

    def register(self, format, parser):
        self._parsers[format] = parser

    def get(self, format):
        parser = self._parsers[format]
        if not parser:
            raise ValueError(f"{format} format parser isn't registered.")
        return parser()



parsers_manager = ParserManager()
parsers = parsers_manager._parsers
