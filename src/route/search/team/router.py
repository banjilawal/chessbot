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
from model.query import TeamQuery
from result import SearchResult
from route import SearchRouter
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
            query: TeamQuery,
            query_validator: TeamQueryValidator | None = None,
    ) -> SearchResult[List[Token]]:
            """
            # ACTION:
            1.  If the collider_candidates is null or the wrong type send the exception in the SearchResult.
            2.  If the context fails validation send the exception in the SearchResult. Else, route to the
                search method which matches the context key.
            3.  The search method returns either an empty result or a list of teams. Any exceptions were caught earlier
                by the search router.
           # PARAMETERS:
                *   collider_candidates (List[Team]):
                *   context: TeamContext
                *   context_validator: TeamContextValidator
            # RETURNS:
                *   SearchResult[List[Team]] containing either:
                        - On error: Exception , payload null
                        - On finding a match: List[Tokem] in the payload.
                        - On no matches found: Exception null, payload null
            Raises:
                *   TypeError
                *   TeamNullDatasetException
                *   TeamSearchException
            """
            method = "TeamFinder.find"
            
            if query_validator is None:
                query_validator = TeamQueryValidator()
            
            # Handle the case that, the collider_candidates is null.
            if dataset is None:
                # Send the exception chain on failure.
                return SearchResult.failure(
                    TeamSearchException(
                        msg=f"{method}: {TeamSearchException.ERR_CODE}",
                        ex=TeamSearchDatasetNullException(f"{method}: {TeamSearchDatasetNullException.MSG}")
                    )
                )
            # Handle the case that, collider_candidates is the wrong type
            if not isinstance(dataset, List):
                # Send the exception chain on failure.
                return SearchResult.failure(
                    TeamSearchException(
                        msg=f"{method}: {TeamSearchException.ERR_CODE}",
                        ex=TypeError(f"{method}: Expected List[Team], got {type(dataset).__name__} instead.")
                    )
                )
            
            # --- Route to the search method which matches the context key. ---#
            
            # Entry point into searching by team's id.
            if context.id is not None:
                return cls._find_by_id(dataset, context.id)
            # Entry point into searching by arena team is playing in.
            if context.arena is not None:
                return cls._find_by_arena(dataset=dataset, arena=context.arena)
            # Entry point into searching by team's owner.
            if context.owner is not None:
                return cls._find_by_player(dataset, context.owner)
            # Entry point into searching by team's color.
            if context.color is not None:
                return cls._find_by_color(dataset=dataset, team=context.color)
            
            # The default path is only reached when a context.key does not have a search route. Return
            # the exception chain.
            return SearchResult.failure(
                TeamSearchException(
                    msg=f"{method}: {TeamSearchException.ERR_CODE}",
                    ex=TeamSearchRouteException(f"{method}: {TeamSearchRouteException.ERR_CODE}")
                )
            )
        
        @classmethod
        @LoggingLevelRouter.monitor
        def _find_by_id(cls, dataset: List[Team], id: int) -> SearchResult[List[Team]]:
            """
            # ACTION:
                1.  Get the Team with the matching id if it exists
                2.  Multiple, unique matches in the result indicate that  a problem.
            # PARAMETERS:
                *   id (int)
                *   collider_candidates (List[Player])
            # RETURNS:
                *   SearchResult[List[Team]] containing either:
                        - On error: Exception , payload null
                        - On searching a match: List[Team] in the payload.
                        - On no matches found: Exception null, payload null
            Raises:
                *   TeamSearchException
            """
            method = "TeamFinder._find_by_id"
            
            matches = [team for team in dataset if team.id == id]
            # Handle the nothing found case.
            if len(matches) == 0:
                return SearchResult.empty()
            # Only other case
            return SearchResult.success(payload=matches)
        
        @classmethod
        @LoggingLevelRouter.monitor
        def _find_by_arena(cls, dataset: [Team], arena: Arena) -> SearchResult[List[Team]]:
            """
            # ACTION:
                1.  Get any teams which have entered the arena
            # PARAMETERS:
                *   arena (Arena)
                *   collider_candidates (List[Player])
            # RETURNS:
                *   SearchResult[List[Team]] containing either:
                        - On error: Exception , payload null
                        - On searching a match: List[Team] in the payload.
                        - On no matches found: Exception null, payload null
            Raises:
                *   TeamSearchException
            """
            method = "TeamFinder._find_by_arena"
            matches = [team for team in dataset if team.arena == arena]
            # Handle the nothing found case.
            if len(matches) == 0:
                return SearchResult.empty()
            # Only other case
            return SearchResult.success(payload=matches)
        
        @classmethod
        @LoggingLevelRouter.monitor
        def _find_by_player(cls, dataset: [Team], player: Player) -> SearchResult[List[Team]]:
            """
            # ACTION:
                1.  Get any teams which have been played by the owner,
            # PARAMETERS:
                *   arena (Arena)
                *   collider_candidates (List[Player])
            # RETURNS:
                *   SearchResult[List[Team]] containing either:
                        - On error: Exception , payload null
                        - On searching a match: List[Team] in the payload.
                        - On no matches found: Exception null, payload null
            Raises:
                *   TeamSearchException
            """
            method = "TeamFinder._find_by_player"
            matches = [team for team in dataset if team.owner == player]
            # Handle the nothing found case.
            if len(matches) == 0:
                return SearchResult.empty()
            # Only other case
            return SearchResult.success(payload=matches)
        
        @classmethod
        @LoggingLevelRouter.monitor
        def _find_by_color(cls, dataset: List[Team], color: GameColor) -> SearchResult[List[Team]]:
            """
            # ACTION:
                1.  Get any teams which have been assigned the targeted color
            # PARAMETERS:
                *   arena (Arena)
                *   collider_candidates (List[Player])
            # RETURNS:
                *   SearchResult[List[Team]] containing either:
                        - On error: Exception , payload null
                        - On searching a match: List[Team] in the payload.
                        - On no matches found: Exception null, payload null
            Raises:
                *   TeamSearchException
            """
            method = "TeamFinder._find_by_color"
            matches = [team for team in dataset if team.schema.color == color]
            # Handle the nothing found case.
            if len(matches) == 0:
                return SearchResult.empty()
            # Only other case
            return SearchResult.success(payload=matches)