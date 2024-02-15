class AdapterManager:
    """Adapter factory class to manage adapters classes."""

    def __init__(self):
        self._adapters = {}

    def register(self, format, adapter):
        self._adapters[format] = adapter

    def get(self, format):
        adapter = self._adapters[format]
        if not adapter:
            raise ValueError(f"{format} format adapter isn't registered.")
        return adapter()


adapters_manager = AdapterManager()
