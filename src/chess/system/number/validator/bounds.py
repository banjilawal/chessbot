# src/chess/system/number/validator/bounds.py

"""
Module: chess.system.number.validator.bounds
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import Any, cast

from chess.system import (
    BOARD_DIMENSION, NumberValidationFailedException, LoggingLevelRouter, NotNegativeNumberValidator,
    NumberAboveCeilingException, NumberBelowFloorException, NumberValidator, ValidationResult, Validator,
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
            floor: int = 0,
            ceiling: int = BOARD_DIMENSION,
            number_validator: NumberValidator = NotNegativeNumberValidator(),
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
        # RETURNS:
            *   ValidationResult[int] containing either:
                    - On failure: Exception.
                    - On success: int in the payload.
        # Raises:
              *     NumberValidationFailedException
              *     NumberBelowFloorException
              *     NumberAboveCeilingException
        """
        method = "NumberInBoundsValidator.validate"
        # Handle the existence and type checks.
        validation = number_validator.validate(candidate=candidate)
        if validation.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                NumberValidationFailedException(
                    message=f"{method}: {NumberValidationFailedException.ERROR_CODE}", ex=validation.exception,
                )
            )
        # As a triple check cast the payload to an int for additional testing.
        number = cast(int, validation.payload)
        
        # Handle case that the number is below the floor
        if number < floor:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                NumberValidationFailedException(
                    message=f"{method}: {NumberValidationFailedException.ERROR_CODE}",
                    ex=NumberBelowFloorException(f"{method}: {NumberBelowFloorException.DEFAULT_MESSAGE}")
                )
            )
        # Handle case that the number is above the floor
        if number < floor:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                NumberValidationFailedException(
                    message=f"{method}: {NumberValidationFailedException.ERROR_CODE}",
                    ex=NumberAboveCeilingException(f"{method}: {NumberAboveCeilingException.DEFAULT_MESSAGE}")
                )
            )
        # On certification success return the number in the ValidationResult
        return ValidationResult.success(payload=number)