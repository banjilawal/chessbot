# src/chess/team/context/finder/finder.py

"""
Module: chess.team.context.finder.finder
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from typing import List

from chess.arena import Arena
from chess.agent import PlayerAgent
from chess.system import DataFinder, GameColor, LoggingLevelRouter, SearchResult
from chess.team import (
    Team, TeamContext, TeamContextValidator, TeamSearchDatasetNullException, TeamSearchRouteException,
    TeamSearchFailedException
)


class TeamFinder(DataFinder[Team]):
    """
    # ROLE: Finder

    # RESPONSIBILITIES:
    1.  Send items in a TeamList whose attribute value match the context.key value to the caller.
    2.  If a search does not complete forward the exception chain to the caller for debugging.

    # LIMITATIONS:
    1.  TeamFinder sends the raw list of matches. Resolving id collisions is the caller's responsibility.

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
            dataset: List[Team],
            context: TeamContext,
            context_validator: TeamContextValidator = TeamContextValidator()
    ) -> SearchResult[List[Team]]:
        """
        # ACTION:
        1.  If the dataset is null or the wrong type send the exception in the SearchResult.
        2.  If the context fails validation send the exception in the SearchResult. Else, route to the
            search method which matches the context key.
        3.  The search method returns either an empty result or a list of teams. Any exceptions were caught earlier
            by the search router.
       # PARAMETERS:
            *   dataset (List[Team]):
            *   context: TeamContext
            *   context_validator: TeamContextValidator
        # RETURNS:
            *   SearchResult[List[Team]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Tokem] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            *   TypeError
            *   TeamNullDatasetException
            *   TeamSearchFailedException
        """
        method = "TeamFinder.find"
        
        # Handle the case that the dataset is null.
        if dataset is None:
            # Return the exception chain on failure.
            return SearchResult.failure(
                TeamSearchFailedException(
                    message=f"{method}: {TeamSearchFailedException.ERROR_CODE}",
                    ex=TeamSearchDatasetNullException(
                        f"{method}: {TeamSearchDatasetNullException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that dataset is the wrong type
        if not isinstance(dataset, List):
            # Return the exception chain on failure.
            return SearchResult.failure(
                TeamSearchFailedException(
                    message=f"{method}: {TeamSearchFailedException.ERROR_CODE}",
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
            return cls._find_by_player_agent(dataset, context.owner)
        # Entry point into searching by team's color.
        if context.color is not None:
            return cls._find_by_color(dataset=dataset, team=context.color)
        
        # The default path is only reached when a context.key does not have a search route. Return
        # the exception chain.
        return SearchResult.failure(
            TeamSearchFailedException(
                message=f"{method}: {TeamSearchFailedException.ERROR_CODE}",
                ex=TeamSearchRouteException(f"{method}: {TeamSearchRouteException.ERROR_CODE}")
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
            *   dataset (List[PlayerAgent])
        # RETURNS:
            *   SearchResult[List[Team]] containing either:
                    - On error: Exception , payload null
                    - On searching a match: List[Team] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            *   TeamSearchFailedException
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
            *   dataset (List[PlayerAgent])
        # RETURNS:
            *   SearchResult[List[Team]] containing either:
                    - On error: Exception , payload null
                    - On searching a match: List[Team] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            *   TeamSearchFailedException
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
    def _find_by_owner(cls, dataset: [Team], owner: PlayerAgent) -> SearchResult[List[Team]]:
        """
        # ACTION:
            1.  Get any teams which have been played by the owner,
        # PARAMETERS:
            *   arena (Arena)
            *   dataset (List[PlayerAgent])
        # RETURNS:
            *   SearchResult[List[Team]] containing either:
                    - On error: Exception , payload null
                    - On searching a match: List[Team] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            *   TeamSearchFailedException
        """
        method = "TeamFinder._find_by_owner"
        matches = [team for team in dataset if team.owner == owner]
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
            *   dataset (List[PlayerAgent])
        # RETURNS:
            *   SearchResult[List[Team]] containing either:
                    - On error: Exception , payload null
                    - On searching a match: List[Team] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            *   TeamSearchFailedException
        """
        method = "TeamFinder._find_by_color"
        matches = [team for team in dataset if team.schema.color == color]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)
    