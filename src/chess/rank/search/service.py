# src/chess/rank/searcher/service.py

"""
Module: chess.rank.searcher.entity_service
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""


from chess.rank import RankSearch, RankSearchContext, RankSearchContextValidator, RankSearchContextBuilder




class RankSearchService:
    """"""
    _context_builder: type[RankSearchContextBuilder]
    _context_validator: type[RankSearchContextValidator]
    _search: type[RankSearch]
    
    def __init__(
            self,
            context_builder: type[RankSearchContextBuilder],
            context_validator: type[RankSearchContextValidator],
            search: type[RankSearch] = type[RankSpecSearch],
    ):
        self._search = search
        self._context_builder = context_builder
        self._context_validator = context_validator
        
        
    @property
    def search(self) -> type[RankSearch]:
        return self._search
    
    #
    # def build_search_context(self, **kwargs) -> RankSearchContext:
    #     return self._context_builder.builder(**kwargs)
    #
    #
    # def validate_search_context(self, candidate: Any) -> SearchResult[RankSearchContext]:
    #     return self._context_validator.validate(candidate)

    