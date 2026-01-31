# src/chess/team/database/database.py

"""
Module: chess.team.database.database
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from __future__ import annotations
from typing import List, Optional, cast

from chess.schema import Schema
from chess.team import Team
from chess.system import (
    DeletionResult, InsertionResult, LoggingLevelRouter, SearchResult, Database, id_emitter
)


class TeamDatabase(Database[Team]):
    """
    # ROLE: Unique Data Stack, Search Service, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Ensure all bag in managed by TeamStack are unique.
    2.  Guarantee consistency of records in TeamStack.

    # PARENT:
        *   Database

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See Database class for inherited attributes.
    """
    SERVICE_NAME = "TeamDatabase"
    _team_database_core: TeamStackService
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            data_service: TeamStackService = TeamStackService(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   member_service (TeamStack)
        # RETURNS:
            None
        # RAISES:
            None
        """
        super().__init__(id=id, name=name, data_service=data_service)
        self._team_stack_service = data_service

    @property
    def integrity_service(self) -> TeamService:
        return self._team_database_core.integrity_service
    
    @property
    def context_service(self) -> TeamContextService:
        return self._team_database_core.context_service
    
    @property
    def size(self) -> int:
        return self.data_service.size
    
    @property
    def is_empty(self) -> bool:
        return self.data_service.is_empty
    
    @property
    def current_team(self) -> Optional[Team]:
        return cast (Team, self.data_service.current_item)
    
    @property
    @LoggingLevelRouter.monitor
    def white_teams(self) -> SearchResult[List[Team]]:
        """Convenience method which turns a common search into a dynamic property"""
        method = "TeamDatabase.white_teams"
        # Use color from the schema incase team color is changed from GameColor.BLACK
        result = self.data_service.search(context=TeamContext(color=Schema.WHITE.color))
        if result.is_failure:
            # Handle the failure case by wrapping the debugging exception then sending in the SearchResult.
            return SearchResult.failure(
                UniqueTeamStackServiceException(
                    message=f"ServiceID:{self.id} {method}: {UniqueTeamStackServiceException.ERROR_CODE}",
                    ex=result.exception
                )
            )
        # On a successful search directly return the result.
        return result
    
    @property
    @LoggingLevelRouter.monitor
    def black_teams(self) -> SearchResult[List[Team]]:
        """Convenience method which turns a common search into a dynamic property"""
        method = "TeamDatabase.black_teams"
        # Use color from the schema incase team color is changed from GameColor.BLACK
        result = self.data_service.search(context=TeamContext(color=Schema.BLACK.color))
        if result.is_failure:
            # Handle the failure case by wrapping the debugging exception then sending in the SearchResult.
            return SearchResult.failure(
                UniqueTeamStackServiceException(
                    message=f"ServiceID:{self.id} {method}: {UniqueTeamStackServiceException.ERROR_CODE}",
                    ex=result.exception
                )
            )
        # On a successful search directly return the result.
        return result
    
    @LoggingLevelRouter.monitor
    def add_team(self, team: Team) -> InsertionResult[Team]:
        method = "TeamDatabase.add_team"
        result = self.push_unique_item(team)
        if result.is_failure:
            # Handle the failure case by wrapping the debugging exception then sending in the InsertionResult.
            return SearchResult.failure(
                UniqueTeamStackServiceException(
                    message=f"ServiceID:{self.id} {method}: {UniqueTeamStackServiceException.ERROR_CODE}",
                    ex=result.exception
                )
            )
        # On a successful search directly return the result.
        return result
    
    @LoggingLevelRouter.monitor
    def undo_team_addition(self) -> DeletionResult[Team]:
        method = "TeamDatabase.undo_add_team"
        result = self.data_service.pop()
        if result.is_failure:
            # Handle the failure case by wrapping the debugging exception then sending in the DeletionResult.
            return SearchResult.failure(
                UniqueTeamStackServiceException(
                    message=f"ServiceID:{self.id} {method}: {UniqueTeamStackServiceException.ERROR_CODE}",
                    ex=result.exception
                )
            )
        # On a successful search directly return the result.
        return result
    
    @LoggingLevelRouter.monitor
    def search_teams(self, context: TeamContext) -> SearchResult[List[Team]]:
        method = "TeamDatabase.search_teams"
        result = self.data_service.search(context)
        if result.is_failure:
            # Handle the failure case by wrapping the debugging exception then sending in the SearchResult.
            return SearchResult.failure(
                UniqueTeamStackServiceException(
                    message=f"ServiceID:{self.id} {method}: {UniqueTeamStackServiceException.ERROR_CODE}",
                    ex=result.exception
                )
            )
        # On a successful search directly return the result.
        return result
