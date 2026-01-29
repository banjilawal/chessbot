# src/chess/team/service/data/service.py

"""
Module: chess.team.service.data.service
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from typing import List, cast

from chess.system import ListService, id_emitter
from chess.team import Team,  TeamContextService,  TeamService


class TeamListService(ListService[Team]):
    """
    # ROLE: Data Stack, Search Service, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing API.
    2.  Microservice for managing team objects and their lifecycles.
    3.  Ensure integrity of team data stack
    4.  Stack data structure for Team objects with no guarantee of uniqueness.
    
    # PARENT:
        *   ListService

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
        *   See ListService class for inherited attributes.
    """
    CAPACITY = 2
    SERVICE_NAME = "TeamListService"
    _capacity: int
    
    def __init__(
            self,
            name: str =SERVICE_NAME,
            capacity: int = CAPACITY,
            id: int = id_emitter.service_id,
            items: List[Team] = List[Team],
            service: TeamService = TeamService(),
            context_service: TeamContextService = TeamContextService(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   items (List[Team])
            *   service (TeamService)
            *   context_service (TeamContextService)
        # RETURNS:
            None
        # RAISES:
            None
        """
        method = "TeamListService.__init__"
        super().__init__(
            id=id,
            name=name,
            items=items,
            entity_service=service,
            context_service=context_service
        )
        self._capacity = capacity
        
    @property
    def capacity(self) -> int:
        return self._capacity
    
    @property
    def is_full(self) -> bool:
        return len(self.items) >= self.capacity
    
    @property
    def is_empty(self) -> bool:
        return len(self.items) == 0
    
    @property
    def integrity_service(self) -> TeamService:
        return cast(TeamService, self.entity_service)
    
    @property
    def team_context_service(self) -> TeamContextService:
        return cast(TeamContextService, self.context_service)
    
    @property
    def items(self) -> List[Team]:
        return self.items