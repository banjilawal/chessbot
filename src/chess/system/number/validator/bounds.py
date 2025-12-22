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
            number_validator: NotNegativeNumberValidator = NotNegativeNumberValidator(),
    ) -> ValidationResult[int]:
        """
        # ACTION:
        1.  If not_negative_validator certifies the candidate is at least zero then test its less than the array size.
        2.  Return an exception if the candidate fails any test. Else pass the certified
            nuber in the ValidationResult.

        # PARAMETERS:
            *   candidate (Any)
            *   not_negative_validator (NotNegativeNumberValidator)

        # Returns:
        ValidationResult[int] containing either:
            - On success: int in the payload.
            - On failure: Exception.

        # Raises:
          *     NegativeNumberException
          *     InvalidNumberException
        """
        method = "NumberInBoundsVAlidator.validate"
        
        try:
            # Certify the candidate is not a negative number.
            validation = number_validator.validate(candidate=candidate)
            if validation.is_failure:
                return ValidationResult.failure(validation.exception)
            
            # Cast the payload to an int.
            number = cast(int, validation.payload)
            
            # Handle case that the number is outside the Board array's dimension.
            if number > BOARD_DIMENSION - 1:
                return ValidationResult.failure(
                    NumberAboveBoundsException(f"{method}: {NumberAboveBoundsException.DEFAULT_MESSAGE}")
                )
            # On passing both tests cast the candidate to an int, wrap in a ValidationResult and send back.
            return ValidationResult.success(payload=cast(int, candidate))
        
        # Finally, catch any missed exception, wrap an InvalidNumberException then return the
        # exception chain inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidNumberException(ex=ex, message=f"{method}: {InvalidNumberException.DEFAULT_MESSAGE}")
            )