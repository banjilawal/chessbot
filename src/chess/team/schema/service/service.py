# src/chess/team/team_schema/service/service.py

"""
Module: chess.team.team_schema.service.service
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from typing import List, cast

from chess.system import Builder, EntityService, GameColor, NotImplementedException, Result, id_emitter
from chess.team import TeamSchemaContextService, TeamSchemaValidator
from chess.team.schema import TeamSchema


class TeamSchemaService(EntityService[TeamSchema]):
    """
    # ROLE: Service, Utility

    # RESPONSIBILITIES:
    1.  Public facing Team State Machine microservice API.
    2.  Encapsulates integrity assurance logic in one extendable module that's easy to maintain.
    3.  Is authoritative, single source of truth for Team state by providing single entry and exit points to Team
        lifecycle.

    # PARENT:
        *   EntityService

    # PROVIDES:
        *   allowed_colors() -> List[GameColor]:
        *   allowed_names() -> List[str]:
        *   enemy_schema(team_schema: TeamSchema) -> Result[TeamSchema]:

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See EntityService for inherited attributes.
    """
    DEFAULT_NAME = "TeamSchemaService"
    _context_service: TeamSchemaContextService
    
    def __init__(
            self,
            builder: Builder[TeamSchema] = None,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            validator: TeamSchemaValidator = TeamSchemaValidator(),
            context_service: TeamSchemaContextService = TeamSchemaContextService(),
    ):
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        self._context_service = context_service
        
    @property
    def context_service(self) -> TeamSchemaContextService:
        return self._context_service
    
    @property
    def validator(self) -> TeamSchemaValidator:
        return cast(TeamSchemaValidator, self._validator)
    
    @property
    def builder(self) -> None:
        """TeamSchemaService does not support building entities."""
        method = "TeamSchemaService.builder"
        raise NotImplementedException(f"{method}: TeamSchemaService does not support building entities.")
    
    
    @property
    def allowed_colors(self) -> List[GameColor]:
        return [member.color for member in TeamSchema]
    
    @property
    def allowed_names(self) -> List[str]:
        return [member.name for member in TeamSchema]
    
    def enemy_schema(self, schema: TeamSchema) -> Result[TeamSchema]:
        validation = self.validator.validate(schema)
        if validation.is_failure:
            return Result.failure(validation.exception)
        if schema == TeamSchema.WHITE:
            return Result[TeamSchema.BLACK]
        return Result[TeamSchema.WHITE]