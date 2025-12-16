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
    None

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
