# src/chess/system/identity/id/validator.py

"""
Module: chess.system.identity.id.validator
Author: Banji Lawal
Created: 2025-08-12
"""

from typing import Any, cast

from chess.system import (
    NumberValidator, Validator, ValidationResult, NegativeIdException, InvalidIdException, LoggingLevelRouter,
)


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
    
        # Returns:
        ValidationResult[int] containing either:
            - On success: int in the payload.
            - On failure: Exception.
    
        # Raises:
            *   NegativeIdException
            *   InvalidIdException
        """
        method = "IdValidator.validate"
        
        try:
            # Verify the candidate is not null and an int.
            validation = number_validator.validate(candidate=candidate)
            if validation.is_failure():
                return ValidationResult.failure(validation.exception)
            
            # Cast and test if the number is negative.
            id = cast(int, candidate)
            if id < 0:
                return ValidationResult.failure(
                    NegativeIdException(f"{method}: {NegativeIdException.DEFAULT_MESSAGE}")
                )
            # If all checks pass return the validated id in a ValidationResult.
            return ValidationResult.success(payload=id)
        
        # Finally, if there is an unhandled exception Wrap an InvalidNIdException around it
        # then return the exception inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidIdException(ex=ex, message=f"{method}: {InvalidIdException.DEFAULT_MESSAGE}")
            )
