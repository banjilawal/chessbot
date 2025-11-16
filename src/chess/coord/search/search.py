# src/chess/coord/search/search.py

"""
Module: chess.coord.search.search
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""
from typing import List

from chess.system import LoggingLevelRouter, Search, SearchException, SearchResult
from chess.coord import Coord, CoordSearchContextValidator, CoordSearchException, CoordService, CoordSearchContext



class CoordSearch:
    """"""

    @classmethod
    @LoggingLevelRouter.monitor
    
    def search(
            cls,
            collection: List[Coord],
            search_context: CoordSearchContext,
            coord_search_context_validator: type[CoordSearchContextValidator] = CoordSearchContextValidator,
    ) -> SearchResult[List[Coord]]:
        method = "CoordSearch.search"
        try:
            context_validation = coord_search_context_validator.validate(search_context)
            if context_validation.is_failure():
                return SearchResult.failure(context_validation.exception)
            
            if search_context.row is not None:
                return cls.search_by_row(collection=collection, row=search_context.row)
            
            if search_context.column is not None:
                return cls.search_by_column(collection=collection, column=search_context.column)
            
            if search_context.coord is not None:
                return cls.search_by_coord(collection=collection, coord=search_context.coord)
            
        except Exception as ex:
            return SearchResult.failure(
                CoordSearchException(
                    f"{method}: {CoordSearchException.DEFAULT_MESSAGE}"
                )
            )
        
        
    @classmethod
    @LoggingLevelRouter.monitor
    def search_by_row(cls, collection: List[Coord], row: int) -> SearchResult[List[Coord]]:
        """"""
        method = "CoordSearch.search_by_row"
        matches = [coord for coord in collection if coord.row == row]
        if len(matches) == 0:
            return SearchResult.empty()
        elif len(matches) >  1:
            return SearchResult.success(payload=matches)
        return SearchResult.failure(
            CoordSearchException(f"{method}: {CoordSearchException.DEFAULT_MESSAGE}")
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def search_by_column(cls, collection: List[Coord], column: int) -> SearchResult[List[Coord]]:
        """"""
        method = "CoordSearch.search_by_column"
        matches = [coord for coord in collection if coord.column == column]
        if len(matches) == 0:
            return SearchResult.empty()
        elif len(matches) > 1:
            return SearchResult.success(payload=matches)
        return SearchResult.failure(
            CoordSearchException(f"{method}: {CoordSearchException.DEFAULT_MESSAGE}")
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def search_by_coord(cls, collection: List[Coord], coord: Coord) -> SearchResult[List[Coord]]:
        """"""
        method = "CoordSearch.search_by_coord"
        matches = [point for point in collection if point == coord]
        if len(matches) == 0:
            return SearchResult.empty()
        elif len(matches) > 1:
            return SearchResult.success(payload=matches)
        return SearchResult.failure(
            CoordSearchException(f"{method}: {CoordSearchException.DEFAULT_MESSAGE}")
        )
    
    