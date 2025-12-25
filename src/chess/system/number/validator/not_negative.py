# src/chess/system/number/validator/not_negative.py

"""
Module: chess.system.number.validator.not_negative
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import Any, cast

from chess.system import LoggingLevelRouter, NegativeNumberException, NumberValidator, ValidationResult, Validator
from chess.system import InvalidNumberException


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
            1.  If number_validator returns an exception wrap it and forward in the ValidationResult.
                Else, get the number from the validation payload.
            2.  If the number is less than zero return the ValidationResult containing the exception.
            4.  All tests are passed return the ValidationResult containing the number in the payload.
        # PARAMETERS:
            *   candidate (Any)
            *   not_negative_validator (NotNegativeNumberValidator)
        # RETURNS:
            *   ValidationResult[int] containing either:
                    - On failure: Exception.
                    - On success: int in the payload.
        # RAISES:
          *     InvalidNumberException
        """
        method = "NotNegativeNumberValidator.validate"
        # Handle the existence and type checks.
        validation = number_validator.validate(candidate=candidate)
        if validation.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                InvalidNumberException(
                    message=f"{method}: {InvalidNumberException.ERROR_CODE}",
                    ex=validation.exception,
                )
            )
        # As a triple check cast the payload to an int for additional testing.
        number = cast(int, validation.payload)

        # Handle negative number case.
        if number < 0:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                InvalidNumberException(
                    message=f"{method}: {InvalidNumberException.ERROR_CODE}",
                    ex=NegativeNumberException(f"{method}: {NegativeNumberException}"),
                )
            )
        # On certification success return the number in the ValidationResult
        return ValidationResult.success(payload=number)