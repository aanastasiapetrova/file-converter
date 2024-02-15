from operator import itemgetter

from file_converter.exceptions import (
    LimitValueIsIncorrect,
    SortDirectionIsIncorrectException,
)
from file_converter.queries.base_query import Query


class RssQuery(Query):
    def __init__(self):
        pass

    @staticmethod
    def get_format():
        return "rss"

    def sort(self, direction, parsed_data):
        """Sort feed items by date in both directions."""

        items = parsed_data["channel"]["item"]

        match direction:
            case "asc":
                items.sort(key=itemgetter("pubDate"))
            case "desc":
                items.sort(key=itemgetter("pubDate"), reverse=True)
            case _:
                raise SortDirectionIsIncorrectException(
                    f"Inputed sort direction {direction} is incorrect. Try asc or desc direction."
                )

        parsed_data["channel"]["item"] = items

        return parsed_data

    def filter(self, name, parsed_data):
        """Filter feed items by author's name."""

        items = parsed_data["channel"]["item"]
        filtered_items_by_name = [
            item
            for item in items
            if "author" in list(item.keys()) and item["author"] == name
        ]
        parsed_data["channel"]["item"] = filtered_items_by_name

        return parsed_data

    def limit(self, limit, parsed_data):
        """Return inputed amount of feed objects."""

        items = parsed_data["channel"]["item"]
        try:
            parsed_data["channel"]["item"] = items[: abs(int(limit))]
        except Exception:
            raise LimitValueIsIncorrect(
                f"The inputed limit value {limit} is incorrect. Try natural number."
            )

        return parsed_data
