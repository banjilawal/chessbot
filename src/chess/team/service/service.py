# src/chess/team/service.py

"""
Module: chess.team.service
Author: Banji Lawal
Created: 2025-10-31
version: 1.0.0
"""

from chess.system import Service, id_emitter
from chess.team import Team, TeamBuilder, TeamSchema, TeamValidator

class TeamService(Service[Team]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing API.
    2.  Protects Team instance's internal state.
    3.  Masks implementation details and business logic making features easier to use.
    4.  Single entry point for managing Team lifecycles with TeamBuilder and TeamValidator.

    # PROVIDES:
        *   TeamBuilder
        *   TeamValidator
        *   TeamSchema

    # ATTRIBUTES:
        *   id (int)
        *   name (str)
        *   builder (TeamBuilder)
        *   validator (TeamValidator)
        *   schema (TeamSchema)
    """
    DEFAULT_NAME = "TeamService"
    _schema: TeamSchema
    
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            schema: TeamSchema = TeamSchema,
            builder: TeamBuilder = TeamBuilder(),
            validator: TeamValidator = TeamValidator(),
    ):
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        self._schema = schema
        
    @property
    def schema(self) -> TeamSchema:
        return self._schema