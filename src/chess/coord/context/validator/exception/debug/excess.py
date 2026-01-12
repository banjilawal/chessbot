# src/chess/coord/context/validator/exception/debug/excess.py

"""
Module: chess.coord.context.validator.exception.debug.excess
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.coord import CoordContextException

__all__ = [
    # ========================= EXCESSIVE_COORD_CONTEXT_FLAG EXCEPTION =========================#
    "ExcessiveCoordContextFlagsException"
]


# ========================= EXCESSIVE_COORD_CONTEXT_FLAG EXCEPTION =========================#
class ExcessiveCoordContextFlagsException(CoordContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate That  more than one CoordContext flag was enabled. Only one Coord attribute-value-tuple can be used in
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
    ERROR_CODE = "EXCESSIVE_COORD_CONTEXT_FLAG_ERROR"
    DEFAULT_MESSAGE = (
        "Excessive CoordContext flags were set. an Coord search can only use one-and-only "
        "map flag at a time."
    )