# src/chess/scalar/validator/exception_.py

"""
Module: chess.scalar.validator.exception
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""


from chess.system import ValidationException
from chess.scalar.exception import ScalarException


__all__ = [
    "InvalidScalarException",
    
    #======================# SCALAR BOUNDS EXCEPTION #======================#
    "ScalarBelowBoundsException",
    "ScalarAboveBoundsException",
]

__all__ = [
    # ======================# SCALAR_VALIDATION_FAILURE EXCEPTION #======================#
    "InvalidScalarException",
]


# ======================# SCALAR_VALIDATION_FAILURE EXCEPTION #======================#
class InvalidScalarException(ScalarException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  A debug exception is created when a Scalar candidate fails a validation test. Validation debug exceptions are
        encapsulated inside an InvalidScalarException creating an exception chain. which is sent to the caller in a
        ValidationResult.
    2.  The InvalidScalarException chain is useful for tracing a  failure to its source.

    # PARENT:
        *   ScalarException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SCALAR_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "Scalar validation failed."



#======================# SCALAR BOUNDS EXCEPTION #======================#
class ScalarBelowBoundsException(InvalidScalarException):
    """Raised if scalar is below its < -LONGEST_KNIGHT_LEG_SIZE"""
    ERROR_CODE = "SCALAR_LOWER_BOUND_ERROR"
    DEFAULT_MESSAGE = "Scalar cannot be less than -LONGEST_KNIGHT_LEG_SIZE."


class ScalarAboveBoundsException(InvalidScalarException):
    """Raised if scalar is above its > LONGEST_KNIGHT_LEG_SIZE"""
    ERROR_CODE = "SCALAR_UPPER_BOUND_ERROR"
    DEFAULT_MESSAGE = "Scalar cannot be greater than LONGEST_KNIGHT_LEG_SIZE."
