# src/logic/team/service/service.py

"""
Module: logic.team.service.service
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from typing import cast

from logic.system import ContextService, id_emitter
from logic.team import TeamContext, TeamContextBuildProcess, TeamContextValidationProcess, TeamFinder


class TeamContextService(ContextService[TeamContext]):
    """
    Role:Search Service, Lifecycle Management, Encapsulation, API layer.

    Responsibilities:
    1.  Public facing Team search microservice API.
    2.  Provides a map aware utility for searching Team objects.
    3.  Encapsulate integrity assurance logic in one extendable module.
    4.  Create a single source of truth for Team search results by having single entry and exit points for the
        Team search flow.

    Super Class:
        *   ContextService

    Provides:


    # INHERITED ATTRIBUTES:
        *   See ContextService for inherited attributes.
    """
    SERVICE_NAME = "TeamContextService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            finder: TeamFinder = TeamFinder(),
            builder: TeamContextBuildProcess = TeamContextBuildProcess(),
            validator: TeamContextValidationProcess = TeamContextValidationProcess(),
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   name (str): Default value - SERVICE_NAME
            *   id (int): Default value - id_emitter.service_id
            *   finder (TeamFinder): Default value - TeamFinder()
            *   builder (TeamContextBuildProcess): Default value - TeamContextBuildProcess()
            *   validator (TeamContextValidationProcess): Default value - TeamContextValidationProcess()

        # RETURNS:
        None

        Raises:
        """
        method = "TeamContextService.__init__"
        super().__init__(id=id, name=name, builder=builder, validator=validator, finder=finder)
    
    @property
    def finder(self) -> TeamFinder:
        """Get TeamFinder instance."""
        return cast(TeamFinder, self.entity_finder)
    
    @property
    def build(self) -> TeamContextBuildProcess:
        """Get TeamContextBuildProcess instance."""
        return cast(TeamContextBuildProcess, self.entity_builder)
    
    @property
    def validation(self) -> TeamContextValidationProcess:
        """Get TeamContextValidationProcess instance."""
        return cast(TeamContextValidationProcess, self.entity_validator)
    
    