# src/chess/board/searcher/finder.py

"""
Module: chess.board.searcher.service
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import List

from chess.arena import Arena
from chess.coord import Coord
from chess.system import DataFinder, LoggingLevelRouter, SearchResult
from chess.board import (
    Board, BoardContext, BoardContextValidator, BoardSearchFailedException, BoardSearchRouteException,
    BoardSearchNullDatasetException, BoardSearchPayloadTypeException,
)


class BoardFinder(DataFinder[Board]):
    """
    # ROLE: AbstractSearcher

    # RESPONSIBILITIES:
    1.  Send items in a BoardList whose attribute value match the context.key value to the caller.
    2.  If a search does not complete forward the exception chain to the caller for debugging.

    # LIMITATIONS:
    1.  BoardFinder sends the raw list of matches. Resolving id collisions is the caller's responsibility.

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
            dataset: List[Board],
            context: BoardContext,
            context_validator: BoardContextValidator = BoardContextValidator()
    ) -> SearchResult[List[Board]]:
        """
        # ACTION:
        1.  If the dataset is null or the wrong type send the exception in the SearchResult.
        2.  If the context fails validation send the exception in the SearchResult. Else, route to the 
            search method which matches the context key.
        3.  The search method returns either an empty result or a list of boards. Any exceptions were caught earlier
            by the search router.
       # PARAMETERS:
            *   dataset (List[Board]):
            *   context: BoardContext
            *   context_validator: BoardContextValidator
        # RETURNS:
            *   SearchResult[List[Board]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Board] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            *   BoardSearchPayloadTypeException
            *   BoardNullDatasetException
            *   BoardSearchFailedException
        """
        method = "BoardFinder.find"
        
        # Handle the case that the dataset is null.
        if dataset is None:
            # Return the exception chain on failure.
            return SearchResult.failure(
                BoardSearchFailedException(
                    message=f"{method}: {BoardSearchFailedException.ERROR_CODE}",
                    ex=BoardSearchNullDatasetException( f"{method}: {BoardSearchNullDatasetException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the case that dataset is the wrong type
        if not isinstance(dataset, List):
            # Return the exception chain on failure.
            return SearchResult.failure(
                BoardSearchFailedException(
                    message=f"{method}: {BoardSearchFailedException.ERROR_CODE}",
                    ex=BoardSearchPayloadTypeException(f"{method}: {BoardSearchPayloadTypeException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the case that the context fails validation.
        validation_result = context_validator.validate(context)
        if validation_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                BoardSearchFailedException(
                    message=f"{method}: {BoardSearchFailedException.ERROR_CODE}",
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
            BoardSearchFailedException(
                message=f"{method}: {BoardSearchFailedException.ERROR_CODE}",
                ex=BoardSearchRouteException(f"{method}: {BoardSearchRouteException.DEFAULT_MESSAGE}")
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
            *   dataset (List[Board])
        # RETURNS:
            *   SearchResult[List[Board]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Board] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
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
            *   dataset (List[Board])
        # RETURNS:
            *   SearchResult[List[Board]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Board] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            None
        """
        matches = [board for board in dataset if board.arena == arena]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)