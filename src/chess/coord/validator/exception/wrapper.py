# src/chess/coord/validator/exception/base.py

"""
Module: chess.coord.validator.exception.base
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.coord import CoordException
from chess.system import ValidationException

__all__ = [
    # ======================# COORD_VALIDATION_FAILURE EXCEPTION #======================#
    "CoordValidationException",
]


# ======================# COORD_VALIDATION_FAILURE EXCEPTION #======================#
class CoordValidationException(CoordException, ValidationException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a candidate failed its validation as a Coord. The exception chain traces the ultimate source of failure.

    # PARENT:
        *   CoordException
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "COORD_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "Coord validation failed."