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
