from file_converter.adapters.base_adapter import Adapter


class JsonAdapter(Adapter):
    """Json adapter class realization."""

    @staticmethod
    def get_format():
        return "json"

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
