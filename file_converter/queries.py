from abc import ABC, abstractmethod
from operator import itemgetter
from file_converter.exceptions import SortDirectionIsIncorrectException, LimitValueIsIncorrect

class QueryManager:

    def __init__(self):
        self._queries = {}

    def register_query(self, format, query):
        self._queries[format] = query

    def get_query(self, format):
        query = self._queries[format]
        if not query:
            raise ValueError(f"{format} format query isn't registered.")
        return query()
    

class Query(ABC):

    def __init__(self):
        pass
    
    
    @abstractmethod
    def sort(self):
        raise NotImplementedError
    
    
    @abstractmethod
    def filter(self):
        raise NotImplementedError
    
    
    @abstractmethod
    def limit(self):
        raise NotImplementedError
    

class JsonQuery(Query):

    def __init__(self):
        pass


    def sort(self, direction, parsed_data):
        """Sort feed items by date in both directions."""

        items = parsed_data['items']

        match direction:
            case 'asc':
                items.sort(key=itemgetter('date_published'))
            case 'desc':
                items.sort(key=itemgetter('date_published'), reverse=True)
            case _:
                raise SortDirectionIsIncorrectException(f'Inputed sort direction {direction} is incorrect. Try asc or desc direction.')
            
        parsed_data['items'] = items

        return parsed_data
    
    
    def filter(self, name, parsed_data):
        """Filter feed items by author's name."""

        if 'author' not in list(parsed_data.keys()):
            items = parsed_data['items']
            filtered_items_by_name = [item for item in items if 'author' in list(item.keys()) and item['author']['name'] == name]
            parsed_data['items'] = filtered_items_by_name

        return parsed_data
    

    def limit(self, limit, parsed_data):
        """Return inputed amount of feed objects."""

        items = parsed_data['items']
        try:
            parsed_data['items'] = items[:abs(int(limit))]
        except Exception:
            raise LimitValueIsIncorrect(f'The inputed limit value {limit} is incorrect. Try natural number.')
        
        return parsed_data
    

class RssQuery(Query):

    def __init__(self):
        pass


    def sort(self, direction, parsed_data):
        """Sort feed items by date in both directions."""

        items = parsed_data['channel']['item']

        match direction:
            case 'asc':
                items.sort(key=itemgetter('pubDate'))
            case 'desc':
                items.sort(key=itemgetter('pubDate'), reverse=True)
            case _:
                raise SortDirectionIsIncorrectException(f'Inputed sort direction {direction} is incorrect. Try asc or desc direction.')
        
        parsed_data['channel']['item'] = items

        return parsed_data
    

    def filter(self, name, parsed_data):
        """Filter feed items by author's name."""

        items = parsed_data['channel']['item']
        filtered_items_by_name = [item for item in items if 'author' in list(item.keys()) and item['author'] == name]
        parsed_data['channel']['item'] = filtered_items_by_name

        return parsed_data
    

    def limit(self, limit, parsed_data):
        """Return inputed amount of feed objects."""
        
        items = parsed_data['channel']['item']
        try:
            parsed_data['channel']['item'] = items[:abs(int(limit))]
        except Exception:
            raise LimitValueIsIncorrect(f'The inputed limit value {limit} is incorrect. Try natural number.')

        return parsed_data


class AtomQuery(Query):

    def __init__(self):
        pass


    def sort(self, direction, parsed_data):
        """Sort feed items by date in both directions."""

        items = parsed_data['entry']

        match direction:
            case 'asc':
                items.sort(key=itemgetter('published'))
            case 'desc':
                items.sort(key=itemgetter('published'), reverse=True)
            case _:
                raise SortDirectionIsIncorrectException(f'Inputed sort direction {direction} is incorrect. Try asc or desc direction.')
        
        parsed_data['entry'] = items

        return parsed_data
    

    def filter(self, name, parsed_data):
        """Filter feed items by author's name."""

        if 'author' not in list(parsed_data.keys()):
            items = parsed_data['entry']
            filtered_items_by_name = [item for item in items if 'author' in list(item.keys()) and item['author']['name'] == name]
            parsed_data['entry'] = filtered_items_by_name

        return parsed_data
    

    def limit(self, limit, parsed_data):
        """Return inputed amount of feed objects."""

        items = parsed_data['entry']
        try:
            parsed_data['entry'] = items[:abs(int(limit))]
        except Exception:
            raise LimitValueIsIncorrect(f'The inputed limit value {limit} is incorrect. Try natural number.')

        return parsed_data

    

query_manager = QueryManager()
query_manager.register_query('json', JsonQuery)
query_manager.register_query('rss', RssQuery)
query_manager.register_query('atom', AtomQuery)