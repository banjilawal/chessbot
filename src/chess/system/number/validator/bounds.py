# src/chess/system/number/validator/bounds.py

"""
Module: chess.system.number.validator.bounds
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import Any, cast

from chess.system import (
    BOARD_DIMENSION, InvalidNumberException, LoggingLevelRouter,  NotNegativeNumberValidator, ValidationResult,
    Validator, NumberAboveBoundsException
)


class NumberInBoundsValidator(Validator[int]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Utility that centralizes logic for ensuring an number is not negative nor larger
        than the Board's dimensions before its used as Coord or Vector component.

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
            not_negative_validator: NotNegativeNumberValidator = NotNegativeNumberValidator(),
    ) -> ValidationResult[int]:
        """
        # ACTION:
            1.  If candidate fails not-negative validation return the validation result containing the exception.
                Else get the number from the validation payload.
            2.  If number > BOARD.DIMENSION -1 return the ValidationResult containing the exception.
            3.  The tests have been passed. Return the ValidationResult with the number in the payload.

        # PARAMETERS:
            *   candidate (Any)
            *   not_negative_validator (NotNegativeNumberValidator)

        # Returns:
        ValidationResult[int] containing either:
            - On failure: Exception.
            - On success: int in the payload.
        # Raises:
          *     InvalidNumberException
        """
        method = "NumberInBoundsValidator.validate"
        # Handle the below bounds case.
        validation = not_negative_validator.validate(candidate=candidate)
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
        
        # Handle case that the number is outside the Board array's dimension.
        if number > BOARD_DIMENSION - 1:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                InvalidNumberException(
                    message=f"{method}: {InvalidNumberException.ERROR_CODE}",
                    ex=NumberAboveBoundsException(f"{method}: {NumberAboveBoundsException.DEFAULT_MESSAGE}")
                )
            )
        # On certification success return the number in the ValidationResult
        return ValidationResult.success(payload=number)