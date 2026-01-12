# src/chess/coord/context/validator/exception/debug/zero.py

"""
Module: chess.coord.context.validator.exception.debug.zero
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.coord import CoordContextException

__all__ = [
    # ========================= ZERO_COORD_CONTEXT_FLAGS EXCEPTION =========================#
    "ZeroCoordContextFlagsException"
]


# ========================= ZERO_COORD_CONTEXT_FLAGS EXCEPTION =========================#
class ZeroCoordContextFlagsException(CoordContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate That  no CoordContext flag was enabled. One and only one Coord attribute-value-tuple is required for
        a search.

    # PARENT:
        *   ContextFlagCountException
        *   CoordContextValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ZERO_COORD_CONTEXT_FLAGS_ERROR"
    DEFAULT_MESSAGE = (
        "Zero CoordContext flags were set. Cannot search for Coords if one-and_oly-one "
        "map flag is enabled."
    )
