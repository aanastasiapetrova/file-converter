from file_converter.adapters.json_adapter import JsonAdapter
from file_converter.adapters.rss_adapter import RssAdapter
from file_converter.adapters.atom_adapter import AtomAdapter


class AdapterManager:
    """Adapter factory class to manage adapters classes."""

    def __init__(self):
        self._adapters = {}

    def register_adapter(self, format, adapter):
        self._adapters[format] = adapter

    def get_adapter(self, format):
        adapter = self._adapters[format]
        if not adapter:
            raise ValueError(f"{format} format adapter isn't registered.")
        return adapter()


adapter_manager = AdapterManager()
adapter_manager.register_adapter("json", JsonAdapter)
adapter_manager.register_adapter("rss", RssAdapter)
adapter_manager.register_adapter("atom", AtomAdapter)
