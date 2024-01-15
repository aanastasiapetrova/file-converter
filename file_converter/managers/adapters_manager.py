# from file_converter.adapters.json_adapter import JsonAdapter
# from file_converter.adapters.rss_adapter import RssAdapter
# from file_converter.adapters.atom_adapter import AtomAdapter


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
# adapter_manager.register("json", JsonAdapter)
# adapter_manager.register("rss", RssAdapter)
# adapter_manager.register("atom", AtomAdapter)
