# src/chess/vector/validator/validator.py

"""
Module: chess.vector.validator
Author: Banji Lawal
Created: 2025-08-26
version: 1.0.0
"""

from typing import Any, cast

from chess.system import (
    LONGEST_KNIGHT_LEG_SIZE, LoggingLevelRouter, BoundNumberValidator, ValidationResult,
    Validator
)
from chess.vector import InvalidVectorException, NullVectorException, Vector


class VectorValidator(Validator[Vector]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Run tests verifying a candidate can safely be used as a Square.
    2.  If verification fails indicate the reason in an exception, returned to the caller.

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
            number_in_bounds_validator: BoundNumberValidator = BoundNumberValidator()
    ) -> ValidationResult[Vector]:
        """
        # ACTION:
            1.  If the candidate fails existence and type checks return the ValidationResult containing an
                exception. Else cast into Vector instance vector.
            2.  If vector.x fails either existence, type of bounds checks return the ValidationResult containing
                an exception.
            3.  If vector.y fails either existence, type of bounds checks return the ValidationResult containing
                an exception.
            4.  All tests are passed return the ValidationResult containing vector in the payload.
        # PARAMETERS:
            *   candidate (Any)
            *   number_in_bounds_validator (BoundNumberValidator)
        # RETURNS:
            *   ValidationResult[Vector] containing either:
                    - On failure: Exception.
                    - On success: Vector in the payload.
        # RAISES:
            *   TypeError
            *   NullVectorException
            *   InvalidVectorException
        """
        method = "VectorValidator.validate"
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                InvalidVectorException(
                    message=f"{method}: {InvalidVectorException.ERROR_CODE}",
                    ex=NullVectorException(f"{method}: {NullVectorException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, Vector):
            return ValidationResult.failure(
                InvalidVectorException(
                    message=f"{method}: {InvalidVectorException.ERROR_CODE}",
                    ex=TypeError(f"{method}: Expected a Vector, got {type(candidate).__name__} instead.")
                )
            )
        # After existence and type checks cast the candidate to a Vector for additional tests.
        vector = cast(Vector, candidate)
        
        # Validate the vector.x field. Use the absolute value because vectors can have negative components.
        x_axis_validation = number_in_bounds_validator.validate(
            floor=0,
            ceiling=LONGEST_KNIGHT_LEG_SIZE,
            candidate=abs(vector.x),
        )
        if x_axis_validation.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                InvalidVectorException(
                    message=f"{method}: {InvalidVectorException.ERROR_CODE}",
                    ex=x_axis_validation.exception
                )
            )
        # Validate the vector.y field. Use the absolute value because vectors can have negative components.
        y_axis_validation = number_in_bounds_validator.validate(
            floor=0,
            ceiling=LONGEST_KNIGHT_LEG_SIZE,
            candidate=abs(vector.y),
        )
        if y_axis_validation.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                InvalidVectorException(
                    message=f"{method}: {InvalidVectorException.ERROR_CODE}",
                    ex=y_axis_validation.exception
                )
            )
        # On certification success return the vector instance in the ValidationResult.
        return ValidationResult.success(payload=vector)