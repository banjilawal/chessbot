# src/chess/schema/service/service.py

"""
Module: chess.schema.service.service
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""
from typing import List

from chess.schema import Schema, SchemaSuperKey, SchemaSuperKeyService, SchemaValidator
from chess.schema.lookup.forward.lookup import ForwardSchemaLookup
from chess.system import CalculationResult, GameColor, SearchResult, id_emitter


class SchemaService:
    SERVICE_NAME = "SchemaService"
    _id: int
    _name: str
    _super_key_service: SchemaSuperKeyService
    _validator: SchemaValidator
    _lookup: ForwardSchemaLookup
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            super_key_service: SchemaSuperKeyService = SchemaSuperKeyService(),
            validator: SchemaValidator = SchemaValidator(),
            lookup: ForwardSchemaLookup = ForwardSchemaLookup(),
    ):
        self._key_service = super_key_service
        self._validator = validator
        self._lookup = lookup
        self._id = id
        self._name = name
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name
        
    @property
    def key_service(self) -> SchemaSuperKeyService:
        return self._key_service
    
    @property
    def schema_validator(self) -> SchemaValidator:
        return self._validator
    
    @property
    def lookup(self) -> ForwardSchemaLookup:
        return self._lookup
    
    def pawn_row(self, schema: Schema) -> CalculationResult[int]:
        validation = self._validator.validate(schema)
        if validation.is_failure:
            return CalculationResult.failure(validation.exception)
        pawn_row = schema.rank_row + schema.advancing_step
        return CalculationResult.success(pawn_row)
    
    @classmethod
    def schema_colors(cls) -> list[GameColor]:
        return [entry.color for entry in Schema]
    
    @classmethod
    def schema_names(cls) -> list[str]:
        return [entry.name for entry in Schema]
    
    def enemy_schema(self, schema: Schema) -> SearchResult[List[Schema]]:
        validation = self._validator.validate(schema)
        if validation.is_failure:
            return SearchResult.failure(validation.exception)
        if schema.color == GameColor.WHITE:
            return SearchResult.success(Schema.BLACK)
        return SearchResult.success(Schema.WHITE)
    
    def lookup_schema(self, super_key: SchemaSuperKey) -> SearchResult[List[Schema]]:
        return self._lookup.lookup(
            super_key=super_key,
            super_key_validator=self._super_key_service.
        )