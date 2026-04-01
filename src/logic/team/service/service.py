# src/logic/team/validator.py

"""
Module: logic.team.service
Author: Banji Lawal
Created: 2025-08-05
version: 1.0.0
"""

from __future__ import annotations
from typing import List, cast


from logic.system import IntegrityMicroService, IdFactory
from logic.team import RosterUtil, Team, TeamBuild, TeamValidator

class TeamService(IntegrityMicroService[Team]):
    """
    Role:MicroService, Lifecycle Management, Encapsulation, API layer.

    Responsibilities:
    1.  Public facing Team microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for Team state by providing single entry and exit points to Team
        lifecycle.

    Super Class:
        *   IntegrityMicroService

    Provides:

    # LOCAL ATTRIBUTES:
        *   roster_util (RosterUtil)

    # INHERITED ATTRIBUTES:
        *   See IntegrityMicroService for inherited attributes.
    """
    SERVICE_NAME = "TeamService"
    _roster_util: RosterUtil
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            builder: TeamBuild = TeamBuild(),
            roster_util: RosterUtil = RosterUtil(),
            validator: TeamValidator = TeamValidator(),
            id: int = IdFactory.next_id(class_name="TeamService"),
    ):
        """
        # ACTION:
             Constructor
        # PARAMETERS:
            *   id (nt)
            *   name (str)
            *   build (TeamBuild)
            *   validation (TeamValidator)
            *   roster_util (RosterUtil)
        # RETURNS:
                None
        Raises:
            None
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        self._roster_util = roster_util
    
    @property
    def builder(self) -> TeamBuild:
        """get TeamBuild."""
        return cast(TeamBuild, self.entity_builder)
    
    @property
    def validation(self) -> TeamValidator:
        """get TeamValidator."""
        return cast(TeamValidator, self.entity_validator)
    
    @property
    def roster_util(self) -> RosterUtil:
        return self._roster_util