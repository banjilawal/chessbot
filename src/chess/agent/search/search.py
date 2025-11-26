# src/chess/agent/search/search

"""
Module: chess.agent.search.search
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""


from typing import List

from chess.team import Team
from chess.system import GameColor, Search, SearchResult, LoggingLevelRouter
from chess.agent import (
    Agent, PlayerAgentValidator, TeamSearchContext, TeamSearchException, TeamSearchIdCollisionException
)


class TeamSearch(Search[Agent, Team]):
    """
    # ROLE: Search
  
    # RESPONSIBILITIES:
    1.  Search an Agent.team_assignments for items whose attribute matches the value in
        TeamsSearchContext function param.
  
    # PROVIDES:
    TeamSearch:
  
    # ATTRIBUTES:
    None
    """

    @classmethod
    @LoggingLevelRouter.monitor
    def search(
            cls, 
            data_owner: Agent,
            search_context: TeamSearchContext,
            agent_validator: type[PlayerAgentValidator]=PlayerAgentValidator,
            search_context_validator: type[TeamSearchContext]=TeamSearchContext,
    ) -> SearchResult[List[Team]]:
        """
        # Action:
        1.  Verify the data_owner is a valid Agent using the agent_validator.
        2.  Verify the context is a valid TeamSearchContext using the search_context_validator.
        3.  Extract the context attribute. and call either _id_search, _name_search, or _color_search.

        # Parameters:
            *   candidate (Any):                                Object to verify is a color.

            *   identity_service (type[GameColorValidator]):    Checks if candidate complies with safety contract.

        # Returns:
          ValidationResult[TeamSearchContext] containing either:
                - On success:   TeamSearchContext in the payload.
                - On failure:    Exception.

        # Raises:
        None
        """
        method = "TeamSearch.search"

        data_owner_validation = agent_validator.validate(data_owner)
        if data_owner_validation.is_failure():
            return SearchResult.failure(data_owner_validation.exception)

        search_context_validation = search_context_validator.validate(search_context)
        if search_context_validation.is_failure():
            return SearchResult.failure(search_context_validation.exception)

        if search_context.id is not None:
            return cls._id_search(data_owner=data_owner, id=search_context.id)

        if search_context.name is not None:
            return cls._name_search(data_owner=data_owner, name=search_context.name)

        if search_context.color is not None:
            return cls._color_search(data_owner=data_owner, color=search_context.color)


    @classmethod
    @LoggingLevelRouter.monitor
    def _id_search(cls, data_owner: Agent, id: int) -> SearchResult[List[Team]]:
        """
        # Action:
        1.  Get the teams whose id matched the target.
        2.  If no matches are found return an empty SearchResult.
        3.  If exactly one match is found return a successful SearchResult with the single item in an array.
        4.  If the search returns multiple hits call _resolve_matching_ids.

        # Parameters:
            *   id (int):              Target color to search for.

            *   data_owner (Agent):     Provides the Team objects to search.

        # Returns:
        SearchResult[List[Team]] containing either:
                - On success:   List[team] in the payload.
                - On failure:   Exception.

        # Raises:
            *   TeamSearchException
        """
        method = "TeamSearch._id_search"
        
        try:
            matches = [team for team in data_owner.teams if team.id == id]
            
            if len(matches) == 0:
                return SearchResult.empty()
            elif len(matches) == 1:
                return SearchResult.success(payload=matches)
            
            else:
                return cls._resolve_matching_ids(matches=matches, data_owner=data_owner)
            
        except Exception as ex:
            return SearchResult.failure(
                TeamSearchException(
                    f"{method}: {TeamSearchException.DEFAULT_MESSAGE}",
                    ex
                )
            )


    @classmethod
    @LoggingLevelRouter.monitor
    def _name_search(cls, data_owner: Agent, name: str) -> SearchResult[List[Team]]:
        """
        # Action:
        1.  Get the teams whose names matched the target, insensitive to case.
        2.  If no matches are found return an empty SearchResult.
        3.  If one or more matches are found return a successful SearchResult with the all
            the items in an array.

        # Parameters:
            *   name (str):             Target color to search for.

            *   data_owner (Agent):     Provides the Team objects to search.

        # Returns:
        SearchResult[List[Team]] containing either:
                - On success:   List[team] in the payload.
                - On failure:   Exception.

        # Raises:
            *   TeamSearchException
        """
        method = "TeamSearch._name_search"
        
        try:
            matches = [
                team for team in data_owner.team_assignments if team.schema.name.upper() == name.upper()
            ]
            
            if len(matches) == 0:
                return SearchResult.empty()
            if len(matches) >= 1:
                return SearchResult.success(payload=matches)
            
        except Exception as e:
            return SearchResult(exception=e)

    @classmethod
    @LoggingLevelRouter.monitor
    def _color_search(cls, data_owner: Agent, color: GameColor) -> SearchResult[List[Team]]:
        """
        # Action:
        1.  Get the teams whose color is the same as the target..
        2.  If no matches are found return an empty SearchResult.
        3.  If one or more matches are found return a successful SearchResult with the all the items
            in an array.

        # Parameters:
            *   color (GameColor):      Target color to search for.

            *   data_owner (Agent):     Provides the Team objects to search.

        # Returns:
        SearchResult[List[Team]] containing either:
                - On success:   List[team] in the payload.
                - On failure:   Exception.

        # Raises:
            *   TeamSearchException
        """
        method = "TeamSearch._color_search"
        
        try:
            matches = [
                team for team in data_owner.team_assignments if team.schema.color == color
            ]
            
            if len(matches) == 0:
                return SearchResult()
            if len(matches) >= 1:
                return SearchResult.success(payload=matches)
            
        except Exception as ex:
            return SearchResult.failure(
                TeamSearchException(
                    f"{method}: {TeamSearchException.DEFAULT_MESSAGE}",
                    ex
                )
            )


    @classmethod
    @LoggingLevelRouter.monitor
    def _resolve_matching_ids(cls, matches: List[Team], data_owner: Agent) -> SearchResult[List[Team]]:
        """
        # Action:
        1.  Pop the first item in the matches list.
        2.  Loop through the remaining items in the matches list.
                *   If only the id matches but color and name differ from the target's put that item in the
                    uniques list.
        3.  If uniques list is empty get the size of the matches list.
        4.  If the size of the matches list is greater than the size of the uniques list, remove the
            duplicates from the data_owner.team_assignments

        # Parameters:
            *   color (GameColor):      Target color to search for.

            *   data_owner (Agent):     Provides the Team objects to search.

        # Returns:
        SearchResult[List[Team]] containing either:
                - On success:   List[team] in the payload.
                - On failure:   Exception.

        # Raises:
            *   TeamSearchException
            *   TeamSearchIdCollisionException
            
        # NOTE
        The while loop used for doing this should be replaced with a recursive method.
        """
        method = "TeamSearch._resolve_matching_ids"
        
        try:
            target = matches.pop()
            uniques = [team for team in matches if team.id == target.id and (
                    team.schema.name.upper() != target.name.upper() or team.schema.color != target.schema.color
                )
            ]
            
            # This should be implemented with a call to a recursive function. I thought I wrote that
            # already.
            if len(uniques) == 0:
                runs = len(matches) - 1
                for team in data_owner.teams:
                    if (
                        team.id == target.id and
                        team.name.upper() == target.name.upper() and
                        team.current_position == target.current_position
                    ):
                        data_owner.teams.remove(team)
                        matches.remove(team)
                return SearchResult.success(payload=matches)
            
            return SearchResult.failure(
                TeamSearchIdCollisionException(
                    f"{method}: {TeamSearchIdCollisionException.DEFAULT_MESSAGE}"
                )
            )
        
        except Exception as ex:
            return SearchResult.failure(
                TeamSearchException(
                    f"{method}: {TeamSearchException.DEFAULT_MESSAGE}",
                    ex
                )
            )