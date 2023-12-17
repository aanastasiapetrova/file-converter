from abc import ABC, abstractmethod


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


class Adapter(ABC):
    """Abstract adapter's interface."""

    def __init__(self):
        pass

    @abstractmethod
    def adapt(self):
        raise NotImplementedError


class JsonAdapter(Adapter):
    """Json adapter class realization."""

    def adapt(self, parsed_data):
        """Adapt parsed json data to general format."""

        if "items" in list(parsed_data.keys()):
            items = parsed_data["items"]
            parsed_data.pop("items")
            parsed_data["records"] = items

        for item in parsed_data["records"]:
            if "date_published" in list(item.keys()):
                date = item["date_published"]
                item.pop("date_published")
                item["date"] = date

        return parsed_data


class RssAdapter(Adapter):
    """Adapt parsed rss data to general format."""

    def adapt(self, parsed_data):
        if "item" in list(parsed_data["channel"].keys()):
            items = parsed_data["channel"]["item"]
            parsed_data["channel"].pop("item")
            parsed_data["channel"]["records"] = items

        for item in parsed_data["channel"]["records"]:
            if "pubDate" in list(item.keys()):
                date = item["pubDate"]
                item.pop("pubDate")
                item["date"] = date
            if "author" in list(item.keys()) and not isinstance(item["author"], dict):
                author = item["author"]
                item["author"] = {"name": author}

        return parsed_data["channel"]


class AtomAdapter(Adapter):
    """Adapt parsed atom data to general format."""

    def adapt(self, parsed_data):
        if "entry" in list(parsed_data.keys()):
            entries = parsed_data["entry"]
            parsed_data.pop("entry")
            parsed_data["records"] = entries

        for item in parsed_data["records"]:
            if "published" in list(item.keys()):
                date = item["published"]
                item.pop("published")
                item["date"] = date

        return parsed_data


adapter_manager = AdapterManager()
adapter_manager.register_adapter("json", JsonAdapter)
adapter_manager.register_adapter("rss", RssAdapter)
adapter_manager.register_adapter("atom", AtomAdapter)
