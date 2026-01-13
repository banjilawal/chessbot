# src/chess/square/searcher/finder.py

"""
Module: chess.square.searcher.service
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import List

from chess.board import Board
from chess.coord import Coord
from chess.system import DataFinder, LoggingLevelRouter, SearchResult
from chess.square import (
    Square, SquareContext, SquareContextValidator, SquareSearchFailedException, SquareSearchRouteException,
    SquareSearchNullDatasetException, SquareSearchPayloadTypeException,
)


class SquareFinder(DataFinder[Square]):
    """
    # ROLE: Finder

    # RESPONSIBILITIES:
    1.  Send items in a SquareList whose attribute value match the context.key value to the caller.
    2.  If a search does not complete forward the exception chain to the caller for debugging.

    # LIMITATIONS:
    1.  SquareFinder sends the raw list of matches. Resolving id collisions is the caller's responsibility.

    # PARENT
        *   Finder

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def find(
            cls,
            dataset: List[Square],
            context: SquareContext,
            context_validator: SquareContextValidator = SquareContextValidator()
    ) -> SearchResult[List[Square]]:
        """
        # ACTION:
        1.  If the dataset is null or the wrong type send the exception in the SearchResult.
        2.  If the context fails validation send the exception in the SearchResult. Else, route to the 
            search method which matches the context key.
        3.  The search method returns either an empty result or a list of squares. Any exceptions were caught earlier
            by the search router.
       # PARAMETERS:
            *   dataset (List[Square]):
            *   context: SquareContext
            *   context_validator: SquareContextValidator
        # RETURNS:
            *   SearchResult[List[Square]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Square] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            *   SquareSearchPayloadTypeException
            *   SquareNullDatasetException
            *   SquareSearchFailedException
        """
        method = "SquareFinder.find"
        
        # Handle the case that the dataset is null.
        if dataset is None:
            # Return the exception chain on failure.
            return SearchResult.failure(
                SquareSearchFailedException(
                    message=f"{method}: {SquareSearchFailedException.ERROR_CODE}",
                    ex=SquareSearchNullDatasetException(
                        f"{method}: {SquareSearchNullDatasetException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that dataset is the wrong type
        if not isinstance(dataset, List):
            # Return the exception chain on failure.
            return SearchResult.failure(
                SquareSearchFailedException(
                    message=f"{method}: {SquareSearchFailedException.ERROR_CODE}",
                    ex=SquareSearchPayloadTypeException(f"{method}: {SquareSearchPayloadTypeException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the case that the context fails validation.
        validation_result = context_validator.validate(context)
        if validation_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                SquareSearchFailedException(
                    message=f"{method}: {SquareSearchFailedException.ERROR_CODE}",
                    ex=validation_result.exception
                )
            )
        # --- Route to the search method which matches the context key. ---#
        
        # Entry point into finding by square's id.
        if context.id is not None:
            return cls._find_by_id(dataset=dataset, id=context.id)
        # Entry point into finding by square's name.
        if context.name is not None:
            return cls._find_by_name(dataset=dataset, name=context.name)
        # Entry point into finding by square's coord.
        if context.coord is not None:
            return cls._find_by_coord(dataset=dataset, coord=context.coord)
        # Entry point into searching by square's board.
        if context.board is not None:
            return cls._find_by_board(dataset=dataset, coord=context.board)
        
        # If a context does not have a search route defined send an exception chain.
        return SearchResult.failure(
            SquareSearchFailedException(
                message=f"{method}: {SquareSearchFailedException.ERROR_CODE}",
                ex=SquareSearchRouteException(f"{method}: {SquareSearchRouteException.DEFAULT_MESSAGE}")
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_id(cls, dataset: List[Square], id: int) -> SearchResult[List[Square]]:
        """
        # ACTION:
            1.  Get the Squares with the desired id.
        # PARAMETERS:
            *   id (int)
            *   dataset (List[Square])
        # RETURNS:
            *   SearchResult[List[Square]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Tokem] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            None
        """
        method = "SquareFinder._find_by_id"
        matches = [square for square in dataset if square.id == id]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_name(cls, dataset: List[Square], name: str) -> SearchResult[List[Square]]:
        """
        # ACTION:
            1.  Get the Squares which match the name.
        # PARAMETERS:
            *   name (str)
            *   dataset (List[Square])
        # RETURNS:
            *   SearchResult[List[Square]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Tokem] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            None
        """
        method = "SquareFinder._find_by_name"
        matches = [square for square in dataset if square.name.upper() == name.upper()]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_coord(cls, dataset: List[Square], coord: Coord) -> SearchResult[List[Square]]:
        """
        # ACTION:
            1.  Get the Squares which match the name.
        # PARAMETERS:
            *   coord (Coord)
            *   dataset (List[Square])
        # RETURNS:
            *   SearchResult[List[Square]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Tokem] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            None
        """
        method = "SquareFinder._find_by_coord"
        matches = [square for square in dataset if square.coord == coord]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_board(cls, dataset: List[Square], board: Board) -> SearchResult[List[Square]]:
        """
        # ACTION:
            1.  Get the Squares which match the board.
        # PARAMETERS:
            *   board (Board)
            *   dataset (List[Square])
        # RETURNS:
            *   SearchResult[List[Square]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Tokem] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            None
        """
        method = "SquareFinder._find_by_board"
        matches = [square for square in dataset if square.board == board]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)