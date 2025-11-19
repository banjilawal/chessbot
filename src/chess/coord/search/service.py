# src/chess/target/search/service.py

"""
Module: chess.target.search.service
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from typing import List, cast
from chess.system import SearchResult
from chess.coord import Coord, CoordSearch, CoordSearchContext, CoordSearchContextBuilder, CoordSearchContextValidator


class CoordSearchService:
    """"""
    _context_builder: type[CoordSearchContextBuilder]
    _context_validator: type[CoordSearchContextValidator]
    _search: type[CoordSearch]
    
    def __init__(
            self,
            context_builder: type[CoordSearchContextBuilder],
            context_validator: type[CoordSearchContextValidator],
            search: type[CoordSearch] = type[CoordSearch],
    ):
        self._search = search
        self._context_builder = context_builder
        self._context_validator = context_validator
        
        
    def search_by_row(self, row) -> List[Coord]:
        try:
            return self._search.search_by_row(row=row)
        except Exception as ex:
            return SearchResult.failure(ex)
    
    def search_by_column(self, column) -> List[Coord]:
        try:
            return self._search.search_by_column(column=column)
        except Exception as ex:
            return SearchResult.failure(ex)
    
    def search_by_coord(self, coord: Coord) -> List[Coord]:
        try:
            return self._search.search_by_row(coord=coord)
        except Exception as ex:
            return SearchResult.failure(ex)
    