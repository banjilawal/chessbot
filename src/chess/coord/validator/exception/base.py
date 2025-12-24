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
    # ======================# COORD_VALIDATION_FAILURE EXCEPTION #======================#
    "InvalidCoordException",
]


# ======================# COORD_VALIDATION_FAILURE EXCEPTION #======================#
class InvalidCoordException(CoordException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  A debug exception is created when a Coord candidate fails a validation test. Validation debug exceptions are
        encapsulated inside an InvalidCoordException creating an exception chain. which is sent to the caller in a
        ValidationResult.
    2.  The InvalidCoordException chain is useful for tracing a  failure to its source.

    # PARENT:
        *   CoordException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "COORD_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "Coord validation failed."