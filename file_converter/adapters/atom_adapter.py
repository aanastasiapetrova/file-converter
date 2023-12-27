from file_converter.adapters.base_adapter import Adapter


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