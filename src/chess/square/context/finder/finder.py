# src/chess/square/context/finder/finder.py

"""
Module: chess.square.context.finder.finder
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import List

from chess.board import Board
from chess.coord import Coord
from chess.system import LoggingLevelRouter, SearchResult, StackSearcher
from chess.square import (
    Square, SquareContext, SquareContextValidator, SquareSearchException, SquareSearchRouteException, SquareState,
    SquareValidator
)
from chess.token import Token


class SquareFinder(StackSearcher[Square]):
    """
    # ROLE: Search

    # RESPONSIBILITIES:
    1.  Single point of entry into different square search routes.
    2.  Return a list of squares which match the context attribute's value.
    3.  Provide an exception chain the client can use to trace a search that does is not completed.
    4.  Manages all phases of the SquareSearch lifecycle.

    # LIMITATIONS:
    1.  A search result might contain duplicates.

    # PARENT
        *   AbstractSearcher

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See AbstractSearcher for inherited attributes.
        
    # CONSTRUCTOR PARAMETERS:
    None
        Inherited:
            *   See AbstractSearcher for inherited constructor parameters.
        
    # LOCAL METHODS:
        *   find(
                dataset: List[Square],
                context: SquareContext,
                square_validator: SquareValidator
                context_validator: SquareContextValidator
            ) -> SearchResult[List[Square]]
        
    # INHERITED METHODS:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def find(
            cls,
            dataset: List[Square],
            context: SquareContext,
            square_validator: SquareValidator = SquareValidator(),
            context_validator: SquareContextValidator = SquareContextValidator()
    ) -> SearchResult[List[Square]]:
        """
        # ACTION:
            1.  If either
                    *   the dataset.
                    *   context.
                Is not certified as safe send an exception chain in the SearchResult.
            2.  Once Action.1 has been completed successfully searches are guaranteed to complete successfully.
            3.  Route to the search method that matches the context.
            4.  The searcher returns a List contain zero or more squares.
        # PARAMETERS:
                *   dataset [List[Square]]
                *   context [SquareContext]
                *   square_validator [SquareValidator]
                *   context_validator [SquareContextValidator]
        # RETURNS:
            *   SearchResult[List[Square]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Square] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            *   SquareSearchException
        """
        method = "SquareFinder.find"
        
        # Handle the case that, the dataset is either null, not List[Square] or empty.
        dataset_validation_result = square_validator.verify_is_square_dataset(candidate=dataset)
        if dataset_validation_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                SquareSearchException(
                    message=f"{method}: {SquareSearchException.ERROR_CODE}",
                    ex=dataset_validation_result.exception
                )
            )
        # Handle the case that the context fails validation.
        context_validation_result = context_validator.validate(context)
        if context_validation_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                SquareSearchException(
                    message=f"{method}: {SquareSearchException.ERROR_CODE}",
                    ex=context_validation_result.exception
                )
            )
        # --- Route to the search method which matches the context key. ---#
        
        # Entry point into finding by the square's id.
        if context.id is not None:
            return cls._find_by_id(dataset=dataset, id=context.id)
        # Entry point into finding by the square's name.
        if context.name is not None:
            return cls._find_by_name(dataset=dataset, name=context.name)
        # Entry point into finding by the square's coord.
        if context.coord is not None:
            return cls._find_by_coord(dataset=dataset, coord=context.coord)
        # Entry point into searching by the square's board.
        if context.board is not None:
            return cls._find_by_board(dataset=dataset, coord=context.board)
        # Entry point into searching by the square's occupant.
        if context.board is not None:
            return cls._find_by_board(dataset=dataset, coord=context.occupant)
        # Entry point into searching by the square's state.
        if context.state:
            return cls._find_by_state(dataset=dataset, state=context.state)
        
        # If a context does not have a search route defined send an exception chain.
        return SearchResult.failure(
            SquareSearchException(
                message=f"{method}: {SquareSearchException.ERROR_CODE}",
                ex=SquareSearchRouteException(f"{method}: {SquareSearchRouteException.DEFAULT_MESSAGE}")
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_id(cls, dataset: List[Square], id: int) -> SearchResult[List[Square]]:
        """
        # ACTION:
            1.  Get the Squares which match the id.
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
        """
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
            1.  Get the Squares which match the coord.
        """
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
        """
        matches = [square for square in dataset if square.board == board]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_occupant(cls, dataset: List[Square], occupant: Token) -> SearchResult[List[Square]]:
        """
        # ACTION:
            1.  Get the Squares which match the occupant.
        """
        matches = [
            square for square in dataset if (square.occupant is not None and square.occupant) == occupant
        ]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_empty_state(cls, dataset: List[Square], state: SquareState) -> SearchResult[List[Square]]:
        """
        # ACTION:
            1.  Get the Squares which the state.
        """
        matches = [square for square in dataset if square.state == state]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)