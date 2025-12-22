# src/chess/team/service/service.py

"""
Module: chess.team.service.service
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from typing import cast

from chess.system import ContextService, id_emitter
from chess.team import TeamContext, TeamContextBuilder, TeamContextValidator, TeamFinder


class TeamContextService(ContextService[TeamContext]):
    """
    # ROLE: Search Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing Team search microservice API.
    2.  Provides a map aware utility for searching Team objects.
    3.  Encapsulate integrity assurance logic in one extendable module.
    4.  Create a single source of truth for Team search results by having single entry and exit points for the
        Team search flow.

    # PARENT:
        *   ContextService

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See ContextService for inherited attributes.
    """
    SERVICE_NAME = "TeamContextService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            finder: TeamFinder = TeamFinder(),
            builder: TeamContextBuilder = TeamContextBuilder(),
            validator: TeamContextValidator = TeamContextValidator(),
    ):
        """
        # Action:
        Constructor

        # Parameters:
            *   name (str): Default value - SERVICE_NAME
            *   id (int): Default value - id_emitter.service_id
            *   finder (TeamFinder): Default value - TeamFinder()
            *   builder (TeamContextBuilder): Default value - TeamContextBuilder()
            *   validator (TeamContextValidator): Default value - TeamContextValidator()

        # Returns:
        None

        # Raises:
        None
        """
        method = "TeamContextService.__init__"
        super().__init__(id=id, name=name, builder=builder, validator=validator, finder=finder)
    
    @property
    def finder(self) -> TeamFinder:
        """Get TeamFinder instance."""
        return cast(TeamFinder, self.entity_finder)
    
    @property
    def builder(self) -> TeamContextBuilder:
        """Get TeamContextBuilder instance."""
        return cast(TeamContextBuilder, self.entity_builder)
    
    @property
    def validator(self) -> TeamContextValidator:
        """Get TeamContextValidator instance."""
        return cast(TeamContextValidator, self.entity_validator)