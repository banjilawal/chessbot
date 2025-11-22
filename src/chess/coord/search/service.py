# src/chess/coord/search/service.py

"""
Module: chess.coord.search.service
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""


from typing import List

from chess.system import LoggingLevelRouter, SearchResult, SearchService
from chess.coord import (
    Coord, CoordSearchContextBuilder, CoordSearchContextValidator, CoordSearchException, CoordContext
)



class CoordSearchService(SearchService[Coord]):
    """"""
    
    @classmethod
    @LoggingLevelRouter.monitor
    def context_builder(cls) -> CoordSearchContextBuilder:
        return CoordSearchContextBuilder()
    
    @classmethod
    @LoggingLevelRouter.monitor
    def search(
            cls,
            data_set: List[Coord],
            context: CoordContext,
            context_validator: CoordSearchContextValidator = CoordSearchContextValidator(),
    ) -> SearchResult[List[Coord]]:
        method = "CoordSearchService.search"
        try:
            context_validation = context_validator.validate(context)
            if context_validation.is_failure():
                return SearchResult.failure(context_validation.exception)
            
            if context.row is not None:
                return cls._search_by_row(
                    data_set=data_set,
                    row=context.row
                )
            
            if context.column is not None:
                return cls._search_by_column(
                    data_set=data_set,
                    column=context.column
                )
            
            if (
                    context.column is not None and
                    context.row is not None
            ):
                return cls._searc_by_both(
                    data_set=data_set,
                    row=context.row,
                    column=context.column
                )
            
        except Exception as ex:
            return SearchResult.failure(
                CoordSearchException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{CoordSearchException.DEFAULT_MESSAGE}"
                    )
                )
            )
        
        
    @classmethod
    @LoggingLevelRouter.monitor
    def _search_by_row(
            cls,
            data_set: List[Coord],
            row: int
    ) -> SearchResult[List[Coord]]:
        """"""
        method = "CoordSearchService.search_by_row"
        
        try:
            matches = [coord for coord in data_set if coord.row == row]
            
            if len(matches) == 0:
                return SearchResult.empty()
            elif len(matches) >  1:
                return SearchResult.success(payload=matches)
            
        except Exception as ex:
            return SearchResult.failure(
                CoordSearchException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{CoordSearchException.DEFAULT_MESSAGE}"
                    )
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _search_by_column(
            cls,
            data_set: List[Coord],
            column: int
    ) -> SearchResult[List[Coord]]:
        """"""
        method = "CoordSearchService.search_by_column"
        try:
            matches = [coord for coord in data_set if coord.column == column]
            
            if len(matches) == 0:
                return SearchResult.empty()
            elif len(matches) > 1:
                return SearchResult.success(payload=matches)
            
        except Exception as ex:
            return SearchResult.failure(
                CoordSearchException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{CoordSearchException.DEFAULT_MESSAGE}"
                    )
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _searc_by_both(cls, data_set: List[Coord], row:int, column: int) -> SearchResult[List[Coord]]:
        """"""
        method = "CoordSearchService.search_by_coord"
        
        try:
            matches = [point for point in data_set if point.row == row and point.column == column]
            
            if len(matches) == 0:
                return SearchResult.empty()
            elif len(matches) > 1:
                
                return SearchResult.success(payload=matches)
        except Exception as ex:
            return SearchResult.failure(
                CoordSearchException(
                    ex=ex,
                    message=f"{method}: {CoordSearchException.DEFAULT_MESSAGE}"
                )
            )
    
    