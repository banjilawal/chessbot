# src/chess/system/identity/id/validator.py

"""
Module: chess.system.identity.id.validator
Author: Banji Lawal
Created: 2025-08-12
"""

import sys
from typing import Any, cast

from chess.system import IdValidationException, NumberValidator, Validator, ValidationResult, LoggingLevelRouter


class IdValidator(Validator[int]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security., Integrity
  
    # RESPONSIBILITIES:
    Verifies a candidate is an int greater than zero before its used an ID.
  
    # PROVIDES:
    ValidationResult[int] containing either:
        - On success: int in the payload.
        - On failure: Exception.
  
    # ATTRIBUTES:
    None
    """
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a designation is certified safe, reliable and consistent before use.
    2.  If verification fails indicate the reason in an exception, returned to the caller.
    3.  An Id is is required to be greater than zero.

    # PARENT:
        *   Validator

    # PROVIDES:
        * IdeValidator

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            number_validator: NumberValidator = NumberValidator()
    ) -> ValidationResult[int]:
        """
        # ACTION:
            1.  Test the candidate is not null and an int with not_negative_validator.
            2.  If the value is negative return an exception in the ValidationResult.
            3.  When all checks pass send the number in a ValidationResult's payload.
        # PARAMETERS:
            *   candidate (Any):
            *   not_negative_validator (NumberValidator)
        # RETURNS:
            *   ValidationResult[int] containing either:
                - On failure: Exception.
                - On success: int in the payload.
        # RAISES:
            *   IdValidationException
        """
        method = "IdValidator.validate"
        
        # Handle the case that the id is not a positive number.
        validation = number_validator.validate(candidate=candidate, floor=1, ceiling=sys.maxsize)
        if validation.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                IdValidationException(
                    message=f"{method}: {IdValidationException.DEFAULT_MESSAGE}:",
                    ex=validation.exception
                )
            )
        # If all checks pass return the validated id in a ValidationResult.
        return ValidationResult.success(payload=cast(int, candidate))

