from lxml import etree

from file_converter.parsers.base_parser import Parser

class XmlParser(Parser):
    """Xml parser class realization."""

    @staticmethod
    def can_parse(data):
        return bool("<?xml" in data)
    
    
    @staticmethod
    def get_format():
        return "xml"
    

    def tranform_to_object(self, elements=[], data={}):
        """Transform XML elements and subelements to result object."""

        while len(elements):
            element = elements[0]
            tag = element.tag.split("}")[-1]
            if not element.getchildren() and element.text:
                data[tag] = element.text.strip()
                elements.remove(element)
            elif not element.getchildren() and not element.text:
                if tag in data.keys():
                    prev_value = data[tag]
                    data[tag] = [prev_value]
                    data[tag].append(element.attrib)
                else:
                    data[tag] = element.attrib
                elements.remove(element)
            else:
                if tag in data:
                    value = data[tag]
                    if not isinstance(data[tag], list):
                        data[tag] = [value]
                    data[tag].append(self.tranform_to_object(element.getchildren(), {}))
                else:
                    data[tag] = {}
                    self.tranform_to_object(element.getchildren(), data[tag])
                grand_children = []
                for child in element.getchildren():
                    if child.getchildren():
                        for grand in child.getchildren():
                            grand_children.append(grand)
                elements = [
                    e
                    for e in elements
                    if e not in element.getchildren() and e not in grand_children
                ]
                elements.remove(element)

        return data

    def parse(self, inputed_data):
        """Prepare data and start parse proccess."""

        root = etree.XML(
            bytes(inputed_data, encoding="utf-8"),
            etree.XMLParser(remove_blank_text=True),
        )
        elements = list(root.iter("*"))[1:].copy()

        return self.tranform_to_object(elements, {})
