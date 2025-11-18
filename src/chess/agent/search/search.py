# chess/agenet/search/search.py

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
    Agent, AgentValidator, TeamSearchContext, TeamSearchException, TeamSearchIdCollisionException
)


class AgentTeamSearchSearch(Search[Agent, Team]):
    """
    # ROLE: Builder implementation
  
    # RESPONSIBILITIES:
    1. Process and validate parameters for creating `Agent` instances.
    2. Create new `Agent` objects if parameters meet specifications.
    2. Report errors and return `BuildResult` with error details.
  
    # PROVIDES:
    `BuildResult`: Return type containing the built `Agent` or error information.
  
    # ATTRIBUTES:
    None
    """

    @classmethod
    @LoggingLevelRouter.monitor
    def search(
            cls, 
            data_owner: Agent,
            search_context: type[TeamSearchContext]=TeamSearchContext,
            agent_validator: type[AgentValidator]=AgentValidator,
            search_context_validator: type[TeamSearchContext]=TeamSearchContext,
    ) -> SearchResult[List[Team]]:
        method = "AgentTeamSearchSearch.search"

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
        method = "AgentTeamSearchSearch._id_search"
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
        method = "AgentTeamSearchSearch._name_search"
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
        method = "AgentTeamSearchSearch._color_search"
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
        method = "AgentTeamSearchSearch._resolve_matching_ids"
        target = matches.pop()
        misses = [team for team in matches if team.id == target.id and (
                team.schema.name.upper() != target.name.upper() or team.schema.color != target.schema.color
            )
        ]
        if len(misses) == 0:
            runs = len(matches) - 1
            for team in data_owner.teams:
                if (
                    team.id == target.id and
                    team.name.upper() == target.name.upper() and
                    team.current_position == target.current_position
                ):
                    data_owner.teams.remove(team)
                    matches.remove(team)
            return SearchResult(payload=matches)
        return SearchResult(exception=TeamSearchIdCollisionException(
                f"{method}: {TeamSearchIdCollisionException.DEFAULT_MESSAGE}"
            )
        )