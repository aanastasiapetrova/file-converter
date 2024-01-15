from lxml import etree

from file_converter.converters.base_converter import Converter


class RssConverter(Converter):
    """Rss converter class realization."""

    @staticmethod
    def get_format():
        return "rss"

    def convert_object_to_rss(self, root, adapted_data):
        """Convert data in general format to rss."""

        for item in adapted_data:
            if item == "records":
                for item in adapted_data[item]:
                    record = etree.Element("item")
                    self.convert_object_to_rss(record, item)
                    root.append(etree.XML(etree.tostring(record)))

            elif isinstance(adapted_data[item], dict):
                nested_element = etree.Element(item)
                for dict_item in adapted_data[item]:
                    etree.SubElement(nested_element, dict_item).text = adapted_data[
                        item
                    ][dict_item]
                nested = etree.tostring(nested_element)
                root.append(etree.XML(nested))

            elif isinstance(adapted_data[item], str):
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
