# src/chess/team/map/finder/finder.py

"""
Module: chess.team.map.finder.finder
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from typing import List

from chess.arena import Arena
from chess.agent import PlayerAgent
from chess.system import GameColor, LoggingLevelRouter, Finder, SearchResult
from chess.team import (
    Team, TeamContext, TeamContextValidator, TeamFinderOperationFailedException, TeamSearchDatasetNullException
)


class TeamFinder(Finder[Team]):
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
        # Action:
        1.  Verify the dataset is not null and contains only Team objects,
        2.  Use context_validator to certify the provided map.
        3.  Context attribute routes the finder. Attribute value is the finder target.
        4.  The outcome of the finder is sent back to the caller in a SearchResult object.

        # Parameters:
            *   dataset (List[Team]):
            *   map: TeamContext
            *   context_validator: TeamContextValidator

        # Returns:
        SearchResult[List[Team]] containing either:
            - On finding a match: List[Team] in the payload.
            - On error: Exception , payload null
            - On no matches found: Exception null, payload null

        # Raises:
            *   TypeError
            *   TeamNullDatasetException
            *   TeamFinderOperationFailedException
        """
        method = "TeamFinder.find"
        try:
            # Don't want to run a finder if the dataset is null.
            if dataset is None:
                return SearchResult.failure(
                    TeamSearchDatasetNullException(f"{method}: {TeamSearchDatasetNullException.DEFAULT_MESSAGE}")
                )
            # certify the map is safe.
            validation_result = context_validator.validate(context)
            if validation_result.is_failure:
                return SearchResult.failure(validation_result.exception)
            # After map is verified select the finder method based on the which flag is enabled.
            
            # Entry point into finding by team's id.
            if context.id is not None:
                return cls._find_by_id(dataset, context.id)
            # Entry point into finding by team's designation.
            if context.name is not None:
                return cls._find_by_name(dataset=dataset, name=context.name)
            # Entry point into finding by arena team is playing in.
            if context.arena is not None:
                return cls._find_by_arena(dataset=dataset, arena=context.arena)
            # Entry point into finding by team's player_agent.
            if context.player_agent is not None:
                return cls._find_by_player_agent(dataset, context.player_agent)
            # Entry point into finding by team's color.
            if context.color is not None:
                return cls._find_by_color(dataset=dataset, team=context.color)
                
                # As a failsafe send a buildResult failure if a map path was missed.
            SearchResult.failure(
                FailsafeBranchExitPointException(f"{method}: {FailsafeBranchExitPointException.DEFAULT_MESSAGE}")
            )
            
            # Finally, if some exception is not handled by the checks wrap it inside an SearchFailedException
            # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                SearchFailedException(ex=ex, message=f"{method}: {SearchFailedException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_id(cls, dataset: List[Team], id: int) -> SearchResult[List[Team]]:
        """
        # Action:
        1.  Get the Team with the matching id if it exists
        2.  Multiple, unique matches in the result indicate that  a problem.

        # Parameters:
            *   id (int)
            *   dataset (List[Team])

        # Returns:
        SearchResult[List[Team]] containing either:
            - On finding a match: List[Team] in the payload.
            - On error: Exception , payload null
            - On no matches found: Exception null, payload null

        # Raises:
            *   TeamFinderOperationFailedException
        """
        method = "TeamFinder._find_by_id"
        try:
            matches = [team for team in dataset if team.id == id]
            # There should be either no Teams with the id or one and only one Team will have that id.
            if len(matches) == 0:
                return SearchResult.empty()
            # Relaxing the 0 <= match_count < 2 requirement for convenience. Will handle the
            # inconsistency later.
            if len(matches) >= 1:
                return SearchResult.success(payload=matches)
            
            # Finally, if some exception is not handled by the checks wrap it inside an SearchFailedException
            # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                SearchFailedException(ex=ex, message=f"{method}: {SearchFailedException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_name(cls, dataset: List[Team], name: str) -> SearchResult[List[Team]]:
        """
        # Action:
        1.  Get the Team with the matching designation if it exists
        2.  There's only two possible team names so multiple matches are possible.
        
        # Parameters:
            *   dataset: (List[Team])
            *   designation (str)

        # Returns:
        SearchResult[List[Team]] containing either:
            - On finding a match: List[Team] in the payload.
            - On error: Exception , payload null
            - On no matches found: Exception null, payload null

        # Raises:
            *   TeamFinderOperationFailedException
        """
        method = "TeamFinder._find_by_name"
        try:
            matches = [team for team in dataset if team.schema.name.upper() == name.upper()]
            if len(matches) == 0:
                return SearchResult.empty()
            if len(matches) >= 1:
                return SearchResult.success(payload=matches)
            
            # Finally, if some exception is not handled by the checks wrap it inside an SearchFailedException
            # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                SearchFailedException(ex=ex, message=f"{method}: {SearchFailedException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_arena(cls, dataset: [Team], arena: Arena) -> SearchResult[List[Team]]:
        """
        # Action:
        1.  Get the Team with the matching arena if it exists.

        # Parameters:
            *   arena (Arena)
            *   dataset (List[PlayerAgent])

        # Returns:
        SearchResult[List[Team]] containing either:
            - On finding a match: List[Team] in the payload.
            - On error: Exception , payload null
            - On no matches found: Exception null, payload null

        # Raises:
            *   TeamFinderOperationFailedException
        """
        method = "TeamFinder._find_by_arena"
        try:
            matches = [team for team in dataset if team.arena == arena]
            if len(matches) == 0:
                return SearchResult.empty()
            if len(matches) >= 1:
                return SearchResult.success(payload=matches)
            
            # Finally, if some exception is not handled by the checks wrap it inside an SearchFailedException
            # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                SearchFailedException(ex=ex, message=f"{method}: {SearchFailedException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_player_agent(cls, dataset: [Team], player_agent: PlayerAgent) -> SearchResult[List[Team]]:
        """
        # Action:
        1.  Get the Team with the matching agent if it exists

        # Parameters:
            *   player_agent (PlayerAgent)
            *   dataset (List[PlayerAgent])

        # Returns:
        SearchResult[List[Team]] containing either:
            - On finding a match: List[Team] in the payload.
            - On error: Exception , payload null
            - On no matches found: Exception null, payload null

        # Raises:
            *   TeamFinderOperationFailedException
        """
        method = "TeamFinder._find_by_player_agent"
        try:
            matches = [team for team in dataset if team.player_agent == player_agent]
            if len(matches) == 0:
                return SearchResult.empty()
            if len(matches) >= 1:
                return SearchResult.success(payload=matches)
            
            # Finally, if some exception is not handled by the checks wrap it inside an SearchFailedException
            # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                SearchFailedException(ex=ex, message=f"{method}: {SearchFailedException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_color(cls, dataset: List[Team], color: GameColor) -> SearchResult[List[Team]]:
        """
        # Action:
        1.  Get the team_service whose color matched the target.
        2.  If no matches are found return an empty SearchResult.
        3.  If exactly one match is found return a successful SearchResult with the single item in an array.

        # Parameters:
            *   dataset: (List[Team])
            *   color (ArenaColor)

        # Returns:
        SearchResult[List[Team]] containing either:
            - On finding a match: List[Team] in the payload.
            - On error: Exception , payload null
            - On no matches found: Exception null, payload null

        # Raises:
            *   TeamFinderOperationFailedException
        """
        method = "TeamFinder._find_by_color"
        
        try:
            matches = [team for team in dataset if team.schema.color == color]
            if len(matches) == 0:
                return SearchResult.empty()
            if len(matches) >= 1:
                return SearchResult.success(payload=matches)
            
            # Finally, if some exception is not handled by the checks wrap it inside an SearchFailedException
            # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                SearchFailedException(ex=ex, message=f"{method}: {SearchFailedException.DEFAULT_MESSAGE}")
            )
    