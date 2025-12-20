# src/chess/coord/number_bounds_validator/exception/null.py

"""
Module: chess.coord.number_bounds_validator.exception.null
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.system import NullException
from chess.coord import InvalidCoordException

__all__ = [
    # ======================# NULL COORD EXCEPTION #======================#
    "NullCoordException",
]


# ======================# NULL COORD EXCEPTION #======================#
class NullCoordException(InvalidCoordException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Raised if a Coord validation candidate is null.
    2.  Raised if an entity, method or operation requires a Coord but receives null instead.

    # PARENT:
        *   InvalidCoordException
        *   NullCoordException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_COORD___ERROR"
    DEFAULT_MESSAGE = "Coord cannot be null."