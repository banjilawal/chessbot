# src/logic/coord/context/validator/exception/debug/zero.py

"""
Module: logic.coord.context.validator.exception.debug.zero
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from logic.system import ContextFlagCountException
from logic.coord import CoordContextException

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
        *   CoordContextValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "ZERO_COORD_CONTEXT_FLAGS_EXCEPTION"
    MSG = (
        "Zero CoordContext flags were set. Cannot search for Coords if one-and_oly-one "
        "map flag is enabled."
    )
