from lxml import etree

from file_converter.converters.base_converter import Converter


class AtomConverter(Converter):
    """Atom converter class realization."""

    @staticmethod
    def get_format():
        return "atom"

    def convert_object_to_atom(self, root, adapted_data):
        """Convert data in general format to atom."""

        for item in adapted_data:
            if item == "records":
                for item in adapted_data[item]:
                    record = etree.Element("entry")
                    self.convert_object_to_atom(record, item)
                    root.append(etree.XML(etree.tostring(record)))

            elif isinstance(adapted_data[item], dict):
                nested_element = etree.Element(item)
                for dict_item in adapted_data[item]:
                    if isinstance(dict_item, str):
                        etree.SubElement(nested_element, dict_item).text = adapted_data[
                            item
                        ][dict_item]
                nested = etree.tostring(nested_element)
                root.append(etree.XML(nested))

            elif isinstance(adapted_data[item], str):
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

