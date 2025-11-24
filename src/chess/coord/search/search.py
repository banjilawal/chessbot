# src/chess/coord/search/search.py

"""
Module: chess.coord.search.search
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from typing import List

from chess.system import LoggingLevelRouter, Search, SearchResult
from chess.coord import Coord, CoordContext, CoordContextValidator, CoordSearchException


class CoordSearch(Search[Coord]):
    """"""
    
    @classmethod
    @LoggingLevelRouter.monitor
    def find(
            cls,
            data_set: List[Coord],
            context: CoordContext,
            context_validator: CoordContextValidator = CoordContextValidator(),
    ) -> SearchResult[List[Coord]]:
        method = "CoordSearch.find"
        try:
            context_validation = context_validator.validate(context)
            if context_validation.is_failure():
                return SearchResult.failure(context_validation.exception)
            
            if context.row is not None and context.column is None:
                return cls._find_by_row(
                    data_set=data_set,
                    row=context.row
                )
            
            if context.column is not None and context.row is None:
                return cls._find_by_column(
                    data_set=data_set,
                    column=context.column
                )
            
            if context.column is not None and context.row is not None:
                return cls._find_by_row_and_column(
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
    def _find_by_row(
            cls,
            data_set: List[Coord],
            row: int
    ) -> SearchResult[List[Coord]]:
        """"""
        method = "CoordSearch._find_by_row"
        
        try:
            matches = [
                coord for coord in data_set if coord.row == row
            ]
            
            if len(matches) == 0:
                return SearchResult.empty()
            elif len(matches) >= 1:
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
    def _find_by_column(
            cls,
            data_set: List[Coord],
            column: int
    ) -> SearchResult[List[Coord]]:
        """"""
        method = "CoordSearch._find_by_column"
        try:
            matches = [
                coord for coord in data_set if coord.column == column
            ]
            
            if len(matches) == 0:
                return SearchResult.empty()
            elif len(matches) >= 1:
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
    def _find_by_row_and_column(
            cls,
            data_set: List[Coord],
            row: int,
            column: int
    ) -> SearchResult[List[Coord]]:
        """"""
        method = "CoordSearch._find_by_row_and_column"
        
        try:
            matches = [
                point for point in data_set if point.row == row and point.column == column
            ]
            
            if len(matches) == 0:
                return SearchResult.empty()
            elif len(matches) >= 1:
                
                return SearchResult.success(payload=matches)
        except Exception as ex:
            return SearchResult.failure(
                CoordSearchException(
                    ex=ex,
                    message=f"{method}: {CoordSearchException.DEFAULT_MESSAGE}"
                )
            )
