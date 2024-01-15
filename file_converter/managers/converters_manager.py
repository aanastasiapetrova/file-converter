# from file_converter.converters.json_converter import JsonConverter
# from file_converter.converters.rss_converter import RssConverter
# from file_converter.converters.atom_converter import AtomConverter


class ConverterManager:
    """Converter factory class to manage converters classes."""

    def __init__(self):
        self._converters = {}

    def register(self, format, converter):
        self._converters[format] = converter

    def get(self, format):
        converter = self._converters[format]
        if not converter:
            raise ValueError(f"{format} format converter isn't registered.")
        return converter()





converters_manager = ConverterManager()
# converter_manager.register("json", JsonConverter)
# converter_manager.register("rss", RssConverter)
# converter_manager.register("atom", AtomConverter)
