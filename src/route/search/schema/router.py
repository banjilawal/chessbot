# src/route/search/token/orange.py

"""
Module: route.search.token.orange
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List

from model import Token
from query import Query, SquareQuery
from result import SearchResult
from system import LoggingLevelRouter


class TokenSearchRouter(SearchRouter[Token]):
    """
    Role:SearchRouter

    Responsibilities:
    1.  Send bag in a TokenList whose attribute value match the context.key value to the caller.
    2.  If a search does not complete forward the exception chain to the caller for debugging.
    
    # LIMITATIONS:
    1.  TokenSearchRouter sends the raw list of matches. Resolving id collisions is the caller's responsibility.

    # PARENT
        *   SearchRouter

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def route(
            cls,
            query: SquareQuery,
            query_validator: SquareQueryValidator | None = None,
    ) -> SearchResult[List[Token]]:
            """
            # ACTION:
            1.  If the collider_candidates is null or the wrong type send the exception in the SearchResult.
            2.  If the context fails validation send the exception in the SearchResult. Else, route to the
                search method which matches the context key.
            3.  The search method returns either an empty result or a list of squares. Any exceptions were caught earlier
                by the search router.
           # PARAMETERS:
                *   collider_candidates (List[Square]):
                *   context: SquareContext
                *   context_validator: SquareContextValidator
            # RETURNS:
                *   SearchResult[List[Square]] containing either:
                        - On error: Exception , payload null
                        - On finding a match: List[Tokem] in the payload.
                        - On no matches found: Exception null, payload null
            Raises:
                *   TypeError
                *   SquareNullDatasetException
                *   SquareSearchException
            """
            method = "SquareFinder.find"
            
            if query_validator is None:
                query_validator = SquareQueryValidator()
            
            # Handle the case that, the collider_candidates is null.
            if dataset is None:
                # Return the exception chain on failure.
                return SearchResult.failure(
                    SquareSearchException(
                        msg=f"{method}: {SquareSearchException.ERR_CODE}",
                        ex=SquareSearchDatasetNullException(f"{method}: {SquareSearchDatasetNullException.MSG}")
                    )
                )
            # Handle the case that, collider_candidates is the wrong type
            if not isinstance(dataset, List):
                # Return the exception chain on failure.
                return SearchResult.failure(
                    SquareSearchException(
                        msg=f"{method}: {SquareSearchException.ERR_CODE}",
                        ex=TypeError(f"{method}: Expected List[Square], got {type(dataset).__name__} instead.")
                    )
                )
            
            # --- Route to the search method which matches the context key. ---#
            
            # Entry point into searching by square's id.
            if context.id is not None:
                return cls._find_by_id(dataset, context.id)
            # Entry point into searching by arena square is playing in.
            if context.arena is not None:
                return cls._find_by_arena(dataset=dataset, arena=context.arena)
            # Entry point into searching by square's owner.
            if context.owner is not None:
                return cls._find_by_player(dataset, context.owner)
            # Entry point into searching by square's color.
            if context.color is not None:
                return cls._find_by_color(dataset=dataset, square=context.color)
            
            # The default path is only reached when a context.key does not have a search route. Return
            # the exception chain.
            return SearchResult.failure(
                SquareSearchException(
                    msg=f"{method}: {SquareSearchException.ERR_CODE}",
                    ex=SquareSearchRouteException(f"{method}: {SquareSearchRouteException.ERR_CODE}")
                )
            )
        
        @classmethod
        @LoggingLevelRouter.monitor
        def _find_by_id(cls, dataset: List[Square], id: int) -> SearchResult[List[Square]]:
            """
            # ACTION:
                1.  Get the Square with the matching id if it exists
                2.  Multiple, unique matches in the result indicate that  a problem.
            # PARAMETERS:
                *   id (int)
                *   collider_candidates (List[Player])
            # RETURNS:
                *   SearchResult[List[Square]] containing either:
                        - On error: Exception , payload null
                        - On searching a match: List[Square] in the payload.
                        - On no matches found: Exception null, payload null
            Raises:
                *   SquareSearchException
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
        def _find_by_arena(cls, dataset: [Square], arena: Arena) -> SearchResult[List[Square]]:
            """
            # ACTION:
                1.  Get any squares which have entered the arena
            # PARAMETERS:
                *   arena (Arena)
                *   collider_candidates (List[Player])
            # RETURNS:
                *   SearchResult[List[Square]] containing either:
                        - On error: Exception , payload null
                        - On searching a match: List[Square] in the payload.
                        - On no matches found: Exception null, payload null
            Raises:
                *   SquareSearchException
            """
            method = "SquareFinder._find_by_arena"
            matches = [square for square in dataset if square.arena == arena]
            # Handle the nothing found case.
            if len(matches) == 0:
                return SearchResult.empty()
            # Only other case
            return SearchResult.success(payload=matches)
        
        @classmethod
        @LoggingLevelRouter.monitor
        def _find_by_player(cls, dataset: [Square], player: Player) -> SearchResult[List[Square]]:
            """
            # ACTION:
                1.  Get any squares which have been played by the owner,
            # PARAMETERS:
                *   arena (Arena)
                *   collider_candidates (List[Player])
            # RETURNS:
                *   SearchResult[List[Square]] containing either:
                        - On error: Exception , payload null
                        - On searching a match: List[Square] in the payload.
                        - On no matches found: Exception null, payload null
            Raises:
                *   SquareSearchException
            """
            method = "SquareFinder._find_by_player"
            matches = [square for square in dataset if square.owner == player]
            # Handle the nothing found case.
            if len(matches) == 0:
                return SearchResult.empty()
            # Only other case
            return SearchResult.success(payload=matches)
        
        @classmethod
        @LoggingLevelRouter.monitor
        def _find_by_color(cls, dataset: List[Square], color: GameColor) -> SearchResult[List[Square]]:
            """
            # ACTION:
                1.  Get any squares which have been assigned the targeted color
            # PARAMETERS:
                *   arena (Arena)
                *   collider_candidates (List[Player])
            # RETURNS:
                *   SearchResult[List[Square]] containing either:
                        - On error: Exception , payload null
                        - On searching a match: List[Square] in the payload.
                        - On no matches found: Exception null, payload null
            Raises:
                *   SquareSearchException
            """
            method = "SquareFinder._find_by_color"
            matches = [square for square in dataset if square.schema.color == color]
            # Handle the nothing found case.
            if len(matches) == 0:
                return SearchResult.empty()
            # Only other case
            return SearchResult.success(payload=matches)