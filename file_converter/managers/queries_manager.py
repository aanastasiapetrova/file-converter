# from file_converter.queries.json_query import JsonQuery
# from file_converter.queries.rss_query import RssQuery
# from file_converter.queries.atom_query import AtomQuery


class QueryManager:
    def __init__(self):
        self._queries = {}

    def register(self, format, query):
        self._queries[format] = query

    def get(self, format):
        query = self._queries[format]
        if not query:
            raise ValueError(f"{format} format query isn't registered.")
        return query()


queries_manager = QueryManager()
# query_manager.register("json", JsonQuery)
# query_manager.register("rss", RssQuery)
# query_manager.register("atom", AtomQuery)
