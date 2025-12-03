# src/chess/team/service.py

"""
Module: chess.team.service
Author: Banji Lawal
Created: 2025-10-31
version: 1.0.0
"""
from typing import cast

from chess.system import IntegrityService, id_emitter
from chess.team import Team, TeamBuilder, TeamSchema, TeamSchemaValidator, TeamValidator


class TeamIntegrityService(IntegrityService[Team]):
    """
    # ROLE: IntegrityService, Lifecycle Management, Encapsulation, API layer.

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
        
    # CONSTRUCTOR:
        *   __init__(
                id: int, name: str, schema: TeamSchema, builder: TeamBuilder, validator: TeamValidator
            )
    
    # CLASS METHODS:
    None
    
    # INSTANCE METHODS:
    None
    """
    DEFAULT_NAME = "TeamIntegrityService"
    _schema: TeamSchema
    _schema_validator: TeamSchemaValidator
    
    def __init__(
            self,
            id: int,
            name: str = DEFAULT_NAME,
            schema: TeamSchema = TeamSchema(),
            builder: TeamBuilder = TeamBuilder(),
            validator: TeamValidator = TeamValidator(),
            team_schema_validator: TeamSchemaValidator = TeamSchemaValidator(),
    ):
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        self._schema = schema
        self._schema_validator = team_schema_validator
    
    @property
    def schema(self) -> TeamSchema:
        return self._schema
    
    @property
    def item_validator(self) -> TeamValidator:
        return cast(TeamValidator, super().item_validator)
    
    @property
    def item_builder(self) -> TeamBuilder:
        return cast(TeamBuilder, super().item_builder)
    
    @property
    def schema_validator(self) -> TeamSchemaValidator:
        return self._schema_validator
