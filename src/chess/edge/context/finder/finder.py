# src/chess/edge/context/finder/finder.py

"""
Module: chess.edge.context.finder.finder
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import List

from chess.board import Board
from chess.coord import Coord
from chess.system import LoggingLevelRouter, SearchResult, StackSearcher
from chess.edge import (
    Edge, EdgeContext, EdgeContextValidator, EdgeSearchException, EdgeSearchRouteException,
    EdgeSearchNullDatasetException, EdgeSearchPayloadTypeException, EdgeState
)
from chess.token import Token


class EdgeFinder(StackSearcher[Edge]):
    """
    # ROLE: AbstractSearcher

    # RESPONSIBILITIES:
    1.  Send bag in a EdgeList whose attribute value match the context.key value to the caller.
    2.  If a search does not complete forward the exception chain to the caller for debugging.

    # LIMITATIONS:
    1.  EdgeFinder sends the raw list of matches. Resolving id collisions is the caller's responsibility.

    # PARENT
        *   AbstractSearcher

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
            dataset: List[Edge],
            context: EdgeContext,
            context_validator: EdgeContextValidator = EdgeContextValidator()
    ) -> SearchResult[List[Edge]]:
        """
        # ACTION:
        1.  If the dataset is null or the wrong type send the exception in the SearchResult.
        2.  If the context fails validation send the exception in the SearchResult. Else, route to the 
            search method which matches the context key.
        3.  The search method returns either an empty result or a list of edges. Any exceptions were caught earlier
            by the search router.
       # PARAMETERS:
            *   dataset (List[Edge]):
            *   context: EdgeContext
            *   context_validator: EdgeContextValidator
        # RETURNS:
            *   SearchResult[List[Edge]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Edge] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            *   EdgeSearchPayloadTypeException
            *   EdgeNullDatasetException
            *   EdgeSearchException
        """
        method = "EdgeFinder.find"
        
        # Handle the case that the dataset is null.
        if dataset is None:
            # Return the exception chain on failure.
            return SearchResult.failure(
                EdgeSearchException(
                    message=f"{method}: {EdgeSearchException.ERROR_CODE}",
                    ex=EdgeSearchNullDatasetException(
                        f"{method}: {EdgeSearchNullDatasetException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that dataset is the wrong type
        if not isinstance(dataset, List):
            # Return the exception chain on failure.
            return SearchResult.failure(
                EdgeSearchException(
                    message=f"{method}: {EdgeSearchException.ERROR_CODE}",
                    ex=EdgeSearchPayloadTypeException(
                        f"{method}: {EdgeSearchPayloadTypeException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that the context fails validation.
        validation_result = context_validator.validate(context)
        if validation_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                EdgeSearchException(
                    message=f"{method}: {EdgeSearchException.ERROR_CODE}",
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
        if context.state is not None and context.state == EdgeState.EMPTY:
            return cls._find_by_empty_state(dataset=dataset)
        # Entry point into searching by fullness.
        if context.state is not None and context.state == EdgeState.OCCUPIED:
            return cls._find_by_occupied_state(dataset=dataset)
        
        # If a context does not have a search route defined send an exception chain.
        return SearchResult.failure(
            EdgeSearchException(
                message=f"{method}: {EdgeSearchException.ERROR_CODE}",
                ex=EdgeSearchRouteException(f"{method}: {EdgeSearchRouteException.DEFAULT_MESSAGE}")
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_id(cls, dataset: List[Edge], id: int) -> SearchResult[List[Edge]]:
        """
        # ACTION:
            1.  Get the Edges with the desired id.
        # PARAMETERS:
            *   id (int)
            *   dataset (List[Edge])
        # RETURNS:
            *   SearchResult[List[Edge]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Edge] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            None
        """
        method = "EdgeFinder._find_by_id"
        matches = [edge for edge in dataset if edge.id == id]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_name(cls, dataset: List[Edge], name: str) -> SearchResult[List[Edge]]:
        """
        # ACTION:
            1.  Get the Edges which match the name.
        # PARAMETERS:
            *   name (str)
            *   dataset (List[Edge])
        # RETURNS:
            *   SearchResult[List[Edge]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Edge] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            None
        """
        matches = [edge for edge in dataset if edge.name.upper() == name.upper()]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_coord(cls, dataset: List[Edge], coord: Coord) -> SearchResult[List[Edge]]:
        """
        # ACTION:
            1.  Get the Edges which match the name.
        # PARAMETERS:
            *   coord (Coord)
            *   dataset (List[Edge])
        # RETURNS:
            *   SearchResult[List[Edge]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Edge] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            None
        """
        matches = [edge for edge in dataset if edge.coord == coord]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_board(cls, dataset: List[Edge], board: Board) -> SearchResult[List[Edge]]:
        """
        # ACTION:
            1.  Get the Edges which match the board.
        # PARAMETERS:
            *   board (Board)
            *   dataset (List[Edge])
        # RETURNS:
            *   SearchResult[List[Edge]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Edge] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            None
        """
        matches = [edge for edge in dataset if edge.board == board]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_occupant(cls, dataset: List[Edge], occupant: Token) -> SearchResult[List[Edge]]:
        """
        # ACTION:
            1.  Get the Edges which match the token.
        # PARAMETERS:
            *   board (Board)
            *   dataset (List[Edge])
        # RETURNS:
            *   SearchResult[List[Edge]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Edge] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            None
        """
        matches = [
            edge for edge in dataset if (edge.occupant is not None and edge.occupant) == occupant
        ]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_empty_state(cls, dataset: List[Edge]) -> SearchResult[List[Edge]]:
        """
        # ACTION:
            1.  Get the Edges which are empty.
        # PARAMETERS:
            *   board (Board)
            *   dataset (List[Edge])
        # RETURNS:
            *   SearchResult[List[Edge]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Edge] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            None
        """
        matches = [edge for edge in dataset if edge.is_empty]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_occupied_state(cls, dataset: List[Edge]) -> SearchResult[List[Edge]]:
        """
        # ACTION:
            1.  Get the Edges which are empty.
        # PARAMETERS:
            *   board (Board)
            *   dataset (List[Edge])
        # RETURNS:
            *   SearchResult[List[Edge]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Edge] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            None
        """
        matches = [edge for edge in dataset if edge.is_occupied]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)