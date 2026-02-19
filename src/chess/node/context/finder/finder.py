# src/chess/node/context/finder/finder.py

"""
Module: chess.node.context.finder.finder
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import List

from chess.square import Square
from chess.system import LoggingLevelRouter, SearchResult, StackSearcher
from chess.node import (
    DiscoveryStatus, Node, NodeContext, NodeContextValidator, NodeSearchFailedException, NodeSearchRouteException,
    NodeSearchNullDatasetException, NodeSearchPayloadTypeException
)


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
        
        # Entry point into finding by item's priority.
        if context.priority is not None:
            return cls._find_by_priority(dataset=dataset, priority=context.priority)
        # Entry point into finding by item's square.
        if context.square is not None:
            return cls._find_by_square(dataset=dataset, square=context.square)
        # Entry point into searching by item's predecessor.
        if context.predecessor is not None:
            return cls._find_by_predecessor(dataset=dataset, priority=context.predecessor)
        # Entry point into searching by discovery status.
        if context.discovery_status is not None:
            return cls._find_by_discovery_status(dataset=dataset, discovery_status=context.discovery_status)
        
        # If a context does not have a search route defined send an exception chain.
        return SearchResult.failure(
            NodeSearchFailedException(
                message=f"{method}: {NodeSearchFailedException.ERROR_CODE}",
                ex=NodeSearchRouteException(f"{method}: {NodeSearchRouteException.DEFAULT_MESSAGE}")
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_priority(cls, dataset: List[Node], priority: int) -> SearchResult[List[Node]]:
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
        method = "NodeFinder._find_by_priority"
        matches = [node for node in dataset if node.priority == priority]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_square(cls, dataset: List[Node], square: Square) -> SearchResult[List[Node]]:
        """
        # ACTION:
            1.  Get the Nodes which match the square.
        # PARAMETERS:
            *   square (square)
            *   dataset (List[Node])
        # RETURNS:
            *   SearchResult[List[Node]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Node] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            None
        """
        matches = [node for node in dataset if node.square == square]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_predecessor(cls, dataset: List[Node], predecessor: Node) -> SearchResult[List[Node]]:
        """
        # ACTION:
            1.  Get the Nodes which match the predecessor.
        # PARAMETERS:
            *   predecessor (Predecessor)
            *   dataset (List[Node])
        # RETURNS:
            *   SearchResult[List[Node]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Node] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            None
        """
        matches = [node for node in dataset if node.predecessor == predecessor]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_discovery_status(
            cls,
            dataset: List[Node],
            discovery_status: DiscoveryStatus
    ) -> SearchResult[List[Node]]:
        """
        # ACTION:
            1.  Get the Nodes which are empty.
        # PARAMETERS:
            *   predecessor (Predecessor)
            *   dataset (List[Node])
        # RETURNS:
            *   SearchResult[List[Node]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Node] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            None
        """
        matches = [node for node in dataset if node.discovery_status == discovery_status]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)