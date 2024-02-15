from file_converter.adapters.base_adapter import Adapter


class RssAdapter(Adapter):
    """Adapt parsed rss data to general format."""

    @staticmethod
    def get_format():
        return "rss"

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
