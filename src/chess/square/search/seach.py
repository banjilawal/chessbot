# src/chess/square/searcher/finder.py

"""
Module: chess.square.searcher.service
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import List

from chess.coord import Coord
from chess.system import LoggingLevelRouter, Finder, SearchResult
from chess.square import Square, SquareContext, SquareContextValidator, SquareFinderException


class SquareFinder(Finder[Square]):
    
    @classmethod
    def find(
            cls,
            data_set: List[T],
            context: SquareContext,
            validator: SquareContextValidator = SquareContextValidator()
    ) -> SearchResult[[Square]]:
        """"""
        method = "SquareSearchService(SearchService.find"
        try:
            context_validation = validator.validate(context)
            if context_validation.is_failure():
                return SearchResult.failure(context_validation.exception)
            
            if context.id is not None:
                return cls._find_by_id(id=context.id, data_set=data_set)
            
            if context.name is not None:
                return cls._find_by_name(name=context.name, data_set=data_set)
            
            if context.coord:
                return cls._find_coord(coord=context.coord, data_set=data_set)
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
    def _find_by_id(
            cls,
            id: int,
            data_set: List[Square],
    ) -> SearchResult[List[Square]]:
        """"""
        method = "CoordSearchService._find_by_id"
        try:
            matches = [square for square in data_set if square.id == id]
            
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
    def _find_by_name(
            cls,
            name: str,
            data_set: List[Square],
    ) -> SearchResult[List[Square]]:
        """"""
        method = "CoordSearchService._find_by_name"
        
        try:
            matches = [square for square in data_set if square.name.upper() == name.upper()]
            
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
    def _find_by_coord(
            cls,
            coord: Coord,
            data_set: List[Square],
    ) -> SearchResult[List[Square]]:
        """"""
        method = "CoordSearchService._find_by_coord"
        
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