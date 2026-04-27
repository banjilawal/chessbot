# src/route/search/board/__init__.py

"""
Module: route.search.board.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List

from model import Board
from model.query import BoardQuery
from result import SearchResult
from route import Router
from system import LoggingLevelRouter


class BoardSearchRouter(Router[Board]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def route(
            cls,
            query: BoardQuery,
            query_validator: BoardQueryValidator | None = None,
    ) -> SearchResult[List[Board]]:
        """
        # ACTION:
        1.  If the collider_candidates is null or the wrong type send the exception in the SearchResult.
        2.  If the context fails validation send the exception in the SearchResult. Else, route to the
            search method which matches the context key.
        3.  The search method returns either an empty result or a list of boards. Any exceptions were caught earlier
            by the search router.
       # PARAMETERS:
            *   collider_candidates (List[Board]):
            *   context: BoardContext
            *   context_validator: BoardContextValidator
        # RETURNS:
            *   SearchResult[List[Board]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Board] in the payload.
                    - On no matches found: Exception null, payload null
        Raises:
            *   BoardSearchPayloadTypeException
            *   BoardNullDatasetException
            *   BoardSearchException
        """
        method = "BoardFinder.find"
        
        # Handle the case that, the collider_candidates is null.
        if dataset is None:
            # Send the exception chain on failure.
            return SearchResult.failure(
                BoardSearchException(
                    msg=f"{method}: {BoardSearchException.ERR_CODE}",
                    ex=BoardSearchNullDatasetException(f"{method}: {BoardSearchNullDatasetException.MSG}")
                )
            )
        # Handle the case that, collider_candidates is the wrong type
        if not isinstance(dataset, List):
            # Send the exception chain on failure.
            return SearchResult.failure(
                BoardSearchException(
                    msg=f"{method}: {BoardSearchException.ERR_CODE}",
                    ex=BoardSearchPayloadTypeException(f"{method}: {BoardSearchPayloadTypeException.MSG}")
                )
            )
        # Handle the case that, the context fails validation.
        validation_result = context_validator.validate(context)
        if validation_result.is_failure:
            # Send the exception chain on failure.
            return SearchResult.failure(
                BoardSearchException(
                    msg=f"{method}: {BoardSearchException.ERR_CODE}",
                    ex=validation_result.exception
                )
            )
        # --- Route to the search method which matches the context key. ---#
        
        # Entry point into finding by board's id.
        if context.id is not None:
            return cls._find_by_id(dataset=dataset, id=context.id)
        # Entry point into searching by board's arena.
        if context.arena is not None:
            return cls._find_by_arena(dataset=dataset, coord=context.arena)
        
        # If a context does not have a search route defined send an exception chain.
        return SearchResult.failure(
            BoardSearchException(
                msg=f"{method}: {BoardSearchException.ERR_CODE}",
                ex=BoardSearchRouteException(f"{method}: {BoardSearchRouteException.MSG}")
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_id(cls, dataset: List[Board], id: int) -> SearchResult[List[Board]]:
        """
        # ACTION:
            1.  Get the Boards with the desired id.
        # PARAMETERS:
            *   id (int)
            *   collider_candidates (List[Board])
        # RETURNS:
            *   SearchResult[List[Board]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Board] in the payload.
                    - On no matches found: Exception null, payload null
        Raises:
            None
        """
        matches = [board for board in dataset if board.id == id]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_arena(cls, dataset: List[Board], arena: Arena) -> SearchResult[List[Board]]:
        """
        # ACTION:
            1.  Get the Boards which match the arena.
        # PARAMETERS:
            *   arena (Arena)
            *   collider_candidates (List[Board])
        # RETURNS:
            *   SearchResult[List[Board]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Board] in the payload.
                    - On no matches found: Exception null, payload null
        Raises:
            None
        """
        matches = [board for board in dataset if board.arena == arena]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)