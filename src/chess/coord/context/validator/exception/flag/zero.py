# src/chess/coord/context/number_bounds_validator/exception/flag/zero.py

"""
Module: chess.coord.context.number_bounds_validator.exception.flag.zero
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""


from chess.system import BoundsException
from chess.coord import InvalidCoordContextException

__all__ = [
    # ========================= ZERO_COORD_CONTEXT_FLAGS EXCEPTION =========================#
    "ZeroCoordContextFlagsSetException"
]


# ========================= ZERO_COORD_CONTEXT_FLAGS EXCEPTION =========================#
class ZeroCoordContextFlagsSetException(InvalidCoordContextException, BoundsException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicates no CoordContext flag was enabled. One and only one Coord attribute-value tuple is required for
        a search.

    # PARENT:
        *   BoundsException
        *   InvalidCoordContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ZERO_COORD_CONTEXT_FLAGS_ERROR"
    DEFAULT_MESSAGE = "Zero CoordContext flags were set. One and only one context flag must be enabled,"
