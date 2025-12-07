
from chess.system import A, R, S, Finder, SearchResult
from chess.checkmate.service import KingLocationRecord

class KingLocationFinder(Finder[KingLocationRecord]):
    
    @classmethod
    def search(cls, data_owner: A, search_context: S, *args, **kwargs) -> SearchResult[R]:
        pass