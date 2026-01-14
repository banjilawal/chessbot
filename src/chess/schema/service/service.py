# src/chess/schema/service/service.py

"""
Module: chess.schema.service.service
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from typing import List, cast

from chess.formation import Formation, FormationService, FormationKey
from chess.persona import Persona
from chess.rank import Bishop, King, Knight, Pawn, Queen, Rank, Rook
from chess.schema import Schema, SchemaServiceException, SchemaSuperKey, SchemaSuperKeyService, SchemaValidator
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
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   validator (SchemaValidator)
            *   super_key_service (SchemaSuperKeyService)
        # RETURNS:
            None
        # RAISES:
            None
        """
        super().__init__(id=id, name=name, validator=validator, super_key_service=super_key_service)
        
    @property
    def key_service(self) -> SchemaSuperKeyService:
        """"""
        return cast(SchemaSuperKeyService, self.hash_key_service)
    
    @property
    def schema_validator(self) -> SchemaValidator:
        """"""
        return cast(SchemaValidator, self.hash_validator)
    
    @classmethod
    def schema_colors(cls) -> List[GameColor]:
        """The values of the color attribute."""
        return [entry.color for entry in Schema]
    
    @classmethod
    def schema_names(cls) -> List[str]:
        """A Schema name is the key to a metadata dictionary."""
        return [entry.name for entry in Schema]
    
    @classmethod
    def rank_quotas_for_schema(cls, p) -> {Rank, int}:
        return {
            King: Persona.KING.quota,
            Pawn: Persona.PAWN.quota,
            Knight: Persona.KNIGHT.quota,
            Bishop: Persona.BISHOP.quota,
            Rook: Persona.ROOK.quota,
            Queen: Persona.QUEEN.quota,
        }
    
    @LoggingLevelRouter.monitor
    def formations_for_schema(
            self,
            schema: Schema,
            formation_service: FormationService = FormationService()
    ) -> SearchResult[List[Formation]]:
        method = "SchemaService.formations_for_schema"
        schema_validation = self.schema_validator.validate(candidate=schema)
        if schema_validation.is_failure:
            # On failure return the exception chain.
            return SearchResult.failure(
                SchemaServiceException(
                    message=f"ServiceId:{self.id}, {method}: {SchemaServiceException.ERROR_CODE}",
                    ex=schema_validation.exception
                )
            )
        return formation_service.lookup_formation(supker_key=FormationKey(color=schema.color))
    
    @LoggingLevelRouter.monitor
    def pawn_row(self, schema: Schema) -> CalculationResult[int]:
        """
        # ACTION:
            1.  If the schema fails verification send SchemaServiceException chain in the CalculationResult.
                Else, send the computed pawn_row in the CalculationResult.
        # PARAMETERS:
            *   schema (Schema)
        # RETURNS:
            *   CalculationResult[int]
                    On failure --> Exception in the CalculationResult.
                    On success --> int in the CalculationResult payload.
        # RAISES:
        None
        """
        method = "SchemaService.pawn_row"
        validation = self.schema_validator.validate(schema)
        
        # Handle the validation failure branch.
        if validation.is_failure:
            return CalculationResult.failure(
                SchemaServiceException(ex=validation.exception, message=f"{method}: {SchemaServiceException.ERROR_CODE}")
            )
        # On validation success compute the pawn_row and return in the CalculationResult.
        pawn_row = schema.rank_row + schema.advancing_step.value
        return CalculationResult.success(pawn_row)
    
    @LoggingLevelRouter.monitor
    def enemy_schema(self, schema: Schema) -> SearchResult[List[Schema]]:
        """
        # ACTION:
            1.  If the schema fails verification send SchemaServiceException chain in the CalculationResult.
                Else, following the convention put opposite Schema in an array then send in the SearchResult.
        # PARAMETERS:
            *   schema (Schema)
        # RETURNS:
            *   Schema
        # RAISES:
            None
        """
        method = "SchemaService.enemy_schema"
        validation = self.schema_validator.validate(schema)
        
        # Handle the validation failure branch.
        if validation.is_failure:
            return SearchResult.failure(
                SchemaServiceException(ex=validation.exception, message=f"{method}: {SchemaServiceException.ERROR_CODE}")
            )
        # On validation success send the opposite Schema entry in the SearchResult.
        if schema.color == GameColor.WHITE:
            return SearchResult.success(List[Schema.BLACK])
        return SearchResult.success(List[Schema.WHITE])
    
    @LoggingLevelRouter.monitor
    def lookup_schema(self, super_key: SchemaSuperKey) -> SearchResult[List[Schema]]:
        """
        # ACTION:
            Using lookup_schema is simpler and more extendable than building searches manually from self.key_service.
            1.  If the self.key_service.lookup does not produce a payload send a SchemaServiceException chain in the
                SearchResult. Otherwise, return the payload.
        # PARAMETERS:
            *   super_key (SchemaSuperKey)
        # RETURNS:
            *   SearchResult[List[Schema]] containing a list if a match is found else an exception chain.
        # RAISES:
            None
        """
        method = "SchemaService.lookup_schema"
        result = self.key_service.lookup.query(super_key=super_key, super_key_validator=self.key_service.validator)
        
        # Handle the case search failed by raising an exception.
        if result.is_failure:
            return SearchResult.failure(
                SchemaServiceException(ex=result.exception, message=f"{method}: {SchemaServiceException.ERROR_CODE}")
            )
        # On search success send the result to the caller.
        return result
    
    