from abc import ABC, abstractmethod

from lxml import etree


class ConverterManager:
    """Converter factory class to manage converters classes."""

    def __init__(self):
        self._converters = {}

    def register_converter(self, format, converter):
        self._converters[format] = converter

    def get_converter(self, format):
        converter = self._converters[format]
        if not converter:
            raise ValueError(f"{format} format converter isn't registered.")
        return converter()


class Converter(ABC):
    """Abstract converter's interface."""

    def __init__(self):
        pass

    @abstractmethod
    def convert(self):
        raise NotImplementedError


class JsonConverter(Converter):
    """Json converter class realization."""

    def convert(self, adapted_data):
        """Convert data in general format to json."""

        if "records" in list(adapted_data.keys()):
            items = adapted_data["records"]
            adapted_data.pop("records")
            adapted_data["items"] = items

        for item in adapted_data["items"]:
            if "date" in list(item.keys()):
                date = item["date"]
                item.pop("date")
                item["date_published"] = date

        return adapted_data


class RssConverter(Converter):
    """Rss converter class realization."""

    def convert_object_to_rss(self, root, adapted_data):
        """Convert data in general format to rss."""

        for item in adapted_data:
            if item == "records":
                for item in adapted_data[item]:
                    record = etree.Element("item")
                    self.convert_object_to_rss(record, item)
                    root.append(etree.XML(etree.tostring(record)))

            elif type(adapted_data[item]) is dict:
                nested_element = etree.Element(item)
                for dict_item in adapted_data[item]:
                    etree.SubElement(nested_element, dict_item).text = adapted_data[
                        item
                    ][dict_item]
                nested = etree.tostring(nested_element)
                root.append(etree.XML(nested))

            elif type(adapted_data[item]) is str:
                if item == "date":
                    etree.SubElement(root, "pubDate").text = adapted_data[item]
                else:
                    etree.SubElement(root, item).text = adapted_data[item]

        return root

    def convert(self, adapted_data):
        """Initialize data for convert method and start convertation."""

        root = etree.Element("rss", version="2.0")
        channel = etree.SubElement(root, "channel")
        etree.tostring(
            self.convert_object_to_rss(channel, adapted_data),
            pretty_print=True,
            encoding="utf-8",
            xml_declaration=True,
        ).decode("utf-8")
        return etree.tostring(
            root, pretty_print=True, encoding="utf-8", xml_declaration=True
        ).decode("utf-8")


class AtomConverter(Converter):
    """Atom converter class realization."""

    def convert_object_to_atom(self, root, adapted_data):
        """Convert data in general format to atom."""

        for item in adapted_data:
            if item == "records":
                for item in adapted_data[item]:
                    record = etree.Element("entry")
                    self.convert_object_to_atom(record, item)
                    root.append(etree.XML(etree.tostring(record)))

            elif type(adapted_data[item]) is dict:
                nested_element = etree.Element(item)
                for dict_item in adapted_data[item]:
                    if type(dict_item) is str:
                        etree.SubElement(nested_element, dict_item).text = adapted_data[
                            item
                        ][dict_item]
                nested = etree.tostring(nested_element)
                root.append(etree.XML(nested))

            elif type(adapted_data[item]) is str:
                if item == "date":
                    etree.SubElement(root, "published").text = adapted_data[item]
                else:
                    etree.SubElement(root, item).text = adapted_data[item]

        return root

    def convert(self, adapted_data):
        """Initialize data for convert method and start convertation."""

        root = etree.Element("feed")
        return etree.tostring(
            self.convert_object_to_atom(root, adapted_data),
            pretty_print=True,
            encoding="utf-8",
            xml_declaration=True,
        ).decode("utf-8")


converter_manager = ConverterManager()
converter_manager.register_converter("json", JsonConverter)
converter_manager.register_converter("rss", RssConverter)
converter_manager.register_converter("atom", AtomConverter)
