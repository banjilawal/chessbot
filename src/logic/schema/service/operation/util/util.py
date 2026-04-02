# src/logic/schema/service/validator.py

"""
Module: logic.schema.service.service
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from typing import List, cast

from logic.formation import Formation, FormationService, FormationKey
from logic.persona import Persona
from logic.rank import Bishop, King, Knight, Pawn, Queen, Rank, Rook
from logic.schema import Schema, SchemaServiceException, SchemaKey, SchemaKeyService, SchemaValidator
from logic.system import ComputationResult, GameColor, HashService, LoggingLevelRouter, SearchResult, id_emitter


class SchemaUtil:
        
    @property
    def schema(self) -> Schema:
        return Schema()
    
    @property
    def colors(self) -> List[GameColor]:
        return [entry.color for entry in Schema]
    
    @property
    def names(self) -> List[str]:
        return [entry.name for entry in Schema]
    
    @property
    def rank_quotas_for_schema(self) -> {Rank, int}:
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
        schema_validation = self.validator.validate(candidate=schema)
        if schema_validation.is_failure:
            # On failure return the exception chain.
            return SearchResult.failure(
                SchemaServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {SchemaServiceException.ERR_CODE}",
                    ex=schema_validation.exception
                )
            )
        return formation_service.lookup_formation(supker_key=FormationKey(color=schema.color))
    
    @LoggingLevelRouter.monitor
    def pawn_row(self, schema: Schema) -> ComputationResult[int]:
        """
        # ACTION:
            1.  If the schema fails verification send SchemaServiceException chain in the ComputationResult.
                Else, send the computed pawn_row in the ComputationResult.
        # PARAMETERS:
            *   schema (Schema)
        # RETURNS:
            *   ComputationResult[int]
                    On failure --> Exception in the ComputationResult.
                    On success --> int in the ComputationResult payload.
        Raises:
        """
        method = "SchemaService.pawn_row"
        validation = self.validator.validate(schema)
        
        # Handle the validation failure branch.
        if validation.is_failure:
            return ComputationResult.failure(
                SchemaServiceException(ex=validation.exception, msg=f"{method}: {SchemaServiceException.ERR_CODE}")
            )
        # On validation success compute the pawn_row and return in the ComputationResult.
        pawn_row = schema.rank_row + schema.advancing_step.value
        return ComputationResult.success(pawn_row)
    
    @LoggingLevelRouter.monitor
    def enemy_schema(self, schema: Schema) -> SearchResult[List[Schema]]:
        """
        # ACTION:
            1.  If the schema fails verification send SchemaServiceException chain in the ComputationResult.
                Else, following the convention put opposite Schema in an array then send in the SearchResult.
        # PARAMETERS:
            *   schema (Schema)
        # RETURNS:
            *   Schema
        Raises:
            None
        """
        method = "SchemaService.enemy_schema"
        validation = self.validator.validate(schema)
        
        # Handle the validation failure branch.
        if validation.is_failure:
            return SearchResult.failure(
                SchemaServiceException(ex=validation.exception, msg=f"{method}: {SchemaServiceException.ERR_CODE}")
            )
        # On validation success send the opposite Schema entry in the SearchResult.
        if schema.color == GameColor.WHITE:
            return SearchResult.success([Schema.BLACK])
        return SearchResult.success([Schema.WHITE])
    
    @LoggingLevelRouter.monitor
    def lookup_schema(self, super_key: SchemaKey) -> SearchResult[List[Schema]]:
        """
        # ACTION:
            Using lookup_schema is simpler and more extendable than building searches manually from self.key_service.
            1.  If the self.key_service.lookup does not produce a payload send a SchemaServiceException chain in the
                SearchResult. Otherwise, return the payload.
        # PARAMETERS:
            *   super_key (SchemaKey)
        # RETURNS:
            *   SearchResult[List[Schema]] containing a list if a match is found else an exception chain.
        Raises:
            None
        """
        method = "SchemaService.lookup_schema"
        result = self.key_service.lookup.query(super_key=super_key, super_key_validator=self.key_service.validation)
        
        # Handle the case search failed by raising an exception.
        if result.is_failure:
            return SearchResult.failure(
                SchemaServiceException(ex=result.exception, msg=f"{method}: {SchemaServiceException.ERR_CODE}")
            )
        # On search success send the result to the caller.
        return result
    
    