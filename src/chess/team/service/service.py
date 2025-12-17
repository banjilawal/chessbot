# src/chess/team/service.py

"""
Module: chess.team.service
Author: Banji Lawal
Created: 2025-08-05
version: 1.0.0
"""

from typing import cast

from chess.system import EntityService, id_emitter
from chess.team import Team, TeamBuilder, TeamSchemaValidator, TeamValidator
from chess.team.schema.service.service import TeamSchemaService


class TeamService(EntityService[Team]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing Team State Machine microservice API.
    2.  Encapsulates integrity assurance logic in one extendable module that's easy to maintain.
    3.  Is authoritative, single source of truth for Team state by providing single entry and exit points to Team
        lifecycle.

    # PARENT:
        *   EntityService

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See EntityService for inherited attributes.
    """
    DEFAULT_NAME = "TeamService"
    _schema_service: TeamSchemaService
    
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            builder: TeamBuilder = TeamBuilder(),
            validator: TeamValidator = TeamValidator(),
            schema_service: TeamSchemaService = TeamSchemaService(),
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (nt)
            *   designation (str)
            *   builder (TeamBuilder)
            *   validator (TeamValidator)
            *   schema_service (TeamSchemaLookup)

        # Returns:
        None

        # Raises:
        None
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        self._schema_service = schema_service
    
    @property
    def builder(self) -> TeamBuilder:
        """get TeamBuilder."""
        return cast(TeamBuilder, self.entity_builder)
    
    @property
    def validator(self) -> TeamValidator:
        """get TeamValidator."""
        return cast(TeamValidator, self.entity_validator)
    
    @property
    def schema_service(self) -> TeamSchemaService:
        """get TeamSchemaLookup."""
        return self._schema_service