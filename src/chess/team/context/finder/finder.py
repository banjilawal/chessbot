# src/chess/team/finder/finder.py

"""
Module: chess.team.finder.finder
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from typing import List

from chess.arena import Arena
from chess.agent import PlayerAgent
from chess.system import DataFinder, GameColor, LoggingLevelRouter, SearchResult
from chess.team import (
    Team, TeamContext, TeamContextValidator, TeamSearchDatasetNullException,
    TeamSearchIdCollisionException, TeamSearchRouteException, TeamSearchFailedException
)


class TeamFinder(DataFinder[Team]):
    """
    # ROLE: Finder

    # RESPONSIBILITIES:
    1.  Finder Team collections for items which match the attribute target specified in the TeamContext parameter.
    2.  Safely forward any errors encountered during a finder to the caller.

    # PARENT:
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
            1.  If the dataset is null send an exception in the SearchResult.
            2.  If the context is faulty send an exception in the SearchResult.
            3.  If there is no search route for the not-null context.attribute send an exception in the SearchResult.
            4.  Return the SearchResult from the attribute search route.
        # PARAMETERS:
            *   dataset (List[Team])
            *   context (TeamContext)
            *   context_validator (TeamContextValidator)
        # RETURNS:
            *   SearchResult[List[Team]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Team] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            *   TypeError
            *   TeamNullDatasetException
            *   TeamFinderOperationFailedException
        """
        method = "TeamFinder.find"
        # Don't want to run a finder if the dataset is null.
        if dataset is None:
            return SearchResult.failure(
                TeamSearchFailedException(
                    message=f"{method}: {TeamSearchFailedException.ERROR_CODE}",
                    ex=TeamSearchDatasetNullException(f"{method}: {TeamSearchDatasetNullException.DEFAULT_MESSAGE}")
                )
            )
        # certify the context is safe.
        validation_result = context_validator.validate(context)
        if validation_result.is_failure:
            return SearchResult.failure(
                TeamSearchFailedException(
                    message=f"{method}: {TeamSearchFailedException.ERROR_CODE}", ex=validation_result.exception
                )
            )
        # After context is verified select the finder method based on the which flag is enabled.
        
        # Entry point into finding by team's id.
        if context.id is not None:
            return cls._find_by_id(dataset, context.id)
        # Entry point into finding by arena team is playing in.
        if context.arena is not None:
            return cls._find_by_arena(dataset=dataset, arena=context.arena)
        # Entry point into finding by team's owner.
        if context.owner is not None:
            return cls._find_by_player_agent(dataset, context.owner)
        # Entry point into finding by team's color.
        if context.color is not None:
            return cls._find_by_color(dataset=dataset, team=context.color)
        #
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
                    - On finding a match: List[Team] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            *   TeamSearchFailedException
        """
        method = "TeamFinder._find_by_id"
        matches = [team for team in dataset if team.id == id]
        # There should be either no Teams with the id or one and only one Team will have that id.
        if len(matches) == 0:
            return SearchResult.empty()
        # Relaxing the 0 <= match_count < 2 requirement for convenience. Will handle the
        # inconsistency later.
        if len(matches) == 1:
            return SearchResult.success(payload=matches)
        # If more than one team has the same id there is an error.
        if len(matches) > 1:
            return SearchResult.failure(
                TeamSearchFailedException(
                    message=f"{method}: {TeamSearchFailedException.ERROR_CODE}",
                    ex=TeamSearchIdCollisionException(f"{method}: {TeamSearchIdCollisionException.DEFAULT_MESSAGE}")
                )
            )
        return SearchResult.failure(TeamSearchFailedException(f"{method}: {TeamSearchFailedException.ERROR_CODE}"))
    
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
                    - On finding a match: List[Team] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            *   TeamSearchFailedException
        """
        method = "TeamFinder._find_by_arena"
        matches = [team for team in dataset if team.arena == arena]
        if len(matches) == 0:
            return SearchResult.empty()
        if len(matches) >= 1:
            return SearchResult.success(payload=matches)
        return SearchResult.failure(TeamSearchFailedException(f"{method}: {TeamSearchFailedException.ERROR_CODE}"))
    
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
                    - On finding a match: List[Team] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            *   TeamSearchFailedException
        """
        method = "TeamFinder._find_by_owner"
        matches = [team for team in dataset if team.owner == owner]
        if len(matches) == 0:
            return SearchResult.empty()
        if len(matches) >= 1:
            return SearchResult.success(payload=matches)
        return SearchResult.failure(TeamSearchFailedException(f"{method}: {TeamSearchFailedException.ERROR_CODE}"))
    
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
                    - On finding a match: List[Team] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            *   TeamSearchFailedException
        """
        method = "TeamFinder._find_by_color"
        matches = [team for team in dataset if team.schema.color == color]
        if len(matches) == 0:
            return SearchResult.empty()
        if len(matches) >= 1:
            return SearchResult.success(payload=matches)
        return SearchResult.failure(TeamSearchFailedException(f"{method}: {TeamSearchFailedException.ERROR_CODE}"))
    