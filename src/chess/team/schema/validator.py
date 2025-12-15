# src/chess/team/team_schema/validator.py

"""
Module: chess.team.team_schema.validator
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from typing import cast, Any

from chess.system import (
    GameColor, IdentityService, InvalidGameColorException, NullGameColorException, Validator, ValidationResult,
    LoggingLevelRouter, NullStringException, TextException
)
from chess.team import (
    InvalidTeamSchemaException, NullTeamSchemaException, TeamSchema, TeamColorBoundsException,
    TeamNameBoundsException
)


class TeamSchemaValidator(Validator[TeamSchema]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a TeamSchema instance is certified safe, reliable and consistent before use.
    2.  Provide the verification customer an exception detailing the contract violation if integrity assurance fails.

    # PARENT:
        *   Validator

    # PROVIDES:
        * TeamSchemaValidator

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Any) -> ValidationResult[TeamSchema]:
        """
        # ACTION:
        1.  Check candidate is not null.
        2.  Check the candidate is a TeamSchema enum
        3.  If both checks pass cast the candidate to a TeamSchema and return in a
            ValidationResult.

        # PARAMETERS:
            *   candidate (Any)

        # Returns:
        ValidationResult[TeamSchema] containing either:
            - On success:   TeamSchema in the payload.
            - On failure:   Exception.

        # RAISES:
            *   TypeError
            *   NullTeamSchemaException
            *   InvalidTeamSchemaException
        """
        method = "TeamSchemaValidator.validate"
        
        try:
            # Start the error detection process.
            if candidate is None:
                return ValidationResult.failure(
                    NullTeamSchemaException(f"{method} {NullTeamSchemaException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, TeamSchema):
                return ValidationResult.failure(
                    TypeError(f"{method} Expected TeamSchema, got {type(candidate).__name__} instead.")
                )
            # If no errors are detected cast the candidate to a TeamSchema object then return in
            # a ValidationResult.
            return ValidationResult.success(cast(TeamSchema, candidate))
        
        # Finally, if there is an unhandled exception Wrap an InvalidPieceException around it
        # then return the exceptions inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidTeamSchemaException(ex=ex, message=f"{method} {InvalidTeamSchemaException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def verify_color_in_schema(
            cls,
            candidate: Any,
            team_schema_hedge: TeamSchema = TeamSchema()
    ) -> ValidationResult[GameColor]:
        """
        # ACTION:
        1.  Check candidate is not null and is a GameColor instance. If both conditions are true
            cast to a GameColor
        2.  If color is not inside the set of TeamSchema.colors send a
            ValidationResult containing an exception.
        4.  If all checks pass return the color in a ValidationResult

        # PARAMETERS:
            *   candidate (Any)
            *   team_schema_hedge (TeamSchema)

        # Returns:
        ValidationResult[GameColor] containing either:
            - On success:   GameColor in the payload.
            - On failure:   Exception.

        # RAISES:
            *   TypeError
            *   NullGameColorException
            *   TeamColorBoundsException
            *   InvalidGameColorException
        """
        method = "TeamSchemaValidator.verify_color_in_schema"
        
        try:
            # Start the error detection process.
            if candidate is None:
                return ValidationResult.failure(
                    NullGameColorException(f"{method}: {NullGameColorException.DEFAULT_MESSAGE}")
                )
            if not isinstance(candidate, GameColor):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected GameColor, got {type(candidate).__name__} instead.")
                )
            # cast candidate to GameColor for the last check.
            color = cast(GameColor, candidate)
            
            if color not in team_schema_hedge.allowed_colors:
                return ValidationResult.failure(
                    TeamColorBoundsException(f"{method}: {TeamColorBoundsException.DEFAULT_MESSAGE}")
                )
            # If no errors are detected send the verified color inside a ValidationResult.
            return ValidationResult.success(payload=color)
            
            # Finally, if there is an unhandled exception Wrap a InvalidGameColorException around it
            # then return the exceptions inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidGameColorException(ex=ex, message=f"{method}: {InvalidGameColorException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor()
    def verify_name_in_schema(
            cls,
            candidate: Any,
            idservice: IdentityService = IdentityService(),
    ) -> ValidationResult[str]:
        """
        # ACTION:
        1.  Check candidate is not null and is a str instance. If both conditions are true
            cast to a str
        2.  If str is not inside the set of TeamSchema.names send a
            ValidationResult containing an exception.
        4.  If all checks pass return the name in a ValidationResult

        # PARAMETERS:
            *   candidate (Any)
            *   team_schema_hedge (TeamSchema)

        # Returns:
        ValidationResult[str] containing either:
            - On success:   str in the payload.
            - On failure:   Exception.

        # RAISES:
            *   TypeError
            *   NullStringException
            *   TeamNameBoundsException
            *   TextException
        """
        method = "TeamSchemaValidator.verify_name_in_schema"
        
        try:
            # Start the error detection process.
            name_validation = idservice.validate_name(candidate)
            if name_validation.is_failure():
                return ValidationResult.failure(name_validation.exception)
            # Get the name from the validation payload on success.
            name = name_validation.payload
            
            if name not in TeamSchema.allowed_names():
                return ValidationResult.failure(
                    TeamNameBoundsException(f"{method} {TeamNameBoundsException.DEFAULT_MESSAGE}")
                )
            # If no errors are detected send the name inside a ValidationResult.
            return ValidationResult.success(payload=name)
            
            # Finally, if there is an unhandled exception Wrap a TextException around it
            # then return the exceptions inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                TeamNameException(ex=ex, message=f"{method} {TeamNameException.DEFAULT_MESSAGE}")
            )
