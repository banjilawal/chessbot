# src/chess/node/context/finder/finder.py

"""
Module: chess.node.context.finder.finder
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import List

from chess.board import Board
from chess.coord import Coord
from chess.system import LoggingLevelRouter, SearchResult, StackSearcher
from chess.node import (
    Node, NodeContext, NodeContextValidator, NodeSearchFailedException, NodeSearchRouteException,
    NodeSearchNullDatasetException, NodeSearchPayloadTypeException, NodeState
)
from chess.token import Token


class NodeFinder(StackSearcher[Node]):
    """
    # ROLE: AbstractSearcher

    # RESPONSIBILITIES:
    1.  Send bag in a NodeList whose attribute value match the context.key value to the caller.
    2.  If a search does not complete forward the exception chain to the caller for debugging.

    # LIMITATIONS:
    1.  NodeFinder sends the raw list of matches. Resolving id collisions is the caller's responsibility.

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
            dataset: List[Node],
            context: NodeContext,
            context_validator: NodeContextValidator = NodeContextValidator()
    ) -> SearchResult[List[Node]]:
        """
        # ACTION:
        1.  If the dataset is null or the wrong type send the exception in the SearchResult.
        2.  If the context fails validation send the exception in the SearchResult. Else, route to the 
            search method which matches the context key.
        3.  The search method returns either an empty result or a list of nodes. Any exceptions were caught earlier
            by the search router.
       # PARAMETERS:
            *   dataset (List[Node]):
            *   context: NodeContext
            *   context_validator: NodeContextValidator
        # RETURNS:
            *   SearchResult[List[Node]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Node] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            *   NodeSearchPayloadTypeException
            *   NodeNullDatasetException
            *   NodeSearchFailedException
        """
        method = "NodeFinder.find"
        
        # Handle the case that the dataset is null.
        if dataset is None:
            # Return the exception chain on failure.
            return SearchResult.failure(
                NodeSearchFailedException(
                    message=f"{method}: {NodeSearchFailedException.ERROR_CODE}",
                    ex=NodeSearchNullDatasetException(
                        f"{method}: {NodeSearchNullDatasetException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that dataset is the wrong type
        if not isinstance(dataset, List):
            # Return the exception chain on failure.
            return SearchResult.failure(
                NodeSearchFailedException(
                    message=f"{method}: {NodeSearchFailedException.ERROR_CODE}",
                    ex=NodeSearchPayloadTypeException(
                        f"{method}: {NodeSearchPayloadTypeException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that the context fails validation.
        validation_result = context_validator.validate(context)
        if validation_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                NodeSearchFailedException(
                    message=f"{method}: {NodeSearchFailedException.ERROR_CODE}",
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
        if context.state is not None and context.state == NodeState.EMPTY:
            return cls._find_by_empty_state(dataset=dataset)
        # Entry point into searching by fullness.
        if context.state is not None and context.state == NodeState.OCCUPIED:
            return cls._find_by_occupied_state(dataset=dataset)
        
        # If a context does not have a search route defined send an exception chain.
        return SearchResult.failure(
            NodeSearchFailedException(
                message=f"{method}: {NodeSearchFailedException.ERROR_CODE}",
                ex=NodeSearchRouteException(f"{method}: {NodeSearchRouteException.DEFAULT_MESSAGE}")
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_id(cls, dataset: List[Node], id: int) -> SearchResult[List[Node]]:
        """
        # ACTION:
            1.  Get the Nodes with the desired id.
        # PARAMETERS:
            *   id (int)
            *   dataset (List[Node])
        # RETURNS:
            *   SearchResult[List[Node]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Node] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            None
        """
        method = "NodeFinder._find_by_id"
        matches = [node for node in dataset if node.id == id]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_name(cls, dataset: List[Node], name: str) -> SearchResult[List[Node]]:
        """
        # ACTION:
            1.  Get the Nodes which match the name.
        # PARAMETERS:
            *   name (str)
            *   dataset (List[Node])
        # RETURNS:
            *   SearchResult[List[Node]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Node] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            None
        """
        matches = [node for node in dataset if node.name.upper() == name.upper()]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_coord(cls, dataset: List[Node], coord: Coord) -> SearchResult[List[Node]]:
        """
        # ACTION:
            1.  Get the Nodes which match the name.
        # PARAMETERS:
            *   coord (Coord)
            *   dataset (List[Node])
        # RETURNS:
            *   SearchResult[List[Node]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Node] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            None
        """
        matches = [node for node in dataset if node.coord == coord]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_board(cls, dataset: List[Node], board: Board) -> SearchResult[List[Node]]:
        """
        # ACTION:
            1.  Get the Nodes which match the board.
        # PARAMETERS:
            *   board (Board)
            *   dataset (List[Node])
        # RETURNS:
            *   SearchResult[List[Node]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Node] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            None
        """
        matches = [node for node in dataset if node.board == board]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_occupant(cls, dataset: List[Node], occupant: Token) -> SearchResult[List[Node]]:
        """
        # ACTION:
            1.  Get the Nodes which match the token.
        # PARAMETERS:
            *   board (Board)
            *   dataset (List[Node])
        # RETURNS:
            *   SearchResult[List[Node]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Node] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            None
        """
        matches = [
            node for node in dataset if (node.occupant is not None and node.occupant) == occupant
        ]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_empty_state(cls, dataset: List[Node]) -> SearchResult[List[Node]]:
        """
        # ACTION:
            1.  Get the Nodes which are empty.
        # PARAMETERS:
            *   board (Board)
            *   dataset (List[Node])
        # RETURNS:
            *   SearchResult[List[Node]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Node] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            None
        """
        matches = [node for node in dataset if node.is_empty]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_occupied_state(cls, dataset: List[Node]) -> SearchResult[List[Node]]:
        """
        # ACTION:
            1.  Get the Nodes which are empty.
        # PARAMETERS:
            *   board (Board)
            *   dataset (List[Node])
        # RETURNS:
            *   SearchResult[List[Node]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Node] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            None
        """
        matches = [node for node in dataset if node.is_occupied]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)