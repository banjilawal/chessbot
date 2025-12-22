# src/chess/system/number/validator/not_negative.py

"""
Module: chess.system.number.validator.not_negative
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import Any, cast

from chess.system import LoggingLevelRouter, NegativeNumberException, NumberValidator, ValidationResult, Validator
from chess.system import InvalidNumberException, NullNumberException


class NotNegativeNumberValidator(Validator[int]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Utility that centralizes logic for testing an object is at least zero before a client uses it.

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
    def validate(
            cls,
            candidate: Any,
            number_validator: NumberValidator = NumberValidator()
    ) -> ValidationResult[int]:
        """
        # ACTION:
        1.  Test the candidate exists and is an int. If both tests pass cast to an int.
        2.  Test the number is at least zero.
        3.  Send an  exception in the ValidationResult for any failed tests. Otherwise, send the non-negative number.

        # PARAMETERS:
            *   candidate (Any)
            *   not_negative_validator (NumberValidator)
            
        # Returns:
        ValidationResult[int] containing either:
            - On success: int in the payload.
            - On failure: Exception.

        # Raises:
          *     NegativeNumberException
          *     InvalidNumberException
        """
        method = "IdValidator.validate"
        
        try:
            # Perform basic number integrity checks with not_negative_validator.
            validation = number_validator.validate(candidate=candidate)
            if validation.is_failure:
                return ValidationResult.failure(validation.exception)
            
            # Cast the payload to an int.
            number = cast(int, validation.payload)
            # Handle negative number case.
            if number < 0:
                return ValidationResult.failure(NegativeNumberException(f"{method}: {NegativeNumberException}"))
            
            # On passing both tests cast the candidate to an int, wrap in a ValidationResult and send back.
            return ValidationResult.success(payload=cast(int, candidate))
        
        # Finally, if there is an unhandled exception Wrap an InvalidNumberException then return the
        # exception chain inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidNumberException(ex=ex, message=f"{method}: {InvalidNumberException.DEFAULT_MESSAGE}")
            )