# src/chess/square/search/service.py

"""
Module: chess.square.search.service
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import List

from chess.coord import Coord
from chess.square import Square
from chess.square.search import SquareSearchServiceException
from chess.system import LoggingLevelRouter, SearchContext, SearchResult, SearchService, Validator
from chess.system.search.service import T


class SquareSearchService(SearchService[Square]):
    
    @classmethod
    def find(cls, data_set: List[T], context: SearchContext, validator: Validator[SearchContext]) -> SearchResult[
        [T]]:
        """"""
        method = "SquareSearchService(SearchService.find"
        try:
            context_validation = validator.validate(context)
            if context_validation.is_failure():
                return SearchResult.failure(context_validation.exception)
            
            if context.id is not None:
                return cls.find_by_id(data_set=data_set, id=context.id)
            
            if context.name is not None:
                return cls.find_by_name(data_set, name=context.naame)
            
            if context.coord:
                return cls._find_coord(data_set=data_set, coord=context.coord)
        except Exception as ex:
            return SearchResult.failure(
                SquareSearchServiceException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{SquareSearchServiceException.DEFAULT_MESSAGE}"
                    )
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_column(
            cls,
            data_set: List[Square],
            column: int
    ) -> SearchResult[List[Square]]:
        """"""
        method = "CoordSearchService._find_by_column"
        try:
            matches = [square for square in data_set if square.coord == coord]
            
            if len(matches) == 0:
                return SearchResult.empty()
            elif len(matches) >= 1:
                return SearchResult.success(payload=matches)
        
        except Exception as ex:
            return SearchResult.failure(
                SquareSearchServiceException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{SquareSearchServiceException.DEFAULT_MESSAGE}"
                    )
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_coord(
            cls,
            data_set: List[Square],
            coord: Coord
    ) -> SearchResult[List[Square]]:
        """"""
        method = "CoordSearchService._find_by_row_and_coord"
        
        try:
            matches = [square for square in data_set if square.coord == coord]
            
            if len(matches) == 0:
                return SearchResult.empty()
            elif len(matches) >= 1:
                return SearchResult.success(payload=matches)
        except Exception as ex:
            return SearchResult.failure(
                SquareSearchServiceException(
                    ex=ex,
                    message=f"{method}: {SquareSearchServiceException.DEFAULT_MESSAGE}"
                )
            )
        