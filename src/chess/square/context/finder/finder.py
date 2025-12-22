# src/chess/square/searcher/finder.py

"""
Module: chess.square.searcher.service
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import List

from chess.coord import Coord
from chess.system import LoggingLevelRouter, Finder, SearchFailedException, SearchResult
from chess.square import Square, SquareContext, SquareContextValidator


class SquareFinder(Finder[Square]):
    
    @classmethod
    def find(
            cls,
            dataset: List[Square],
            context: SquareContext,
            validator: SquareContextValidator = SquareContextValidator()
    ) -> SearchResult[[Square]]:
        """"""
        method = "SquareSearchService(SearchService.find"
        try:
            context_validation = validator.validate(context)
            if context_validation.is_failure:
                return SearchResult.failure(context_validation.exception)
            
            if context.id is not None:
                return cls._find_by_id(id=context.id, dataset=dataset)
            
            if context.name is not None:
                return cls._find_by_name(name=context.name, dataset=dataset)
            
            if context.coord:
                return cls._find_coord(coord=context.coord, dataset=dataset)
            # Finally, if some exception is not handled by the checks wrap it inside an SearchFailedException
            # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                SearchFailedException(ex=ex, message=f"{method}: {SearchFailedException.DEFAULT_MESSAGE}")
            )

    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_id(
            cls,
            id: int,
            dataset: List[Square],
    ) -> SearchResult[List[Square]]:
        """"""
        method = "CoordSearchService._find_by_id"
        try:
            matches = [square for square in dataset if square.id == id]
            
            if len(matches) == 0:
                return SearchResult.empty()
            elif len(matches) >= 1:
                return SearchResult.success(payload=matches)
                
            # Finally, if some exception is not handled by the checks wrap it inside an SearchFailedException
            # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                SearchFailedException(ex=ex, message=f"{method}: {SearchFailedException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_name(
            cls,
            name: str,
            dataset: List[Square],
    ) -> SearchResult[List[Square]]:
        """"""
        method = "CoordSearchService._find_by_name"
        
        try:
            matches = [square for square in dataset if square.name.upper() == name.upper()]
            
            if len(matches) == 0:
                return SearchResult.empty()
            elif len(matches) >= 1:
                return SearchResult.success(payload=matches)
                
            # Finally, if some exception is not handled by the checks wrap it inside an SearchFailedException
            # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                SearchFailedException(ex=ex, message=f"{method}: {SearchFailedException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_coord(
            cls,
            coord: Coord,
            dataset: List[Square],
    ) -> SearchResult[List[Square]]:
        """"""
        method = "CoordSearchService._find_by_coord"
        
        try:
            matches = [square for square in dataset if square.coord == coord]
            
            if len(matches) == 0:
                return SearchResult.empty()
            elif len(matches) >= 1:
                return SearchResult.success(payload=matches)
                
            # Finally, if some exception is not handled by the checks wrap it inside an SearchFailedException
            # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                SearchFailedException(ex=ex, message=f"{method}: {SearchFailedException.DEFAULT_MESSAGE}")
            )