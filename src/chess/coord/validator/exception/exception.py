# src/chess/coord/validator/exception_.py

"""
Module: chess.square.validator.exception
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.coord import CoordException
from chess.system import  NullException, ValidationException

__all__ = [
    "InvalidCoordException",
]


# ====================== COORD VALIDATION EXCEPTIONS #======================#
class InvalidCoordException(CoordException, ValidationException):
    """Catchall Exception for CoordValidator when a candidate fails a sanity check.""""""
    ERROR_CODE = "COORD_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Coord validation failed."




