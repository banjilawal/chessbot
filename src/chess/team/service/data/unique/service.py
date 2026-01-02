# src/chess/team/service/data/unique/service.py

"""
Module: chess.team.service.data.unique.service
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from typing import List, Optional, cast

from chess.schema import Schema
from chess.team import (
    Team, TeamContext, TeamContextService, TeamDataService, TeamService, UniqueTeamDataServiceException
)
from chess.system import (
    DeletionResult, InsertionResult, LoggingLevelRouter, SearchResult, UniqueDataService, id_emitter
)


class UniqueTeamDataService(UniqueDataService[Team]):
    """
    # ROLE: Unique Data Stack, Search Service, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Ensure all items in managed by TeamDataService are unique.
    2.  Guarantee consistency of records in TeamDataService.

    # PARENT:
        *   UniqueDataService

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See UniqueDataService class for inherited attributes.
    """
    SERVICE_NAME = "UniqueTeamDataService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            data_service: TeamDataService = TeamDataService(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   data_service (TeamDataService)
        # RETURNS:
            None
        # RAISES:
            None
        """
        super().__init__(id=id, name=name, data_service=data_service)

    @property
    def team_service(self) -> TeamService:
        return cast(TeamDataService, self.data_service).team_service
    
    @property
    def context_service(self) -> TeamContextService:
        return cast(TeamDataService, self.data_service).team_context_service
    
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
        method = "UniqueTeamDataService.white_teams"
        # Use color from the schema incase team color is changed from GameColor.BLACK
        result = self.data_service.search(context=TeamContext(color=Schema.WHITE.color))
        if result.is_failure:
            # Handle the failure case by wrapping the debugging exception then sending in the SearchResult.
            return SearchResult.failure(
                UniqueTeamDataServiceException(
                    message=f"ServiceID:{self.id} {method}: {UniqueTeamDataServiceException.ERROR_CODE}",
                    ex=result.exception
                )
            )
        # On a successful search directly return the result.
        return result
    
    @property
    @LoggingLevelRouter.monitor
    def black_teams(self) -> SearchResult[List[Team]]:
        """Convenience method which turns a common search into a dynamic property"""
        method = "UniqueTeamDataService.black_teams"
        # Use color from the schema incase team color is changed from GameColor.BLACK
        result = self.data_service.search(context=TeamContext(color=Schema.BLACK.color))
        if result.is_failure:
            # Handle the failure case by wrapping the debugging exception then sending in the SearchResult.
            return SearchResult.failure(
                UniqueTeamDataServiceException(
                    message=f"ServiceID:{self.id} {method}: {UniqueTeamDataServiceException.ERROR_CODE}",
                    ex=result.exception
                )
            )
        # On a successful search directly return the result.
        return result
    
    @LoggingLevelRouter.monitor
    def add_team(self, team: Team) -> InsertionResult[Team]:
        method = "UniqueTeamDataService.add_team"
        result = self.push_unique_item(team)
        if result.is_failure:
            # Handle the failure case by wrapping the debugging exception then sending in the InsertionResult.
            return SearchResult.failure(
                UniqueTeamDataServiceException(
                    message=f"ServiceID:{self.id} {method}: {UniqueTeamDataServiceException.ERROR_CODE}",
                    ex=result.exception
                )
            )
        # On a successful search directly return the result.
        return result
    
    @LoggingLevelRouter.monitor
    def undo_add_team(self) -> DeletionResult[Team]:
        method = "UniqueTeamDataService.undo_add_team"
        result = self.data_service.undo_item_push()
        if result.is_failure:
            # Handle the failure case by wrapping the debugging exception then sending in the DeletionResult.
            return SearchResult.failure(
                UniqueTeamDataServiceException(
                    message=f"ServiceID:{self.id} {method}: {UniqueTeamDataServiceException.ERROR_CODE}",
                    ex=result.exception
                )
            )
        # On a successful search directly return the result.
        return result
    
    @LoggingLevelRouter.monitor
    def search_teams(self, context: TeamContext) -> SearchResult[List[Team]]:
        method = "UniqueTeamDataService.search_teams"
        result = self.data_service.search(context)
        if result.is_failure:
            # Handle the failure case by wrapping the debugging exception then sending in the SearchResult.
            return SearchResult.failure(
                UniqueTeamDataServiceException(
                    message=f"ServiceID:{self.id} {method}: {UniqueTeamDataServiceException.ERROR_CODE}",
                    ex=result.exception
                )
            )
        # On a successful search directly return the result.
        return result
