# src/chess/scalar/number_bounds_validator/exception_.py

"""
Module: chess.scalar.number_bounds_validator.exception
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


#======================# SCALAR VALIDATION EXCEPTION #======================#
class InvalidScalarException(ScalarException, ValidationException):
    """Catchall Exception for ScalarValidator when a candidate fails a sanity check.""""""
    ERROR_CODE = "SCALAR_VALIDATION_ERROR"
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
