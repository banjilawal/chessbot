# src/chess/team/finder/finder.py

"""
Module: chess.team.finder.searcher
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from typing import List

from chess.agent import Agent
from chess.system import GameColor, LoggingLevelRouter, Finder, SearchResult
from chess.team import Team, TeamContext, TeamContextValidator, TeamFinderException


class TeamFinder(Finder[Team]):
    """
    # ROLE: Finder
  
    # RESPONSIBILITIES:
    Find Team instances that match target attributes set in TeamContext
  
    # PROVIDES:
    SearchResult[List[Team]' containing either:
        - On success: List[Team] in the payload.
        - On failure: Exception.
  
    # ATTRIBUTES:
    No attributes
  
    # CONSTRUCTOR:
    Default Constructor
  
    # CLASS METHODS:
        ## searcher signature:
                def searcher(
                        cls,
                        data_set: List[Team],
                        search_context: TeamSearchContext
                ) -> SearchResult[List[Team]]:
                
    # INSTANCE METHODS:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def find(
            cls,
            data_set: List[Team],
            context: TeamContext,
            context_validator: TeamContextValidator = TeamContextValidator()
    ) -> SearchResult[List[Team]]:
        """"""
        method = "TeamFinder.find"
        try:
            result = context_validator.validate(candidate=context)
            if result.is_failure:
                return SearchResult.failure(result.exception)
            
            if context.id is not None:
                return cls._find_by_id(data_set=data_set, id=context.id)
            
            if context.name is not None:
                return cls._find_by_name(data_set=data_set, name=context.name)
            
            if context.agent is not None:
                return cls._find_by_agent(data_set=data_set, team=context.agent)
            
            if context.color is not None:
                return cls._find_by_color(data_set=data_set, team=context.color)
            
            if context.game is not None:
                return cls._find_by_game(data_set=data_set, game=context.game)
        # Finally, if there is an unhandled exception Wrap a TeamSearchFailedException exception around it
        # then return the exceptions inside a BuildResult.
        except Exception as ex:
            return SearchResult.failure(
                TeamFinderException(ex=ex, message=f"{method}: {TeamFinderFailedException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_id(cls, data_set: List[Team], id: int) -> SearchResult[List[Team]]:
        """
        # Action:
        1.  Get the team_service whose id matched the target.
        2.  If no matches are found return an empty SearchResult.
        3.  If exactly one match is found return a successful SearchResult with the single item in an array.

        # Parameters:
            *   data_set: (List[Team])
            *   id (int)


        # Returns:
        SearchResult[List[Team]] containing either:
                - On success:   List[Team] in the payload.
                - On failure:   Exception.

        # Raises:
            *   TeamSearchFailedException
        """
        method = "TeamFinder._find_by_id"
        try:
            matches = [team for team in data_set if team.id == id]
            if len(matches) == 0:
                return SearchResult.empty()
            
            if len(matches) >= 1:
                return SearchResult.success(payload=matches)
        except Exception as ex:
            # Finally, if there is an unhandled exception Wrap a TeamSearchFailedException exception around it
            # then return the exceptions inside a BuildResult.
            return SearchResult.failure(
                TeamSearchFailedException(ex=ex, message=f"{method}: {TeamSearchFailedException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_name(cls, data_set: List[Team], name: str) -> SearchResult[List[Team]]:
        """
        # Action:
        1.  Get the team_service whose name matched the target.
        2.  If no matches are found return an empty SearchResult.
        3.  If exactly one match is found return a successful SearchResult with the single item in an array.

        # Parameters:
            *   data_set: (List[Team])
            *   name (str)


        # Returns:
        SearchResult[List[Team]] containing either:
                - On success:   List[Team] in the payload.
                - On failure:   Exception.

        # Raises:
            *   TeamSearchFailedException
        """
        method = "TeamFinder._find_by_name"
        
        try:
            matches = [team for team in data_set if team.schema.name.upper() == name.upper()]
            if len(matches) == 0:
                return SearchResult.empty()
            
            if len(matches) >= 1:
                return SearchResult.success(payload=matches)
        except Exception as ex:
            # Finally, if there is an unhandled exception Wrap a TeamSearchFailedException exception around it
            # then return the exceptions inside a BuildResult.
            return SearchResult.failure(
                TeamSearchFailedException(ex=ex, message=f"{method}: {TeamSearchFailedException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_agent(cls, data_set: List[Team], agent: Agent) -> SearchResult[List[Team]]:
        """
        # Action:
        1.  Get the team_service whose agent matched the target.
        2.  If no matches are found return an empty SearchResult.
        3.  If exactly one match is found return a successful SearchResult with the single item in an array.

        # Parameters:
            *   data_set: (List[Team])
            *   agent (Agent)


        # Returns:
        SearchResult[List[Team]] containing either:
                - On success:   List[Team] in the payload.
                - On failure:   Exception.

        # Raises:
            *   TeamSearchFailedException
        """
        method = "TeamFinder._find_by_agent"
        
        try:
            matches = [team for team in data_set if team.agent == agent]
            if len(matches) == 0:
                return SearchResult.empty()
            
            if len(matches) >= 1:
                return SearchResult.success(payload=matches)
        # Finally, if there is an unhandled exception Wrap a TeamSearchFailedException exception around it
        # then return the exceptions inside a BuildResult.
        except Exception as ex:
            return SearchResult.failure(
                TeamSearchFailedException(ex=ex, message=f"{method}: {TeamSearchFailedException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_color(cls, data_set: List[Team], color: GameColor) -> SearchResult[List[Team]]:
        """
        # Action:
        1.  Get the team_service whose color matched the target.
        2.  If no matches are found return an empty SearchResult.
        3.  If exactly one match is found return a successful SearchResult with the single item in an array.

        # Parameters:
            *   data_set: (List[Team])
            *   color (GameColor)

        # Returns:
        SearchResult[List[Team]] containing either:
                - On success:   List[Team] in the payload.
                - On failure:   Exception.

        # Raises:
            *   TeamSearchFailedException
        """
        method = "TeamFinder._find_by_color"
        
        try:
            matches = [team for team in data_set if team.schema.color == color]
            if len(matches) == 0:
                return SearchResult.empty()
            
            if len(matches) >= 1:
                return SearchResult.success(payload=matches)
        # Finally, if there is an unhandled exception Wrap a TeamSearchFailedException exception around it
        # then return the exceptions inside a BuildResult.
        except Exception as ex:
            return SearchResult.failure(
                TeamSearchFailedException(ex=ex, message=f"{method}: {TeamSearchFailedException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_game(cls, data_set: List[Team], game: GameColor) -> SearchResult[List[Team]]:
        """
        # Action:
        1.  Get the team_service whose game matched the target.
        2.  If no matches are found return an empty SearchResult.
        3.  If exactly one match is found return a successful SearchResult with the single item in an array.

        # Parameters:
            *   data_set: (List[Team])
            *   game (Game)

        # Returns:
        SearchResult[List[Team]] containing either:
                - On success:   List[Team] in the payload.
                - On failure:   Exception.

        # Raises:
            *   TeamSearchFailedException
        """
        method = "TeamFinder._find_by_game"
        
        try:
            matches = [team for team in data_set if team.game == game]
            if len(matches) == 0:
                return SearchResult.empty()
            
            if len(matches) >= 1:
                return SearchResult.success(payload=matches)
        # Finally, if there is an unhandled exception Wrap a TeamSearchFailedException exception around it
        # then return the exceptions inside a BuildResult.
        except Exception as ex:
            return SearchResult.failure(
                TeamSearchFailedException(ex=ex, message=f"{method}:{TeamSearchFailedException.DEFAULT_MESSAGE}")
            )