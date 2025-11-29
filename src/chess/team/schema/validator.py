# src/chess/team/schema/coord_stack_validator.py

"""
Module: chess.team.schema.coord_stack_validator
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
    
    @classmethod
    @LoggingLevelRouter.monitor()
    def validate_team_color(cls, candidate: Any) -> ValidationResult[GameColor]:
        method = "TeamValidator.validate_team_color"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullGameColorException(f"{method} {NullGameColorException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, str):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected GameColor, got {type(candidate).__name__} instead.")
                )
            
            color = cast(GameColor, candidate)
            if color not in [TeamSchema.WHITE.color, TeamSchema.BLACK.color]:
                return ValidationResult.failure(
                    TeamColorBoundsException(f"{method}: {TeamColorBoundsException.DEFAULT_MESSAGE}")
                )
            # Send the successfully validated color..
            return ValidationResult.success(color)
            
            # Finally, if there is an unhandled exception Wrap a PieceBuildFailed exception around it
            # then return the exceptions inside a BuildResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidTeamException(ex=ex, message=f"{method}: {InvalidTeamException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor()
    def validate_team_name(cls, candidate: Any) -> ValidationResult[str]:
        method = "TeamValidator.validate_team_name"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullTeamNameException(f"{method}: {NullTeamNameException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, str):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected str, got {type(candidate).__name__} instead.")
                )
            
            name = cast(str, candidate)
            if name not in [TeamSchema.WHITE.name, TeamSchema.BLACK.name]:
                return ValidationResult.failure(
                    TeamNameBoundsException(
                        f"{method} {TeamNameBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            
            return ValidationResult.success(name)
        
        except Exception as ex:
            return ValidationResult.failure(
                InvalidTeamException(ex=ex, message=f"{method} {InvalidTeamException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor()
    def validate_schema(cls, candidate: Any, schema) -> ValidationResult[TeamSchema]:
        method = "TeamValidator.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullTeamSchemaException(f"{method}: {NullTeamSchemaException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, TeamSchema):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected TeamSchema, got {type(candidate).__name__} instead.")
                )
            
            team_schema = cast(TeamSchema, candidate)
            return ValidationResult.success(team_schema)
        
        except Exception as ex:
            return ValidationResult.failure(
                InvalidTeamSchemaException(ex=ex, message=f"{method}: {InvalidTeamSchemaException.DEFAULT_MESSAGE}")
            )
