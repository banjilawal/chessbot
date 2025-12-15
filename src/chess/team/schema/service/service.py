# src/chess/team/schema/service.py

"""
Module: chess.team.schema.service
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""
from typing import cast

from chess.system import Builder, EntityService, NotImplementedException, id_emitter
from chess.team import TeamSchemaContextService, TeamSchemaValidator
from chess.team.schema import TeamSchema


class TeamSchemaService(EntityService[TeamSchema]):
    """"""
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
        raise NotImplementedException("TeamSchemaService does not support building entities.")
        return None