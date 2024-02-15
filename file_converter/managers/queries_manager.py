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