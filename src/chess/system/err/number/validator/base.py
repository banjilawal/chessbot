# src/chess/system/err/number/number_bounds_validator/base.py

"""
Module: chess.system.err.number.number_bounds_validator.base
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import Any, cast

from chess.system import LoggingLevelRouter, ValidationResult, Validator
from chess.system import InvalidNumberException, NullNumberException


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
        1.  Test the candidate exists and is an int. If either test fails return an appropriate exception
            in the ValidationResult. Otherwise, send the  certified number in the ValidationResult.

        # PARAMETERS:
            *   candidate (Any) object to certify is an int.

        # Returns:
        ValidationResult[int] containing either:
            - On success: int in the payload.
            - On failure: Exception.

        # Raises:
          *     TypeError
          *     NullNumberException
          *     InvalidNumberException
        """
        method = "IdValidator.validate"
        
        try:
            # Handle the case, the candidate does not exist.
            if candidate is None:
                return ValidationResult.failure(
                    NullNumberException(f"{method}: {NullNumberException.DEFAULT_MESSAGE}")
                )
            # Raise an error if the candidate is not an int.
            if not isinstance(candidate, int):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected an integer, got {type(candidate).__name__} instead.")
                )
            # On passing both tests cast the candidate to an int, wrap in a ValidationResult and send back.
            return ValidationResult.success(payload=cast(int, candidate))
        
        # Finally, if there is an unhandled exception Wrap an InvalidNumberException around it
        # then return the exception inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidNumberException(ex=ex, message=f"{method}: {InvalidNumberException.DEFAULT_MESSAGE}")
            )