# src/chess/coord/validator/exception/null.py

"""
Module: chess.coord.validator.exception.null
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

__all__ = [
    # ======================# NULL_COORD EXCEPTION #======================#
    "NullCoordException",
]

from chess.system import NullException
from chess.coord import CoordDebugException


# ======================# NULL_COORD EXCEPTION #======================#
class NullCoordException(CoordDebugException, NullException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    A failing ValidationResult was returned because the candidate was null.

    # PARENT:
        *   CoordDebugException
        *   NullException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_COORD_ERROR"
    DEFAULT_MESSAGE = "Coord validation failed: The candidate cannot be null."