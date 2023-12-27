from operator import itemgetter


from file_converter.exceptions import (
    LimitValueIsIncorrect,
    SortDirectionIsIncorrectException,
)
from file_converter.queries.base_query import Query


class JsonQuery(Query):
    def __init__(self):
        pass

    def sort(self, direction, parsed_data):
        """Sort feed items by date in both directions."""

        items = parsed_data["items"]

        match direction:
            case "asc":
                items.sort(key=itemgetter("date_published"))
            case "desc":
                items.sort(key=itemgetter("date_published"), reverse=True)
            case _:
                raise SortDirectionIsIncorrectException(
                    f"Inputed sort direction {direction} is incorrect. Try asc or desc direction."
                )

        parsed_data["items"] = items

        return parsed_data

    def filter(self, name, parsed_data):
        """Filter feed items by author's name."""

        if "author" not in list(parsed_data.keys()):
            items = parsed_data["items"]
            filtered_items_by_name = [
                item
                for item in items
                if "author" in list(item.keys()) and item["author"]["name"] == name
            ]
            parsed_data["items"] = filtered_items_by_name

        return parsed_data

    def limit(self, limit, parsed_data):
        """Return inputed amount of feed objects."""

        items = parsed_data["items"]
        try:
            parsed_data["items"] = items[: abs(int(limit))]
        except Exception:
            raise LimitValueIsIncorrect(
                f"The inputed limit value {limit} is incorrect. Try natural number."
            )

        return parsed_data
