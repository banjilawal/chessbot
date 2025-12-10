# src/chess/team/schema/context/service/service.py

"""
Module: chess.team.schema.context.service.service
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import cast

from chess.system import ContextService, id_emitter
from chess.team import TeamSchemaContext, TeamSchemaContextBuilder, TeamSchemaContextValidator, TeamSchemaFinder


class TeamSchemaContextService(ContextService[TeamSchemaContext]):
    """
    # ROLE: Search Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing TeamSchema search microservice API.
    2.  Provides a context aware utility for searching TeamSchema objects.
    3.  Encapsulates integrity assurance logic in one extendable module that's easy to maintain.
    4.  Create a single source of truth for TeamSchema search results by having single entry and exit points for the
        TeamSchema search flow.

    # PARENT
        *   ContextService

    # PROVIDES:
        *   TeamSchemaContextService

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
        *   See ContextService for inherited attributes.
    """
    DEFAULT_NAME = "TeamSchemaContextService"
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            finder: TeamSchemaFinder = TeamSchemaFinder(),
            builder: TeamSchemaContextBuilder = TeamSchemaContextBuilder(),
            validator: TeamSchemaContextValidator = TeamSchemaContextValidator(),
    ):
        """
        # Action:
        Constructor

        # Parameters:
            *   name (str): Default value - DEFAULT_NAME
            *   id (int): Default value - id_emitter.service_id
            *   finder (TeamSchemaFinder): Default value - TeamSchemaFinder()
            *   builder (TeamSchemaContextBuilder): Default value - TeamSchemaContextBuilder()
            *   validator (TeamSchemaContextValidator): Default value - TeamSchemaContextValidator()

        # Returns:
        None

        # Raises:
        None
        """
        method = "TeamSchemaContextService.__init__"
        super().__init__(id=id, name=name, builder=builder, validator=validator, finder=finder)
        
    @property
    def finder(self) -> TeamSchemaFinder:
        """Get TeamSchemaFinder instance."""
        return cast(TeamSchemaFinder, self.entity_finder)
    
    @property
    def builder(self) -> TeamSchemaContextBuilder:
        """Get TeamSchemaContextBuilder instance."""
        return cast(TeamSchemaContextBuilder, self.entity_builder)
    
    @property
    def validator(self) -> TeamSchemaContextValidator:
        """Get TeamSchemaContextValidator instance."""
        return cast(TeamSchemaContextValidator, self.entity_validator)