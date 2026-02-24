# src/chess/square/context/finder/finder.py

"""
Module: chess.square.context.finder.finder
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, List, cast

from chess.board import Board
from chess.coord import Coord
from chess.system import LoggingLevelRouter, SearchResult, StackSearcher, ValidationResult
from chess.square import (
    SquareDataSourceNullException, Square, SquareContext, SquareContextValidator, SquareDataSourceEmptyException,
    SquareSearchException,
    SquareSearchRouteException,
    SquareSearchNullDatasetException, SquareSearchPayloadException, SquareState
)
from chess.token import Token


class SquareFinder(StackSearcher[Square]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing Square microservice API.
    2.  Encapsulate integrity logic for Square instances in one extendable module.
    3.  Authoritative, single source of truth for Square state by providing single entry and exit points to Square
        lifecycle.

    # PARENT:
        *   EntityService

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   SERVICE_NAME (str)
        *   token_visit_handler (TokenVisitHandler)
        *   collision_detector (SquareCollisionDetector)

    # INHERITED ATTRIBUTES:
        *   See EntityService for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        Local:
            *   token_visit_handler (TokenVisitHandler)
            *   collision_detector (SquareCollisionDetector)
        Inherited:
            *   See EntityService for inherited parameters.

    # LOCAL METHODS:
        *   begin_square_visit(square: Square, visitor: Token) -> UpdateResult[Square]
        *   end_square_visit(square: Square) -> DeletionResult[Token]

    # INHERITED METHODS:
    None
    """
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
            context_validator: SquareContextValidator = SquareContextValidator()
    ) -> SearchResult[List[Square]]:
        """
        # ACTION:
            1.  Send an exception chain in the SearchResult if either
                    *   A null check.
                    *   A type check.
                Ssend an exception chain in the ValidationResult. Else, cast candidate to SquareContext
                instance context.
            2.  Send an exception chain in the BuildResult if either
                    *   One and only one of attributes is not null.
                    *   There is no build route for the enabled option.
                    *   The enabled attribute is not certified as safe by its service.
                are not certified as safe by their services.
            3.  Build the appropriate context, sed the build success result.
        # PARAMETERS:
            Only one these must be provided:
                *   id Optional[(int)]
                *   name Optional[(str)]
                *   cord Optional[(Coord)]
                *   board Optional[(Board)]
                *   state Optional[SquareState]
            These Parameters must be provided:
                *   board_service (BoardService)
                *   coord_service (CoordService)
                *   token_service (TokenService)
                *   identity_service (IdentityService)
        # RETURNS:
            *   BuildResult[SquareContext] containing either:
                    - On failure: Exception.
                    - On success: SquareContext in the payload.
        # RAISES:
            *   ZeroSquareContextFlagsException
            *   SquareContextBuildException
            *   ExcessiveSquareContextFlagsException
            *   SquareContextBuildRouteException
        """
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
            *   SquareSearchPayloadException
            *   SquareNullDatasetException
            *   SquareSearchException
        """
        method = "SquareFinder.find"
        

        # Handle the case that the context fails validation.
        validation_result = context_validator.validate(context)
        if validation_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                SquareSearchException(
                    message=f"{method}: {SquareSearchException.ERROR_CODE}",
                    ex=validation_result.exception
                )
            )
        # --- Route to the search method which matches the context key. ---#
        
        # Entry point into finding by item's id.
        if context.id is not None:
            return cls._find_by_id(dataset=dataset, id=context.id)
        # Entry point into finding by item's name.
        if context.name is not None:
            return cls._find_by_name(dataset=dataset, name=context.name)
        # Entry point into finding by item's coord.
        if context.coord is not None:
            return cls._find_by_coord(dataset=dataset, coord=context.coord)
        # Entry point into searching by item's board.
        if context.board is not None:
            return cls._find_by_board(dataset=dataset, coord=context.board)
        # Entry point into searching by item's occupant.
        if context.board is not None:
            return cls._find_by_board(dataset=dataset, coord=context.occupant)
        # Entry point into searching by emptiness.
        if context.state is not None and context.state == SquareState.EMPTY:
            return cls._find_by_empty_state(dataset=dataset)
        # Entry point into searching by fullness.
        if context.state is not None and context.state == SquareState.OCCUPIED:
            return cls._find_by_occupied_state(dataset=dataset)
        
        # If a context does not have a search route defined send an exception chain.
        return SearchResult.failure(
            SquareSearchException(
                message=f"{method}: {SquareSearchException.ERROR_CODE}",
                ex=SquareSearchRouteException(f"{method}: {SquareSearchRouteException.DEFAULT_MESSAGE}")
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _validate_dataset(cls, candidate: Any) -> ValidationResult[List[Square]]:
        """
        # ACTION:
            1.  Send an exception chain in the ValidationResult if either
                    *   A null check.
                    *   A type check.
                Ssend an exception chain in the ValidationResult. Else, cast candidate to SquareContext
                instance context.
            2.  Send an exception chain in the BuildResult if either
                    *   One and only one of attributes is not null.
                    *   There is no build route for the enabled option.
                    *   The enabled attribute is not certified as safe by its service.
                are not certified as safe by their services.
            3.  Build the appropriate context, sed the build success result.
        # PARAMETERS:
            Only one these must be provided:
                *   id Optional[(int)]
                *   name Optional[(str)]
                *   cord Optional[(Coord)]
                *   board Optional[(Board)]
                *   state Optional[SquareState]
            These Parameters must be provided:
                *   board_service (BoardService)
                *   coord_service (CoordService)
                *   token_service (TokenService)
                *   identity_service (IdentityService)
        # RETURNS:
            *   BuildResult[SquareContext] containing either:
                    - On failure: Exception.
                    - On success: SquareContext in the payload.
        # RAISES:
            *   ZeroSquareContextFlagsException
            *   SquareContextBuildException
            *   ExcessiveSquareContextFlagsException
            *   SquareContextBuildRouteException
        """
        method = "SquareFinder._validate_dataset"
        # Handle the nonexistence case.
        if candidate is None:
            return ValidationResult.failure(
                SquareDataSourceNullException(
                    f"{method}: {SquareDataSourceNullException.DEFAULT_MESSAGE}"
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, List):
            return ValidationResult.failure(
                TypeError(f"{method}: Expected List[Square], got {type(candidate).__name__} instead.")
            )
        
        squares = cast(List[Square], candidate)
        # Handle the case that, the dataset is empty
        if len(squares) == 0:
            return ValidationResult.failure(
                SquareDataSourceEmptyException(f"{method}: {SquareDataSourceEmptyException.DEFAULT_MESSAGE}")
            )
        # Handle the case that, the list does not contain squares.
        if not isinstance(squares[0], Square):
            return ValidationResult.failure(
                TypeError(f"{method}: The dataset does not contain squares, it has {type(squares).__name__} instead.")
            )
        # --- Send the success result to the caller. ---#
    
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
                    - On finding a match: List[Square] in the payload.
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
                    - On finding a match: List[Square] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            None
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
            1.  Get the Squares which match the name.
        # PARAMETERS:
            *   coord (Coord)
            *   dataset (List[Square])
        # RETURNS:
            *   SearchResult[List[Square]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Square] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            None
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
        # PARAMETERS:
            *   board (Board)
            *   dataset (List[Square])
        # RETURNS:
            *   SearchResult[List[Square]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Square] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            None
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
            1.  Get the Squares which match the token.
        # PARAMETERS:
            *   board (Board)
            *   dataset (List[Square])
        # RETURNS:
            *   SearchResult[List[Square]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Square] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            None
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
    def _find_by_empty_state(cls, dataset: List[Square]) -> SearchResult[List[Square]]:
        """
        # ACTION:
            1.  Get the Squares which are empty.
        # PARAMETERS:
            *   board (Board)
            *   dataset (List[Square])
        # RETURNS:
            *   SearchResult[List[Square]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Square] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            None
        """
        matches = [square for square in dataset if square.is_empty]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_occupied_state(cls, dataset: List[Square]) -> SearchResult[List[Square]]:
        """
        # ACTION:
            1.  Get the Squares which are empty.
        # PARAMETERS:
            *   board (Board)
            *   dataset (List[Square])
        # RETURNS:
            *   SearchResult[List[Square]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Square] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            None
        """
        matches = [square for square in dataset if square.is_occupied]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)