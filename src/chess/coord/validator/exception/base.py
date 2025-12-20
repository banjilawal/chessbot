# src/chess/coord/validator/exception/base.py

"""
Module: chess.coord.validator.exception.base
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.coord import CoordException
from chess.system import ValidationFailedException

__all__ = [
    "InvalidCoordException",
]


#====================== COORD VALIDATION EXCEPTION #======================#
class InvalidCoordException(CoordException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised when an existing object violates Coord integrity constraints..
    2.  Wraps unhandled exception that hit the finally-block in CoordValidator methods.

    # PARENT:
        *   CoordException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "COORD_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Coord validation failed."




