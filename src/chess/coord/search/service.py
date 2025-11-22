# src/chess/target/search/service.py

"""
Module: chess.target.search.search
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""


from typing import List

from chess.system import LoggingLevelRouter, SearchResult
from chess.coord import (
    Coord, CoordSearchContextBuilder, CoordSearchContextValidator, CoordSearchException, CoordSearchContext
)



class CoordSearchService:
    """"""
    
    @classmethod
    @LoggingLevelRouter.monitor
    def context_builder(cls) -> CoordSearchContextBuilder:
        return CoordSearchContextBuilder()
    
    def search(
            cls,
            data_set: List[Coord],
            search_context: CoordSearchContext,
            context_validator: CoordSearchContextValidator = CoordSearchContextValidator(),
    ) -> SearchResult[List[Coord]]:
        method = "CoordSearchService.search"
        try:
            context_validation = context_validator.validate(search_context)
            if context_validation.is_failure():
                return SearchResult.failure(context_validation.exception)
            
            if search_context.row is not None:
                return cls._search_by_row(data_set=data_set, row=search_context.row)
            
            if search_context.column is not None:
                return cls._search_by_column(data_set=data_set, column=search_context.column)
            
            if search_context.column is not None and search_context.row is not None:
                return cls._search_by_row_and_coord(
                    data_set=data_set,
                    row=search_context.row,
                    column=search_context.column
                )
            
        except Exception as ex:
            return SearchResult.failure(
                CoordSearchException(
                    ex=ex,
                    message=f"{method}: {CoordSearchException.DEFAULT_MESSAGE}"
                )
            )
        
        
    @classmethod
    @LoggingLevelRouter.monitor
    def _search_by_row(cls, data_set: List[Coord], row: int) -> SearchResult[List[Coord]]:
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
                    message=f"{method}: {CoordSearchException.DEFAULT_MESSAGE}"
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _search_by_column(cls, data_set: List[Coord], column: int) -> SearchResult[List[Coord]]:
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
                    message=f"{method}: {CoordSearchException.DEFAULT_MESSAGE}"
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _search_by_row_and_coord(cls, data_set: List[Coord], row:int, column: int) -> SearchResult[List[Coord]]:
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
    
    