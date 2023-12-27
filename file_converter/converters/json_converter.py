from file_converter.converters.base_converter import Converter


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

        return str(adapted_data).replace("'", '"')
