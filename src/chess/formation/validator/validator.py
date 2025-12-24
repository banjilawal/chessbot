# src/chess/formation/validator/validator.py

"""
Module: chess.formation.validator.validator
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from typing import cast, Any

from chess.system import Validator, ValidationResult, LoggingLevelRouter
from chess.team import InvalidFormationException, NullFormationException, Formation


class FormationValidator(Validator[Formation]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a Formation instance is certified safe, reliable and consistent before use.
    2.  If verification fails indicate the reason in an exception, returned to the caller.

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
    def validate(cls, candidate: Any) -> ValidationResult[Formation]:
        """
        # ACTION:
        1.  Check candidate is not null.
        2.  Check the candidate is a Formation enum
        3.  If both checks pass cast the candidate to a Formation and return in a
            ValidationResult.

        # PARAMETERS:
            *   candidate (Any)

        # Returns:
        ValidationResult[Formation] containing either:
            - On success:   Formation in the payload.
            - On failure:   Exception.

        # RAISES:
            *   TypeError
            *   NullFormationException
            *   InvalidFormationException
        """
        method = "FormationValidator.validate"
        
        try:
            # Start the error detection process.
            if candidate is None:
                return ValidationResult.failure(
                    NullFormationException(f"{method} {NullFormationException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, Formation):
                return ValidationResult.failure(
                    TypeError(f"{method} Expected Formation, got {type(candidate).__name__} instead.")
                )
            # If no errors are detected cast the candidate to a Formation object then return in
            # a ValidationResult.
            return ValidationResult.success(cast(Formation, candidate))
        
        # Finally, catch any missed exception, wrap an InvalidPieceException around it
        # then return the exceptions inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidFormationException(ex=ex, message=f"{method} {InvalidFormationException.DEFAULT_MESSAGE}")
            )
