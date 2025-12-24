# src/chess/schema/service/service.py

"""
Module: chess.schema.service.service
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""
from typing import List, cast

from chess.schema import (
    Schema, SchemaLookup, SchemaServiceException, SchemaSuperKey, SchemaSuperKeyService,
    SchemaValidator
)
from chess.system import CalculationResult, GameColor, HashService, LoggingLevelRouter, SearchResult, id_emitter


class SchemaService(HashService[Schema]):
    SERVICE_NAME = "SchemaService"
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            validator: SchemaValidator = SchemaValidator(),
            super_key_service: SchemaSuperKeyService = SchemaSuperKeyService(),
    ):
        super().__init__(id=id, name=name, validator=validator, super_key_service=super_key_service)
        
    @property
    def key_service(self) -> SchemaSuperKeyService:
        return cast(SchemaSuperKeyService, self.hash_super_key_service)
    
    @property
    def schema_validator(self) -> SchemaValidator:
        return cast(SchemaValidator, self.hash_validator)
    
    @classmethod
    def schema_colors(cls) -> list[GameColor]:
        return [entry.color for entry in Schema]
    
    @classmethod
    def schema_names(cls) -> list[str]:
        return [entry.name for entry in Schema]
    
    @LoggingLevelRouter.monitor
    def pawn_row(self, schema: Schema) -> CalculationResult[int]:
        """"""
        method = "SchemaService.pawn_row"
        validation = self.schema_validator.validate(schema)
        if validation.is_failure:
            # Handle the invalid case
            return CalculationResult.failure(
                SchemaServiceException(ex=validation.exception, message=f"{method}: {SchemaServiceException.ERROR_CODE}")
            )
        #
        pawn_row = schema.rank_row + schema.advancing_step.value
        return CalculationResult.success(pawn_row)
    
    @LoggingLevelRouter.monitor
    def enemy_schema(self, schema: Schema) -> SearchResult[List[Schema]]:
        """"""
        method = "SchemaService.enemy_schema"
        validation = self._validator.validate(schema)
        if validation.is_failure:
            return SearchResult.failure(validation.exception)
        if schema.color == GameColor.WHITE:
            return SearchResult.success(Schema.BLACK)
        return SearchResult.success(Schema.WHITE)
    
    def lookup_schema(self, super_key: SchemaSuperKey) -> SearchResult[List[Schema]]:
        """"""
        method = "SchemaService.lookup_schema"
        return self.key_service.lookup.query(super_key=super_key, super_key_validator=self.key_service.validator)