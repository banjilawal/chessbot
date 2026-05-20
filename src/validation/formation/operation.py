# src/validation/formation/validator.py

"""
Module: validation.formation.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


class FormationValidator(Validator[Formation]):
    """
     Role:Validation, Data Integrity Guarantor, Security.

    Responsibilities:
    1.  Ensure a rank is not null and the correct type before its used as a Formation.
    2.  If verification fails indicate the reason in an exception returned to the caller.

    Super Class:
        *   Validator

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Any) -> ValidationResult[Formation]:
        """
        # ACTION:.
            1.  If the rank passes existence and type checks cast into a Formation instance and return
                in the ValidationResult. Else return an exception in the ValidationResult.
        # PARAMETERS:
            *   rank (Any)
        # RETURNS:
            *   ValidationResult[Formation] containing either:
                    - On failure: Exception.
                    - On success: Formation in the payload.
        Raises:
            *   TypeError
            *   NullFormationException
            *   FormationValidationException
        """
        method = "FormationValidator.validate"
        # Handle the nonexistence case.
        if candidate is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                FormationValidationException(
                    msg=f"{method}: {FormationValidationException.ERR_CODE}",
                    ex=NullFormationException(f"{method} {NullFormationException.MSG}")
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, Formation):
            # Return the exception chain on failure
            return ValidationResult.failure(
                FormationValidationException(
                    msg=f"{method}: {FormationValidationException.ERR_CODE}",
                    ex=TypeError(f"{method} Expected a Formation, got {type(candidate).__name__} instead.")
                )
            )
        # On certification success return the formation instance in a ValidationResult.
        return ValidationResult.success(payload=cast(Formation, candidate))
