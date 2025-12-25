# src/chess/formation/validator/validator.py

"""
Module: chess.formation.validator.validator
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from typing import cast, Any

from chess.system import Validator, ValidationResult, LoggingLevelRouter
from chess.formation import Formation, InvalidFormationException, NullFormationException


class FormationValidator(Validator[Formation]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a candidate is not null and the correct type before its used as a Formation.
    2.  If verification fails indicate the reason in an exception returned to the caller.

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
        # ACTION:.
            1.  If the candidate passes existence and type checks cast into a Formation instance and return
                in the ValidationResult. Else return an exception in the ValidationResult.
        # PARAMETERS:
            *   candidate (Any)
        # RETURNS:
            *   ValidationResult[Formation] containing either:
                    - On failure: Exception.
                    - On success: Formation in the payload.
        # RAISES:
            *   TypeError
            *   NullFormationException
            *   InvalidFormationException
        """
        method = "FormationValidator.validate"
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                InvalidFormationException(
                    message=f"{method}: {InvalidFormationException.ERROR_CODE}",
                    ex=NullFormationException(f"{method} {NullFormationException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, Formation):
            # Return the exception chain on failure
            return ValidationResult.failure(
                InvalidFormationException(
                    message=f"{method}: {InvalidFormationException.ERROR_CODE}",
                    ex=TypeError(f"{method} Expected a Formation instance, got {type(candidate).__name__} instead.")
                )
            )
        # On certification success return the formation instance in a ValidationResult.
        return ValidationResult.success(payload=cast(Formation, candidate))
