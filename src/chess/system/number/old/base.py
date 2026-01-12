# src/chess/system/number/validator/base.py

"""
Module: chess.system.number.validator.base
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import Any, cast

from chess.system import LoggingLevelRouter, ValidationResult, Validator
from chess.system import NumberValidationFailedException, NullNumberException


class NumberValidator(Validator[int]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Verifies an object is not null and an int before a client tries to use it.
    2.  Utility that encapsulates existence and types checks that are performed frequently.
    2.  Return useful debugging information if a candidate does not satisfy basic integer constraints.

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
    def validate(cls, candidate: Any) -> ValidationResult[int]:
        """
        # ACTION:
            1.  If the candidate is null or not an int return the ValidationResult containing an exception.
                Otherwise, cast the candidate to an int and return in the ValidationResult.
        # PARAMETERS:
            *   candidate (Any)
        # RETURNS:
            *   ValidationResult[int] containing either:
                    - On failure: Exception.
                    - On success: int in the payload.
        # RAISES:
          *     TypeError
          *     NullNumberException
          *     NumberValidationFailedException
        """
        method = "NumberValidator.validate"
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                NumberValidationFailedException(
                    message=f"{method}: {NumberValidationFailedException.ERROR_CODE}",
                    ex=NullNumberException(f"{method}: {NullNumberException.DEFAULT_MESSAGE}"),
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, int):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                NumberValidationFailedException(
                    message=f"{method}: {NumberValidationFailedException.ERROR_CODE}",
                    ex=TypeError(f"{method}: Expected an integer, got {type(candidate).__name__} instead."),
                )
            )
        # On certification success cast the candidate to an int and return in the ValidationResult.
        return ValidationResult.success(payload=cast(int, candidate))