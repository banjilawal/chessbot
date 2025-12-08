# src/chess/team/service.py

"""
Module: chess.team.service
Author: Banji Lawal
Created: 2025-08-05
version: 1.0.0
"""

from typing import cast

from chess.system import EntityService
from chess.team import Team, TeamBuilder, TeamSchemaValidator, TeamValidator


class TeamService(EntityService[Team]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing API.
    2.  Protects Team instance's internal state.
    3.  Encapsulates integrity assurance logic in one extendable module that's easy to maintain.
    4.  Single entry point Team integrity lifecycle management with TeamBuilder and TeamValidator.
    
    # PARENT
        *   EntityService

    # PROVIDES:
        *   TeamBuilder
        *   TeamValidator

    # LOCAL ATTRIBUTES:
        *   schema_validator (TeamSchemaValidator)

    # INHERITED ATTRIBUTES:
    See EntityService class for inherited attributes.
    """
    DEFAULT_NAME = "TeamService"
    _schema_validator: TeamSchemaValidator
    
    def __init__(
            self,
            id: int,
            name: str = DEFAULT_NAME,
            builder: TeamBuilder = TeamBuilder(),
            validator: TeamValidator = TeamValidator(),
            team_schema_validator: TeamSchemaValidator = TeamSchemaValidator(),
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (nt)
            *   name (str)
            *   builder (TeamBuilder)
            *   validator (TeamValidator)

        # Returns:
        None

        # Raises:
        None
        """
        method = "TeamService.__init__"
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        self._schema_validator = team_schema_validator
    
    @property
    def builder(self) -> TeamBuilder:
        return cast(TeamBuilder, self.entity_builder)
    
    @property
    def validator(self) -> TeamValidator:
        return cast(TeamValidator, self.entity_validator)
    
    @property
    def schema_validator(self) -> TeamSchemaValidator:
        return self._schema_validator