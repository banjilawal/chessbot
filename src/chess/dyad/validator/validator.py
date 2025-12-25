# src/chess/dyad/validator.py

"""
Module: chess.dyad.validator
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import Any, cast

from chess.agent import AgentService
from chess.schema import InvalidSchemaException, SchemaLookup
from chess.system import LoggingLevelRouter, ValidationResult, Validator
from chess.dyad import InvalidSchemaAgentPairException, NullSchemaAgentPairException, SchemaAgentPair



class SchemaAgentPairValidator(Validator[SchemaAgentPair]):
    """"""
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            agent_service: AgentService = AgentService(),
            schema_service: SchemaLookup = SchemaLookup(),
    ) -> ValidationResult[SchemaAgentPair]:
        """"""
        method = "SchemaAgentPairValidator.validate"
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullSchemaAgentPairException(f"{method}: {NullSchemaAgentPairException.DEFAULT_MESSAGE}")
                )
            if not isinstance(candidate, SchemaAgentPair):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected SchemaAgentTuple instance, got {type(candidate).__name__} instead.")
                )
            pair = cast(SchemaAgentPair, candidate)
            agent_validation = agent_service.validator.validate(pair.agent)
            if agent_validation.is_failure:
                return ValidationResult.failure(agent_validation.exception)
            schema_validation = schema_service.validator.validate(pair.schema)
            if schema_validation.is_failure:
                return ValidationResult.failure(schema_validation.exception)
            return ValidationResult.success(pair)
            
        except Exception as ex:
            return ValidationResult.failure(
                InvalidSchemaAgentPairException(
                    ex=ex, message=f"{method}: {InvalidSchemaAgentPairException.DEFAULT_MESSAGE}"
                )
            )
    
    