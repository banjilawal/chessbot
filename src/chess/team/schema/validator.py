# src/chess/team/schema/validator.py

"""
Module: chess.team.schema.validator
Author: Banji Lawal
Created: 2025-11-18
"""

from typing import cast, Any


from chess.system import Validator, ValidationResult, LoggingLevelRouter
from chess.team import InvalidTeamSchemaException, NullTeamSchemaException, TeamSchema



class TeamSchemaValidator(Validator[TeamSchema]):
    
    @classmethod
    @LoggingLevelRouter.monitor()
    def validate(cls, candidate: Any) -> ValidationResult[TeamSchema]:
        method = "TeamSchemaValidator.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullTeamSchemaException(f"{method} {NullTeamSchemaException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, TeamSchema):
                return ValidationResult.failure(
                    TypeError(f"{method} Expected TeamSchema, got {type(candidate).__name__} instead.")
                )
            
            team_schema = cast(TeamSchema, candidate)
            return ValidationResult.success(team_schema)
        
        except Exception as ex:
            return ValidationResult.failure(
                InvalidTeamSchemaException(
                    f"{method} {InvalidTeamSchemaException.DEFAULT_MESSAGE}",
                    ex
                )
            )