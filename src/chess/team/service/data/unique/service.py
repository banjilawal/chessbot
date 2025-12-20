# src/chess/team/service/data/unique/service.py

"""
Module: chess.team.service.data.unique.service
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from typing import List, Optional, cast

from chess.team import Team, TeamContext, TeamContextService, TeamDataService, TeamService
from chess.system import (
    DeletionResult, EntityService, GameColor, InsertionResult, LoggingLevelRouter, SearchResult, UniqueDataService,
    id_emitter
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
        *   team_service: -> TeamService
        *   context_service: -> TeamContextService
        *   add_team: -> InsertionResult[Team]
        *   undo_add_team: -> DeletionResult[Team]
        *   search_teams: -> SearchResult[List[Team]]

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See UniqueDataService class for inherited attributes.
    """
    DEFAULT_NAME = "UniqueTeamDataService"
    
    def __init__(
            self,
            id: int,
            name: str = DEFAULT_NAME,
            data_service: TeamDataService = TeamDataService()
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (int): = id_emitter.service_id
            *   designation (str): = SERVICE_NAME
            *   data_service (TeamDataService): = TeamDataService()

        # Returns:
        None

        # Raises:
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
    def white_teams(self) -> List[Team]:
        result = self.data_service.search(context=TeamContext(color=GameColor.WHITE))
        return result.payload if result.success else []
    
    @property
    def black_teams(self) -> List[Team]:
        result = self.data_service.search(context=TeamContext(color=GameColor.BLACK))
        return result.payload if result.success else []
    
    def add_team(self, team: Team) -> InsertionResult[Team]:
        return self.push_unique_item(team)
    
    def undo_add_team(self) -> DeletionResult[Team]:
        return self.data_service.undo_item_push()
    
    def search_teams(self, context: TeamContext) -> SearchResult[List[Team]]:
        return self.data_service.search(context)