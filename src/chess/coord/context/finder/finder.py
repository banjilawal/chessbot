# src/chess/coord/searcher/finder.py

"""
Module: chess.coord.searcher.searcher
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from typing import List

from chess.system import LoggingLevelRouter, Finder, SearchResult
from chess.coord import Coord, CoordContext, CoordContextValidator, CoordFinderException


class CoordFinder(Finder[Coord]):
    """"""
    
    @classmethod
    @LoggingLevelRouter.monitor
    def find(
            cls,
            dataset: List[Coord],
            context: CoordContext,
            context_validator: CoordContextValidator = CoordContextValidator(),
    ) -> SearchResult[List[Coord]]:
        method = "CoordFinder.find"
        try:
            context_validation = context_validator.validate(context)
            if context_validation.is_failure():
                return SearchResult.failure(context_validation.exception)
            
            if context.row is not None and context.column is None:
                return cls._find_by_row(
                    dataset=dataset,
                    row=context.row
                )
            
            if context.column is not None and context.row is None:
                return cls._find_by_column(
                    dataset=dataset,
                    column=context.column
                )
            
            if context.column is not None and context.row is not None:
                return cls._find_by_row_and_column(
                    dataset=dataset,
                    row=context.row,
                    column=context.column
                )
        
        except Exception as ex:
            return SearchResult.failure(
                CoordFinderException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{CoordFinderException.DEFAULT_MESSAGE}"
                    )
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_row(
            cls,
            dataset: List[Coord],
            row: int
    ) -> SearchResult[List[Coord]]:
        """"""
        method = "CoordFinder._find_by_row"
        
        try:
            matches = [
                coord for coord in dataset if coord.row == row
            ]
            
            if len(matches) == 0:
                return SearchResult.empty()
            elif len(matches) >= 1:
                return SearchResult.success(payload=matches)
        
        except Exception as ex:
            return SearchResult.failure(
                CoordFinderException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{CoordFinderException.DEFAULT_MESSAGE}"
                    )
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_column(
            cls,
            dataset: List[Coord],
            column: int
    ) -> SearchResult[List[Coord]]:
        """"""
        method = "CoordFinder._find_by_column"
        try:
            matches = [
                coord for coord in dataset if coord.column == column
            ]
            
            if len(matches) == 0:
                return SearchResult.empty()
            elif len(matches) >= 1:
                return SearchResult.success(payload=matches)
        
        except Exception as ex:
            return SearchResult.failure(
                CoordFinderException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{CoordFinderException.DEFAULT_MESSAGE}"
                    )
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_row_and_column(
            cls,
            dataset: List[Coord],
            row: int,
            column: int
    ) -> SearchResult[List[Coord]]:
        """"""
        method = "CoordFinder._find_by_row_and_column"
        
        try:
            matches = [
                point for point in dataset if point.row == row and point.column == column
            ]
            
            if len(matches) == 0:
                return SearchResult.empty()
            elif len(matches) >= 1:
                
                return SearchResult.success(payload=matches)
        except Exception as ex:
            return SearchResult.failure(
                CoordFinderException(
                    ex=ex,
                    message=f"{method}: {CoordFinderException.DEFAULT_MESSAGE}"
                )
            )
