
from chess.system import A, R, S, Search, SearchResult
from chess.checkmate.service import KingLocationRecord

class KingLocationSearch(Search[KingLocationRecord]):
    
    @classmethod
    def search(cls, data_owner: A, search_context: S, *args, **kwargs) -> SearchResult[R]:
        pass